from tkinter import *
import math

SIZE = 600

def rektangel(img, punkt1, punkt2, färg):
    """Adds a rectangle with specified position of corners and color to img."""
    for y in range(punkt1[1],punkt2[1]+1):
        for x in range(punkt1[0],punkt2[0]+1):
            img.put(färg, (x, y))


def triangel(img, punkt1, punkt2, punkt3, färg):
    """ritar en triangel på img utifrån koordinater för 3 hörn"""
    Triangelarea = heron(punkt1, punkt2, punkt3)
    for x in range(SIZE):
        for y in range(SIZE):
            Delarea = round((((heron((x,y),punkt1,punkt2)+heron((x,y),punkt2,punkt3)+heron((x,y),punkt1,punkt3)))),3)
            """Testar för alla (x,y) om delareorna är lika med triangelns area, för då ligger (x,y) i triangeln"""
            if Triangelarea == Delarea:
                img.put(färg, (x, y))

def heron(punkt1, punkt2, punkt3):
    sidaA = (((punkt1[0]-punkt2[0])**2) + (punkt1[1]-punkt2[1])**2) ** 0.5
    sidaB = (((punkt3[0]-punkt2[0])**2) + (punkt3[1]-punkt2[1])**2) ** 0.5
    sidaC = (((punkt1[0]-punkt3[0])**2) + (punkt1[1]-punkt3[1])**2) ** 0.5
    s = (sidaA + sidaB + sidaC) / 2
    """tar fram triangelns area m.h.a herons formel"""
    if (s * (s - sidaA) * (s - sidaB) * (s - sidaC)) > 0:
        Area = round(((math.sqrt((s * (s - sidaA) * (s - sidaB) * (s - sidaC))))), 3)
        """avrundar till 3 decimaler för att undvika problem med == """
        return Area
    else:
        return 0

def cirkel(img, punkt, radie, färg):
    for x in range(SIZE):
        for y in range(SIZE):
            if ((x-punkt[0])**2 + (y-punkt[1])**2)**0.5 <= radie:
                img.put(färg, (x, y))


def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000", highlightthickness=0)
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    rektangel(img, (0, 0), (SIZE, SIZE), "#add8e6")
    rektangel(img, (0, 300), (SIZE, SIZE), "#90EE90")
    rektangel(img, (100, 250), (300, 500), "#F4A460")
    rektangel(img, (230, 130), (280, 250), "#000000")
    rektangel(img, (450, 150), (500, 450), "#8B4513")
    triangel(img, (80, 250), (320, 250), (200, 150), "#A0522D")
    cirkel(img, (475, 125), 75, "#228B22")
    cirkel(img, (225, 320), 40, "#B0C4DE")
    rektangel(img, (125, 400), (200, 500), "#A0522D")
    mainloop()


if __name__ == '__main__':
    main()
