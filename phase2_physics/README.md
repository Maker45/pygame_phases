# Phase 2: Control Flow (Input & Conditionals)

**Goal:** Make the game interactive using logic.

**PCEP Concepts:** `if`, `elif`, `else`, Comparison Operators (`>`, `<`, `==`), Logical Operators (`and`, `or`, `not`)

---

## 01_keyboard_dodger.py

### Lesson 2.1: The Keyboard Dodger — "Taking Control"

📊 **Slides:** [Phase 2, Lesson 2.1](https://docs.google.com/presentation/d/1M_vGXort4ILt63RAzviV89gAUEBQA4g8BKhEnMXBLog/view)

**Goal:** Move the player square using the arrow keys and keep it inside the window.

**Two ways to listen to the keyboard**
- **Events (a doorbell):** Good for typing or menus. "Did they just press Space?"
- **Polling (a light switch):** Good for movement. "Is the Right Arrow held down right now?"

**Steps**
1. **The Setup:** Create variables for the player's X and Y, and a `player_speed` variable. Avoid "magic numbers" — don't write `5` everywhere. If you want to go faster later, you only change one line!
2. **The Input Check:** `keys = pygame.key.get_pressed()` returns a list of every key on the keyboard. `if keys[pygame.K_LEFT]:` means "If the Left Arrow is True…". Left is subtract, right is add.
3. **The `elif` Trap:** What happens if you press Left AND Right at the same time?
   - With `if` / `elif`: It checks Left. If true, it skips Right. You only move left.
   - With `if` / `if`: It moves -5, then +5. You stay still.
4. **Boundaries:** Stop the player from driving off the screen using `and`: "Move left ONLY IF the key is pressed AND we are not at the edge."
5. **The "Dodger" Element:** Create an enemy variable and make it fall (`y += speed`). When it hits the bottom (`y > 600`), reset it to the top (`y = -50`) and pick a new random X.

### Lab Challenge: "The Endless Rain"
- Implement player movement (left/right).
- Implement the screen boundaries.
- Add one falling enemy that resets when it hits the bottom.
- **Bonus:** Make the enemy get faster every time it resets! (`enemy_speed += 1`)
- *Hint:* You will need `import random` at the top of your file.

---

## 02_survival_mode.py

### Lesson 2.2: Collision Detection — "Contact!"

📊 **Slides:** [Phase 2, Lesson 2.2](https://docs.google.com/presentation/d/1WF12RloMK3L6CGBgd5oLbh1hvKwcb_PIvuV-NC8BgC8/view)

**Goal:** Detect when the player touches an enemy and trigger a "Game Over" state.

**PCEP Concepts:** Boolean Logic, Objects (introductory), Methods, Tuple assignment

**Steps**
1. **The Power of the Rect:** A `pygame.Rect` is a container that holds 4 numbers: X, Y, width, height. It tracks the corners for you. Access values with `player_rect.x` and `player_rect.y`.
2. **Update Movement:** Change `player_rect.x` directly. When you draw, use the Rect instead of separate variables: `pygame.draw.rect(screen, RED, player_rect)`.
3. **The Magic Method:** A method is a function that belongs to an object. `.colliderect()` asks: "Am I touching that other rectangle?"
4. **The "Game Over" State:** Use a Boolean like `game_active` to track the mode. If `True`, play the game. If `False`, show the restart screen.

### Lab Challenge: "Survival Mode"
- Convert your player and enemy x, y variables into `pygame.Rect` objects.
- Use `.colliderect()` to detect a hit.
- **The Consequence** (pick your level):
  - **Easy:** Close the window when hit.
  - **Medium:** Reset the player to the start position when hit.
  - **Hard:** Stop the game and fill the screen with red when hit.
- *Hint:* Remember to change your `pygame.draw.rect()` command to use the new Rect objects!
