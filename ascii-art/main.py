from PIL import Image

def load_image(path):
    im = Image.open(path)
    width, height = im.size
    im = im.convert("L")
    new_width = 50
    new_height = int((height / width) * new_width * 0.5)
    im = im.resize((new_width, new_height))
    return im, new_width, new_height

def to_ascii(image, width, height):
    row = ""
    chars = "@%#&-=+_:.,$!*"
    for y in range(height):
        row = ""
        for x in range(width):
            pixel = image.getpixel((x, y))
            index = int(pixel) * (len(chars) - 1) // 255    # type: ignore
            row += chars[index]
        print(row)

def main():
    path = "images/car.png"
    image, width, height = load_image(path)
    to_ascii(image, width, height)

if __name__ == "__main__":
    main()
