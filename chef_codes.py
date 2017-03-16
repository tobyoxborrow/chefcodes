"""Display all barcodes as a slideshow in a GUI window"""

import tkinter as tk

from PIL import ImageTk

from barcode_generator import BarcodeGenerator


def test_code():
    """Start about 5 codes below a known good code, to verify recognition"""
    global ACTIVE
    ACTIVE = True
    ccg.jump(188430)
    update_image()


def toggle_start():
    """Start/Stop the slideshow of barcodes"""
    global ACTIVE
    ACTIVE = not ACTIVE

    if ACTIVE:
        startstop_button.config(text="Stop")
        update_image()
    else:
        startstop_button.config(text="Start")


def update_image():
    """Change the image that is displayed with the next one"""
    if not ACTIVE:
        return False

    code = ccg.next()

    label = "{0}: {1}".format(ccg.index, code)
    code_label.config(text=label)

    # treepoem returns a PIL object, we can resize that directly
    barcode = ccg.barcode.resize((100, 100))

    # Use PhotoImage so the barcode image data can be understood by tk
    barcode = ImageTk.PhotoImage(barcode)

    panel.image = barcode     # avoid garbage collection
    panel.config(image=barcode)

    panel.after(2000, update_image)


ACTIVE = False

ccg = BarcodeGenerator()
ccg.init()

ccg.jump(3390)

root = tk.Tk()
root.title('ChefCodes')

w = 400
h = 400

x = 0
y = 0

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

code_label = tk.Label(root, text="")
code_label.pack(side='top', fill='both', expand='no')

panel = tk.Label(root)
panel.pack(side='top', fill='both', expand='yes')

startstop_button = tk.Button(panel, text='Start', command=toggle_start)
startstop_button.pack(side='bottom')

test_button = tk.Button(panel, text='Test', command=test_code)
test_button.pack(side='bottom')

root.mainloop()
