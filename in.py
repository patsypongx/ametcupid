from PIL import Image, ImageDraw, ImageFont

# Create a blank image
image = Image.new('RGB', (400, 200), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load a rounded font
font_path = "path/to/your/rounded_font.ttf"
font = ImageFont.truetype(font_path, 17)

# Draw text on the image
text = "This is text in a rounded font at 17 points."
text_width, text_height = draw.textsize(text, font)
x = (image.width - text_width) // 2
y = (image.height - text_height) // 2
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# Save or display the image
image.show()
