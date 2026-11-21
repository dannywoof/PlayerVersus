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
| super_oracle.ogg | Mystical Enigmatic Background Music | Cleyton Kauffman | 2015 | [mystical-enigmatic-background-music](https://opengameart.org/content/mystical-enigmatic-background-music) |
| super_raven.ogg | "Crow Man's Stage" (fast) | Spring Spring | 2018 | [crow-mans-stage](https://opengameart.org/content/crow-mans-stage) |
| super_scarecrow.ogg | scarecrow [16bit] | obscure music | 2017 | [scarecrow-16bit](https://opengameart.org/content/scarecrow-16bit) (CC-BY 3.0 / CC0) |
| super_strongman.ogg | Fistauffjustice | Sudocolon | 2015 | [fistauffjustice](https://opengameart.org/content/fistauffjustice) |
| super_tinker.ogg | Welcome to the machine (Tale on the Late) | Komiku (Loyalty Freak Music) | 2018 | [welcome-to-the-machine](https://opengameart.org/content/welcome-to-the-machine) |
| super_undertaker.ogg | Kokopelli's Graveyard Theme | Cleyton Kauffman | 2018 | [kokopellis-graveyard-theme](https://opengameart.org/content/kokopellis-graveyard-theme) |
| super_warden.ogg | Synthia's Prison Escape (in-game) | Spring Spring | 2018 | [synthias-prison-escape](https://opengameart.org/content/synthias-prison-escape) |
| super_zero.ogg | ring master (battle, black) | Bobjt | 2018 | [ring-master](https://opengameart.org/content/ring-master) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala, Bobjt, The Cynic Project, Indieteur), and all of them are worth thanking in the game's credits.
