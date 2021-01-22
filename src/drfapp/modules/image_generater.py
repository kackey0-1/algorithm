from PIL import Image, ImageDraw, ImageFont
import sys
import numpy

from PIL import Image, ImageDraw, ImageFont


def generate(text, color, fonttype='modules/fonts/Ricty-Bold.ttf', fontsize=64):

    # Specify True-Type font and Font-Size
    font = ImageFont.truetype(fonttype, fontsize)
    image = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    print(text[0:2])
    print(text[2:4])
    draw.text((0, 0), '{}\n{}'.format(text[0:2], text[2:4]), font=font, fill=color)
    image_name = 'emoji_{}.png'.format(text)
    image.save('static/images/' + image_name, 'PNG')
    return image_name


if __name__ == '__main__':
    generate(text='スゲーナ', color='#000000', fonttype='modules/fonts/Ricty-Bold.ttf')

    """
    from modules import image_generater
    image_generater.generate(text='それな', color='#000000')
    #
    arg = sys.argv
    # created file name
    lines = arg[1].split(',')
    line1 = lines[0]
    line2 = lines[1]
    imgname = line1 + line2 + '.png'
    color = arg[2]
    img = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
    # font size = 1行の場合: 100, 2行の場合: 50, 3行の場合: 33
    font = ImageFont.truetype('fonts/03SmartFontUI.ttf', size=50,)
    textd = ImageDraw.Draw(img)
    img_size = numpy.array(img.size)
    txt_size = numpy.array(font.font.getsize(line1))

    txt_size[0]
    txt_size[1]
    mid = 128 / 2
    font_hight = (txt_size[0][1] + txt_size[1][1]) / 2
    hight_s = (128 - font_hight)/2
    # print(img_size)
    print(txt_size)
    # 0-128: left & right should be equal
    # print(img_size - txt_size)
    textd.text((0, hight_s - txt_size[1][1]), line1, fill=color, spacing=4, align='center', font=font)
    # textd.text((0, 64), line1, fill=color, spacing=4, align='center', font=font)

    img.save(imgname)
    print("Save " + imgname)
    """




