from tkinter import *


SIZE = 600


def sierpinski(img):
    """Adds a Sierpinski Fractal to img and returns None."""
    for y in range(SIZE):
        for x in range(SIZE):
            if x&y == 0:
                img.put("#ffffff", (x, y))


def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    sierpinski(img)
    mainloop()


if __name__ == '__main__':
    main()
