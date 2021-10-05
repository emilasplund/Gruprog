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





def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    triangel(img, (599, 11), (202, 156), (21, 497), "#ffffff")
    mainloop()


if __name__ == '__main__':
    main()
