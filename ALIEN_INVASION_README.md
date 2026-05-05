# Alien Invasion Game

A 2D space shooter game built with Python and Pygame where you defend Earth from an invading alien fleet!

## Game Overview

In **Alien Invasion**, you control a rocket ship at the bottom of the screen and defend against waves of descending aliens. Destroy all the aliens to advance to the next level. Each level moves faster and is more challenging than the last.

## How to Play

### Controls
- **Left Arrow Key** - Move ship left
- **Right Arrow Key** - Move ship right
- **Space Bar** - Fire bullets
- **Q Key** - Quit game

### Game Rules
1. Click the **"Play Game"** button to start a new game
2. Move your ship side to side to avoid aliens and position for shots
3. Fire bullets to destroy aliens
4. **Destroy all aliens** to complete a level and advance to the next (faster) level
5. **Avoid letting aliens hit your ship** or reach the bottom of the screen
6. **Lose one ship** each time an alien hits you or reaches the bottom
7. **Game Over** when you lose all 3 ships

### Scoring
- **100 points** per alien destroyed
- Your score, current level, and remaining ships are displayed at the top-left

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pygame package

### Installation Steps

1. Navigate to the game directory:
```bash
cd path/to/CSC-121
```

2. Install pygame (if not already installed):
```bash
pip install pygame
```

3. Run the game:
```bash
python alien_invasion.py
```

Or run the image asset generator first if images are missing:
```bash
python create_assets.py
python alien_invasion.py
```

## Project Structure

### Core Game Files

| File | Purpose |
|------|---------|
| `alien_invasion.py` | Main game file with game loop and event handling |
| `settings.py` | Game configuration (screen size, speeds, difficulty settings) |
| `ship.py` | Player's ship class and movement logic |
| `bullet.py` | Bullet class (projectile fired by the ship) |
| `alien.py` | Alien enemy class and movement logic |
| `game_stats.py` | Game statistics tracking (score, lives, level) |
| `button.py` | Play button for starting the game |
| `game_functions.py` | Game logic functions (collisions, fleet management, etc.) |
| `create_assets.py` | Generates ship.bmp and alien.bmp image files |

## Game Features

### Gameplay Mechanics
- **Player Control**: Smooth ship movement with arrow keys
- **Bullet Firing**: Limited bullets on screen (max 3) to balance difficulty
- **Fleet Management**: Aliens move left/right and drop down the screen
- **Collision Detection**: Bullets vs aliens, aliens vs ship, aliens vs screen bottom
- **Progressive Difficulty**: Each new fleet moves faster and increases bullet speed

### Difficulty Progression
- Each level increases alien speed by 10%
- Bullet speed increases by 10% per level
- Fleet drop speed increases by 10% per level
- More challenging and exciting as you progress!

### Game States
- **Inactive**: Play button visible, waiting to start
- **Active**: Game in progress, aliens and player moving
- **Game Over**: Display when you lose all 3 ships

## Code Explanation

### Key Classes and Functions

#### `Ship` Class (ship.py)
- Manages player's ship position and movement
- Updates position based on arrow key input
- Stays within screen boundaries

#### `Bullet` Class (bullet.py)
- Represents a projectile fired by the ship
- Moves upward automatically each frame
- Removed from game when it goes off-screen

#### `Alien` Class (alien.py)
- Represents individual alien enemies
- Moves horizontally and drops down
- Changes direction when hitting screen edges

#### `GameStats` Class (game_stats.py)
- Tracks score, remaining ships, and current level
- Manages game active state (playing vs. menu)

#### Key Functions (game_functions.py)
- `create_fleet()` - Generates a grid of aliens
- `update_aliens()` - Updates alien positions and checks collisions
- `update_bullets()` - Updates bullet positions and checks collisions
- `check_bullet_alien_collisions()` - Handles bullet-alien impacts
- `ship_hit()` - Handles ship being hit or alien reaching bottom
- `change_fleet_direction()` - Makes aliens drop down and reverse direction

## Tips for Playing

1. **Stay centered** - Position yourself in the middle of the screen for quick escapes
2. **Plan your shots** - Remember you can only have 3 bullets on screen at once
3. **Watch the bottom** - Aliens dropping to the bottom are especially dangerous
4. **Embrace the challenge** - Each level is harder, but you get more points!
5. **Quick reflexes** - The game speeds up significantly in higher levels

## Technical Details

### Display Resolution
- Screen: 1200 x 800 pixels
- Refresh Rate: 60 FPS (frames per second)

### Game Mechanics
- Ship speed: 5 pixels/frame
- Initial bullet speed: 7 pixels/frame
- Initial alien speed: 1 pixel/frame
- Fleet drop amount: 10 pixels when hitting edge
- Difficulty multiplier: 1.1x (10% increase per level)

### Sprite Management
- Uses pygame sprite groups for efficient collision detection
- Automatic removal of off-screen objects
- Efficient batch drawing of aliens

## Troubleshooting

### Game won't start
- Make sure pygame is installed: `pip install pygame`
- Make sure you're in the correct directory
- Check that ship.bmp and alien.bmp exist (run create_assets.py if needed)

### No images displaying
- Run `python create_assets.py` to generate the image files
- Images should be created as ship.bmp and alien.bmp

### Game is too fast/slow
- Modify `self.clock.tick(60)` in alien_invasion.py to adjust FPS
- Modify game speed settings in settings.py

### Can't quit the game
- Press Q while in the game
- Or close the window

## Future Enhancement Ideas

- Add sound effects and background music
- Create different alien types with unique behaviors
- Implement power-ups (shield, rapid fire, etc.)
- Add a high score leaderboard
- Multiple difficulty settings
- Different weapon types
- Boss battles
- Particle effects for explosions

## Learning Objectives

This project demonstrates:
- Object-oriented programming with Python classes
- Pygame library fundamentals (sprites, groups, collisions)
- Game loop structure and event handling
- Collision detection algorithms
- Difficulty scaling and game progression
- Sprite animation and movement
- User input handling

## Credits

Built as an educational Python game project using pygame.

---

**Enjoy the game and good luck defending Earth! 🚀👽**
