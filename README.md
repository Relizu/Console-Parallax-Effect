# 🌌 ASCII Parallax Effect

A mesmerizing **parallax-style ASCII effect** that runs directly in your terminal!  
This Python script creates a layered background that moves at different speeds, producing a smooth **depth illusion** — just like the classic parallax effect seen in games and art.

---

## 🌀 Features

- 🎞️ **True parallax motion** with multiple ASCII layers  
- 💻 **Terminal-based** — no external libraries required  
- 🎨 **Easily customizable** ASCII art backgrounds  
- ⚙️ **Smooth animation** using timed updates  

---

## 🧠 How It Works

The effect uses **three layers** of ASCII art (`layer1`, `layer2`, `layer3`) defined in `backgrounds.py`.

Each layer scrolls horizontally at a different speed:

| Layer | Speed | Description |
|--------|--------|-------------|
| `layer1` | Fast | Foreground (closest layer) |
| `layer2` | Medium | Midground |
| `layer3` | Slow | Background (farthest layer) |

Every frame, the program:
1. Merges the three layers — characters from the front layer overwrite empty spaces in the layers behind.
2. Shifts each layer based on its speed.
3. Reprints the full frame in place using ANSI escape codes.

This creates a **smooth parallax scrolling effect** — entirely in ASCII!

---

## 🚀 Run It Yourself

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ascii-parallax-effect.git
cd ascii-parallax-effect
```
### 2. Run the effect
```bash
python3 main.py
```

🐍 Requires Python 3.7+
Works best in a terminal that supports ANSI escape sequences (Linux, macOS, Windows Terminal, etc.)

### 🎨 Customizing the Layers

Open backgrounds.py and edit the three ASCII art layers.
Example:

```py
layer1 = """
  ~~~~     ~~~~     ~~~~
"""

layer2 = """
    ^     ^      ^     ^
"""

layer3 = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
```

Each layer should have the same number of lines and roughly the same width for smooth blending.
### Output
```
      ~~~~     ~~~~     ~~~~
           ^     ^      ^    ^
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```
