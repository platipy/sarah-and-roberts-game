# Sarah and Robert's Awesome Game

## Where everyone's a winner

![screenshot of game](https://github.com/platipy/sarah-and-roberts-game/blob/master/game.png)

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## Tutorial

- Move your cursor around to see colors.

- Press `space` to change the size of the paintbrush.

- Press `left shift` to see the current size of the paintbrush in the top left
white square.

- Start the game with `python3 main.py random` to draw with random colors;
otherwise, the game will draw with a randomly generated gradient sequence.

- Press `enter` to stop and start drawing.

- Hold `control` to erase.

- Press `c` to clear the canvas.

- Press `q` to quit.

## Troubleshooting

- If the screen resolution is too large, decrease the `SIZE` in `main.py`.
