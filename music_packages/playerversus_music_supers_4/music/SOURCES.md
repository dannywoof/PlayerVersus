# Music sources

Every track here is human-made music released under **CC0** (public domain: free for commercial
use, no attribution required) on [OpenGameArt](https://opengameart.org). All of them were
published between 2010 and 2020, before generative music tools were in use, and none of the pages
mentions AI. Some are dual-licensed (OGA-BY 3.0, CC-BY 3.0 or GPL 3.0, each alongside CC0) and are used under CC0.
The Holst recording is a U.S. government work, in the public domain, and marked CC0 on OpenGameArt.

Each was converted unedited (apart from the format) to Ogg Vorbis, quality 3, 44.1 kHz, with
EBU R128 loudness normalization to -16 LUFS so that tracks sit at the same volume:

    ffmpeg -i SOURCE -vn -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 44100 -c:a libvorbis -q:a 3 NAME.ogg

and then, to keep this package small enough for the registry, re-encoded at quality 0 (about
64 kbps):

    ffmpeg -i NAME.ogg -map_metadata 0 -c:a libvorbis -q:a 0 music/NAME.ogg

PLAYER VERSUS's `music.fw` picks what plays: the menus, a rotating set of fight tracks (a finale track for a
deciding round), the item draft, the result jingle, and each fighter's own theme for their super.

| File | Track | Author | Published | Page |
|---|---|---|---|---|
| super_clockwork.ogg | Clocktower / Clockwise / Clockwork / Time Passing / Loop | KiluaBoy | 2018 | [clocktower-clockwise-clockwork-time-passing-loop](https://opengameart.org/content/clocktower-clockwise-clockwork-time-passing-loop) |
| super_conductor.ogg | Chase! | Wolfgang_ | 2018 | [chase](https://opengameart.org/content/chase) |
| super_deadbolt.ogg | Dark Rooms and Scary Things | isaiah658 | 2016 | [dark-rooms-and-scary-things](https://opengameart.org/content/dark-rooms-and-scary-things) |
| super_death.ogg | The Plague | Indieteur | 2018 | [the-plague](https://opengameart.org/content/the-plague) |
| super_flasque.ogg | The Hex (mix Hex 09) | Steven Ruud (The Cynic Project, cynicmusic) | 2018 | [the-hex](https://opengameart.org/content/the-hex) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala, Bobjt, The Cynic Project, Indieteur), and all of them are worth thanking in the game's credits.
