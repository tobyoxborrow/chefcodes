"""Slideshow of ChefClub barcodes"""


from PIL import ImageTk
from slideshow import SlideShow
from barcode_generator import BarcodeGenerator


class ChefShow(SlideShow):
    """Class to represent the ChefClub barcode slideshow"""

    def __init__(self, start_index=None):
        super().__init__()
        self.ccg = BarcodeGenerator()
        self.window = SlideShow()
        self.after_id = None

        self.ccg.init()

        if start_index:
            self.ccg.jump(start_index)

        self.window.init('ChefCodes', self.update_image)

    def update_image(self):
        """Change the image that is displayed with the next one"""
        if not self.window.is_active():
            return False

        code = self.ccg.next()

        self.window.update_progress(self.ccg.index, self.ccg.count, code)

        # treepoem returns a PIL object, we can resize that directly
        barcode = self.ccg.barcode.resize((100, 100))

        # Use PhotoImage so the barcode image data can be understood by tk
        barcode = ImageTk.PhotoImage(barcode)

        self.window.panel.image = barcode     # avoid garbage collection
        self.window.panel.config(image=barcode)

        # Delay can not be too low, treepoem will choke running the barcode
        # generation child processes
        self.after_id = self.window.panel.after(1000, self.update_image)
