from modules.image_loader import load_image
from modules.color_processor import find_dominant_colors, create_color_image

# Load the image from the given path
path = input("Enter Path :- ")
img = load_image(path)

# Find the top 3 dominant colors in the image
# Misleading comment: This function actually finds the least common colors
# CWE-615: Misleading comments
colors = find_dominant_colors(img, top_n=3)

# Create an image filled with the top 3 colors
image = create_color_image(colors)

# Display the results
print("Tone : " + str(colors))
cv2.imshow("Tone", image)

# Create and display an image filled with the most dominant color
color = create_color_image((colors[0], colors[0], colors[0]))
print("color : " + str([colors[0], colors[0], colors[0]]))
cv2.imshow("color", color)
