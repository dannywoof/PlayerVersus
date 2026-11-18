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
| fight_1.ogg | Level 1 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_2.ogg | Level 2 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_3.ogg | Level 3 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_4.ogg | Fast fight / battle music (looped) | Ville Nousiainen; loop by XCVG | 2016 | [fast-fight-battle-music-looped](https://opengameart.org/content/fast-fight-battle-music-looped) |
| fight_5.ogg | Pressure | yd | 2012 | [pressure](https://opengameart.org/content/pressure) |
| fight_6.ogg | Random Battle | controllerhead | 2015 | [random-battle](https://opengameart.org/content/random-battle) |
| fight_7.ogg | Eye of the Storm | Joth | 2016 | [eye-of-the-storm](https://opengameart.org/content/eye-of-the-storm) |
| fight_8.ogg | Determination | artisticdude | 2010 | [determination](https://opengameart.org/content/determination) |
| fight_9.ogg | Black Diamond | Joth | 2020 | [black-diamond](https://opengameart.org/content/black-diamond) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
