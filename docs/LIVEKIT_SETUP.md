# LiveKit and radio bridge
Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` only in FastAPI. The `/api/livekit/token` endpoint issues short-lived participant tokens in production; never embed the secret in Flutter. Restrict studio access to RJ/ADMIN.

The bridge is a separate process: it subscribes to the LiveKit room, mixes/normalizes participant audio, then uses GStreamer/FFmpeg or a dedicated encoder to publish to AzuraCast’s configured DJ/source endpoint using `RADIO_SOURCE_USERNAME` and `RADIO_SOURCE_PASSWORD`. Add reconnecting, silence detection, loudness limiting, and a fallback automation playlist. The shipped bridge interface returns `pending_configuration` rather than claiming live audio works without an encoder and credentials.
