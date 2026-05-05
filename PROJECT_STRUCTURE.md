# Alien Invasion - Project Structure & Architecture

## 🏗️ Project Overview

The Alien Invasion game is built using **Object-Oriented Programming (OOP)** with clean separation of concerns. Each file has a specific responsibility.

```
Alien Invasion Game
├── Main Game
│   └── alien_invasion.py          (Game class & main loop)
├── Game Entities (Sprites)
│   ├── ship.py                    (Player's spaceship)
│   ├── bullet.py                  (Projectiles fired by ship)
│   └── alien.py                   (Enemy alien class)
├── Game State
│   ├── settings.py                (Configuration & game settings)
│   └── game_stats.py              (Score, lives, level tracking)
├── UI & Controls
│   ├── button.py                  (Play button widget)
│   └── game_functions.py          (Event handling & game logic)
├── Assets
│   ├── ship.bmp                   (Ship image)
│   └── alien.bmp                  (Alien image)
└── Documentation
    ├── ALIEN_INVASION_README.md   (Complete game documentation)
    ├── QUICK_START.md             (Quick start guide)
    └── PROJECT_STRUCTURE.md       (This file)
```

## 📋 File-by-File Explanation

### 1. **alien_invasion.py** - Main Game File
**Purpose**: Entry point and main game loop

**Key Components**:
- `AlienInvasion` class: Manages all game systems
  - Initializes pygame and game resources
  - Runs the main game loop (60 FPS)
  - Handles user input (keyboard & mouse)
  - Updates game state each frame
  - Renders everything to screen

**Main Methods**:
- `run_game()` - Main game loop
- `_check_events()` - Handles keyboard and mouse input
- `_check_keydown_events()` - Processes key presses
- `_check_keyup_events()` - Processes key releases
- `_check_play_button()` - Handles clicking Play button
- `_update_screen()` - Renders all game objects

**Flow**:
```
Initialize Game
    ↓
Start Main Loop
    ├→ Check for events (keyboard, mouse, quit)
    ├→ Update game state (if active)
    │  ├─ Update ship position
    │  ├─ Update bullets
    │  └─ Update aliens & check collisions
    ├→ Draw everything to screen
    └→ Repeat at 60 FPS
```

---

### 2. **ship.py** - Player's Spaceship
**Purpose**: Manage the player's controllable ship

**Key Features**:
- Smooth movement with arrow keys
- Stays within screen boundaries
- Centered by default at bottom of screen

**Key Methods**:
- `update()` - Updates ship position based on movement flags
- `blitme()` - Draws ship to screen
- `center_ship()` - Resets ship to center (when hit)

**Key Attributes**:
- `moving_left / moving_right` - Movement flags (boolean)
- `x` - Decimal position for smooth movement
- `image / rect` - Ship sprite and collision box

---

### 3. **bullet.py** - Projectiles
**Purpose**: Manage bullets fired by the player

**Key Features**:
- Moves upward automatically
- Auto-removed when off-screen
- Can have max 3 bullets on screen (prevents overpowered firing)

**Key Methods**:
- `update()` - Moves bullet upward
- `draw_bullet()` - Draws bullet to screen

**Key Attributes**:
- `y` - Decimal position for smooth movement
- `rect` - Collision box

---

### 4. **alien.py** - Enemy Aliens
**Purpose**: Define individual alien behavior

**Key Features**:
- Moves left/right across screen
- Drops down when hitting screen edges
- Checks for edge collision

**Key Methods**:
- `update()` - Moves alien left or right
- `check_edges()` - Returns True if at screen edge
- `blitme()` - Draws alien to screen

**Key Attributes**:
- `x` - Decimal position for smooth movement
- `settings.fleet_direction` - 1 for right, -1 for left

---

### 5. **settings.py** - Game Configuration
**Purpose**: Centralized game settings and difficulty control

**Key Settings**:
```python
Screen:       1200 x 800 pixels
Ship:         Speed 5, Health 3 ships
Bullets:      Max 3 on screen, Speed 7
Aliens:       Initial speed 1, Drop speed 10
Difficulty:   1.1x multiplier per level (10% increase)
```

**Key Method**:
- `increase_difficulty()` - Called each level, speeds up game

**Why Separate?**: Easy to adjust difficulty without changing code in other files

---

### 6. **game_stats.py** - Game Statistics
**Purpose**: Track game state and statistics

**Tracks**:
- `score` - Points earned (100 per alien)
- `level` - Current difficulty level
- `ships_left` - Lives remaining (starts at 3)
- `game_active` - Is game running? (True/False)

**Key Method**:
- `reset_stats()` - Called when starting new game

---

### 7. **button.py** - UI Button
**Purpose**: Render the "Play Game" button

**Features**:
- Green button with white text
- Centered on screen
- Detectable for mouse clicks (via rect collision)

**Key Methods**:
- `prep_msg()` - Create text image for button
- `draw_button()` - Draw button to screen

---

