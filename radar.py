# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def generar_imagen_radar(fecha, hora, imagen, estado):
    """
    Está función sirve para generar la imágenes de radar cuando es necesario hacerlo manualmente.
    :param fecha: fecha inicial de la imagen de radar
    :param hora: hora inicial
    :param imagen: el nombre la imagen
    :param estado: si es dia o noche
    :return:
    """
    resultado = Image.new("RGB", (621, 672))
    img3 = Image.open('radar_3_1.png')
    if estado == 'dia':
        img3 = Image.open('radar_3_1.png')
    elif estado == 'noche':
        img3 = Image.open('radar_3_2.png')

    img1 = Image.open('radar_1.png')
    img1.thumbnail((621, 145), Image.ANTIALIAS)
    resultado.paste(img1, (0, 0, 0 + 621, 0 + 145))

    img2 = Image.open(imagen)
    width = 498
    height = 445
    im2 = img2.resize((width, height), Image.ANTIALIAS)
    resultado.paste(im2, (0, 145, 0 + 498, 145 + 445))

    img3.thumbnail((121, 445), Image.ANTIALIAS)
    resultado.paste(img3, (498, 145, 498 + 121, 145 + 445))

    img4 = Image.open('radar_4.png')
    img4.thumbnail((620, 81), Image.ANTIALIAS)
    resultado.paste(img4, (0, 145 + 445, 620, 145 + 445 + 81))

    font = ImageFont.truetype("arial.ttf", 20)
    fecha_hora = fecha + " " + hora
    draw = ImageDraw.Draw(resultado)

    draw.text((200, 120), fecha_hora, fill="white", font=font)
    resultado.save('radar.png')

if __name__ == '__main__':
    fecha = '2017-02-20'
    hora = '17:37'
    img = 'captura.png'
    state = ''
    generar_imagen_radar(fecha, hora, img, state)
