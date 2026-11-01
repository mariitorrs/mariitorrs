"""Busca as últimas músicas tocadas no Spotify e gera assets/spotify-recent.svg.

Precisa de três segredos do repositório (veja COMO_INSTALAR.md):
SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET e SPOTIFY_REFRESH_TOKEN.
"""
import base64
import datetime
import json
import os
import pathlib
import urllib.parse
import urllib.request

from build_assets import spotify_card


def access_token():
    cid = os.environ["SPOTIFY_CLIENT_ID"]
    secret = os.environ["SPOTIFY_CLIENT_SECRET"]
    refresh = os.environ["SPOTIFY_REFRESH_TOKEN"]
    auth = base64.b64encode(f"{cid}:{secret}".encode()).decode()
    data = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": refresh}).encode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token", data=data,
        headers={"Authorization": f"Basic {auth}",
                 "Content-Type": "application/x-www-form-urlencoded"})
    return json.load(urllib.request.urlopen(req))["access_token"]


def recently_played(token, limit=5):
    req = urllib.request.Request(
        f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}",
        headers={"Authorization": f"Bearer {token}"})
    items = json.load(urllib.request.urlopen(req))["items"]
    now = datetime.datetime.now(datetime.timezone.utc)
    tracks = []
    for item in items:
        track = item["track"]
        played = datetime.datetime.fromisoformat(item["played_at"].replace("Z", "+00:00"))
        tracks.append({
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "minutes": int((now - played).total_seconds() // 60),
            "explicit": track.get("explicit", False),
        })
    return tracks


if __name__ == "__main__":
    tracks = recently_played(access_token())
    if not tracks:
        raise SystemExit("Nenhuma música recente encontrada; mantendo o card anterior.")
    spotify_card(tracks)
    print(f"{len(tracks)} músicas escritas em assets/spotify-recent.svg")
