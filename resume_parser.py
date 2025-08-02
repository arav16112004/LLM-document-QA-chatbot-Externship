import fitz
import os
import re

doc = fitz.open("LenderFeesWorksheetNew.pdf")

text = doc[0].get_text()


name = re.search(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", text)

if name:
    phone_number = name.group()
    print(f"Candidate Phone Number: {phone_number}")
else:
    print("Phone number not found.")



import cv2
import numpy as np
from PIL import Image

from IPython.display import display

# Convert PDF page to an image
pix = doc[0].get_pixmap()
img = np.array(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))

# Convert image to OpenCV BGR format
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Get the actual image height
img_height = img.shape[0]  # OpenCV uses (height, width, channels)

# Extract words and their bounding boxes
words = doc[0].get_text("words")

# Define the field we are looking for
target_word = "Loan"  # Replace with actual phone number

# Flag to check if the word was found
word_found = False

# Search for the target word and retrieve its bounding box
for word in words:
    x0, y0, x1, y1, text, block, line, word_no = word  # Unpack correctly

    print

    if target_word in text:  # Case-sensitive match (modify if needed)
        # Convert PyMuPDF's y-coordinates (bottom-left origin) to OpenCV's (top-left origin)
        y0_new = y1  # Convert bottom-left to top-left
        y1_new = y0  # Convert bottom-left to top-left

        # Convert coordinates to integers
        x0, y0_new, x1, y1_new = map(int, [x0, y0_new, x1, y1_new])

        # Draw a rectangle around the detected word
        cv2.rectangle(img, (x0, y0_new), (x1, y1_new), (0, 255, 0), 2)

        print(f"Found '{target_word}' at: ({x0}, {y0_new}, {x1}, {y1_new})")
        word_found = True

# Ensure an image is displayed even if no word is found
if not word_found:
    print(f"'{target_word}' not found in document.")

# Convert back to RGB for displaying in PIL
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to PIL image and show
Image.fromarray(img_rgb).show()