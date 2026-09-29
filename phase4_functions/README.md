# Phase 4: Functions & Safe Code

---

## 01_function_refactor.py

### Lesson 4.1: The Function Refactor — "Cleaning Up the Workshop"

**Goal:** Take the massive `while` loop and break it into neat, reusable mini-programs (functions).

**PCEP Concepts:** `def`, calling functions, Parameters vs. Arguments, `return`, `None`, and Variable Scope (Local vs. Global)

**The Problem (Spaghetti Code):** The game loop does too much — events, movement, collisions, and drawing. A bug in the drawing code means digging through the movement code to find it. The solution: hire "specialists" to do specific jobs.

**What is a function?** A named block of code that only runs when you call it. In CodeCombat you used them all the time (`hero.moveRight()`). Now you'll build your own: `def name_of_function():`

**Steps**
1. **The Builder and the Caller:** Defining a function with `def` does **not** run it — it saves it for later. To run it, call it by name with parentheses `()`.
2. **Passing Data:**
   - **Parameter:** the variable name inside the parentheses when you *define* the function.
   - **Argument:** the actual data you pass in when you *call* the function.
3. **Refactor the Draw Loop:** Pass `player_rect` and `stars` as arguments so the function knows what to draw. Look how clean the main loop gets!
4. **Getting Data Back:** `return` instantly stops the function and gives back a value. A function with no `return` returns `None` (big PCEP concept!).
5. **The Scope Trap:**
   - **Global variables** are created outside any function and can be seen by everyone.
   - **Local variables** are created inside a function — and they **die** the moment the function finishes!

### Lab Challenge: "The Great Cleanup"
- Create a function called `draw_everything(player, enemies_list)`.
- Move all your `screen.fill`, `pygame.draw`, and `display.flip` code inside it.
- Call `draw_everything(...)` inside your `while` loop.
- **Bonus:** Create a `spawn_enemy()` function that uses `return` to give you a new enemy Rect at a random location. Use it to refill your list when enemies are eaten!

---

## 02_asset_manager.py

### Lesson 4.2: Loading Assets Safely (Exceptions)

**Goal:** Use real pictures instead of colored squares without crashing the game.

`pygame.image.load("hero.png")` loads a picture. **The trap:** if you misspell the file name or put it in the wrong folder, Python crashes the whole game.

**Syntax Errors vs. Exceptions**
- **Syntax errors:** You typed it wrong. Python won't even run the code. You **cannot** catch these.
- **Exceptions (runtime errors):** The code is written correctly, but something went wrong while running. You **can** catch these.

**Steps**
1. **The Safety Net:** Python attempts the risky code in `try:`. If an error happens, it jumps to `except:` instead of crashing, then keeps going.
2. **Catch Specific Errors:** A bare `except:` catches everything, which hides typos (bad practice). Name the error you expect, like `FileNotFoundError`.
3. **Load an Image Safely:** Try to load the image. If it fails, create a blank `pygame.Surface` and fill it with a color. Either way the image variable exists, so the draw loop won't crash.
4. **Update the Draw Loop:** `screen.blit(image, rect)` — *blit* means "stamp this picture onto the screen" at the Rect's position.

### Lab Challenge: "The Asset Manager"
- Find a small `.png` image online (under 100×100 pixels). Save it in the **`images`** folder as `enemy.png`.
- Write a `try` / `except` block to load `enemy.png` into a variable called `enemy_image`.
- If it fails (`FileNotFoundError`), make `enemy_image` a green `pygame.Surface((40, 40))`.
- Update your draw loop to use `screen.blit(enemy_image, enemy_rect)` instead of `pygame.draw.rect`.
- **Test the Net:** Rename your image file to `enemy_broken.png` and run the game to prove your backup green square works!
