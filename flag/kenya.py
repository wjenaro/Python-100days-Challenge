from PIL import Image, ImageDraw

# Define the dimensions of the flag
width = 300
height = 200

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define the colors of the flag
black_color = (0, 0, 0)
red_color = (206, 17, 38)
green_color = (0, 122, 61)

# Calculate the height of each stripe
stripe_height = height // 3

# Draw the three horizontal stripes
draw.rectangle([0, 0, width, stripe_height], fill=black_color)
draw.rectangle([0, stripe_height, width, 2 * stripe_height], fill=red_color)
draw.rectangle([0, 2 * stripe_height, width, height], fill=green_color)

# Save and display the flag
image.show()