### 8. **game_functions.py** - Core Game Logic
**Purpose**: Functions that drive game mechanics

**Key Functions**:

#### Event Handling
- `check_keydown_events()` - Process key presses
- `check_keyup_events()` - Process key releases
- `fire_bullet()` - Create new bullet

#### Game Updates
- `update_bullets()` - Move bullets, remove off-screen
- `update_aliens()` - Move aliens, check collisions
- `check_fleet_edges()` - Check if aliens hit screen edge

#### Collision Detection
- `check_bullet_alien_collisions()` - Detect hits
- `check_aliens_bottom()` - Did aliens reach bottom?
- `ship_hit()` - Handle ship collision

#### Fleet Management
- `create_fleet()` - Generate grid of aliens
- `create_alien()` - Place single alien
- `check_fleet_empty()` - New fleet if all destroyed
- `change_fleet_direction()` - Aliens drop and reverse

#### Game Control
- `reset_game()` - Start fresh game

---

## 🔄 Game Loop Explained

The game runs continuously at 60 frames per second:

```
FRAME 1 (60 times per second):
├─ Check Events
│  └─ Did player press a key? Click mouse?
├─ Update Game (if playing)
│  ├─ Move ship left/right
│  ├─ Move bullets upward
│  ├─ Move aliens
│  └─ Check all collisions
├─ Draw Everything
│  ├─ Clear screen
│  ├─ Draw ship
│  ├─ Draw bullets
│  ├─ Draw aliens
│  ├─ Draw score/level/lives
│  └─ Update display
└─ Wait for next frame (1/60th second)
```

---

## 🎮 Game States

### State 1: Menu / Inactive
- Play button visible
- Game logic not running
- Waiting for player to click Play

### State 2: Active / Playing
- Game logic running
- Ship and aliens moving
- Bullets being fired
- Collisions being checked

### State 3: Game Over
- No ships left
- Game pauses
- Play button reappears
- Ready for new game

---

## 🎯 Key Game Mechanics

### Collision Detection
```python
pygame.sprite.groupcollide(bullets, aliens, ...)
# Checks every bullet against every alien
# Returns groups of collisions
```

### Difficulty Scaling
```python
# Each new level:
alien_speed *= 1.1        # 10% faster
bullet_speed *= 1.1       # 10% faster
fleet_drop_speed *= 1.1   # 10% faster
```

### Movement System
```python
# Use decimal values for smooth movement
self.x += speed           # Decimal position
self.rect.x = self.x      # Update collision box
```

---

## 📊 Class Inheritance

```
Sprite (pygame.sprite.Sprite)
├─ Bullet
│  └─ Has update(), draw_bullet()
└─ Alien
   └─ Has update(), check_edges()

Ship (no inheritance, custom class)
└─ Has update(), blitme()

GameStats (no inheritance)
└─ Tracks score, level, ships

Settings (no inheritance)
└─ Stores configuration
```

---

## 🔧 How to Modify the Game

### Change Game Speed
Edit `settings.py`:
```python
self.alien_speed = 2         # Faster aliens
self.bullet_speed = 10       # Faster bullets
self.speedup_scale = 1.2     # 20% increase per level (was 1.1)
```

### Change Screen Size
Edit `settings.py`:
```python
self.screen_width = 1600     # Wider screen
self.screen_height = 900     # Taller screen
```

### Change Ship Lives
Edit `settings.py`:
```python
self.ship_limit = 5          # More lives (was 3)
```

### Change Difficulty per Level
Edit `settings.py`:
```python
self.speedup_scale = 1.15    # 15% harder each level (was 1.1)
```

---

## 🎨 Asset Information

### Ship Image (ship.bmp)
- Size: 40×50 pixels
- Color: Green triangle pointing up
- Generated by create_assets.py

### Alien Image (alien.bmp)
- Size: 40×30 pixels
- Color: Red square with white eyes and mouth
- Generated by create_assets.py

---

## 📈 Progression Example

**Level 1**
- Alien Speed: 1.0
- Bullet Speed: 7.0
- Fleet Drop: 10

**Level 2** (after speedup)
- Alien Speed: 1.1
- Bullet Speed: 7.7
- Fleet Drop: 11

**Level 3** (after speedup again)
- Alien Speed: 1.21
- Bullet Speed: 8.47
- Fleet Drop: 12.1

Game gets noticeably harder each level!

---

## 🚀 Performance Notes

- **60 FPS Target** - Smooth gameplay
- **Sprite Groups** - Efficient collision detection
- **Auto-removal** - Off-screen objects deleted
- **Limited Bullets** - Max 3 prevents lag

---

## 🎓 What You Can Learn

1. **OOP Design** - How to structure a game with classes
2. **Event Handling** - Responding to user input
3. **Collision Detection** - Detecting object overlap
4. **Game Loops** - How games update and render
5. **State Management** - Tracking game active/inactive
6. **Pygame** - Popular Python game library
7. **Progressive Difficulty** - Scaling challenges

---

**Next Step**: Explore the code files to understand each component better!
