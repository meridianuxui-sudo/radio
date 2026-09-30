from ..core.config import settings
from ..integrations.azuracast import AzuraCastService
from .demo_data import now_playing
class RadioService:
 async def current(self):
  if settings.demo_mode: return now_playing()
  data=await AzuraCastService().now_playing(); return {'live':data.get('live',{}).get('is_live',False),'station':data.get('station',{}).get('name'),'stream_url':settings.azuracast_stream_url,'listeners':data.get('listeners',{}).get('current',0),'raw':data,'is_demo':False}
