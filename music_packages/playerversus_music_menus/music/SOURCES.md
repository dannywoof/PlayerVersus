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
| title.ogg | Opening Theme [Action/Suspense] (V2) | nene | 2017 | [opening-theme-actionsuspense](https://opengameart.org/content/opening-theme-actionsuspense) |
| select.ogg | Party Sector | Joth | 2016 | [party-sector](https://opengameart.org/content/party-sector) |
| shop.ogg | Buy Something! | Cleyton Kauffman | 2016 | [shop-theme](https://opengameart.org/content/shop-theme) |
| victory.ogg | Victory | celestialghost8 | 2017 | [victory](https://opengameart.org/content/victory) |
| defeat.ogg | No Hope | Cleyton Kauffman | 2015 | [game-over-theme](https://opengameart.org/content/game-over-theme) |
| results.ogg | Ending (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| finale_1.ogg | Epic Boss Battle [Seamlessly Looping] | Juhani Junkala (SubspaceAudio) | 2016 | [boss-battle-music](https://opengameart.org/content/boss-battle-music) |
| finale_2.ogg | Boss Battle #2 [Symphonic Metal] (loop) | nene | 2018 | [boss-battle-2-symphonic-metal](https://opengameart.org/content/boss-battle-2-symphonic-metal) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
