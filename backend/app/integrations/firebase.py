class FirebaseService:
    """Backend-only FCM adapter boundary for station and recording notifications."""
    def configured(self, project_id: str): return bool(project_id)
