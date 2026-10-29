# ⏱️ Guess the Time

A tiny command-line game where you try to **estimate the passage of time** — no stopwatch, just your intuition! A random number of seconds is shown, and you press **Enter** to start and stop the timer. How close can you get?

## How to Run

Requirements:

- **Python 3.x** (any recent version)
- **No external dependencies** — only the standard library (`time`, `random`)

Run the game from the project directory:

```bash
python mian.py
```

> **Note:** the filename `mian.py` appears to be a typo for `main.py`. It's kept as-is here so the instructions match the actual file.

## How the Game Works

1. The game picks a **random target time between 5 and 15 seconds** and tells you what it is.
2. Press **Enter** to start the timer.
3. Try to wait *exactly* that long in your head, then press **Enter** to stop the timer.
4. The game shows the target time, your actual elapsed time, and **how far off you were**.
5. The loop repeats immediately with a new random target — there is currently **no quit option**, so close the terminal (or press `Ctrl+C`) to exit.

### Example Output

```
Guess the time. Your time is 12s
press enter to start>
Press enter to stop time>

The time to guess was: 12.
Your time was: 11.42
You where off by: -0.58
```

A **negative** "off by" value means you stopped *early*; a positive one means you went *over* the target. The value shown is `your time − target time`.

## How It Works (Code Logic)

The whole game lives in a single `while True:` loop, so each round follows the same steps:

```python
import time
import random

while True:
    # 1. Pick a random target: 5 to 15 seconds (inclusive)
    time_to_guess = random.randint(5, 15)

    # 2. Show the target and wait for the player to start
    print(f"Guess the time. Your time is {time_to_guess}s")
    input("press enter to start>")

    # 3. Record the start timestamp
    start_time = time.time()

    # 4. Wait for the player to stop
    input("Press enter to stop time>")

    # 5. Record the end timestamp and compute the results
    end_time = time.time()
    final_time = end_time - start_time
    off_time = final_time - time_to_guess

    # 6. Print the round results, then loop again
    print(f"\nThe time to guess was: {time_to_guess}.\n"
          f"Your time was: {final_time :.2f}\n"
          f"You where off by: {off_time :.2f}\n")
```

Key ideas:

- **`random.randint(5, 15)`** — generates the target duration in seconds (both endpoints included).
- **`time.time()`** — returns the current time as a float (seconds since the epoch). Taking it *before* and *after* the second `input()` gives the elapsed time as the difference of the two timestamps.
- **`input()` blocks** — the program simply waits for you to press Enter, which is what makes the timing entirely up to you.
- **`:.2f`** — formats the floats to exactly **two decimal places**.
- **`while True`** — an infinite loop; the game never breaks out on its own.

## Possible Improvements

Ideas for extending the game if you'd like to tinker:

- 🚪 **Quit option** — e.g., accept `q` instead of Enter to exit the loop gracefully (currently you must press `Ctrl+C`).
- 🏆 **Score tracking** — keep a running total or average accuracy across rounds and show it after each one.
- 🎚️ **Difficulty levels** — shorter/easier ranges for beginners, tighter ranges (e.g., 25–30s) for experts.
- 📛 **Fix the filename typo** — rename `mian.py` → `main.py` (remember to update the run command).
- ✏️ **Fix the message typo** — the output says `"You where off by"`; it should be **"You were off by"**.
- ⏱️ **Millisecond precision** — format with `:.3f` if you want more precise feedback.
- 📊 **Feedback/grading** — say "Great!" when within 0.5s, "Not bad!" within 1s, and "Try again!" otherwise.

## Project Structure

```
guess_the_time/
├── mian.py       # The entire game (single file)
└── README.md     # This file
```

## License

No license specified — feel free to use this for learning and fun.
