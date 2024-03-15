# PingPong Game User Manual

Welcome to the PingPong Game, a classic arcade-style game designed to provide hours of fun and competition. This manual will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to play the game.

## Main Functions of the Software

The PingPong Game is a simple yet engaging game where two players control paddles to hit a ball back and forth across the screen. The main functions of the game include:

- **Paddle Movement**: Players can move their paddles up and down to intercept the ball.
- **Ball Movement**: The ball moves across the screen, bouncing off the top and bottom edges and the paddles.
- **Scoring**: A point is scored when a player fails to return the ball, and the score is displayed at the top of the screen.
- **Game Reset**: After a point is scored, the ball is reset to the center of the screen to resume play.

## Quick Install

Before you can start playing the PingPong Game, you need to install the Pygame library, which is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library, allowing you real-time control over graphics, sound, and input devices.

### Installing Pygame

To install Pygame, you can use `pip`, which is the package installer for Python. Open your command line or terminal and run the following command:

```bash
pip install pygame==2.0.1
```

Alternatively, you can install Pygame by using the `requirements.txt` file provided with the game. Navigate to the directory containing `requirements.txt` and run:

```bash
pip install -r requirements.txt
```

## How to Play the PingPong Game

Once you have installed Pygame, you are ready to play the game. Follow these steps to get started:

1. **Start the Game**: Run `main.py` to start the game. You can do this by typing `python main.py` in your terminal or command line, assuming you are in the directory where `main.py` is located.

2. **Control the Paddles**: Use the `W` and `S` keys to move the left paddle up and down. Use the `UP ARROW` and `DOWN ARROW` keys to move the right paddle up and down.

3. **Play the Game**: The ball will automatically start moving when the game begins. Each player must move their paddle to hit the ball back to the other side. If the ball passes a paddle and hits the edge of the screen, the opposing player scores a point.

4. **Scoring**: The game keeps track of each player's score, which is displayed at the top of the screen. The game continues indefinitely, so you can set your own winning score or play as long as you like.

5. **Exiting the Game**: To exit the game, simply close the game window or press the `ESC` key.

Enjoy the game and have fun competing with friends or practicing against yourself!