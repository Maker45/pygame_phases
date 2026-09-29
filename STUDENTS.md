# Getting the Pygame Lesson Files

Repo link: **https://github.com/Maker45/pygame_phases**

## Option A: Download a ZIP (easiest, no setup)

1. Go to **https://github.com/Maker45/pygame_phases**
2. Click the green **Code** button, then **Download ZIP**.
3. Unzip the folder onto your Desktop.
4. When new lessons are posted, repeat these steps to get a fresh copy. Move your own work out of the old folder first!

## Option B: Use Git (recommended if Git is installed)

**First time only:** open a terminal (PowerShell on Windows, Terminal on Mac) and run:

```
cd Desktop
git clone https://github.com/Maker45/pygame_phases.git
```

This creates a `pygame_phases` folder on your Desktop.

**Every time new lessons are posted:**

```
cd Desktop/pygame_phases
git pull
```

## Important: protect your work

Don't edit the original lesson files. Make a copy and add your name, for example `01_moving_square_jsmith.py`. Your copies won't be touched when you run `git pull`, and the pull won't fail.

## Running a lesson

```
cd Desktop/pygame_phases/phase1_basics
python 01_moving_square.py
```

If you get `No module named pygame`, run `python -m pip install pygame` first.
