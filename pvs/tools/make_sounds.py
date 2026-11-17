#!/usr/bin/env python3
"""Builds every sound effect of PLAYER VERSUS into assets/sounds/ as WAV files.

    python3 tools/make_sounds.py

Nothing here is a recording: each sound is put together from layers of filtered noise,
sine sweeps and ringing partials, the way a gunshot is a crack, a body and a tail. To use a
recorded effect instead, drop a WAV or OGG with the same name into assets/sounds/ (and do
not run this again, or it will be overwritten). The game falls back to a plain beep for any
file that is missing. Needs numpy.
"""
import os
import wave
import numpy as np

RATE = 44100
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "sounds", "legacy", "generated")
rng = np.random.default_rng(7)


def t(seconds):
    return np.arange(int(RATE * seconds)) / RATE


def noise(seconds, low=20, high=20000):
    """White noise kept between two frequencies."""
    n = int(RATE * seconds)
    spectrum = np.fft.rfft(rng.standard_normal(n))
    freqs = np.fft.rfftfreq(n, 1 / RATE)
    # Soft edges, so the band does not ring.
    keep = 1 / (1 + (low / np.maximum(freqs, 1)) ** 6) / (1 + (freqs / high) ** 6)
    out = np.fft.irfft(spectrum * keep, n)
    return out / (np.max(np.abs(out)) + 1e-9)


def decay(seconds, tau):
    return np.exp(-t(seconds) / tau)


def bell(seconds, power=1.0):
    """Up and down again: the shape of something passing."""
    return np.sin(np.pi * t(seconds) / seconds) ** power


def attack(x, seconds=0.002):
    n = min(int(RATE * seconds), len(x))
    x = x.copy()
    x[:n] *= np.linspace(0, 1, n)
    return x


def sweep(seconds, start, finish, curve=1.0, shape="sine"):
    """A tone sliding from one pitch to another."""
    x = t(seconds) / seconds
    freq = start + (finish - start) * x ** curve
    phase = 2 * np.pi * np.cumsum(freq) / RATE
    if shape == "saw":
        return 2 * ((phase / (2 * np.pi)) % 1) - 1
    if shape == "square":
        return np.sign(np.sin(phase))
    return np.sin(phase)


def ring(seconds, partials, tau, spread=0.6):
    """Struck metal: partials that do not line up, the high ones dying first."""
    out = np.zeros(int(RATE * seconds))
    x = t(seconds)
    for i, f in enumerate(partials):
        out += np.sin(2 * np.pi * f * x + rng.uniform(0, 6.28)) * np.exp(-x / (tau * spread ** i)) / (1 + i * 0.4)
    return out


def mix(*layers):
    """Layers of (samples, gain[, start seconds]) laid over each other."""
    length = max(len(l[0]) + int(RATE * (l[2] if len(l) > 2 else 0)) for l in layers)
    out = np.zeros(length)
    for l in layers:
        at = int(RATE * (l[2] if len(l) > 2 else 0))
        out[at:at + len(l[0])] += l[0] * l[1]
    return out


def room(x, wet=0.25, tail=0.25):
    """A little air after the sound: a few fading echoes."""
    out = np.concatenate([x, np.zeros(int(RATE * tail))])
    for delay, gain in ((0.023, 0.5), (0.041, 0.35), (0.067, 0.25), (0.097, 0.15)):
        d = int(RATE * delay)
        out[d:d + len(x)] += x * gain * wet
    return out


def drive(x, amount=2.0):
    return np.tanh(x * amount) / np.tanh(amount)


def save(name, x, level=0.85):
    x = np.asarray(x, dtype=float)
    fade = min(int(RATE * 0.01), len(x))
    x[-fade:] *= np.linspace(1, 0, fade)
    x = x / (np.max(np.abs(x)) + 1e-9) * level
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(RATE)
        f.writeframes((x * 32767).astype("<i2").tobytes())


