# Music sources

Every track here is human-made music released under **CC0** (public domain: free for commercial
use, no attribution required) on [OpenGameArt](https://opengameart.org). All of them were
published between 2010 and 2020, before generative music tools were in use, and none of the pages
mentions AI. Three are dual-licensed OGA-BY 3.0 / CC0 and are used under CC0.

Each was converted unedited (apart from the format) to Ogg Vorbis, quality 3, 44.1 kHz, with
EBU R128 loudness normalization to -16 LUFS so that tracks sit at the same volume:

    ffmpeg -i SOURCE -vn -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 44100 -c:a libvorbis -q:a 3 NAME.ogg

`music.fw` picks what plays: the menus, a rotating set of fight tracks (a finale track for a
deciding round), the item draft, the result jingle, and each fighter's own theme for their super.

| File | Track | Author | Published | Page |
|---|---|---|---|---|
| title.ogg | Opening Theme [Action/Suspense] (V2) | nene | 2017 | [opening-theme-actionsuspense](https://opengameart.org/content/opening-theme-actionsuspense) |
| select.ogg | Party Sector | Joth | 2016 | [party-sector](https://opengameart.org/content/party-sector) |
| shop.ogg | Buy Something! | Cleyton Kauffman | 2016 | [shop-theme](https://opengameart.org/content/shop-theme) |
| victory.ogg | Victory | celestialghost8 | 2017 | [victory](https://opengameart.org/content/victory) |
| defeat.ogg | No Hope | Cleyton Kauffman | 2015 | [game-over-theme](https://opengameart.org/content/game-over-theme) |
| results.ogg | Ending (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_1.ogg | Level 1 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_2.ogg | Level 2 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_3.ogg | Level 3 (Retro Game Music Pack) | Juhani Junkala (SubspaceAudio) | 2016 | [5-chiptunes-action](https://opengameart.org/content/5-chiptunes-action) |
| fight_4.ogg | Fast fight / battle music (looped) | Ville Nousiainen; loop by XCVG | 2016 | [fast-fight-battle-music-looped](https://opengameart.org/content/fast-fight-battle-music-looped) |
| fight_5.ogg | Pressure | yd | 2012 | [pressure](https://opengameart.org/content/pressure) |
| fight_6.ogg | Random Battle | controllerhead | 2015 | [random-battle](https://opengameart.org/content/random-battle) |
| fight_7.ogg | Eye of the Storm | Joth | 2016 | [eye-of-the-storm](https://opengameart.org/content/eye-of-the-storm) |
| fight_8.ogg | Determination | artisticdude | 2010 | [determination](https://opengameart.org/content/determination) |
| fight_9.ogg | Black Diamond | Joth | 2020 | [black-diamond](https://opengameart.org/content/black-diamond) |
| finale_1.ogg | Epic Boss Battle [Seamlessly Looping] | Juhani Junkala (SubspaceAudio) | 2016 | [boss-battle-music](https://opengameart.org/content/boss-battle-music) |
| finale_2.ogg | Boss Battle #2 [Symphonic Metal] (loop) | nene | 2018 | [boss-battle-2-symphonic-metal](https://opengameart.org/content/boss-battle-2-symphonic-metal) |
| super_fangs.ogg | Vampire's Piano | TAD | 2020 | [vampires-piano](https://opengameart.org/content/vampires-piano) |
| super_aster.ogg | Rock theme | obscure music | 2014 | [rock-theme](https://opengameart.org/content/rock-theme) |
| super_anaconda.ogg | Rat Sewer | HaelDB | 2010 | [rat-sewer](https://opengameart.org/content/rat-sewer) (OGA-BY 3.0 / CC0) |
| super_rapier.ogg | "Prepare your swords" | Bojidar Marinov (bojidar-bg) | 2015 | [prepare-your-swords](https://opengameart.org/content/prepare-your-swords) |
| super_quickdraw.ogg | Spaghetti Western | Spring Spring | 2017 | [spaghetti-western](https://opengameart.org/content/spaghetti-western) |
| super_void.ogg | The 9th Circle (V2) | Joth | 2017 | [the-9th-circle](https://opengameart.org/content/the-9th-circle) |
| super_sherman.ogg | Short Theme [Rock/Metal] | nene | 2016 | [short-theme-rockmetal](https://opengameart.org/content/short-theme-rockmetal) |
| super_shepherd.ogg | Night Prowler | Section 31 - Tech (section31) | 2016 | [night-prowler](https://opengameart.org/content/night-prowler) |
| super_don.ogg | Magic Space | CodeManu | 2016 | [magic-space](https://opengameart.org/content/magic-space) |
| super_hotline.ogg | Winning the Race | Section 31 - Tech (section31) | 2015 | [winning-the-race](https://opengameart.org/content/winning-the-race) |
| super_buckshot.ogg | Covert Operations | artisticdude | 2010 | [covert-operations](https://opengameart.org/content/covert-operations) |
| super_stab.ogg | Night of the Streets [Horror/Suspense] | nene | 2017 | [night-of-the-streets-horrorsuspense](https://opengameart.org/content/night-of-the-streets-horrorsuspense) |
| super_atomic.ogg | Menace | yd | 2012 | [menace](https://opengameart.org/content/menace) |
| super_cat.ogg | Carnival Rides | Écrivain | 2011 | [carnival-rides](https://opengameart.org/content/carnival-rides) |
| super_droid.ogg | Anti Matter Magic (T & T Free Cyberpunk Pack) | tricksntraps | 2019 | [t-t-free-cyberpunk-pack](https://opengameart.org/content/t-t-free-cyberpunk-pack) |
| super_laser.ogg | Pulsar [Famitracker 2A03] | celestialghost8 | 2017 | [pulsar-famitracker-2a03](https://opengameart.org/content/pulsar-famitracker-2a03) |
| super_eagle.ogg | Desert Theme (Caravan) | yd | 2011 | [desert-theme](https://opengameart.org/content/desert-theme) |
| super_combatant.ogg | Great Boss | Spring Spring | 2017 | [great-boss](https://opengameart.org/content/great-boss) |
| super_phantom.ogg | Mysterious | nene | 2017 | [mysterious](https://opengameart.org/content/mysterious) |
| super_carbon.ogg | Cave Theme | Brandon75689 (uploaded by HaelDB) | 2010 | [cave-theme](https://opengameart.org/content/cave-theme) (OGA-BY 3.0 / CC0) |
| super_monopolist.ogg | 8bit Bossa | Joth | 2016 | [bossa-nova](https://opengameart.org/content/bossa-nova) |
| super_mirrorman.ogg | Etirwer (Looped) | Kistol | 2013 | [etirwer](https://opengameart.org/content/etirwer) |
| super_bob.ogg | Talking Cute (Chiptune) | Alex McCulloch (Pro Sensory) | 2017 | [talking-cute-chiptune](https://opengameart.org/content/talking-cute-chiptune) |
| super_teleman.ogg | Life in Corrupted Binary | HaelDB | 2011 | [life-corrupted-binary](https://opengameart.org/content/life-corrupted-binary) (OGA-BY 3.0 / CC0) |
| super_dismantle.ogg | Zombies' March (Zombies Are Coming) | yd | 2012 | [zombies-march](https://opengameart.org/content/zombies-march) |
| super_spruce.ogg | Shrine | yd | 2012 | [shrine](https://opengameart.org/content/shrine) |

Credit is not required by any of these licenses, but several authors ask kindly for it (Joth,
Cleyton Kauffman, Section 31, Bojidar Marinov, Kistol, Alex McCulloch, Ville Nousiainen and XCVG,
Juhani Junkala), and all of them are worth thanking in the game's credits.
