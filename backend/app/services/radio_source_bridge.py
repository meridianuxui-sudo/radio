class RadioSourceBridgeService:
    """Server-side contribution boundary: mixes LiveKit audio then sends it to AzuraCast DJ/source input.
    This interface deliberately never returns source credentials to a client."""
    async def start(self, room_name: str): return {'state':'pending_configuration','room':room_name,'message':'Configure a server-side GStreamer/FFmpeg LiveKit egress bridge and RADIO_SOURCE_* credentials.'}
    async def stop(self, room_name: str): return {'state':'stopped','room':room_name}
