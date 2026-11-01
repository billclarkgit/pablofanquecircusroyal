# Pablo Fanque’s Circus Royal

A portable, responsive website with the full three-act narrative and all eighteen songs in the supplied order. Original decorative SVG covers evoke a Victorian circus pavilion; they can be replaced with your album artwork. No external fonts, libraries, tracking, or build step are required.

## Preview

Open `index.html` in a browser for a quick preview. For the most reliable audio testing, serve this folder using any static web server. With Python installed:

```sh
python3 serve.py
```

Then visit http://localhost:8765. Stop the server with Ctrl+C.

## Add your recordings

Copy your MP3s into `audio/` using the filenames below. Every file maps directly to the corresponding track in `album.js`. The prototype includes your supplied Nymph recording as `audio/act-1-04.wav`; all other recordings are awaiting your files. There are no invented durations. The player reads the duration from the selected recording's metadata.

| File | Song |
| --- | --- |
| act-1-01.mp3 | Curtain Rises |
| act-1-02.mp3 | The Thrill of Mr. K |
| act-1-03.mp3 | The Life and Death of Cock Robin |
| act-1-04.wav (included) | Nymph of the Flowing Veil |
| act-1-05.mp3 | Unrelated Acts of Wonder |
| act-1-06.mp3 | Amateur Gentlemen |
| act-2-01.mp3 | Slack Wire Siren |
| act-2-02.mp3 | A Splendid Night |
| act-2-03.mp3 | Wallett's Jam |
| act-2-04.mp3 | Henry was Zanthus |
| act-2-05.mp3 | La Sprite Diavolo |
| act-2-06.mp3 | On the Tightrope |
| act-3-01.mp3 | Save Me a Spotlight, Brother |
| act-3-02.mp3 | Trampoline Leaps |
| act-3-03.mp3 | Ten Somersets |
| act-3-04.mp3 | Hogshead of Real Fire |
| act-3-05.mp3 | Last Night but Three (Pablo’s Thank You) |
| act-3-06.mp3 | Pablo Fanque's Circus Royal (Reprise) |

Keep filenames lowercase and exact. Alternatively, change each track's `file` value in `album.js` to your own relative path. Do not add a leading slash: relative paths support GitHub Pages project URLs.

To show a download link for a particular song, change its `"download": false` to `"download": true` in `album.js` after adding that recording. Links are hidden by default. Playback files are necessarily accessible to visitors even when download buttons are hidden.

Controls include play/pause, previous/next (wrapping within the act), direct track selection, seeking once metadata is loaded, and automatic advance to the next track. Playback stops at the end of the act. Starting another act pauses the previous player. A missing recording produces a readable status message and never displays a fictitious duration.

## Publish with GitHub Pages

1. Create a repository and upload the **contents of this folder** to its root, keeping `index.html` at the root. Include `assets`, `audio`, and `.nojekyll`.
2. Enable GitHub Pages for that repository and select the branch containing the website, with the root folder as its publishing source.
3. Open the Pages URL supplied by GitHub after publishing completes.
4. Add recordings using the same folder layout and commit changes to update the website.

This project has no server component or secret configuration. It also works on any static host. Large recordings may exceed your repository or hosting limits; check those limits before uploading. External audio hosts need HTTPS and appropriate cross-origin support; same-origin files are the simplest option.

## Editing

- `index.html`: entrance, introduction, final story, navigation.
- `album.js`: all act narratives, exact track order, descriptions, recording paths, download settings.
- `style.css`: palette, typography, responsive layout.
- `player.js`: the three independent HTML audio players.
- `assets/act-1.svg` through `act-3.svg`: original illustrated covers. These are decorative contemporary artwork, not archival circus documents.

The supplied Nymph WAV has been connected and browser-tested for playback, pause, seeking, and its inline description. Check other tracks after adding their recordings. Select each track, confirm its duration, seek, pause/resume, move between tracks, and start a different act to confirm the earlier one pauses.

## Expandable track descriptions

Select a track name to expand its full description directly underneath inside the player and start playback. Select the same name again to collapse it without interrupting playback. Selecting another track opens that song and collapses the previous description. The play/pause button controls playback separately. All song descriptions remain accessible even before recordings are added. There are no modal dialogs.

## Included working prototype

Act I selects Nymph of the Flowing Veil by default. Click its play button or track row to hear your supplied September 14 mix and expand its description. A browser-compatible 16-bit, 44.1 kHz WAV copy is included; the original source remains untouched. Its duration is read from the recording (approximately 4:34). The other seventeen songs have no recordings attached yet. `serve.py` supports audio range requests so seeking works during local preview. No audio has been published to an external host.


### Track recording details

Each track in `album.js` supports `recorded` (a confirmed recording date in `YYYY-MM-DD` format, or `null`) and `duration` (seconds, when measured). Missing values display as dashes. When an audio file loads, its measured duration updates the track’s length automatically. Save measured durations in `album.js` to show them before playback. Never infer recording dates from upload dates or file modification times.
