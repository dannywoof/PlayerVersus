"""Builds PLAYER VERSUS's sound effects from human-made CC0 sources (Kenney, OpenGameArt).

    python3 tools/import_sounds.py <downloads> assets/sounds

<downloads> holds kenney/<pack>/ (each Kenney pack unzipped: impact-sounds, rpg-audio,
interface-sounds, sci-fi-sounds, digital-audio) and oga/dl/<page-slug>/ (each OpenGameArt
page's attachments, unpacked). assets/sounds/SOURCES.md lists every pack with its link.
"""
import array, os, subprocess, sys

WEB = sys.argv[1]           # folder holding kenney/ and oga/dl/
OUT = sys.argv[2]           # assets/sounds
K = os.path.join(WEB, "kenney")
O = os.path.join(WEB, "oga", "dl")
F = os.path.join(O, "the-free-firearm-sound-library", "Prepared SFX Library")


def onset(src, start=0.0, window=1.5, threshold=0.1):
    """Seconds into `src` where the sound first reaches `threshold` of its peak, from `start`."""
    raw = subprocess.run(["sox", src, "-t", "raw", "-r", "8000", "-e", "float", "-b", "32", "-c", "1", "-",
                          "trim", str(start), str(window)], capture_output=True, check=True).stdout
    a = array.array("f", raw)
    peak = max(abs(x) for x in a)
    return start + next(i for i, x in enumerate(a) if abs(x) > threshold * peak) / 8000


def make(name, src, length, start=0.0, effects=(), fade=0.08, gain=-1.0, window=1.5):
    out = os.path.join(OUT, name + ".wav")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    at = max(0.0, onset(src, start, window) - 0.004)
    cmd = ["sox", src, "-r", "44100", "-b", "16", out, "trim", f"{at:.4f}", str(length), *effects,
           "fade", "t", "0.002", "0", str(fade), "norm", str(gain)]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"{name:34s} <- {os.path.relpath(src, WEB)} @{at:.3f}s")


def k(pack, file):
    for root, _, files in os.walk(os.path.join(K, pack)):
        for f in files:
            if f == file:
                return os.path.join(root, f)
    raise FileNotFoundError(f"{pack}/{file}")


def o(*parts):
    p = os.path.join(O, *parts)
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    return p


RPG = ("rpg-sound-pack", "RPG Sound Pack")
YELL = ("male-gruntyelling-sounds", "yelling sounds")
SWORDS = "20-sword-sound-effects-attacks-and-clashes"

# --- Guns: real recordings (The Free Firearm Sound Library). `start` is near the first shot.
# Quickdraw's and Eagle's shots (weapons/snake_9mm_single.wav, weapons/snake_308_single.wav) are
# "9mm Single" and ".308 Single" from Snake's SECOND Authentic Gun Sounds, copied unedited.
make("weapons/pistol_1911", os.path.join(F, "1911", "A_42P.wav"), 0.8, 0.8)
make("weapons/shotgun_mossberg", os.path.join(F, "Mossberg", "N_26P.wav"), 1.0, 0.65)
make("weapons/shotgun_nova", os.path.join(F, "Nova", "O_17P.wav"), 1.0, 0.55)
make("weapons/reload_click", k("rpg-audio", "metalClick.ogg"), 0.2)
make("weapons/latch", k("rpg-audio", "metalLatch.ogg"), 0.35)
make("weapons/casing", o(*RPG, "inventory", "metal-small1.wav"), 0.35, effects=("pitch", "500"), gain=-3)
# A ricochet: a light metal ping, bent downward and given a short tail.
make("weapons/ricochet", k("impact-sounds", "impactMetal_light_002.ogg"), 0.6,
     effects=("pad", "0", "0.4", "pitch", "900", "bend", "0.01,-1400,0.4"),
     fade=0.2)

