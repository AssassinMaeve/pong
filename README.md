# Pong Game - README

## Introduction
This is a simple Pong game implemented in Python using the Pygame library. The game features a ball that bounces off the walls and paddles, an AI-controlled opponent, and player controls for movement.

## Requirements
- Python 3.x
- Pygame library

To install Pygame, run:
```bash
pip install pygame
```

## How to Run
1. Ensure Python and Pygame are installed.
2. Save the script as `pong.py`.
3. Run the script using:
```bash
python pong.py
```

## Game Controls
- **Arrow Up (`↑`)**: Move player paddle up
- **Arrow Down (`↓`)**: Move player paddle down
- **Close Window**: Quit the game

## Code Overview
- `ballAnimation()`: Moves the ball, detects collisions with walls and paddles.
- `ballRestart()`: Resets the ball to the center after scoring.
- `playerAnimation()`: Controls player paddle movement within screen boundaries.
- `opponentAi()`: Simple AI to move opponent paddle towards the ball.

## Features
- Basic Pong mechanics with bouncing ball and paddles.
- AI-controlled opponent.
- Player controls using arrow keys.
- Frame rate managed using `pygame.time.Clock()`.

## Possible Enhancements
- Add scoring system.
- Implement sound effects.
- Improve AI for more challenging gameplay.
- Add power-ups or different game modes.

## License
This project is open-source and can be modified or distributed under the MIT License.

Enjoy the game! 🏓

