# Phase 1: The Engine (Variables & The Game Loop)

**Goal:** Understand that a "game" is just an infinite loop that updates variables and draws pictures very fast.

**PCEP Concepts:** Variables, Assignments, Basic I/O (Console), Boolean Operators (True/False)

---

## 01_moving_square.py

### Part 1 – Lesson 1.1: Hello VS Code & The Infinite Loop

📊 **Slides:** [Phase 1.1: The Engine](https://docs.google.com/presentation/d/18MKw0KJQcVK5UXV7hBy-3iUhYnlsJiYn0pbofUQyZVc/view)

**Goal:** Create a black window that stays open until the user closes it.

**PCEP Concepts:** Modules (`import`), Tuples, Variables, Boolean Logic, `while` loops

**How games work:** A game is a loop that runs 60 times per second. Each time through:
1. **Events:** Did the player press a key?
2. **Update:** Move the characters.
3. **Draw:** Paint the screen.

**Steps**
1. **The Setup:** `import pygame` grabs the toolbox. `(800, 600)` is a **tuple** — like a list, but you can't change it.
2. **The Flag:** Make a variable `running = True`. As long as `running` is `True`, the game lives.
3. **The Loop & Exit Strategy:** `while running:` runs forever. Inside it, `pygame.event.get()` checks "Did anything happen since the last frame?" Indentation defines what belongs inside the loop.
4. **The Refresh:** `screen.fill(...)` wipes the screen every frame. Colors are RGB: `(0, 0, 0)` is black, `(255, 255, 255)` is white. `pygame.display.flip()` puts the image on the monitor.

**Lab Challenge**
- Type the code into VS Code.
- Run it to make sure the black window appears.
- **Challenge:** Change the background color to **blue**.
- **Bonus:** Change the window title to your name.
- *Hint:* Blue is mixed using (Red, Green, Blue). The max value is 255.

### Part 2 – Lesson 1.2: Making Things Move

📊 **Slides:** [Phase 1.2: The Bouncing Square](https://docs.google.com/presentation/d/1TGDGzIbr5E4XhLqqzaMsrnI4H24bMm6rMqftu3jIJu4/view)

**Goal:** Draw a square and make it move across the screen.

**PCEP Concepts:** Variables, Integer Arithmetic (`+`, `-`, `*`), Assignment Operators (`=`, `+=`), Coordinate Systems

**The Grid:** On a computer screen, `(0, 0)` is the **top-left** corner. Larger X goes **right**. Larger Y goes **down**.

**Steps**
1. **Define the actor:** Create `rect_x` and `rect_y` variables to store the square's position. Create them **before** the loop starts. (Why?)
2. **Draw it:** `pygame.draw.rect(screen, (255, 0, 0), [rect_x, rect_y, 50, 50])` — where to draw, the color (red), and the position and size.
3. **Make it move:** Inside the loop, before drawing, add `rect_x += 5`. (`rect_x += 5` is the same as `rect_x = rect_x + 5`.) Every time the loop runs, X gets bigger.
4. **Fix the speed:** Without a limit, the loop runs 2000+ times a second. Add a `pygame.time.Clock()` to slow it down.

---

## 02_dvd_screensaver.py

### Lesson 1.2 Lab Challenge: "The DVD Screensaver"

📊 **Slides:** [Phase 1.2: The Bouncing Square](https://docs.google.com/presentation/d/1TGDGzIbr5E4XhLqqzaMsrnI4H24bMm6rMqftu3jIJu4/view)

**The Bounce:** If the square goes too far, reverse it. To reverse direction, multiply the speed by `-1` (or set it to a negative number).

**Task**
- Make the square bounce off **all 4 walls** (top, bottom, left, right).
- **Bonus:** Change the color of the square every time it hits a wall.

**Hints**
- You need `if` statements for `rect_x` too.
- The right wall is at 800.
- Remember the square has width! The wall is at 800 and the square is 50 wide, so bounce at **750**.
