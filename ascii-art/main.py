from PIL import Image
import sys
import os

def load_image(path, new_width=100):
    path = "images/" + path
    image = Image.open(path)
    image = image.convert("L")
    width, height = image.size
    new_height = int((height / width) * new_width * 0.5)
    image = image.resize((new_width, new_height))
    return image, new_width, new_height

def to_ascii(image, width, height):
    chars = "@%#&-=+_:.,$!*"
    art = ""
    for y in range(height):
        row = ""
        for x in range(width):
            pixel = image.getpixel((x, y))
            index = int(pixel) * (len(chars) - 1) // 255    # type: ignore
            row += chars[index]
        art += row + "\n"
    return art

def save_ascii(rows, path):
    name = os.path.splitext(path)[0]
    output_filename = "ascii-" + name + ".txt"
    output_path = os.path.join("outputs", output_filename)
    with open(output_path, "w") as f:
        f.write(rows)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    path = sys.argv[1]
    image, width, height = load_image(path)
    art = to_ascii(image, width, height)
    user = int(input("1. Save to file \t 2. Print to terminal\nChoice: "))
    if user == 1:
        save_ascii(art, path)
    elif user == 2:
        print(art)

if __name__ == "__main__":
    main()