# --- Blades and swings
make("blades/swing_light", o("swishes-sound-pack", "swishes", "swish-7.wav"), 0.25, fade=0.05)
make("blades/swing_a", o("swishes-sound-pack", "swishes", "swish-3.wav"), 0.25, fade=0.05)
make("blades/swing_b", o("swishes-sound-pack", "swishes", "swish-9.wav"), 0.25, fade=0.05)
make("blades/swing_c", o(*RPG, "battle", "swing.wav"), 0.25, fade=0.05)
make("blades/swing_fist_a", o(*RPG, "battle", "swing2.wav"), 0.2, fade=0.05)
make("blades/swing_fist_b", o("swishes-sound-pack", "swishes", "swish-5.wav"), 0.2, fade=0.05)
make("blades/whoosh_long", o("battle-sound-effects", "battle_sound_effects", "swish_3.wav"), 0.45)
make("blades/whoosh_short", o("battle-sound-effects", "battle_sound_effects", "swish_2.wav"), 0.3)
make("blades/slash", o(SWORDS, "sword - StarNinjas", "sword.4.ogg"), 0.45)
make("blades/clash_a", o(SWORDS, "sword_clash.2.ogg"), 0.4)
make("blades/clash_b", o(SWORDS, "sword_clash.3.ogg"), 0.4)
make("blades/clash_c", o(SWORDS, "sword_clash.8.ogg"), 0.4)
make("blades/parry", o(SWORDS, "sword_clash.1.ogg"), 0.55, fade=0.2)
make("blades/shield_block", o("10-impactshield-blocks", "impact.2.ogg"), 0.4)
make("blades/unsheathe", o(*RPG, "battle", "sword-unsheathe.wav"), 0.4)

# --- Bodies and impacts
make("impacts/punch_a", k("impact-sounds", "impactPunch_medium_000.ogg"), 0.3)
make("impacts/punch_b", k("impact-sounds", "impactPunch_medium_002.ogg"), 0.3)
make("impacts/punch_c", k("impact-sounds", "impactPunch_heavy_001.ogg"), 0.35)
make("impacts/hit", k("impact-sounds", "impactPunch_heavy_000.ogg"), 0.35)
make("impacts/hit_heavy", k("impact-sounds", "impactPunch_heavy_003.ogg"), 0.45, effects=("pitch", "-200"))
make("impacts/thud", k("impact-sounds", "impactSoft_heavy_000.ogg"), 0.4)
make("impacts/footstep", k("impact-sounds", "footstep_concrete_000.ogg"), 0.3)
make("impacts/explosion", o("25-cc0-bang-firework-sfx", "bang_01.ogg"), 0.9, fade=0.3)
make("impacts/explosion_big", k("sci-fi-sounds", "lowFrequency_explosion_000.ogg"), 1.6, fade=0.5)
make("impacts/launch", o("25-cc0-bang-firework-sfx", "fw_01.ogg"), 0.7, fade=0.2)
make("impacts/splash", o("40-cc0-water-splash-slime-sfx", "splash_02.ogg"), 0.5)
# HAMMERHEAD's drag under: the plunge, the air going out, coming back up.
make("impacts/plunge", o("40-cc0-water-splash-slime-sfx", "splash_04.ogg"), 1.0, fade=0.25)
make("impacts/bubbles_a", o("40-cc0-water-splash-slime-sfx", "bubble_01.ogg"), 0.7, fade=0.15, gain=-4.0)
make("impacts/bubbles_b", o("40-cc0-water-splash-slime-sfx", "bubble_02.ogg"), 0.36, fade=0.1, gain=-4.0)
make("impacts/surface", o("40-cc0-water-splash-slime-sfx", "splash_10.ogg"), 0.32, fade=0.1)

# --- Creatures and voices
make("creatures/growl", o("80-cc0-rpg-sfx", "creature_roar_01.ogg"), 0.6, fade=0.15)
make("creatures/ambush", o(*RPG, "NPC", "shade", "shade1.wav"), 0.9, fade=0.25)
make("creatures/bite", o(*RPG, "NPC", "beetle", "bite-small.wav"), 0.3)
make("creatures/hiss", o("80-cc0-creature-sfx", "breath.ogg"), 0.4, fade=0.15)
make("creatures/spit", o("80-cc0-creature-sfx", "spit_01.ogg"), 0.4)
make("voice/kiai", o(*YELL, "1yell9.wav"), 0.4, fade=0.12)

