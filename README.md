# Meradio'N — Your Sound. Your Stories.

A production-minded live radio platform: Flutter listener/RJ app, FastAPI gateway, React admin dashboard, PostgreSQL schema, and explicit AzuraCast + LiveKit contribution architecture. It starts in **Demo Mode** so no paid infrastructure or secret is needed.

## Run locally
```bash
cd backend && python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
cp .env.example .env && uvicorn app.main:app --reload --port 8000
# another terminal
cd admin && npm install && npm run dev
# Flutter (if Flutter SDK is installed)
cd mobile && flutter pub get && flutter run
```
The demo API is at `http://localhost:8000/docs`. Demo credentials: `rj@meradion.local` / `demo-rj`, or `admin@meradion.local` / `demo-admin`. These only exist in in-memory Demo Mode—change all credentials and use real authentication before deployment.

## Architecture and operations
* [Architecture](docs/ARCHITECTURE.md) · [API](docs/API.md) · [Setup](docs/SETUP.md) · [Deployment](docs/DEPLOYMENT.md)
* [Local AzuraCast](docs/AZURACAST_LOCAL_SETUP.md) · [Production AzuraCast](docs/AZURACAST_PRODUCTION_SETUP.md)
* [LiveKit and bridge](docs/LIVEKIT_SETUP.md) · [Recording](docs/RECORDING.md) · [Troubleshooting](docs/TROUBLESHOOTING.md)
