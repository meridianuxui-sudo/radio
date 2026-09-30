from .radio_source_bridge import RadioSourceBridgeService
class LiveBroadcastService:
    def __init__(self): self.bridge=RadioSourceBridgeService()
    async def start(self, show_id): return await self.bridge.start(f'meradion-{show_id}')
    async def end(self, show_id): return await self.bridge.stop(f'meradion-{show_id}')
