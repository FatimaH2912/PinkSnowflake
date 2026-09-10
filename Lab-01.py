import turtle
import random
import math

# -----------------------------
# Screen setup
# -----------------------------
screen = turtle.Screen()
screen.bgcolor("#160B14")
screen.title("Pink Dream Koch Snowflake")
screen.setup(width=900, height=900)

# -----------------------------
# Main turtle
# -----------------------------
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.hideturtle()
snowflake.penup()

# Pink color palette
pink_colors = [
    "#FFB6D9",
    "#FF8FC7",
    "#FF6FB5",
    "#FFC8E3",
    "#F48FB1"
]

# -----------------------------
# Draw a tiny cute flower
# -----------------------------
def draw_flower(t, size=5):
    t.pendown()

    for _ in range(5):
        t.dot(size, random.choice(pink_colors))
        t.penup()
        t.forward(size * 1.4)
        t.pendown()
        t.right(72)

    t.penup()


# -----------------------------
# Draw decorative sparkle
# -----------------------------
def draw_sparkle(t, size=5):
    original_heading = t.heading()

    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.backward(size * 2)
        t.forward(size)
        t.right(90)

    t.penup()
    t.setheading(original_heading)


# -----------------------------
# Koch fractal function
# -----------------------------
def koch_curve(t, length, depth):

    # Base case
    if depth == 0:
        t.pendown()
        t.forward(length)
        t.penup()
        return

    # Four recursive sections
    koch_curve(t, length / 3, depth - 1)

    t.left(60)
    koch_curve(t, length / 3, depth - 1)

    t.right(120)
    koch_curve(t, length / 3, depth - 1)

    t.left(60)
    koch_curve(t, length / 3, depth - 1)


# -----------------------------
# Draw the main snowflake
# -----------------------------

snowflake.goto(-250, 145)
snowflake.setheading(0)

# Draw three sides
for side in range(3):

    # Change color for each side
    snowflake.pencolor(pink_colors[side + 1])
    snowflake.width(3)

    koch_curve(
        snowflake,
        500,
        4
    )

    snowflake.right(120)


# -----------------------------
# Add decorative flowers
# -----------------------------

# Positions around the snowflake
decorations = [
    (-250, 145),
    (250, 145),
    (0, -288),
    (-115, 45),
    (115, 45),
    (0, 145)
]

for x, y in decorations:
    snowflake.goto(x, y)

    # Randomly choose decoration
    if random.choice([True, False]):
        draw_flower(snowflake, 6)
    else:
        draw_sparkle(snowflake, 7)


# -----------------------------
# Add small floating sparkles
# -----------------------------

sparkles = [
    (-340, 250),
    (320, 260),
    (-350, -100),
    (350, -120),
    (-80, -350),
    (100, -350),
    (-410, 30),
    (410, 40),
    (-190, 300),
    (190, 300)
]

for x, y in sparkles:

    snowflake.goto(x, y)

    snowflake.pencolor(random.choice(pink_colors))

    draw_sparkle(
        snowflake,
        random.randint(5, 9)
    )


# Keep window open
turtle.done()
