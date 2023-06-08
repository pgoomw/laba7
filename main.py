from PIL import Image, ImageFilter

def z1():
    image = Image.open('1.jpg')
    image.show()

    width, height = image.size
    format = image.format
    mode = image.mode

    print("Ширина:", width)
    print("Высота:",height)
    print("Формат:", format)
    print("Цветовая модель:", mode)
print(z1())

def z2():
    image1 = Image.open('2.jpg')
    width, height = image1.size
    new_image = image1.resize((width // 3, height // 3))
    new_image.save('n_image.jpg')
    ver_image = image1.transpose(Image.FLIP_LEFT_RIGHT)
    ver_image.save('r_image.jpg')
    hor_image = image1.transpose(Image.FLIP_TOP_BOTTOM)
    hor_image.save('b_image.jpg')
print(z2())

def z3():
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for name in images:
        image = Image.open(name)
        filtered_image = image.filter(ImageFilter.EMBOSS)
        new3_name = "new3_" + name
        filtered_image.save(new3_name)
print(z3())

def z4():
    image4 = Image.open('sobaken.jpg')
    watermark = Image.open('watermark.png')

    watermark_resized = watermark.resize((200, 200)) # возвращаем новую картинку с новыми размерами  в виде кортежа '(ширина, высота)
    width, height = image4.size
    water_width, water_height = watermark_resized.size
    x = width - water_width - 120
    y = height - water_height - 10

    image4.paste(watermark_resized, (x, y), watermark_resized)
    image4.save('wmphoto.jpg')
print(z4())