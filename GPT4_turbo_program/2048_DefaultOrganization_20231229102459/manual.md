# 2048 Game User Manual

Welcome to the 2048 Game with a 10x10 grid! This manual will guide you through the installation process and how to play the game.

## Introduction

The 2048 game is a single-player sliding tile puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. However, you can continue to play the game after reaching the goal to achieve higher scores.

In this version, you will be playing on a larger 10x10 grid, which provides a more extended gameplay experience compared to the classic 4x4 version of the game.

## Main Functions

- **Grid Initialization**: The game starts with two tiles on the grid, each with a value of either 2 or 4.
- **Game Moves**: Players can move the tiles in four directions: up, down, left, and right. Tiles with the same number merge into one when they touch.
- **New Tile**: After each move, a new tile (with a value of 2 or 4) appears in a random empty spot on the grid.
- **Game Over**: The game ends when there are no more moves available (no empty spaces and no adjacent tiles with the same value).

## Installation

### Prerequisites

Ensure you have Python 3.6 or higher installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Environment Setup

1. **Clone the repository or download the source code**:
   If you have `git` installed, you can clone the repository using the following command:
   ```
   git clone https://github.com/your-repository/2048-game.git
   ```
   Alternatively, download the source code as a ZIP file and extract it.

2. **Install dependencies**:
   Navigate to the directory where you have the game files and install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
   This will ensure you have the correct version of Python for the game.

## How to Play

1. **Start the Game**:
   Run the `main.py` script to start the game. You can do this by opening a terminal or command prompt, navigating to the game directory, and running:
   ```
   python main.py
   ```

2. **Playing the Game**:
   - Use the arrow keys on your keyboard to move the tiles:
     - **Up Arrow**: Move tiles up.
     - **Down Arrow**: Move tiles down.
     - **Left Arrow**: Move tiles left.
     - **Right Arrow**: Move tiles right.
   - After each move, the tiles will slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid.
   - If two tiles of the same number collide while moving, they will merge into a single tile with the total value of the two tiles that collided.
   - A new tile will appear randomly on the grid on an empty spot after each move.
   - The game continues until no more moves are available.

3. **End of the Game**:
   - The game ends when there are no empty spaces and no possible merges left on the grid.
   - A message box will appear notifying you that the game is over.

4. **Restarting the Game**:
   - To play again after the game is over, simply close the game window and run the `main.py` script again.

Enjoy the game and aim for the highest score possible!