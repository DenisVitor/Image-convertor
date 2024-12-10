from PIL import Image
import os


def convert_to_grayscale(image):
    if image.mode != "RGB":
        image = image.convert("RGB")

    width, height = image.size
    grayscale_image = Image.new("L", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_image.putpixel((x, y), grayscale_value)

    return grayscale_image


def binarize_image(grayscale_image, threshold=127):
    width, height = grayscale_image.size
    binary_image = Image.new("1", (width, height))

    for y in range(height):
        for x in range(width):
            grayscale_value = grayscale_image.getpixel((x, y))
            binary_value = 255 if grayscale_value > threshold else 0
            binary_image.putpixel((x, y), binary_value)

    return binary_image


def process_image(image_path):
    original_image = Image.open(image_path)

    grayscale_image = convert_to_grayscale(original_image)
    grayscale_path = os.path.splitext(image_path)[0] + "_grayscale.png"
    grayscale_image.save(grayscale_path)

    binary_image = binarize_image(grayscale_image)
    binary_path = os.path.splitext(image_path)[0] + "_binary.png"
    binary_image.save(binary_path)

    original_image.show()
    grayscale_image.show()
    binary_image.show()


process_image("lena_color.png")
