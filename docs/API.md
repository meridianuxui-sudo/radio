# API
All endpoints are prefixed `/api`. Public: `GET /radio/live`, `/radio/station`, `/radio/now-playing`, `/radio/health`, `/shows`, `/shows/{id}`, `/schedule`, `/recordings`, `/recordings/{id}`. Auth: `POST /auth/register`, `/auth/login`, `/auth/logout`. Bearer JWT user endpoints: favorites. RJ/admin endpoints: show start/end, recordings create, LiveKit room/session/token. Admin endpoints: show and schedule mutation, notifications. `GET /analytics` requires RJ/admin.

`/radio/health` returns controlled HTTP 503 when real AzuraCast cannot be reached; in Demo Mode it returns a healthy demo diagnostic. Public stream URLs may be returned; privileged credentials never are.
