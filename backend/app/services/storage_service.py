class StorageService:
    """Production adapter boundary for Supabase private recording storage."""
    async def signed_url(self, path: str): return {'path':path,'url':None,'message':'Configure Supabase Storage to issue signed URLs.'}
