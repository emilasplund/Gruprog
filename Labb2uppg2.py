from tkinter import *


SIZE = 600


def rektangel(img, punkt1, punkt2, färg):
    """Adds a rectangle with specified position of corners and color to img."""
    for y in range(punkt1[1],punkt2[1]+1):
        for x in range(punkt1[0],punkt2[0]+1):
            img.put(färg, (x, y))


def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    rektangel(img, (100, 100), (500, 500), "#ffffff")
    mainloop()


if __name__ == '__main__':
    main()
