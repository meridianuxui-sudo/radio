from ..core.config import settings
class LiveKitService:
    def configured(self): return bool(settings.livekit_url and settings.livekit_api_key and settings.livekit_api_secret)
    def token(self, room, identity, host=False):
        if not self.configured(): return None
        # Use livekit-api AccessToken here in production; secrets never leave this service.
        raise NotImplementedError('Install/configure livekit-api token provider for production')
