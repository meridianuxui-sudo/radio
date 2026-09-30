class RecordingService:
    """Coordinates capture metadata, processing, storage, and publication."""
    async def create_pending(self, metadata: dict): return {'state':'pending_upload', **metadata}
