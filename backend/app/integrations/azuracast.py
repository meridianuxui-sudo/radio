import httpx
from ..core.config import settings
class AzuraCastUnavailable(RuntimeError): pass
class AzuraCastService:
    def __init__(self): self.base=settings.azuracast_base_url.rstrip('/'); self.headers={'X-API-Key':settings.azuracast_api_key} if settings.azuracast_api_key else {}
    async def now_playing(self):
        if not self.base or not settings.azuracast_station_id: raise AzuraCastUnavailable('AzuraCast is not configured')
        async with httpx.AsyncClient(timeout=8) as c:
            r=await c.get(f'{self.base}/api/nowplaying/{settings.azuracast_station_id}',headers=self.headers); r.raise_for_status(); return r.json()
    async def health(self):
        try: return {'reachable':True,'station_configured':bool(settings.azuracast_station_id),'stream_configured':bool(settings.azuracast_stream_url),'data':await self.now_playing()}
        except Exception as e: return {'reachable':False,'station_configured':bool(settings.azuracast_station_id),'stream_configured':bool(settings.azuracast_stream_url),'error':str(e)}
