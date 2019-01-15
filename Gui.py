from itertools import cycle
import tkinter as tk
from PIL import Image, ImageTk
import io


class App(tk.Tk):
    def __init__(self, image_files, delay):
        # the root will be self
        tk.Tk.__init__(self)
        self.geometry(str(self.winfo_screenwidth()) + 'x' + str(self.winfo_screenheight()))
        self.delay = delay
        # allows repeat cycling through the pictures
        self.pictures = cycle(self.photo_image(image) for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2, anchor="center")

    def photo_image(self, jpg_filename):
        with io.open(jpg_filename, 'rb') as ifh:
            pil_image = Image.open(ifh)
            return ImageTk.PhotoImage(pil_image)

    def show_slides(self):
        img_object = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()