from PIL import Image
import random

def getRandomPixels(size):
    pixels = []

    while len(pixels) < size:
        pixels.append(random.randint(0,255))

    return pixels


# We will be creating a 128 X 128 RGB bitmap using random pixels
# Each pixel is 8 bit RGB ... so color range 0-255

bPix = getRandomPixels(16384) # 128*128 pixels
rPix = getRandomPixels(16384) # 128*128 pixels
gPix = getRandomPixels(16384) # 128*128 pixels
#print(randPix[0])



# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (128,128), "black") # create a new black image
pixels = img.load() # create the pixel map

idx = 0
for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (rPix[idx], gPix[idx], bPix[idx]) # set the colour accordingly
        idx += 1

img.show()