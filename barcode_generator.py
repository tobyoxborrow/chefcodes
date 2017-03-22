"""Generate Data Matrix barcodes for data in the format: [a-zA-Z0-9]{3}"""
import treepoem


class BarcodeGenerator():
    """Class to represent the barcode generator"""

    def __init__(self):
        """Initialise counters and generate every code"""
        self.charset = tuple(
            '0123456789'
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.codes = list()
        for a in self.charset:
            for b in self.charset:
                for c in self.charset:
                    code = "{0}{1}{2}".format(a, b, c)
                    self.codes.append(code)
        self.index = 0
        self.code = self.codes[0]
        self.count = len(self.codes)
        self.barcode = None

    def jump(self, index, generate_barcode=True):
        """Skip to a specific code index"""
        self.index = index
        self.code = self.codes[self.index]
        if generate_barcode:
            self.generate_barcode()
        return self.code

    def next(self, generate_barcode=True):
        """Move to the next code"""
        return self.jump(self.index + 1, generate_barcode)

    def generate_barcode(self):
        """Generate image of current barcode and return the image object"""
        self.barcode = treepoem.generate_barcode(
            barcode_type='datamatrix',
            data=self.code,
            options={
                'rows': 10,
                'columns': 10
                },
            )
