# Setup
Copy `backend/.env.example` to `backend/.env`. Keep `DEMO_MODE=true` for first launch. Set `DATABASE_URL` to local PostgreSQL or Supabase Postgres when persistence is enabled and apply `database/schema.sql`. Configure CORS for your admin origin. The checked-in demo repository uses in-memory data deliberately; connect a repository implementation to PostgreSQL before production.

Only backend environment variables may contain AzuraCast keys, LiveKit secret, Supabase service role, source passwords, and Firebase credentials. Flutter gets only public station configuration and temporary LiveKit tokens.
