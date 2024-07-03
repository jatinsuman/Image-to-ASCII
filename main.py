from PIL import Image, ImageDraw, ImageFont, ImageEnhance

nonrgbim = Image.open("testpic.jpg", "r")
im = nonrgbim.convert("RGB")

im_width, im_height = im.size

new_width, new_height = int(im_width) * (1200 / max(im.size)), int(im_height) * (1200 / max(im.size))
new_image = im.resize((int(new_width), int(new_height)))

pixel_val = []

for x in range(0, int(new_width), 6):
    for y in range(0, int(new_height), 6):
        pixelRGB = new_image.getpixel((x, y))
        R, G, B = pixelRGB
        brightness = sum([R, G, B])/3
        pixel_val.append(int(brightness))

ascii_chars = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q',\
               'w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r',\
                'j','f','t','/',"|",'()','1',"{}",'[]','?','-','_','+','~','<','>','i','!','l','I',';',':',',','"',\
                    '^','`',"'",'.']

n = 0
for pix in pixel_val:
    if pix == 0:
        pixel_val[n] = " "
    else:
        pixel_val[n] = ascii_chars[pix // 4]
    n += 1
n = 0

ascii_image = Image.new(mode="RGB", size=(int(new_width), int(new_height)))

draw = ImageDraw.Draw(ascii_image)

font = ImageFont.truetype("OpenSans-Regular.ttf", 6)

for x_pos in range(0, int(new_width), 6):
    for y_pos in range(0, int(new_height), 6):
        draw.text((x_pos, y_pos), pixel_val[n], font=font)
        n += 1

ascii_image = ImageEnhance.Brightness(ascii_image).enhance(3)
ascii_image.show()
