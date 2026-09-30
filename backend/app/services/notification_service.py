class NotificationService:
    async def send(self, notification: dict): return {'queued':True,'notification':notification}
