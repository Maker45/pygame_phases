# Phase 3: Data Collections (Lists & Dictionaries)

**Goal:** Manage many things (enemies, bullets, particles) without creating 100 variables. This is the most critical part for PCEP.

**PCEP Concepts:** Lists (`append`, `pop`, `len`, `sort`), Tuples (immutability), Dictionaries (keys, values), Loops (`for item in list`)

---

## 01_50_stars.py

### Lesson 3.1: "Scaling Up"

**Goal:** Create 50 stars scattered randomly across the screen using a list and a loop.

**PCEP Concepts:** Lists, `append()`, `range()`, `for` loops (iteration), Indexing

**The Problem:** Writing a separate variable for each of 50 stars is impossible. We need a container that holds many things.

**Steps**
1. **The List (the "bag"):** Use square brackets `[]`. `stars = []` starts empty. You can put numbers, strings, or even Pygame Rects inside.
2. **Populate the List (the factory):** `for i in range(50):` repeats code 50 times. `stars.append(...)` adds an item to the end of the list. Each time the loop runs, a new Rect is created and saved.
3. **Draw the List:** `for star in stars:` — Python grabs the first item, calls it `star`, and runs the code. Then it grabs the second item, and so on for all 50.

---

## 02_galaxy_grazer.py

### Lesson 3.1 Lab Challenge: "Galaxy Grazer"
- Create a list called `raindrops`.
- Use a loop to add **100** small blue Rects at random positions.
- Draw them all in the game loop.
- **Bonus:** Make them all fall down (`raindrop.y += 1`).
- **Ultra Bonus:** When a drop hits the bottom, move it back to the top (Infinite Rain).

---

## 03_hungry_block.py

### Lesson 3.2: Processing Lists — "The Assembly Line"

**Goal:** Loop through the list of stars to draw them, check for collisions, and safely remove them when "collected."

**PCEP Concepts:** `for` loops, iteration variables, `len()`, `list.remove()`, `del list[i]`, and the danger of changing a list while looping

**Anatomy of the `for` loop:** `for item in collection:`
- `for` starts the loop.
- `item` is a temporary name you make up. It holds one thing at a time.
- `in` links the variable to the list.
- `collection` is the list you're pulling from (like `stars`).

**Steps**
1. **Draw the Swarm:** Loop through `stars` and draw each one. At 60 frames per second, that's 3,000 stars drawn every second!
2. **The Collision Check:** Use `colliderect` from Lesson 2.2, but check **every** star in the list. If the player touches one, remove it.
3. **The Golden Rule:** If you `remove()` an item while looping, the list shrinks, everything shifts left, and Python skips the next item! *Never delete steps on a staircase while you're walking up it.*
4. **Safe Removal (the slice hack):** Loop over `stars[:]`, which is a temporary copy. You walk on the copy's staircase and delete steps from the original.

### Lab Challenge: "Hungry Block"
- Get your 50 stars drawing on the screen.
- Use the safe `for` loop to check for collisions.
- `remove` the star when the player touches it.
- **Bonus:** Print how many stars are left in the terminal using `print(len(stars))`!
- *Hint:* Put your collision check in the main `while` loop, not the event loop!

---

## 04_stat_tracker.py

### Lesson 3.3: High Scores (Dictionaries)

**Goal:** Store complex data, like game settings and player stats.

**PCEP Concepts:** Accessing dictionary values (`settings["difficulty"]`), changing values

**The Problem ("Variable Soup"):** Lists are great for 50 identical stars, but not for `score`, `lives`, and `name`. (Is index 0 the score or the lives?)

**The Dictionary:** A Python dictionary maps a **key** to a **value** — like a filing cabinet with labeled folders.

**Steps**
1. **Create the Dictionary:** Use curly braces `{}`. Keys are usually strings in quotes. Values can be anything. Separate each key and value with a colon `:`.
2. **Access and Update:** Look inside a folder with `my_dict["key"]`. Dictionaries can change while the game runs — update them like a normal variable.
3. **Integrate with the Game:** Put the dictionary update inside your collision check. Every time a star vanishes, the score goes up. Use `print()` to see it in the terminal.
4. **Bonus — New Keys on the Fly:** If you assign a value to a key that doesn't exist yet, Python creates it for you!

### Lab Challenge: "Stat Tracker"
- Create a `player_stats` dictionary at the top of your code.
- Include `score` (starts at 0) and `level` (starts at 1).
- When your player eats a star, increase the score in the dictionary by 10.
- Print the dictionary to the terminal every time the score changes.
- **Bonus:** If `player_stats["score"]` reaches 100, increase the level by 1 and print `"LEVEL UP!"`
