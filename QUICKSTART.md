# Quick Start Guide

## 🚀 Get Started in 5 Minutes!

### Step 1: Download Ren'Py
1. Go to https://www.renpy.org/latest.html
2. Download Ren'Py SDK (free!)
3. Extract and run it

### Step 2: Open Project
1. Launch Ren'Py SDK
2. Click "+ Projects"
3. Select this folder
4. Click "Launch Project" to see the example!

### Step 3: Add Your Content

#### Add Images:
- **Character sprites** → `game/images/characters/`
- **Backgrounds** → `game/images/backgrounds/`

#### Add Audio:
- **Music** → `game/audio/music/`
- **Sound effects** → `game/audio/sfx/`

### Step 4: Write Your Story

Open `game/script.rpy` and edit it!

**Basic Template:**
```python
## Define characters at the top
define mc = Character("Hero", color="#00ff00")
define friend = Character("Friend", color="#0000ff")

## Your story starts here
label start:
    scene bg bedroom
    with fade

    mc "Hello! This is my dialogue!"

    show mc happy at center

    friend "Nice to meet you!"

    menu:
        "What do you say?"

        "Nice to meet you too!":
            mc "Nice to meet you too!"

        "See you later!":
            mc "See you later!"

    return
```

### Step 5: Test & Build

- **Test:** Click "Launch Project" in Ren'Py SDK
- **Build:** Click "Build Distributions" when ready to share

---

## 📝 Quick Reference

### Show Background:
```python
scene bg bedroom
with fade
```

### Show Character:
```python
show protagonist happy at center
```

### Character Dialogue:
```python
mc "What I'm saying!"
```

### Play Music:
```python
play music "audio/music/theme.mp3"
```

### Create Choice:
```python
menu:
    "Choice A":
        jump path_a
    "Choice B":
        jump path_b
```

---

## 🆘 Need Help?

Read the full **README.md** for detailed instructions!

**Resources:**
- Ren'Py Docs: https://www.renpy.org/doc/html/
- Discord: https://discord.gg/6ckxWYm
- Subreddit: r/RenPy

---

**You're ready to create! Good luck! 🎉**
