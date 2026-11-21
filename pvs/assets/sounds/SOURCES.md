# Sound sources

Every effect in `blades/`, `creatures/`, `impacts/`, `magic/`, `money/`, `ui/`, `voice/` and `weapons/` is cut from
human-made recordings or sound design released under **CC0** (public domain: free for commercial use,
no attribution required), except the two Snake gunshots noted below. The CC0 sources were published
between 2010 and 2021, before generative audio tools existed; the Snake pack (2022) states that no
generative AI was used. None of the packs uses AI-generated audio.

`tools/import_sounds.py` rebuilds the whole set from the downloaded packs: it trims each clip to where
it starts, cuts it to length, fades it out and normalizes it to 44.1 kHz 16-bit WAV.

| Pack | Author | Published | Used for |
|---|---|---|---|
| [The Free Firearm Sound Library](https://opengameart.org/content/the-free-firearm-sound-library) ([freefirearmsfx.com](http://freefirearmsfx.com)) | bart (upload); Kickstarter-funded field recordings | 2014 | generic shot (1911), shotguns (Mossberg, Nova) |
| [Snake's SECOND Authentic Gun Sounds](https://f8studios.itch.io/snakes-second-authentic-gun-sounds-pack) | SnakeF8 (F8 Studios); recorded by the author, page states "No generative AI was used" | 2022 | Quickdraw (`snake_9mm_single`, "9mm Single") and Eagle (`snake_308_single`, ".308 Single"), unedited. Page: "All sounds can be used commercially, and credit is not needed" |
| Kenney [Impact Sounds](https://kenney.nl/assets/impact-sounds) | Kenney | 2019 | punches, hits, thud, footstep, bell, ricochet (a metal ping bent downward) |
| Kenney [RPG Audio](https://kenney.nl/assets/rpg-audio) | Kenney | — | reload click, latch |
| Kenney [Interface Sounds](https://kenney.nl/assets/interface-sounds) | Kenney | 2020 | menu move, pick, deny |
| Kenney [Sci-fi Sounds](https://kenney.nl/assets/sci-fi-sounds) | Kenney | 2020 | charge, flash, beam, zap, KO explosion |
| Kenney [Digital Audio](https://kenney.nl/assets/digital-audio) | Kenney | — | rift |
| [Swishes Sound Pack](https://opengameart.org/content/swishes-sound-pack) | artisticdude | 2011 | swings |
| [RPG Sound Pack](https://opengameart.org/content/rpg-sound-pack) | artisticdude | 2011 | swings, unsheathe, casing, bite, ambush (shade) |
| [Freeze Spell](https://opengameart.org/content/freeze-spell-0) | artisticdude | 2011 | cloak |
| [Battle Sound Effects](https://opengameart.org/content/battle-sound-effects) | Ogrebane | 2010 | dash and rush whooshes |
| [20 Sword Sound Effects](https://opengameart.org/content/20-sword-sound-effects-attacks-and-clashes) | StarNinjas | 2021 | slash, blade clashes, parry |
| [10 Impact/Shield Blocks](https://opengameart.org/content/10-impactshield-blocks) | StarNinjas | 2021 | block |
| [25 CC0 bang / firework SFX](https://opengameart.org/content/25-cc0-bang-firework-sfx) | rubberduck | 2019 | explosion, rocket launch |
| [40 CC0 water / splash / slime SFX](https://opengameart.org/content/40-cc0-water-splash-slime-sfx) | rubberduck | 2018 | splash; HAMMERHEAD's drag under (plunge, bubbles, surfacing) |
| [80 CC0 RPG SFX](https://opengameart.org/content/80-cc0-rpg-sfx) | rubberduck | 2018 | growl, fire cast |
| [80 CC0 creature SFX](https://opengameart.org/content/80-cc0-creature-sfx) | rubberduck | 2018 | hiss, spit |
| [Magic Spell SFX](https://opengameart.org/content/magic-spell-sfx) | JaggedStone | 2014 | heal, shimmer, wisp |
| [Male Grunt/Yelling sounds](https://opengameart.org/content/male-gruntyelling-sounds) | HaelDB | 2012 | kiai (dual-licensed OGA-BY 3.0 / CC0; used under CC0) |
| Kenney [Casino Audio](https://opengameart.org/content/54-casino-sound-effects-cards-dice-chips) (OpenGameArt upload) | Kenney | 2012 | chips, card shuffle, card fan, card place (MONOPOLIST, CAT, the item draft) |
| Kenney [RPG Audio](https://opengameart.org/content/50-rpg-sound-effects) (OpenGameArt upload) | Kenney | 2014 | coin handling, knife slice, drawing a knife, chop, book page, cloth, creak |
| [12 Coin Sound Effects](https://opengameart.org/content/12-coin-sound-effects) | StarNinjas | 2021 | coins (recorded by rumbling real coins) |
| [Coin Drop](https://opengameart.org/content/coin-drop) | Vinrax | 2014 | coin drop (bankruptcy) |
| [Coin Splash](https://opengameart.org/content/coin-splash) | LordTomorrow | 2020 | coin splash |
| [Sack of Gold](https://opengameart.org/content/sack-of-gold) | Amarikah | 2020 | sack of gold (SOLD!, the bailout, saving) |

Credit is not required, but these authors are worth thanking in the game's credits.

The original procedural and user-supplied WAVs are preserved in `legacy/`. The procedural generator
(`tools/make_sounds.py`) writes to `legacy/generated/`.
