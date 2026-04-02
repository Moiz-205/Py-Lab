from PIL import Image
import sys
import os

def load_image(path, color: bool, new_width=100):
    path = "images/" + path
    image = Image.open(path)
    if color:
        image = image.convert("RGB")
    else:
        image = image.convert("L")
    width, height = image.size
    new_height = int((height / width) * new_width * 0.5)
    image = image.resize((new_width, new_height))
    return image, new_width, new_height

def to_ascii(image, width, height, color):
    chars = "@%#&-=+_:.,$!*"
    art = ""

    if color:
        for y in range(height):
            row = ""
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                brightness = int(0.299*r + 0.587*g + 0.114*b)
                index = brightness * (len(chars) - 1) // 255
                row += f"\033[38;2;{r};{g};{b}m{chars[index]}\033[0m"   # standard luminance formula
            art += row + "\n"
    else:
        for y in range(height):
            row = ""
            for x in range(width):
                pixel = image.getpixel((x, y))
                index = int(pixel) * (len(chars) - 1) // 255    # type: ignore
                row += chars[index]
            art += row + "\n"
    return art

def save_ascii(art, path):
    name = os.path.splitext(path)[0]
    output_filename = "ascii-" + name + ".txt"
    output_path = os.path.join("outputs", output_filename)
    print(f"File saved at location: {output_path}")
    with open(output_path, "w") as f:
        f.write(art)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    path = sys.argv[1]
    color = input("Want color ascii art (y/n): ").strip().lower() == 'y'
    image, width, height = load_image(path, color)
    art = to_ascii(image, width, height, color)
    print(art)
    save = input("Want to save ascii art (y/n) :").strip().lower() == 'y'
    if save:
        save_ascii(art, path)
    else:
        print("Exited.")

if __name__ == "__main__":
    main()
