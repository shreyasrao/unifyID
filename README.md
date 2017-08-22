# UnifyID Technical Challenge

randomORG.py has the function onlineRandom() which is used to grab random integers from random.org

createRGB.py uses the random integers to generate 128 x 128 RGB picture

## Details

We used 8-bit RGB encoding scheme during picture generation. For (128 x 128 pixels) and (3 colors), we would need 49,152 random integers. Since random.org only provides a max of 1000 ints, we created a work around.

The minimum value for our 1000 random ints was 2^25. This was to ensure a min of 24 bits in each random int. Then for each color in each pixel, we randomly selected a number from the output of random.org, and randomly selected 8 bits to use as our color value. This was done using bit masking and bit shifting. 

The resulting image of random colored pixels is saved as 'random.jpg'.

### Dependencies

python3

PIL
