# Alien Invasion - Quick Start Guide

## ✅ Your Game is Ready!

All game files have been created and tested. You have a fully functional 2D space shooter game!

## 🎮 How to Start Playing

### Step 1: Open Terminal
Open your terminal/command prompt in VS Code or navigate to the game directory:
```bash
cd c:\Users\arthu\OneDrive\Desktop\CSC-121
```

### Step 2: Run the Game
```bash
python alien_invasion.py
```

The game window should open in a few seconds!

## 🕹️ Controls While Playing

| Key | Action |
|-----|--------|
| **← LEFT ARROW** | Move ship left |
| **→ RIGHT ARROW** | Move ship right |
| **SPACE BAR** | Fire bullets |
| **Q** | Quit game |

## 📋 What to Expect

### Starting the Game
1. A game window will appear (1200x800 pixels)
2. You'll see a **green triangle** (your ship) at the bottom center
3. The sky will be filled with **red squares** (aliens)
4. A green **"Play Game"** button will appear in the center

### Gameplay
1. Click the **"Play Game"** button to start
2. Aliens will begin moving back and forth and dropping down
3. Use arrow keys to position your ship
4. Press SPACE to fire bullets and destroy aliens
5. Destroy all aliens to advance to the next level (faster!)
6. Try to survive as long as possible without losing 3 ships!

### Game Over
- Game ends when you lose all 3 ships
- Click "Play Game" again to restart

## 📊 Game Info Display

At the top-left of the screen you'll see:
- **Score**: Number of aliens × 100 points each
- **Level**: Current wave number (increases with each destroyed fleet)
- **Ships**: Number of lives remaining (starts at 3)

## 🎯 Strategy Tips

1. **Watch Your Reflexes** - The game gets progressively faster
2. **Manage Your Bullets** - You can only fire 3 bullets at a time
3. **Stay Mobile** - Don't get trapped in corners
4. **Predict Alien Movement** - They bounce at screen edges
5. **Focus on Rows** - Clear aliens row by row, bottom to top

## 📂 Game Files Overview

**Main Game:**
- `alien_invasion.py` - Start here! The main game file

**Game Components:**
- `ship.py` - Your controllable spaceship
- `bullet.py` - Your weapon projectiles
- `alien.py` - The enemy aliens
- `settings.py` - Game configuration & difficulty
- `game_stats.py` - Score, lives, and level tracking
- `button.py` - The Play button UI
- `game_functions.py` - Core game logic

**Assets:**
- `ship.bmp` - Your spaceship image (green triangle)
- `alien.bmp` - Alien image (red square)

**Documentation:**
- `ALIEN_INVASION_README.md` - Full game documentation
- `QUICK_START.md` - This file!

## ⚙️ System Requirements Met

✓ Python 3.13.2 configured  
✓ Pygame 2.6.1 installed  
✓ All game files created and tested  
✓ Image assets generated  
✓ All imports verified  

## 🐛 Troubleshooting

### "pygame not found"
```bash
pip install pygame
```

### Game window doesn't appear
- Wait a few seconds after running the command
- Check if a window opened in the background
- Try closing and rerunning the game

### No images showing (aliens/ship are invisible)
The image files should already be created, but if needed:
```bash
python create_assets.py
python alien_invasion.py
```

### Game is too fast or too slow
Edit `alien_invasion.py` line where it says:
```python
self.clock.tick(60)  # Change 60 to a different number
# Lower numbers = slower
# Higher numbers = faster
```

## 🚀 Next Steps

1. **Play the game** - Launch it and see how high a score you can get!
2. **Explore the code** - Read through the Python files to understand how it works
3. **Customize it** - Modify settings.py to change colors, speeds, difficulty
4. **Add features** - Try adding sounds, power-ups, or new enemy types

## 📚 Learning Resources

This project teaches you:
- **Object-Oriented Programming (OOP)** - Classes and inheritance
- **Game Development Basics** - Game loops and collision detection
- **Pygame Library** - Sprites, groups, and event handling
- **Game Design** - Difficulty progression and game balance

## 🎓 Code Learning Points

Try exploring and understanding:
1. How the game loop works in `alien_invasion.py`
2. How collision detection works in `game_functions.py`
3. How the Ship class handles movement in `ship.py`
4. How difficulty increases in `settings.py`

---

**Ready to defend Earth? Launch the game and start playing!** 🚀👽

For detailed information, see `ALIEN_INVASION_README.md`
