from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_demo_radio():
 r=c.get('/api/radio/live'); assert r.status_code==200 and r.json()['is_demo'] is True
def test_radio_health(): assert c.get('/api/radio/health').json()['healthy'] is True
def test_auth_and_favorites():
 auth=c.post('/api/auth/login',json={'email':'rj@meradion.local','password':'demo-rj'}).json()['access_token']; h={'Authorization':f'Bearer {auth}'}
 assert c.post('/api/favorites',json={'show_id':'morning-vibes'},headers=h).status_code==201
 assert len(c.get('/api/favorites',headers=h).json())==1
def test_authorization(): assert c.post('/api/shows',json={'title':'Nope'},headers={}).status_code==401
def test_shows_and_schedule(): assert len(c.get('/api/shows').json())>=4 and len(c.get('/api/schedule').json())>=3
