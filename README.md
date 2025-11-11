# CyberSlime2077 Visual Novel

A visual novel framework built with Ren'Py. This template provides everything you need to create your own visual novel game!

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Adding Your Content](#adding-your-content)
- [Writing Your Story](#writing-your-story)
- [Testing Your Game](#testing-your-game)
- [Building for Distribution](#building-for-distribution)
- [Tips and Tricks](#tips-and-tricks)

---

## 🚀 Getting Started

### Prerequisites

You need to download and install **Ren'Py SDK** (completely free!):

1. Go to https://www.renpy.org/latest.html
2. Download the Ren'Py SDK for your operating system (Windows, Mac, or Linux)
3. Extract the downloaded file to a folder on your computer

### Opening Your Project

1. Launch the Ren'Py SDK
2. Click **"+ Projects"** button at the bottom
3. Navigate to and select this project folder (`CyberSlime2077s-Visual-novel-project`)
4. Your project will now appear in the Ren'Py launcher

### Running the Example

Click **"Launch Project"** in the Ren'Py launcher to see the example visual novel in action!

---

## 📁 Project Structure

```
CyberSlime2077s-Visual-novel-project/
│
├── game/                          # Main game folder
│   ├── images/                    # All your visual assets
│   │   ├── characters/            # Character sprites go here
│   │   └── backgrounds/           # Background images go here
│   │
│   ├── audio/                     # All your audio assets
│   │   ├── music/                 # Background music files
│   │   └── sfx/                   # Sound effects files
│   │
│   ├── gui/                       # GUI graphics (auto-generated placeholders)
│   │
│   ├── script.rpy                 # YOUR STORY GOES HERE! Main script file
│   ├── options.rpy                # Game configuration (title, version, etc.)
│   ├── gui.rpy                    # GUI screens (menus, save/load, etc.)
│   └── gui_init.rpy               # GUI styling and colors
│
└── README.md                      # This file
```

---

## 🎨 Adding Your Content

### Adding Character Sprites

1. Create your character sprite images (PNG format recommended with transparency)
2. Place them in: `game/images/characters/`
3. Name them clearly, for example:
   - `protagonist_happy.png`
   - `protagonist_sad.png`
   - `protagonist_angry.png`
   - `friend_neutral.png`
   - `villain_smirk.png`

### Adding Background Images

1. Create or find background images (JPG or PNG)
2. Place them in: `game/images/backgrounds/`
3. Name them clearly, for example:
   - `bedroom.jpg`
   - `school_hallway.jpg`
   - `city_street.png`
   - `park.jpg`

### Adding Music

1. Get your music files (MP3, OGG, or WAV)
2. Place them in: `game/audio/music/`
3. Name them clearly, for example:
   - `main_theme.mp3`
   - `sad_moment.mp3`
   - `action_scene.ogg`

### Adding Sound Effects

1. Get your sound effect files (OGG or WAV recommended)
2. Place them in: `game/audio/sfx/`
3. Name them clearly, for example:
   - `door_close.ogg`
   - `footsteps.wav`
   - `notification.ogg`

---

## ✍️ Writing Your Story

### Opening the Script File

Open `game/script.rpy` in any text editor (Ren'Py SDK has a built-in editor, or use VS Code, Sublime Text, etc.)

### Defining Characters

At the top of `script.rpy`, define your characters:

```python
## Define your characters
define mc = Character("Alex", color="#c8ffc8")
define friend = Character("Sarah", color="#c8c8ff")
define villain = Character("Dr. Evil", color="#ff0000")
```

### Writing Dialogue

```python
label start:
    ## Narrator text (no character name)
    "This is narration text."

    ## Character dialogue
    mc "Hi! This is what the main character says."

    friend "And this is what the friend says!"
```

### Showing Backgrounds

```python
## Show a background image
scene bg bedroom
with fade

## You can use transitions: fade, dissolve, pixellate, etc.
scene bg school
with dissolve
```

### Showing Character Sprites

```python
## Show a character sprite
show protagonist happy at center

## Show multiple characters
show protagonist happy at left
show friend neutral at right

## Hide a character
hide protagonist
```

**Position options:** `left`, `center`, `right`, or custom positions

### Creating Choices

```python
menu:
    "What should I do?"

    "Go to school":
        jump school_scene

    "Stay home":
        jump home_scene

    "Call a friend":
        jump phone_scene
```

### Using Variables

```python
## Define variables
$ affection_points = 0
$ player_name = "Alex"

## Use variables in dialogue
mc "My name is [player_name]!"

## Modify variables
$ affection_points += 5

## Conditional dialogue
if affection_points > 10:
    friend "I really like you!"
else:
    friend "We're just friends."
```

### Playing Music and Sound

```python
## Play background music (loops automatically)
play music "audio/music/main_theme.mp3" fadeout 1.0 fadein 1.0

## Stop music
stop music fadeout 1.0

## Play a sound effect (plays once)
play sound "audio/sfx/door_close.ogg"
```

### Scene Labels and Jumps

```python
label start:
    "This is the beginning."
    jump chapter_1

label chapter_1:
    scene bg bedroom
    "This is chapter 1!"
    jump chapter_2

label chapter_2:
    scene bg school
    "This is chapter 2!"
    return  # End the game
```

### Example Story Structure

```python
label start:
    scene bg bedroom
    with fade

    "I woke up to a beautiful morning."

    show protagonist happy at center

    mc "Today is going to be a great day!"

    menu:
        "Where should I go?"

        "School":
            jump school_route

        "Park":
            jump park_route

label school_route:
    scene bg school
    with fade

    "I arrived at school."

    show friend happy at right

    friend "Hey! Good to see you!"

    return

label park_route:
    scene bg park
    with fade

    "I went to the park instead."

    "It was peaceful and quiet."

    return
```

---

## 🧪 Testing Your Game

### Launch from Ren'Py SDK

1. Open Ren'Py SDK
2. Select your project
3. Click **"Launch Project"**

### Quick Reload

While testing, you can press **Shift+R** to reload the script without restarting the game!

### Useful Keyboard Shortcuts

- **Space/Enter** - Advance dialogue
- **Ctrl** - Skip dialogue (hold)
- **Tab** - Toggle skip mode
- **Escape** - Open game menu
- **H** - Hide UI
- **S** - Screenshot
- **Shift+R** - Reload script (during development)

---

## 📦 Building for Distribution

When your visual novel is ready to share:

1. Open Ren'Py SDK
2. Select your project
3. Click **"Build Distributions"**
4. Select the platforms you want to build for:
   - **Windows** - Creates a Windows .exe
   - **Mac** - Creates a Mac .app
   - **Linux** - Creates a Linux executable
   - **Android** - Creates an Android .apk (requires Android SDK)
   - **Web** - Creates a web version
5. Click **"Build"**
6. Your build will be in the project folder under `[projectname]-dists/`

### Distribution Files

After building, you'll get:
- **[GameName]-[Version]-win.zip** - Windows version
- **[GameName]-[Version]-mac.zip** - Mac version
- **[GameName]-[Version]-linux.tar.bz2** - Linux version
- **[GameName]-[Version]-web.zip** - Web version

You can upload these to:
- **itch.io** (highly recommended for indie games!)
- Your own website
- Steam (requires Steam Direct)
- Game Jolt
- Other game distribution platforms

---

## 💡 Tips and Tricks

### Naming Conventions

- Use **lowercase with underscores** for files: `main_character_happy.png`
- Use **descriptive names**: `bedroom_night.jpg` instead of `bg1.jpg`
- Keep **character sprite names consistent**: `alex_happy.png`, `alex_sad.png`, etc.

### Image Recommendations

- **Backgrounds:** 1920x1080 pixels (Full HD)
- **Character Sprites:** 600-1200 pixels tall, PNG with transparency
- **File formats:** PNG for transparency, JPG for backgrounds without transparency

### Audio Recommendations

- **Music:** MP3 or OGG format, 128-192 kbps
- **Sound Effects:** OGG or WAV format
- Keep file sizes reasonable (music under 5MB each)

### Story Writing Tips

1. **Plan your story structure** before coding
2. **Use comments** to organize your script: `## This is a comment`
3. **Test frequently** - Run your game often to catch errors early
4. **Save multiple versions** - Keep backups of your script file
5. **Use version control** (Git) for larger projects

### Character Sprite Tips

- Keep characters at consistent scales
- Use PNG format with transparency
- Consider creating a "sprite sheet" with multiple expressions
- Use descriptive filenames: `protagonist_happy.png`, `protagonist_sad.png`

### Performance Tips

- Compress images appropriately (use online tools like TinyPNG)
- Use MP3/OGG for music (smaller file sizes than WAV)
- Avoid extremely high-resolution images if not necessary
- Test on different computers/devices

---

## 🆘 Common Issues

### "Image not found" Error

- Check that your image file is in the correct folder
- Verify the filename in your script matches exactly (case-sensitive!)
- Make sure you're using the right path: `"images/backgrounds/bedroom.jpg"`

### "Character not defined" Error

- Make sure you defined the character at the top of script.rpy
- Check for typos in character names

### Music Not Playing

- Verify the audio file is in the correct format (MP3, OGG, WAV)
- Check the file path in your script
- Make sure the file isn't corrupted (try playing it in a media player)

---

## 📚 Learning Resources

- **Ren'Py Documentation:** https://www.renpy.org/doc/html/
- **Ren'Py Cookbook:** https://www.renpy.org/wiki/renpy/doc/cookbook
- **Ren'Py Discord:** https://discord.gg/6ckxWYm
- **Ren'Py Subreddit:** r/RenPy

---

## 🎮 Ready to Create!

You now have everything you need to create your visual novel!

1. **Add your assets** (images, music, sounds)
2. **Write your story** in `game/script.rpy`
3. **Test frequently** with the Ren'Py launcher
4. **Build and share** your finished game!

Good luck with your visual novel! 🎉

---

## 📝 License

This template is free to use for any purpose (personal or commercial). Create amazing visual novels!

The Ren'Py engine itself is also free and open-source under the MIT license.
