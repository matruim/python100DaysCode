from PIL import Image

def adjust(image, size):
    image = image.convert('RGBA')
    width, height = image.size
    new_width = size[0]
    new_height = new_width * height // width
    image = image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
    new_image = Image.new('RGBA', size, (0, 0, 0, 0))
    upper = (size[1] - image.size[1]) // 2
    new_image.paste(image, (0, upper))
    new_image.putalpha(50)

    return new_image

#watermark image
image1 = Image.open('cyberpunk.png')

#Main image
image2 = Image.open('/Users/matruim/Pictures/Me.png')

image1 = adjust(image1, image2.size)

#watermarked image
image3 = Image.alpha_composite(image2, image1)
image3.show()


