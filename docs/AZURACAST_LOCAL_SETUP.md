# Local AzuraCast development
**Local development is not public production.** AzuraCast is free/open-source; Docker and a developer machine are enough for experimentation.

1. Install Docker Desktop/Engine and Docker Compose.
2. Follow the current AzuraCast Docker installation instructions, then start its compose stack on the developer PC.
3. Open the local web UI, create a development station, add a general-rotation playlist, upload test MP3s, and start the station.
4. Copy the station’s public mount/stream URL. Test continuous playback in VLC: `vlc http://localhost:PORT/radio.mp3` (use the exact mount and port shown by AzuraCast).
5. Confirm AzuraCast Now Playing and listener count after connecting VLC. Create an API key, record the station ID, and set `AZURACAST_BASE_URL`, `AZURACAST_API_KEY`, `AZURACAST_STATION_ID`, and `AZURACAST_STREAM_URL` in backend `.env`; set `DEMO_MODE=false`.
6. A physical Flutter phone cannot use its own `localhost`: use LAN IP and allow the port, or an Android emulator host mapping.

Developer PC → Docker → AzuraCast → local stream → VLC/Flutter. A local server is suitable only for development/testing; public listeners need a publicly reachable production server and domain.
