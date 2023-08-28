from PIL import Image, ImageDraw

# Define the dimensions of the flag
width = 500
height = 200
# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)
# Define the colors of the flag
blue_color = (0, 43, 127)
yellow_color = (255, 213, 0)
# Calculate the height of each stripe
stripe_height = height // 2
# Draw the two horizontal stripes
draw.rectangle([0, 0, width, stripe_height], fill=blue_color)
draw.rectangle([0, stripe_height, width, height], fill=yellow_color)
# Save and display the flag
image.show()
