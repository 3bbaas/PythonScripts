from PIL import Image, ImageDraw, ImageFont


def Gen(_file_name, _name, _out_f):
    cer = Image.open(_file_name)
    draw = ImageDraw.Draw(cer)
    font = ImageFont.truetype("arial.ttf", 160)
    t_w = font.getmask(_name).getbbox()[2]
    w, h = cer.size
    draw.text(((w - t_w) // 2, 1300), _name, font=font, fill=(0, 0, 0))
    cer.save(_out_f)


if __name__ == '__main__':
    imgPath = input("Enter img path")
    names = list(input("Enter names separated by \',\' ").split(", "))
    outPath = input("Enter output folder: ")
    for name in names:
        Gen(imgPath, name, outPath + "\\" + name + ".png")
