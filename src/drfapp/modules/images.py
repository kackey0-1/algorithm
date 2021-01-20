from PIL import Image, ImageDraw, ImageFont
import sys


if __name__ == '__main__':

    # 絵文字にしたい文字を入れる引数を定義
    arg = sys.argv
    imgname = arg[1] + arg[2] + '.png'
    len_1 = arg[1]
    len_2 = arg[2]
    # 透明な256×256pxの画像を生成する
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    # 使用したいフォントの絶対パス、フォントサイズを指定する
    fontcustom = ImageFont.truetype('~/Library/Fonts/GenJyuuGothicX-Heavy.ttf', 124)
    # フォントカラーを引数から指定する
    fontcolor = arg[3]
    textd = ImageDraw.Draw(img)
    # 2文字×2文字の引数が来たらテキストを描画する
    if len(len_1) == 2:
        textd.text((0, -25), arg[1], fill=fontcolor, spacing=5, align='center', font=fontcustom)
    else:
        print("1行目の文字数は大文字2文字にして下さい")
        sys.exit()

    if len(len_2) == 2:
        textd.text((0, 105), arg[2], fill=fontcolor, spacing=5, align='center', font=fontcustom)
    else:
        print("2行目の文字数は大文字2文字にして下さい")
        sys.exit()

    # 「引数1+引数2」というファイルをpng形式で保存する
    img.save(imgname)
    print("Save " + imgname)