# --- Guns --------------------------------------------------------------------------------------

def gunshot(crack, body, thump, tail, low_from, low_to, bite=3.0):
    """The crack of the powder, the body of the report, the thump you feel, and the air after."""
    return drive(mix(
        (noise(0.03, 2500, 16000) * decay(0.03, 0.004), crack),
        (noise(0.22, 250, 3200) * decay(0.22, 0.035), body),
        (sweep(0.3, low_from, low_to, 0.5) * decay(0.3, 0.06), thump),
        (noise(tail, 120, 1400) * decay(tail, tail / 4), 0.35, 0.01),
    ), bite)


def click(freq, seconds=0.03):
    return mix((noise(0.004, 1500, 12000), 1.0), (ring(seconds, [freq, freq * 2.3, freq * 3.7], seconds / 3), 0.6))


def guns():
    for i, (a, b) in enumerate(((1.0, 150), (0.9, 165), (1.1, 140))):
        save(f"pistol{i + 1}", room(gunshot(a, 0.8, 0.7, 0.3, b, 55), 0.2, 0.2))
    for i, b in enumerate((115, 105)):
        # A heavy revolver: slower, lower, and it rolls on.
        save(f"revolver{i + 1}", room(gunshot(1.0, 1.0, 1.1, 0.55, b, 38, 3.6), 0.35, 0.35))
    for i, b in enumerate((95, 88)):
        # A shotgun is two reports nearly on top of each other and a long, wide tail.
        one = gunshot(0.8, 1.2, 1.2, 0.7, b, 34, 4.0)
        save(f"shotgun{i + 1}", room(mix((one, 1.0), (one * 0.5, 1.0, 0.012)), 0.45, 0.45))
    save("cock", mix((click(1900), 1.0), (click(1300, 0.04), 0.9, 0.07)))
    save("reload", mix((click(2400, 0.02), 0.8), (click(1500, 0.03), 1.0, 0.045)))
    save("empty", click(900, 0.02), 0.5)
    save("casing", mix((ring(0.12, [3900, 5600, 7300], 0.03), 1.0), (ring(0.1, [4200, 6100], 0.02), 0.6, 0.09),
                       (ring(0.08, [4500, 6400], 0.015), 0.35, 0.15)), 0.5)
    x = t(0.5)
    whine = np.sin(2 * np.pi * np.cumsum(3200 * np.exp(-x * 2.6) + 500 + 60 * np.sin(x * 70)) / RATE)
    save("ricochet", mix((noise(0.02, 2000, 12000) * decay(0.02, 0.004), 0.8), (whine * decay(0.5, 0.16), 1.0)), 0.6)
    save("launch", room(mix((noise(0.7, 150, 2600) * attack(decay(0.7, 0.22), 0.03), 1.0),
                            (sweep(0.7, 90, 240, 1.5) * bell(0.7, 0.6), 0.6),
                            (noise(0.05, 1000, 9000) * decay(0.05, 0.01), 0.7)), 0.3))
    save("zap", mix((sweep(0.28, 2600, 500, 0.5, "saw") * decay(0.28, 0.07), 0.6),
                    (sweep(0.28, 3900, 760, 0.5) * decay(0.28, 0.06), 0.6),
                    (noise(0.05, 4000, 15000) * decay(0.05, 0.012), 0.5)))
    save("beam", mix((sweep(0.4, 950, 880, 1, "saw") * bell(0.4, 0.4) * (1 + 0.4 * np.sin(t(0.4) * 380)), 0.5),
                     (sweep(0.4, 1900, 1760) * bell(0.4, 0.4), 0.5), (noise(0.4, 3000, 12000) * bell(0.4, 0.5), 0.25)), 0.6)


# --- Blades, fists and bodies ------------------------------------------------------------------

