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
| super_fangs.ogg | Vampire's Piano | TAD | 2020 | [vampires-piano](https://opengameart.org/content/vampires-piano) |
| super_quickdraw.ogg | Spaghetti Western | Spring Spring | 2017 | [spaghetti-western](https://opengameart.org/content/spaghetti-western) |
| super_don.ogg | Magic Space | CodeManu | 2016 | [magic-space](https://opengameart.org/content/magic-space) |
| super_hotline.ogg | Winning the Race | Section 31 - Tech (section31) | 2015 | [winning-the-race](https://opengameart.org/content/winning-the-race) |
| super_droid.ogg | Anti Matter Magic (T & T Free Cyberpunk Pack) | tricksntraps | 2019 | [t-t-free-cyberpunk-pack](https://opengameart.org/content/t-t-free-cyberpunk-pack) |
| super_laser.ogg | Pulsar [Famitracker 2A03] | celestialghost8 | 2017 | [pulsar-famitracker-2a03](https://opengameart.org/content/pulsar-famitracker-2a03) |
| super_eagle.ogg | Desert Theme (Caravan) | yd | 2011 | [desert-theme](https://opengameart.org/content/desert-theme) |
| super_phantom.ogg | Mysterious | nene | 2017 | [mysterious](https://opengameart.org/content/mysterious) |
| super_monopolist.ogg | 8bit Bossa | Joth | 2016 | [bossa-nova](https://opengameart.org/content/bossa-nova) |
| super_mirrorman.ogg | Etirwer (Looped) | Kistol | 2013 | [etirwer](https://opengameart.org/content/etirwer) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
