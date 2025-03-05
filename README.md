# Game 1010!

## Description
This is a game inspired by the classic **1010!** game, implemented using the **Pygame** library. The game involves placing blocks on an 8x8 board. The goal is to complete full rows and columns to earn points. The game also includes a system for saving the best score.

## Requirements
To run the game, you need to install **Pygame**. You can do this using the following command:

```sh
pip install pygame
```

## Running the Game
After installing Pygame, launch the game using the following command:

```sh
python game.py
```

Once the game starts, you'll see an 8x8 board where you must place blocks. The game also allows you to restart by pressing the **Restart** button at the top of the screen.

## Controls
- **Drag and drop blocks**: Click on a block, then drag it onto the board to place it in the desired position.
- **Click the Restart button**: To start a new game, click the **Restart** button at the top of the screen.

## Game Features
- **Blocks**: The game includes various block shapes, such as a square, horizontal line, vertical line, "T" shape, "Z" shape, and more.
- **Scoring**: Points are earned for each completed row or column, as well as for placing blocks on the board.
- **Best Score**: The game saves the highest score in the `best_score.txt` file, which is loaded at the start of the game and updated when a new high score is achieved.

## Configuration File
The game uses the following constants:
- **WINDOW_SIZE**: The size of the game window (500 pixels).
- **GRID_SIZE**: The board size (8x8).
- **CELL_SIZE**: The size of an individual cell on the board.
- **BLOCK_COLORS**: The colors of the blocks that can appear in the game.

## Rules
- The blocks you drag must fit into the available space on the board.
- A completed row or column is removed, and the player earns points.


![image](https://github.com/user-attachments/assets/9dafdee5-2e3e-48ec-96ba-d640c90f0239)