def whoosh(seconds, low, high, tilt=1.0):
    """Air parting: two bands crossing, so the pitch seems to rise through the swing."""
    a = noise(seconds, low, high * 0.5) * bell(seconds, 2) * (1 - t(seconds) / seconds) ** tilt
    b = noise(seconds, low * 2, high) * bell(seconds, 2) * (t(seconds) / seconds) ** tilt
    return a + b


def blades():
    for i, (s, hi) in enumerate(((0.2, 7000), (0.17, 8500), (0.24, 6000))):
        # A blade sings a little as it cuts the air.
        save(f"blade_swing{i + 1}", mix((whoosh(s, 900, hi), 1.0),
                                        (sweep(s, 2600, 3400) * bell(s, 3), 0.08)), 0.6)
    for i, base in enumerate((2300, 2700, 2000)):
        save(f"blade_hit{i + 1}", mix((noise(0.08, 2500, 12000) * decay(0.08, 0.015), 1.0),
                                      (ring(0.2, [base, base * 1.51, base * 2.2], 0.05), 0.35),
                                      (noise(0.12, 150, 900) * decay(0.12, 0.03), 0.9),
                                      (sweep(0.1, 170, 70) * decay(0.1, 0.03), 0.6)))
    for i, base in enumerate((2100, 2500)):
        # Steel on steel: a hard tick and a long bright ring.
        save(f"clash{i + 1}", room(mix((noise(0.01, 3000, 16000), 1.0),
                                       (ring(0.7, [base, base * 1.47, base * 2.09, base * 2.83, base * 3.6], 0.22, 0.75), 0.9)), 0.2))
    save("stab", mix((noise(0.05, 1800, 9000) * decay(0.05, 0.01), 0.8), (noise(0.14, 120, 700) * decay(0.14, 0.035), 1.0),
                     (sweep(0.1, 150, 60) * decay(0.1, 0.03), 0.7)))
    # Drawing steel: a scrape that climbs into a ring.
    save("shing", room(mix((noise(0.3, 3000, 14000) * bell(0.3, 1.5) * (t(0.3) / 0.3), 0.5),
                           (sweep(0.3, 3200, 4200) * bell(0.3, 1), 0.25),
                           (ring(0.6, [4200, 5300, 6900, 8200], 0.2, 0.8), 0.5, 0.24)), 0.2), 0.6)
    save("slash", mix((whoosh(0.16, 1500, 11000, 0.6), 1.0), (ring(0.2, [3300, 4700], 0.05), 0.15, 0.08)), 0.7)
    save("parry", room(mix((noise(0.008, 4000, 16000), 0.8), (ring(0.9, [2900, 4350, 5870, 7400, 9100], 0.3, 0.8), 1.0)), 0.3), 0.7)


