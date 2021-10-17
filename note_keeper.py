import numpy
import cv2
import ctypes
import os, sys

def setSolidBackground(dim_x, dim_y, rgb_color=(0,0,0)):
    
    img = numpy.ones((dim_x,dim_y,3),numpy.uint8)
    bgr_color = tuple(reversed(rgb_color)) 
    img[:] = bgr_color

    return img


def main():
    width, height = 1080,1920

    image = setSolidBackground(width, height, (0,0,102))
    cv2.imwrite('red.jpg', image)

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    
    real_file = os.path.join(path, 'red.jpg' )

    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, real_file, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
main()