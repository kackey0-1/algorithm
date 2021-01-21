from PIL import Image, ImageDraw, ImageFont
import sys


if __name__ == '__main__':

    #
    arg = sys.argv
    imgname = arg[1] + arg[2] + '.png'
    len_1 = arg[1]
    len_2 = arg[2]
    img = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
    fontcustom = ImageFont.truetype('fonts/arial.ttf', 124)
    fontcolor = arg[3]
    textd = ImageDraw.Draw(img)
    if len(len_1) == 2:
        textd.text((0, -25), arg[1], fill=fontcolor, spacing=5, align='center', font=fontcustom)
    else:
        print("")
        sys.exit()

    if len(len_2) == 2:
        textd.text((0, 105), arg[2], fill=fontcolor, spacing=5, align='center', font=fontcustom)
    else:
        print("")
        sys.exit()

    #
    img.save(imgname)
    print("Save " + imgname)
