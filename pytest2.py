import pytesseract
from PIL import ImageGrab
import sys
import os

def take_screenshot_and_extract_text():
    words = sys.argv[1:]
    words = [element.replace("'", "") for element in words[0][1:-1].split(", ")]

    # Create directories to store the images and text
    img_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'images')
    text_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'text')
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(text_dir, exist_ok=True)
    print(f"Saving images to directory {img_dir}")
    print(f"Saving text to directory {text_dir}")

    counter = 0

    # Continuously take screenshots and extract text
    while True:
        # Take a screenshot
        img = ImageGrab.grab()

        # Save the screenshot to a file in the images directory
        img_file = os.path.join(img_dir, f"screenshot_{counter}.png")
        img.save(img_file)

        # Extract text from the screenshot using pytesseract
        text = pytesseract.image_to_string(img)
# FIND THE COORDINATES OF THE PLAY BUTTO AND THEN FROM THERE YOU ALSO TAKE THE WORD BESIDE IT AND THEN ITERATE THROUGH THE ARRAY TO THEN POP THAT WORD 
        # Check if the first element of the words list is present in the extracted text
        print(str(words) + " " + words[0])
        while words and words[0] in text:
            if 'Notes found in file: ⁨0⁩' in text:
                continue
            else:
                # Print and remove the element if found
                found_word = words.pop(0)
                print(f"Found '{found_word}' in screenshot {counter}")
                text_file = os.path.join(text_dir, f"{found_word}.txt")
                with open(text_file, 'w') as f:
                    f.write(text)

        # Save the extracted text to a file in the text directory
        text_file = os.path.join(text_dir, f"text_{counter}.txt")
        with open(text_file, 'w') as f:
            f.write(text)

        # Print the extracted text
#        print(f"Extracted text from screenshot {counter}: {text.strip()}")

        counter += 1

if __name__ == '__main__':
    take_screenshot_and_extract_text()
