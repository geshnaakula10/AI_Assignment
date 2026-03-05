import random
import string
from PIL import Image, ImageDraw, ImageFont


def generate_captcha_text(length=6):
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text


def create_captcha_image(text):
    width = 200
    height = 80

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()


    draw.text((40, 20), text, fill="black", font=font)


    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill="gray", width=1)

    image.save("captcha.png")
    image.show()


def verify_captcha(original_text):
    user_input = input("Enter CAPTCHA: ")

    if user_input == original_text:
        print("Verification Successful: You are human!")
    else:
        print("CAPTCHA Incorrect. Try again.")



def main():
    print("Generating CAPTCHA...\n")

    captcha_text = generate_captcha_text()
    create_captcha_image(captcha_text)

    verify_captcha(captcha_text)


if __name__ == "__main__":
    main()