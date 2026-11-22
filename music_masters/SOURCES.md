# Music sources

Every track here is human-made music released under **CC0** (public domain: free for commercial
use, no attribution required) on [OpenGameArt](https://opengameart.org). All of them were
published between 2010 and 2020, before generative music tools were in use, and none of the pages
mentions AI. Some are dual-licensed (OGA-BY 3.0, CC-BY 3.0 or GPL 3.0, each alongside CC0) and are used under CC0.
The Holst recording is a U.S. government work, in the public domain, and marked CC0 on OpenGameArt.

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
| super_clockwork.ogg | Clocktower / Clockwise / Clockwork / Time Passing / Loop | KiluaBoy | 2018 | [clocktower-clockwise-clockwork-time-passing-loop](https://opengameart.org/content/clocktower-clockwise-clockwork-time-passing-loop) |
| super_conductor.ogg | Chase! | Wolfgang_ | 2018 | [chase](https://opengameart.org/content/chase) |
| super_deadbolt.ogg | Dark Rooms and Scary Things | isaiah658 | 2016 | [dark-rooms-and-scary-things](https://opengameart.org/content/dark-rooms-and-scary-things) |
| super_death.ogg | The Plague | Indieteur | 2018 | [the-plague](https://opengameart.org/content/the-plague) |
| super_flasque.ogg | The Hex (mix Hex 09) | Steven Ruud (The Cynic Project, cynicmusic) | 2018 | [the-hex](https://opengameart.org/content/the-hex) |
| super_hammerhead.ogg | War on Water: Chapter 3 | yd | 2013 | [war-on-water-tracks](https://opengameart.org/content/war-on-water-tracks) |
| super_hollow.ogg | Evil Battle (Battle- Reborn) | KarateStudios | 2019 | [evil-battle](https://opengameart.org/content/evil-battle) |
| super_maestro.ogg | Mars, the Bringer of War (Holst, The Planets) | Gustav Holst (1914-16), played by the U.S. Air Force Heritage of America Band (1998); uploaded by XCVG | 2015 | [holst-the-planets-suite](https://opengameart.org/content/holst-the-planets-suite) (public domain: a U.S. government recording) |
| super_moth.ogg | Lunar Moth | Locomule | 2019 | [lunar-moth](https://opengameart.org/content/lunar-moth) (GPL 3.0 / CC0) |
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

## PURGATORY

The second mode's tracks (packages playerversus_purgatory and playerversus_purgatory_fights,
installed on demand), chosen and converted the same way.

| File | Track | Author | Published | Page |
|---|---|---|---|---|
| purgatory_menu.ogg | Tragic ambient main menu | haeldb | 2010 | [tragic-ambient-main-menu](https://opengameart.org/content/tragic-ambient-main-menu) |
| purgatory_threshold.ogg | Deep Humidity | tinyworlds | 2014 | [deep-humidity](https://opengameart.org/content/deep-humidity) |
| purgatory_dojo.ogg | Dream 2 (Ambience) | tokyogeisha | 2014 | [dream-2-ambience](https://opengameart.org/content/dream-2-ambience) |
| purgatory_explore_1.ogg | Dungeon Ambience | yd | 2014 | [dungeon-ambience](https://opengameart.org/content/dungeon-ambience) |
| purgatory_explore_2.ogg | Telos Ruins Creepy | Tozan | 2016 | [telos-ruins-creepy](https://opengameart.org/content/telos-ruins-creepy) |
| purgatory_explore_3.ogg | Dark Shrine Loop | qubodup, remixing yd's "Shrine" | 2012 | [dark-shrine-loop](https://opengameart.org/content/dark-shrine-loop) |
| purgatory_explore_4.ogg | The Birth of Evil | spiderdave | 2015 | [the-birth-of-evil](https://opengameart.org/content/the-birth-of-evil) |
| purgatory_combat_1.ogg | Swordfight III | Kistol | 2016 | [swordfight-iii](https://opengameart.org/content/swordfight-iii) |
| purgatory_combat_2.ogg | Fighting is not an option (RPG Battle Theme II) | Cleyton Kauffman | 2015 | [rpg-battle-theme-ii](https://opengameart.org/content/rpg-battle-theme-ii) |
| purgatory_combat_3.ogg | Running from something | haeldb | 2010 | [running-from-something](https://opengameart.org/content/running-from-something) |
| purgatory_boss_1.ogg | Sinister Boss Appears! | cynicmusic | 2018 | [sinister-boss-appears](https://opengameart.org/content/sinister-boss-appears) |
| purgatory_boss_2.ogg | Most Stereotypical Boss Theme Ever | spring spring | 2017 | [most-stereotypical-boss-theme-ever](https://opengameart.org/content/most-stereotypical-boss-theme-ever) |
| purgatory_boss_3.ogg | Last Battle (Free Vapour 2013 Soundtrack) | Alexander Ehlers (tricksntraps) | 2013 (page 2020) | [free-vapour-2013-soundtrack](https://opengameart.org/content/free-vapour-2013-soundtrack) |
| purgatory_finale.ogg | Battle Theme A | cynicmusic (The Cynic Project) | 2013 | [battle-theme-a](https://opengameart.org/content/battle-theme-a) |
| purgatory_satan.ogg | Determined Pursuit (epic orchestra loop) | Emma_MA | 2017 | [determined-pursuit-epic-orchestra-loop](https://opengameart.org/content/determined-pursuit-epic-orchestra-loop) |
| purgatory_meadow.ogg | Ambient Bird Sounds | isaiah658 | 2017 | [ambient-bird-sounds](https://opengameart.org/content/ambient-bird-sounds) |
