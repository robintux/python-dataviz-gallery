#!/usr/bin/env python

"""
Convert the Tableau data color RGB values to hex values for mplstyles
(http://tableaufriction.blogspot.ro/2012/11/finally-you-can-use-tableau-data-colors.html)
"""

t10 = [(31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40),
       (148, 103, 189), (140, 86, 75), (227, 119, 194), (127, 127, 127),
       (188, 189, 34), (23, 190, 207)]

t10l = [(174, 199, 232), (255, 187, 120), (152, 223, 138), (255, 152, 150),
        (197, 176, 213), (196, 156, 148), (247, 182, 210), (199, 199, 199),
        (219, 219, 141), (158, 218, 229)]

t10m = [(114, 158, 206), (255, 158, 74), (103, 191, 92), (237, 102, 93),
        (173, 139, 201), (168, 120, 110), (237, 151, 202), (162, 162, 162),
        (205, 204, 93), (109, 204, 218)]

t20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
       (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
       (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
       (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
       (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

tgr5 = [(96, 99, 106), (165, 172, 175), (65, 68, 81),
        (143, 135, 130), (207, 207, 207)]

tcb10 = [(0, 107, 164), (255, 128, 14), (171, 171, 171), (89, 89, 89),
         (95, 158, 209), (200, 82, 0), (137, 137, 137), (162, 200, 236),
         (255, 188, 121), (207, 207, 207)]

palette_names = ['t10', 't10l', 't10m', 't20', 'tgr5', 'tcb10']

color_palettes = [t10, t10l, t10m, t20, tgr5, tcb10]


def rgb2hex(rgb):
    """Convert rgb values to hex values"""
    return '{:02x}{:02x}{:02x}'.format(*rgb)


def rgblist2hexlist(rgblist):
    """Convert rgb list to hex list"""
    hexlist = [rgb2hex(rgb) for rgb in rgblist]
    return hexlist


def main():
    for palette_name, color_palette in zip(palette_names, color_palettes):
        print(palette_name)
        print(rgblist2hexlist(color_palette), '\n')


if __name__ == '__main__':
    main()