def bodies():
    for i, (f, n) in enumerate(((170, 0.022), (190, 0.018), (150, 0.026))):
        save(f"punch{i + 1}", mix((sweep(0.14, f, 60) * decay(0.14, 0.04), 1.0),
                                  (noise(0.09, 300, 2200) * decay(0.09, n), 0.9),
                                  (noise(0.01, 2000, 8000), 0.3)))
    for i, f in enumerate((120, 105)):
        save(f"heavy{i + 1}", drive(mix((sweep(0.3, f, 38) * decay(0.3, 0.08), 1.2),
                                        (noise(0.16, 200, 1800) * decay(0.16, 0.035), 1.0),
                                        (noise(0.03, 1500, 9000) * decay(0.03, 0.006), 0.6)), 2.5))
    for i, hi in enumerate((3200, 4200)):
        save(f"swing{i + 1}", whoosh(0.17, 300, hi), 0.45)
    save("block", mix((sweep(0.12, 240, 110) * decay(0.12, 0.03), 1.0), (noise(0.08, 400, 3000) * decay(0.08, 0.018), 0.8),
                      (ring(0.1, [800, 1270], 0.02), 0.3)), 0.7)
    save("thud", drive(mix((sweep(0.6, 110, 30, 0.6) * decay(0.6, 0.16), 1.2), (noise(0.2, 60, 500) * decay(0.2, 0.06), 0.8)), 2.0))
    save("step", noise(0.06, 80, 900) * decay(0.06, 0.012), 0.5)
    save("dash", whoosh(0.22, 400, 5000, 1.5), 0.5)
    save("rush", mix((whoosh(0.08, 500, 5000), 0.7), (sweep(0.07, 200, 80) * decay(0.07, 0.02), 1.0)), 0.7)
    save("bite", mix((noise(0.04, 1200, 9000) * decay(0.04, 0.008), 1.0), (noise(0.05, 900, 7000) * decay(0.05, 0.01), 0.8, 0.05),
                     (noise(0.12, 150, 800) * decay(0.12, 0.03), 0.9, 0.045)))
    x = t(0.5)
    save("growl", sweep(0.5, 105, 70, 1, "saw") * (0.6 + 0.4 * np.sin(x * 2 * np.pi * 31)) * bell(0.5, 0.5) + noise(0.5, 200, 1200) * bell(0.5, 1) * 0.3, 0.7)
    # A shout: a buzzing throat pushed through two mouth shapes.
    voice = sweep(0.22, 250, 330, 0.5, "saw") * bell(0.22, 0.5)
    save("kiai", mix((voice, 0.4), (noise(0.22, 700, 1100) * bell(0.22, 0.6) * np.abs(voice), 1.0), (noise(0.22, 1900, 2700) * bell(0.22, 0.6), 0.25)), 0.6)
    x = t(0.4)
    mew = np.sin(2 * np.pi * np.cumsum(520 + 280 * np.sin(np.pi * x / 0.4) ** 0.6) / RATE)
    save("meow", mix((np.sign(mew) * 0.25 + mew, 0.5), (noise(0.4, 1400, 3200) * np.abs(mew), 0.6)) * bell(0.4, 0.7), 0.55)
    save("servo", sweep(0.25, 300, 520, 1, "square") * bell(0.25, 0.4) * 0.5 + sweep(0.25, 900, 1560) * bell(0.25, 0.4), 0.35)


# --- Blasts, magic and everything else ------------------------------------------------------------

def blasts():
    save("boom", room(drive(mix((noise(0.04, 800, 9000) * decay(0.04, 0.008), 0.8),
                                (sweep(1.0, 95, 26, 0.5) * decay(1.0, 0.25), 1.3),
                                (noise(1.0, 40, 700) * decay(1.0, 0.22), 1.1),
                                (noise(0.8, 600, 3000) * decay(0.8, 0.1), 0.4)), 3.0), 0.4, 0.4))
    save("splash", mix((noise(0.3, 400, 5000) * decay(0.3, 0.06), 1.0), (noise(0.3, 150, 900) * decay(0.3, 0.09), 0.7),
                       (sweep(0.08, 700, 1500) * decay(0.08, 0.02), 0.3, 0.12), (sweep(0.06, 900, 1900) * decay(0.06, 0.015), 0.25, 0.2)), 0.6)
    save("spit", mix((noise(0.14, 1200, 7000) * bell(0.14, 2), 1.0), (sweep(0.1, 500, 180) * decay(0.1, 0.03), 0.5)), 0.5)
    save("hiss", noise(0.45, 4500, 15000) * attack(decay(0.45, 0.18), 0.04), 0.4)


