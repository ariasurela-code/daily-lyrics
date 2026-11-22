#!/usr/bin/env python3
"""Builds the static site into ./site: today's page + archive of all past days.
Entry for a date = songs[days_since_epoch % len(songs)], so it needs no state."""
import json, datetime, pathlib, shutil, html

root = pathlib.Path(__file__).resolve().parent.parent
songs = json.loads((root / "songs.json").read_text(encoding="utf-8"))
tpl = (root / "player.html").read_text(encoding="utf-8")
out = root / "site"
if out.exists():
    shutil.rmtree(out)
(out / "archive").mkdir(parents=True)

START = datetime.date(2026, 1, 1)  # archive start
today = datetime.date.today()

def entry_for(d):
    return songs[(d - datetime.date(1970, 1, 1)).days % len(songs)]

def render(entry):
    return tpl.replace("/*ENTRY*/null", json.dumps(entry, ensure_ascii=False))

# today's page
(out / "index.html").write_text(render(entry_for(today)), encoding="utf-8")
(out / "songs.json").write_text(json.dumps(songs, ensure_ascii=False), encoding="utf-8")

# archive pages (every day since START up to today)
rows = []
d = START
while d <= today:
    e = entry_for(d)
    page = render(e).replace('href="archive/index.html"', 'href="index.html"')
    (out / "archive" / f"{d.isoformat()}.html").write_text(page, encoding="utf-8")
    rows.append(f'<li><a href="{d.isoformat()}.html">{d.isoformat()}</a> — {html.escape(e["title"])} <small>({html.escape(e["flower"])})</small></li>')
    d += datetime.timedelta(days=1)

(out / "archive" / "index.html").write_text(
    '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>Archive</title><style>body{font:16px Inter,sans-serif;background:#120a1e;color:#fff;max-width:640px;margin:30px auto;padding:0 16px}'
    'a{color:#ffb3c1}li{margin:8px 0}</style><h1>Daily Lyrics — Archive</h1><p><a href="../index.html">← Aaj ka</a></p><ul>'
    + "\n".join(reversed(rows)) + "</ul>", encoding="utf-8")
print(f"Built {len(rows)} pages; today = {entry_for(today)['title']}")
