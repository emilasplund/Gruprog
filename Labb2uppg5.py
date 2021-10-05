from tkinter import *


SIZE = 600

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
    cirkel(img, (100, 50), 5, "#438548")
    mainloop()


if __name__ == '__main__':
    main()
