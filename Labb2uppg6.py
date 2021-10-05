from tkinter import *
import math

SIZE = 600


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

def rektangel(img, punkt1, punkt2, färg):
    """Adds a rectangle with specified position of corners and color to img."""
    for y in range(punkt1[1],punkt2[1]+1):
        for x in range(punkt1[0],punkt2[0]+1):
            img.put(färg, (x, y))

def cirkel(img, punkt, radie, färg):
    for x in range(SIZE):
        for y in range(SIZE):
            if ((x-punkt[0])**2 + (y-punkt[1])**2)**0.5 <= radie:
                img.put(färg, (x, y))

def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    for y in range(300, 501, 100):
        punkt1 = (250, y)
        punkt2 = (350, y)
        punkt3 = (300, y-150)
        triangel(img, punkt1, punkt2, punkt3, "#006400")
    rektangel(img, (290, 501), (310, 540), "#8B4513")
    cirkel(img, (310, 420), 10, "#A52A2A")
    cirkel(img, (280, 330), 10, "#A52A2A")
    mainloop()


if __name__ == '__main__':
    main()
