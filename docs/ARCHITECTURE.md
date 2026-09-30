# Architecture
Flutter obtains public metadata and a public stream URL from FastAPI. FastAPI alone holds AzuraCast keys and calls AzuraCast, whose integrated Icecast-compatible server distributes one continuous station stream to all listeners. Supabase/PostgreSQL stores application metadata and recordings storage uses signed URLs where access is private.

`RJs → LiveKit room → server-side mixed-audio bridge → AzuraCast DJ/source input → public stream → listeners`

LiveKit is contribution audio, not public radio distribution. `RadioSourceBridgeService` is intentionally modular and server-side; production deployers provide LiveKit egress/GStreamer or FFmpeg mixing and use `RADIO_SOURCE_*` only there. It is not falsely enabled in Demo Mode.
