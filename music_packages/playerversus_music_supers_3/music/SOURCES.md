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
| super_rapier.ogg | "Prepare your swords" | Bojidar Marinov (bojidar-bg) | 2015 | [prepare-your-swords](https://opengameart.org/content/prepare-your-swords) |
| super_void.ogg | The 9th Circle (V2) | Joth | 2017 | [the-9th-circle](https://opengameart.org/content/the-9th-circle) |
| super_sherman.ogg | Short Theme [Rock/Metal] | nene | 2016 | [short-theme-rockmetal](https://opengameart.org/content/short-theme-rockmetal) |
| super_shepherd.ogg | Night Prowler | Section 31 - Tech (section31) | 2016 | [night-prowler](https://opengameart.org/content/night-prowler) |
| super_stab.ogg | Night of the Streets [Horror/Suspense] | nene | 2017 | [night-of-the-streets-horrorsuspense](https://opengameart.org/content/night-of-the-streets-horrorsuspense) |
| super_teleman.ogg | Life in Corrupted Binary | HaelDB | 2011 | [life-corrupted-binary](https://opengameart.org/content/life-corrupted-binary) (OGA-BY 3.0 / CC0) |
| super_spruce.ogg | Shrine | yd | 2012 | [shrine](https://opengameart.org/content/shrine) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
