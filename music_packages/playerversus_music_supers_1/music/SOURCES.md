# Music sources

Every track here is human-made music released under **CC0** (public domain: free for commercial
use, no attribution required) on [OpenGameArt](https://opengameart.org). All of them were
published between 2010 and 2020, before generative music tools were in use, and none of the pages
mentions AI. Three are dual-licensed OGA-BY 3.0 / CC0 and are used under CC0.

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
| super_aster.ogg | Rock theme | obscure music | 2014 | [rock-theme](https://opengameart.org/content/rock-theme) |
| super_anaconda.ogg | Rat Sewer | HaelDB | 2010 | [rat-sewer](https://opengameart.org/content/rat-sewer) (OGA-BY 3.0 / CC0) |
| super_buckshot.ogg | Covert Operations | artisticdude | 2010 | [covert-operations](https://opengameart.org/content/covert-operations) |
| super_atomic.ogg | Menace | yd | 2012 | [menace](https://opengameart.org/content/menace) |
| super_cat.ogg | Carnival Rides | Écrivain | 2011 | [carnival-rides](https://opengameart.org/content/carnival-rides) |
| super_combatant.ogg | Great Boss | Spring Spring | 2017 | [great-boss](https://opengameart.org/content/great-boss) |
| super_carbon.ogg | Cave Theme | Brandon75689 (uploaded by HaelDB) | 2010 | [cave-theme](https://opengameart.org/content/cave-theme) (OGA-BY 3.0 / CC0) |
| super_bob.ogg | Talking Cute (Chiptune) | Alex McCulloch (Pro Sensory) | 2017 | [talking-cute-chiptune](https://opengameart.org/content/talking-cute-chiptune) |
| super_dismantle.ogg | Zombies' March (Zombies Are Coming) | yd | 2012 | [zombies-march](https://opengameart.org/content/zombies-march) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
