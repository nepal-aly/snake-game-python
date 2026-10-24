# Classic Snake Game

A modernized Arcade Snake game developed in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles.

---

## Project Architecture

```text
snake-game-python/
│-- main.py          # Entry point & game loop
│-- snake.py         # Snake class (movement & growth)
│-- food.py          # Food class (random spawning)
│-- scoreboard.py    # Scoreboard class (UI & Highscore tracking)
│-- highscore.txt    # Persistent data store for high score
└── README.md        # Project documentation
```

---

## Game Controls

- **Up Arrow:** Move Snake Up
- **Down Arrow:** Move Snake Down
- **Left Arrow:** Move Snake Left
- **Right Arrow:** Move Snake Right

The snake can't turn straight back into itself (e.g. pressing Down while moving Up is ignored).

The game ends when the snake hits the wall or its own tail.

---

## Key Features

- **OOP Architecture:** Clean separation of concerns across multiple modules (`Snake`, `Food`, `Scoreboard`).
- **Data Persistence:** Automatically tracks, reads, and overwrites the highest score locally in `highscore.txt`.
- **Collision Engine:** Accurate distance-based collision logic for food detection, wall hits, and self-tail collisions.
- **Dynamic Rendering:** Smooth frame updates utilizing `screen.tracer(0)` and `screen.update()`.

---

## Setup & Execution

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/snake-game-python.git`

2. **Navigate to directory:**
   `cd snake-game-python`

3. **Run the application:**
   `python main.py`
