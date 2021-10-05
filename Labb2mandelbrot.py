from tkinter import *
import cmath


SIZE = 600

def mandelbrot(img, SIZE, color):
    for x in range(0, SIZE):
        for y in range(0, SIZE):
            a = x/200
            b = y/200
            c = complex(a-1.5, b-1.5)
            z = 0
            n = 0
            if mandeltest(c, z, n) == 1:
                img.put(color, (x, y))

def mandeltest(c, z, n):
    if abs(z) >=2:
        svar = 1
        return svar
    elif n >= 200:
        svar = 0
        return svar
    else:
        return mandeltest(c, (z ** 2) + c, n + 1)



def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    mandelbrot(img, 600, "#ffffff")
    mainloop()


if __name__ == '__main__':
    main()