def magic():
    x = t(0.45)
    save("cast", room(mix((sweep(0.45, 420, 1250, 1.6) * bell(0.45, 0.7) * (1 + 0.3 * np.sin(x * 60)), 0.6),
                          (sweep(0.45, 630, 1880, 1.6) * bell(0.45, 0.8), 0.3),
                          (noise(0.45, 5000, 14000) * bell(0.45, 1.5), 0.2)), 0.4), 0.55)
    notes = [1760, 1480, 1175, 988, 784]
    save("shimmer", room(mix(*[(ring(0.4, [f, f * 2.01, f * 3.02], 0.12), 1.0, i * 0.05) for i, f in enumerate(notes)]), 0.5), 0.5)
    save("heal", room(mix(*[(ring(0.5, [f, f * 2], 0.18), 1.0, i * 0.07) for i, f in enumerate([523, 659, 784, 1047])]), 0.5), 0.5)
    x = t(0.4)
    save("charge", mix((sweep(0.4, 180, 900, 2) * (0.6 + 0.4 * np.sin(x * (40 + 200 * x))) * (x / 0.4), 0.7),
                       (sweep(0.4, 360, 1800, 2, "saw") * (x / 0.4) ** 2, 0.2), (noise(0.4, 2000, 9000) * (x / 0.4) ** 2, 0.2)), 0.55)
    save("flash", mix((sweep(0.18, 2400, 200, 0.4, "saw") * decay(0.18, 0.05), 0.6), (noise(0.18, 1000, 9000) * decay(0.18, 0.04), 0.7)), 0.6)
    swell = noise(0.4, 100, 2500) * (t(0.4) / 0.4) ** 3
    save("rift", mix((swell, 1.0), (sweep(0.4, 70, 480, 2, "saw") * (t(0.4) / 0.4) ** 2, 0.5)), 0.6)
    save("cloak", room(mix((noise(0.55, 300, 5000) * decay(0.55, 0.2) * attack(np.ones(int(RATE * 0.55)), 0.05), 1.0),
                           (sweep(0.55, 800, 160, 0.6) * decay(0.55, 0.2), 0.4)), 0.4), 0.5)
    save("wisp", (sweep(0.7, 280, 920, 1.4) * bell(0.7, 1.2) * 0.6 + noise(0.7, 1500, 6000) * bell(0.7, 2) * 0.4), 0.4)
    save("ambush", room(mix((ring(0.35, [880, 932, 1320], 0.1), 1.0), (noise(0.03, 2000, 9000) * decay(0.03, 0.006), 0.6)), 0.3), 0.6)
    save("bell", room(ring(1.6, [440, 1214, 2376, 3916, 5810], 0.7, 0.7), 0.4), 0.6)
    save("ko", room(drive(mix((ring(1.8, [98, 147, 233, 370, 521], 0.9, 0.8), 1.0), (noise(0.3, 100, 2000) * decay(0.3, 0.06), 0.6),
                              (sweep(0.6, 160, 40) * decay(0.6, 0.15), 0.8)), 1.5), 0.5, 0.5), 0.7)


def odds():
    save("deny", sweep(0.11, 150, 120, 1, "square") * bell(0.11, 0.3) * 0.5 + sweep(0.11, 100, 80, 1, "saw") * 0.5, 0.35)
    save("lock", sweep(0.06, 1000, 1000) * bell(0.06, 0.3), 0.4)
    save("move", ring(0.07, [660, 1320], 0.02), 0.4)
    save("pick", mix((ring(0.12, [660, 1320], 0.04), 1.0), (ring(0.2, [990, 1980], 0.06), 1.0, 0.07)), 0.5)
    x = t(0.5)
    two = (np.sin(2 * np.pi * 1400 * x) + np.sin(2 * np.pi * 1750 * x)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 22 * x)))
    save("phone", two * attack(np.ones(len(x)), 0.01), 0.4)
    horn = sweep(0.35, 392, 392, 1, "saw") + sweep(0.35, 494, 494, 1, "saw")
    save("horn", (horn * 0.5 + noise(0.35, 300, 2500) * np.abs(horn) * 0.3) * attack(bell(0.35, 0.15), 0.01), 0.5)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    guns()
    blades()
    bodies()
    blasts()
    magic()
    odds()
    print(f"{len(os.listdir(OUT))} sounds in {os.path.normpath(OUT)}")
