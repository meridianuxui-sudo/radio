class SupabaseService:
    """Backend-only adapter; service role credentials must never reach a client."""
    def configured(self, url: str, service_role_key: str): return bool(url and service_role_key)
