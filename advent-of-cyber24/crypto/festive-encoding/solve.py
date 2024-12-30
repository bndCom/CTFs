from emoji import *
emojis = '''🦌🔔🎅🎳 🎁❄️⛄🎶🦌,

🎤🎮🎨 🦌⛄🦌 🎭❄️🔔 🦌🎅⛄🎶🎤 🎁🎭🕯️!!!

⛄'🎵 🎰🎮 🎲🎳🎮🎨🦌 🎮🕯️ 🎤🎮🎨.

🎰🎮🎵🔔🎮🎸🔔 🎵🎅🎤 🎁🎮🎸🎭🎅🎁🎭 🎤🎮🎨 🎰🎮🎮🎸.

🕯️🎮🎳 🎵🎅🎸🦌🎅🎭🎮🎳🎤 🔔🎵🎲🎶🎮🎤🎵🔔🎸🎭 🎅🎭 🎭❄️🔔 🎸🎮🎳🎭❄️ 🎲🎮🎶🔔.

🎅 🎮🎸🔔 🦌🎮🎶🎶🎅🎳 🎲🔔🎳 🎁❄️🎳⛄🎰🎭🎵🎅🎰. 🕯️🎨🎶🎶-🎭⛄🎵🔔.

🎵🔔🎳🎳🎤 🎁❄️🎳⛄🎰🎭🎵🎅🎰!'''
chars = '''DEAR CHILD,

YOU DID THE DAILY CTF!!!

I'M SO PROUD OF YOU.

SOMEONE MAY CONTACT YOU SOON.

FOR MANDATORY EMPLOYMENT AT THE NORTH POLE.

A ONE DOLLAR PER CHRISTMAS. FULL-TIME.

MERRY CHRISTMAS!'''
list_emoji = [e for e in emojis if is_emoji(e)]
print(list_emoji)
list_chars = [e for e in chars if ord(e) >= 65 and ord(e) <= 90]
print(list_chars)
enc = open("enc", 'r').read()

if len(list_chars) != len(list_emoji):
    print(f"chars: {len(list_chars)}, emoji: {len(list_emoji)}")
    print("lengths are not equal")
    exit(-1)

mp = {list_emoji[i]: list_chars[i] for i in range(len(list_emoji))}

print("".join(mp.get(e) if is_emoji(e) and e in list_emoji else e for e in enc))

# complete the remaining non mapped emojis by your own
# CSD{BAG_BIG_JAW_BOX_WEB_VOW_WAX_BAGGY_WAVY_WOVEN_GLOW}