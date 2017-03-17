"""Slideshow of ChefClub barcodes"""


import tkinter as tk

from PIL import ImageTk

from barcode_generator import BarcodeGenerator
from slideshow import SlideShow


class ChefShow(SlideShow):
    """Class to represent the ChefClub barcode slideshow"""

    def __init__(self, start_index=None):
        super().__init__('ChefCodes', self.update_image)

        self.ccg = BarcodeGenerator()
        self.ccg.init()

        if start_index:
            self.ccg.jump(start_index)

        self.back_button = tk.Button(
            self.panel,
            text='Back',
            command=self.jump_back)
        self.back_button.pack(side='bottom')

        # display the main window and enter the main loop
        self.show()

    def update_image(self):
        """Change the image that is displayed with the next one"""
        if not self.is_active():
            return False

        code = self.ccg.next()

        self.update_progress(code)

        # treepoem returns a PIL object, we can resize that directly
        barcode = self.ccg.barcode.resize((100, 100))

        # Use PhotoImage so the barcode image data can be understood by tk
        barcode = ImageTk.PhotoImage(barcode)

        self.panel.image = barcode     # avoid garbage collection
        self.panel.config(image=barcode)

        # Delay can not be too low, treepoem will choke running the barcode
        # generation child processes
        self.panel.after(1000, self.update_image)

    def jump_back(self, distance=10):
        """Jump backwards some number of places in the slideshow"""
        self.ccg.jump(self.ccg.index - distance)
        self.update_progress()

    def update_progress(self, code=''):
        """Update the progress label with some stats"""
        super().update_progress(self.ccg.index, self.ccg.count, code)
