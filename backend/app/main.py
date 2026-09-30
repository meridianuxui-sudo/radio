from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .core.config import settings
from .core.security import token_for, require, current_user
from .services.radio_service import RadioService
from .services.demo_data import SHOWS, schedule, recordings
from .integrations.azuracast import AzuraCastService
from .integrations.livekit import LiveKitService
from .services.live_broadcast_service import LiveBroadcastService
app=FastAPI(title="Meradio'N API", version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origins.split(','),allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
users={'admin@meradion.local':{'password':'demo-admin','role':'ADMIN','name':'Admin'},'rj@meradion.local':{'password':'demo-rj','role':'RJ','name':'RJ Sai'}}
favorites={}
class Credentials(BaseModel): email: str; password: str; name: str|None=None
class ShowInput(BaseModel): title:str; category:str='Talk Show'; description:str=''; hosts:list[str]=[]
class FavoriteInput(BaseModel): show_id:str
class RoomInput(BaseModel): room:str; identity:str; host:bool=False
@app.get('/api/health')
def health(): return {'status':'ok','demo_mode':settings.demo_mode}
@app.post('/api/auth/register')
def register(body:Credentials):
 if body.email in users: raise HTTPException(409,'Email already registered')
 users[body.email]={'password':body.password,'role':'USER','name':body.name or body.email.split('@')[0]}
 return {'access_token':token_for(body.email,'USER'),'role':'USER'}
@app.post('/api/auth/login')
def login(body:Credentials):
 user=users.get(body.email)
 if not user or user['password']!=body.password: raise HTTPException(401,'Incorrect email or password')
 return {'access_token':token_for(body.email,user['role']),'role':user['role'],'name':user['name']}
@app.post('/api/auth/logout',status_code=204)
def logout(): return
@app.get('/api/radio/live')
async def live(): return await RadioService().current()
@app.get('/api/radio/now-playing')
async def now_playing(): return await RadioService().current()
@app.get('/api/radio/station')
async def station():
 current=await RadioService().current(); return {'name':"Meradio'N",'tagline':'Your Sound. Your Stories.','stream_url':current.get('stream_url',''),'demo_mode':settings.demo_mode}
@app.get('/api/radio/health')
async def radio_health():
 if settings.demo_mode: return {'healthy':True,'demo_mode':True,'azuracast_reachable':False,'station_configured':False,'stream_configured':False,'message':'Demo Mode supplies station data; configure AzuraCast to validate a stream.'}
 status=await AzuraCastService().health()
 if not status['reachable']: raise HTTPException(503,detail=status)
 return {'healthy':True,'demo_mode':False,'azuracast_reachable':True,**status}
@app.get('/api/shows')
def get_shows(q:str=''): return [s for s in SHOWS if q.lower() in (s['title']+' '+s['category']+' '+s['description']).lower()]
@app.get('/api/shows/{show_id}')
def get_show(show_id:str):
 for s in SHOWS:
  if s['id']==show_id:return s
 raise HTTPException(404,'Show not found')
@app.post('/api/shows',dependencies=[Depends(require('ADMIN'))],status_code=201)
def add_show(body:ShowInput):
 item={'id':body.title.lower().replace(' ','-'),'artwork':'',**body.model_dump()}; SHOWS.append(item);return item
@app.put('/api/shows/{show_id}',dependencies=[Depends(require('ADMIN'))])
def update_show(show_id:str,body:ShowInput):
 item=get_show(show_id);item.update(body.model_dump());return item
@app.delete('/api/shows/{show_id}',dependencies=[Depends(require('ADMIN'))],status_code=204)
def delete_show(show_id:str): SHOWS.remove(get_show(show_id))
@app.get('/api/schedule')
def get_schedule(): return schedule()
@app.post('/api/schedule',dependencies=[Depends(require('ADMIN'))],status_code=201)
def create_schedule(body:dict): return {'id':'new',**body}
@app.put('/api/schedule/{item_id}',dependencies=[Depends(require('ADMIN'))])
def update_schedule(item_id:str,body:dict): return {'id':item_id,**body}
@app.delete('/api/schedule/{item_id}',dependencies=[Depends(require('ADMIN'))],status_code=204)
def delete_schedule(item_id:str): return
@app.post('/api/shows/{show_id}/start',dependencies=[Depends(require('RJ','ADMIN'))])
async def start_show(show_id:str): return await LiveBroadcastService().start(show_id)
@app.post('/api/shows/{show_id}/end',dependencies=[Depends(require('RJ','ADMIN'))])
async def end_show(show_id:str): return await LiveBroadcastService().end(show_id)
@app.get('/api/recordings')
def get_recordings(q:str=''): return [r for r in recordings() if q.lower() in r['title'].lower()]
@app.get('/api/recordings/{recording_id}')
def get_recording(recording_id:str):
 for r in recordings():
  if r['id']==recording_id:return r
 raise HTTPException(404,'Recording not found')
@app.post('/api/recordings',dependencies=[Depends(require('RJ','ADMIN'))],status_code=201)
def create_recording(body:dict): return {'id':'pending-upload', 'published':False, **body}
@app.get('/api/favorites')
def get_favorites(user=Depends(current_user)): return favorites.get(user['sub'],[])
@app.post('/api/favorites',status_code=201)
def add_favorite(body:FavoriteInput,user=Depends(current_user)):
 item=get_show(body.show_id); bucket=favorites.setdefault(user['sub'],[])
 if item not in bucket:bucket.append(item)
 return item
@app.delete('/api/favorites/{show_id}',status_code=204)
def remove_favorite(show_id:str,user=Depends(current_user)):
 favorites[user['sub']]=[s for s in favorites.get(user['sub'],[]) if s['id']!=show_id]
@app.post('/api/notifications',dependencies=[Depends(require('ADMIN'))],status_code=202)
def notify(body:dict): return {'queued':True,'provider':'demo' if settings.demo_mode else 'firebase','notification':body}
@app.get('/api/analytics',dependencies=[Depends(require('RJ','ADMIN'))])
def analytics(): return {'current_listeners':128,'listening_hours':842,'total_shows':len(SHOWS),'total_recordings':len(recordings()),'listener_trend':[52,64,71,86,92,111,128],'popular_shows':SHOWS[:3]}
@app.post('/api/livekit/token')
def livekit_token(body:RoomInput,user=Depends(require('RJ','ADMIN'))):
 token=LiveKitService().token(body.room,body.identity,body.host) if LiveKitService().configured() else None
 return {'room':body.room,'token':token,'configured':token is not None,'message':'Configure LiveKit server credentials to issue a production token.' if token is None else 'ok'}
@app.post('/api/livekit/rooms',dependencies=[Depends(require('RJ','ADMIN'))])
def create_room(body:RoomInput): return {'room':body.room,'state':'created' if LiveKitService().configured() else 'demo'}
@app.post('/api/livekit/session/start',dependencies=[Depends(require('RJ','ADMIN'))])
async def session_start(body:dict): return await LiveBroadcastService().start(body.get('show_id','live'))
@app.post('/api/livekit/session/end',dependencies=[Depends(require('RJ','ADMIN'))])
async def session_end(body:dict): return await LiveBroadcastService().end(body.get('show_id','live'))
