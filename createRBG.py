from PIL import Image
from randomORG import onlineRandom
import random


def getRandom8bits(randomIntegers):
    # randomly select an int from list of random integers
    randomNum = randomIntegers[random.randint(0,len(randomIntegers)-1)]

    # randomly select which 8 bits to grab
    op = random.randint(0,2)

    #8 bit mask
    mask = 0xFF

    low8 = 0
    if op==0:
        low8 = (randomNum & mask)
    elif op==1:
        low8 = (randomNum >> 8) & mask
    else:
        low8 = (randomNum >> 16) & mask

    return low8


def getPixelMatrix():
    # create arrays to hold 8 bit RGB pixel values

    rPix = []
    gPix = []
    bPix = []

    # Generate 1000 random numbers with min val 2^25 (we need at least 24 bits in each number for 3 8-bit rgb values)
    randomInts = random.sample(range(2**25,2**28),1000) #use this for testing
    #randomInts = onlineRandom(2**25,2**28,1000) #use this is actual implementation

    while len(rPix) < (128*128):
        rPix.append(getRandom8bits(randomInts))
        gPix.append(getRandom8bits(randomInts))
        bPix.append(getRandom8bits(randomInts))

    matrix = [rPix, gPix, bPix]
    return matrix

matrix = getPixelMatrix()
#print(len(matrix[1]))

#PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (128,128), "black") # create a new black image
pixels = img.load() # create the pixel map

idx = 0
for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (matrix[0][idx], matrix[1][idx], matrix[2][idx]) # set the colour accordingly
        idx += 1

img.show()