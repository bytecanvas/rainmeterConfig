# rainmeter_showcase.py

import time
import webbrowser

def print_with_delay(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_menu():
    print("\n🌧️  Welcome to Personal Rainmeter Configs\n")
    print_with_delay("Hey there, awesome human! 👋")
    print_with_delay("Ready to pimp your desktop? Let's go! 😎✨\n")

    print("🎨 What's Inside?\n")
    skins = {
        "1": ("🎵 Cleartext", "See lyrics dancing on your desktop.", "https://visualskins.com/skin/cleartext"),
        "2": ("🌙 Night Flow", "Late-night vibes in style.", "https://visualskins.com/skin/night-flow"),
        "3": ("🧭 NORTHWEST", "Minimal, organized, and clean.", "https://visualskins.com/skin/northwest"),
        "4": ("🌐 WebNowPlayingRedux", "Shows your online tunes.", "https://github.com/keifufu/WebNowPlaying-Rainmeter/releases/")
    }

    for key, (name, desc, _) in skins.items():
        print(f"{key}. {name} — {desc}")

    print("\n🚀 How to Use")
    steps = [
        "Download & install Rainmeter: https://www.rainmeter.net/",
        "Grab the skins from the links above.",
        "Drop them in your Rainmeter Skins folder.",
        "Open Rainmeter, load your new skins, and customize!"
    ]
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

    print("\n🤔 Why use these?")
    print("- Simple, stylish, no rocket science.")
    print("- Great for music lovers & minimalists.")
    print("- Impress your friends (or confuse them). 😜\n")

    print("💬 Got feedback?")
    print("Open an issue or send a message. Let’s make desktop magic. 🔥\n")

    print("✨ Thanks for stopping by — now go make your desktop shine! 🌟")

    return skins

def open_skin_link(skins):
    choice = input("\nWant to open a skin link? Enter the number (or press Enter to skip): ").strip()
    if choice in skins:
        _, name, url = skins[choice]
        print(f"Opening {name}...")
        webbrowser.open(url)
    else:
        print("No link opened. Have a great day! ✨")

if __name__ == "__main__":
    skins = show_menu()
    open_skin_link(skins)