# --- Magic and tech
make("magic/cast_fire", o("80-cc0-rpg-sfx", "spell_fire_07.ogg"), 0.55, fade=0.15)
make("magic/heal", o("magic-spell-sfx", "magical_1_0.ogg"), 1.2, fade=0.4)
make("magic/shimmer", o("magic-spell-sfx", "magical_3.ogg"), 1.0, fade=0.4)
make("magic/wisp", o("magic-spell-sfx", "magical_5.ogg"), 0.9, fade=0.4)
make("magic/cloak", o("freeze-spell-0", "freeze.wav"), 1.2, fade=0.4)
make("magic/charge", k("sci-fi-sounds", "forceField_000.ogg"), 0.8, fade=0.3)
make("magic/rift", k("digital-audio", "phaseJump1.ogg"), 0.6, fade=0.2)
make("magic/flash", k("sci-fi-sounds", "forceField_002.ogg"), 0.5, fade=0.2)
make("magic/beam", k("sci-fi-sounds", "laserLarge_000.ogg"), 0.6, fade=0.2)
make("magic/zap", k("sci-fi-sounds", "laserSmall_000.ogg"), 0.4, fade=0.1)

# --- Interface
make("ui/move", k("interface-sounds", "click_001.ogg"), 0.15, fade=0.03, gain=-4)
make("ui/pick", k("interface-sounds", "confirmation_001.ogg"), 0.6, fade=0.1, gain=-3)
make("ui/deny", k("interface-sounds", "error_004.ogg"), 0.4, fade=0.1, gain=-3)
make("ui/bell", k("impact-sounds", "impactBell_heavy_000.ogg"), 1.5, fade=0.5)

# --- Money, cards and odd jobs (added for MONOPOLIST, CAT, STAB and the item draft). Kenney's casino and
# RPG packs here are the OpenGameArt uploads (kenney/casino-audio, kenney/rpg-audio: "54 Casino sound
# effects" and "50 RPG sound effects").
make("money/coin_a", o("12-coin-sound-effects", "coins_-_starninjas", "coin.1.ogg"), 0.45, fade=0.15)
make("money/coin_b", o("12-coin-sound-effects", "coins_-_starninjas", "coin.5.ogg"), 0.6, fade=0.2)
make("money/coin_drop", o("coin-drop", "coin_drop.wav"), 1.4, fade=0.4)
make("money/coin_splash", o("coin-splash", "coinsplash_0.ogg"), 0.33, fade=0.1)
make("money/gold_sack", o("sack-of-gold", "gold_sack.wav"), 1.2, fade=0.4)
make("money/coins_handle", k("rpg-audio", "handleCoins.ogg"), 0.6, fade=0.2)
make("money/coins_handle2", k("rpg-audio", "handleCoins2.ogg"), 0.6, fade=0.2)
make("money/chips", k("casino-audio", "chips-collide-1.ogg"), 0.5, fade=0.15)
make("money/chip_stack", k("casino-audio", "chips-handle-2.ogg"), 0.6, fade=0.2)
make("money/card_shuffle", k("casino-audio", "card-shuffle.ogg"), 0.9, fade=0.3)
make("money/card_fan", k("casino-audio", "card-fan-1.ogg"), 0.5, fade=0.15)
make("money/card_place", k("casino-audio", "card-place-1.ogg"), 0.3, fade=0.1)
make("blades/knife_slice", k("rpg-audio", "knifeSlice.ogg"), 0.4, fade=0.1)
make("blades/draw_knife", k("rpg-audio", "drawKnife1.ogg"), 0.4, fade=0.1)
make("blades/chop", k("rpg-audio", "chop.ogg"), 0.4, fade=0.1)
make("magic/book_flip", k("rpg-audio", "bookFlip1.ogg"), 0.4, fade=0.1)
make("impacts/cloth", k("rpg-audio", "cloth2.ogg"), 0.4, fade=0.1)
make("impacts/creak", k("rpg-audio", "creak1.ogg"), 0.7, fade=0.2)
