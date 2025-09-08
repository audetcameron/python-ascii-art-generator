from PIL import Image
import sys



# Define the ASCII characters based on brightness
# Characters are ordered from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

# Function to resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55) # Adjust height for terminal aspect ratio
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    return ascii_str

# Main function to convert image to ASCII art
def image_to_ascii(name, new_width=100):

    image_path = f"images/{name}.png"
    # print(f"ASCII art successfully saved to {name}")
    # sys.exit()

    try:
        # Open the image and convert it to grayscale
        image = Image.open(image_path).convert("L")
    except FileNotFoundError:
        print(f"Error: The image at '{image_path}' was not found.")
        return

    # Resize and convert the image
    resized_image = resize_image(image, new_width)
    ascii_art = pixels_to_ascii(resized_image)

    # Format the ASCII string with newlines
    img_width, _ = resized_image.size
    ascii_art_with_newlines = ""
    for i in range(0, len(ascii_art), img_width):
        ascii_art_with_newlines += ascii_art[i:i+img_width] + "\n"

    # Print the result
    print(ascii_art_with_newlines)

    # 2. Define the output file name
    output_filename = f"ascii-art/{name}.txt"

    # 3. Write the ASCII art to the text file
    try:
        with open(output_filename, "w") as f:
            f.write(ascii_art_with_newlines)
        print(f"ASCII art successfully saved to {output_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Main function
if __name__ == "__main__":
    # print(f"First argument: {sys.argv[1]}")
    image_to_ascii( f"{sys.argv[1]}")
