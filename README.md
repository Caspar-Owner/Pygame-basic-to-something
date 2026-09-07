```This is just Pygame CMD and the way to learn```

## 1. Install Pygame

Open **CMD / PowerShell**:

```cmd
python --version
```

Then:

```cmd
pip install pygame
```

Check installation:

```cmd
python -m pygame --version
```

Create a project folder:

```cmd
mkdir pygame_project
cd pygame_project
```

Create your first file:

```cmd
notepad main.py
```

Run it:

```cmd
python main.py
```

---

# 2. Essential Pygame commands

### Import

```python
import pygame
```

### Initialize Pygame

```python
pygame.init()
```

### Create a window

```python
screen = pygame.display.set_mode((800, 600))
```

### Set window title

```python
pygame.display.set_caption("My Game")
```

### Set background

```python
screen.fill((0, 0, 0))
```

RGB:

```python
(255, 0, 0)      # Red
(0, 255, 0)      # Green
(0, 0, 255)      # Blue
(255, 255, 255)  # White
(0, 0, 0)        # Black
```

### Update the screen

```python
pygame.display.flip()
```

or:

```python
pygame.display.update()
```

---

# 3. The Game Loop

This is **the most important concept in Pygame**.

```python
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
```

Then:

```python
pygame.quit()
```

Complete basic program:

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
```

---

# 4. Drawing shapes

### Rectangle

```python
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))
```

The rectangle is:

```text
(x, y, width, height)
```

### Circle

```python
pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)
```

### Line

```python
pygame.draw.line(screen, (255, 255, 255), (0, 0), (800, 600), 5)
```

### Polygon

```python
pygame.draw.polygon(
    screen,
    (255, 0, 0),
    [(100, 100), (200, 50), (300, 100)]
)
```

---

# 5. Images

Load an image:

```python
image = pygame.image.load("player.png")
```

Better:

```python
image = pygame.image.load("player.png").convert_alpha()
```

Display it:

```python
screen.blit(image, (100, 100))
```

---

# 6. Scale images

You asked about this recently, so this one is important.

```python
image = pygame.transform.scale(image, (200, 200))
```

Or scale by a percentage:

```python
image = pygame.transform.scale_by(image, 0.5)
```

Rotate:

```python
image = pygame.transform.rotate(image, 90)
```

Flip:

```python
image = pygame.transform.flip(image, True, False)
```

---

# 7. Keyboard controls

Check whether a key is being held:

```python
keys = pygame.key.get_pressed()
```

Then:

```python
if keys[pygame.K_LEFT]:
    x -= 5

if keys[pygame.K_RIGHT]:
    x += 5

if keys[pygame.K_UP]:
    y -= 5

if keys[pygame.K_DOWN]:
    y += 5
```

Common keys:

```python
pygame.K_a
pygame.K_d
pygame.K_w
pygame.K_s

pygame.K_LEFT
pygame.K_RIGHT
pygame.K_UP
pygame.K_DOWN

pygame.K_SPACE
pygame.K_ESCAPE
pygame.K_RETURN
```

---

# 8. Mouse

Get mouse position:

```python
mouse_x, mouse_y = pygame.mouse.get_pos()
```

Check buttons:

```python
mouse_buttons = pygame.mouse.get_pressed()
```

Mouse click event:

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    print("Clicked!")
```

Get click position:

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    print(event.pos)
```

---

# 9. Text

Create a font:

```python
font = pygame.font.Font(None, 50)
```

Create text:

```python
text = font.render("Hello World", True, (255, 255, 255))
```

Display it:

```python
screen.blit(text, (100, 100))
```

Use a specific font:

```python
font = pygame.font.Font("font.ttf", 50)
```

---

# 10. FPS / Game speed

Create a clock:

```python
clock = pygame.time.Clock()
```

Limit the game to 60 FPS:

```python
clock.tick(60)
```

You'll eventually want movement based on **delta time**:

```python
dt = clock.tick(60) / 1000
```

Then:

```python
x += speed * dt
```

---

# 11. Sound

Load sound:

```python
sound = pygame.mixer.Sound("jump.wav")
```

Play it:

```python
sound.play()
```

Music:

```python
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
```

Stop:

```python
pygame.mixer.music.stop()
```

Volume:

```python
pygame.mixer.music.set_volume(0.5)
```

---

# 12. Rect — VERY IMPORTANT

Pygame's `Rect` system is one of the things you should learn early.

```python
player = pygame.Rect(100, 100, 50, 50)
```

Move:

```python
player.x += 5
```

or:

```python
player.y += 5
```

Draw:

```python
pygame.draw.rect(screen, (255, 0, 0), player)
```

Get position:

```python
player.x
player.y
```

Get dimensions:

```python
player.width
player.height
```

Collision:

```python
if player.colliderect(enemy):
    print("Collision!")
```

---

# 13. Collision

Two rectangles:

```python
player = pygame.Rect(100, 100, 50, 50)
enemy = pygame.Rect(300, 100, 50, 50)
```

Check:

```python
if player.colliderect(enemy):
    print("Hit!")
```

Point inside rectangle:

```python
if player.collidepoint(mouse_x, mouse_y):
    print("Mouse is inside player")
```

---

# 14. Timers

Wait:

```python
pygame.time.delay(1000)
```

This waits 1 second.

For actual games, don't usually use `delay()` because it freezes the game.

You can create timed events:

```python
pygame.time.set_timer(pygame.USEREVENT, 1000)
```

Then:

```python
if event.type == pygame.USEREVENT:
    print("1 second passed")
```

---

# 15. Groups

Once you have multiple enemies:

```python
enemies = pygame.sprite.Group()
```

This becomes very useful when you learn sprites.

---

# 16. Sprites

Eventually you'll use:

```python
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
```

Then:

```python
player = Player()
```

And:

```python
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
```

Draw everything:

```python
all_sprites.draw(screen)
```

---

# Your learning order

**Don't try to memorize everything above.** Learn Pygame in this order:

```text
1. pygame.init()
        ↓
2. display.set_mode()
        ↓
3. Game Loop
        ↓
4. Events
        ↓
5. Drawing shapes
        ↓
6. Images + blit()
        ↓
7. Keyboard
        ↓
8. Mouse
        ↓
9. Rect
        ↓
10. Collision
        ↓
11. FPS / Clock
        ↓
12. Text
        ↓
13. Sound
        ↓
14. Sprites
        ↓
15. Sprite Groups
        ↓
16. Animation
        ↓
17. Scenes / Menus
        ↓
18. Build a complete game
```

And the **core Pygame skeleton** you should eventually be able to write without copying is:

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()

    # Update
    # player movement, enemies, collision, etc.

    # Draw
    screen.fill((0, 0, 0))

    # pygame.draw...
    # screen.blit...

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
```

**That loop is the foundation.** Once you understand what happens in **Events → Input → Update → Draw → FPS**, Pygame starts making a lot more sense.
