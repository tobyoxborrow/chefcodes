"""Single window to display slideshow of images"""


import tkinter as tk


class SlideShow():
    """Class to represent the slideshow window"""

    def __init__(self, title, start_callback, width=400, height=400):
        """Initialise window and elements"""
        self.active = False

        self.start_callback = start_callback

        self.root = tk.Tk()
        self.root.title(title)

        self.root.geometry("%dx%d+%d+%d" % (width, height, 0, 0))

        self.progress_label = tk.Label(
            self.root,
            text="Click 'Start' to begin")
        self.progress_label.pack(side='top', fill='both', expand='no')

        self.panel = tk.Label(self.root)
        self.panel.pack(side='top', fill='both', expand='yes')

        self.startstop_button = tk.Button(
            self.panel,
            text='Start',
            command=self.toggle_start)
        self.startstop_button.pack(side='bottom')

    def show(self):
        """Show the main window and enter the main loop"""
        self.root.mainloop()

    def toggle_start(self):
        """Start/Stop the slideshow"""
        self.active = not self.active
        if self.active:
            self.startstop_button.config(text="Stop")
            self.start_callback()
        else:
            self.startstop_button.config(text="Start")

    def is_active(self):
        """Is the slideshow active?"""
        return self.active

    def update_progress(self, index, max_items, message):
        """Update the progress label with some stats"""
        progress = (index / max_items)
        label = "{:d} ({:.2%}): {:s}".format(index, progress, message)
        self.progress_label.config(text=label)
