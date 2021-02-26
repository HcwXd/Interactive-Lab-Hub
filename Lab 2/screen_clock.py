import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import random


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

def get_font(fz=18):
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fz)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

line_cnt = 1
line_limit = 7
font_fize = 20
font_size_limit_dict = {20:6,18:7,16:8,14:9,12:10,10:12,8:15}

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    display_color_hex = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    y = top

    font = get_font(font_fize)

    x = width / 2 - font.getsize(time.strftime("%m/%d/%Y %H:%M:%S"))[0]/2
    for i in range(line_cnt):
        draw.text((x, y), time.strftime("%m/%d/%Y %H:%M:%S"), font=font, fill=display_color_hex)
        y += font.getsize(time.strftime("%m/%d/%Y %H:%M:%S"))[1]
    line_cnt += 1
    if line_cnt > font_size_limit_dict[font_fize]:
        line_cnt = 1
        font_fize -= 2
        if font_fize < 8:
            font_fize = 20
    # Display image.
    disp.image(image, rotation)
    # time.sleep(1)