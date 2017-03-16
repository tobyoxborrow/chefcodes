"""Generate Data Matrix barcodes for data in the format: [a-zA-Z0-9]{3}"""
import treepoem


class BarcodeGenerator():
    """Class to represent the barcode generator"""

    def __init__(self):
        self.charset = tuple(
            '0123456789'
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.codes = list()
        self.count = 0
        self.code = None
        self.active = False
        self.index = 0
        self.barcode = None

    def init(self):
        """Initialise counters and generate every code"""
        for a in self.charset:
            for b in self.charset:
                for c in self.charset:
                    code = "{0}{1}{2}".format(a, b, c)
                    self.codes.append(code)
        self.active = True
        self.index = 0
        self.code = self.codes[0]
        self.count = len(self.codes)
        return self.count

    def jump(self, index):
        """Skip to a specific code index"""
        if not self.active:
            return None

        self.index = index
        self.code = self.codes[self.index]
        self.generate_barcode()
        return self.code

    def next(self):
        """Move to the next code"""
        return self.jump(self.index + 1)

    def generate_barcode(self):
        """Generate image of current barcode and return the image object"""
        if not self.active:
            return None

        self.barcode = treepoem.generate_barcode(
            barcode_type='datamatrix',
            data=self.code,
            options={
                'rows': 10,
                'columns': 10
                },
            )
