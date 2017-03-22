from barcode_generator import BarcodeGenerator
import PIL


def test_init():
    """Test init function populates its internal list of codes"""
    bcg = BarcodeGenerator()
    assert bcg.count > 0


def test_next():
    """Test next function moves index by 1"""
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.next(False)
    assert bcg.index == 1
    assert bcg.code == "001"


def test_jump_1():
    """Test jump function with argument of 1"""
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(1, False)
    assert bcg.index == 1
    assert bcg.code == "001"


def test_jump_10():
    """Test jump function with argument of 10"""
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(10, False)
    assert bcg.index == 10
    assert bcg.code == "00a"


def test_jump_100():
    """Test jump function with argument of 100"""
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(100, False)
    assert bcg.index == 100
    assert bcg.code == "01C"


def test_generate_barcode():
    """Test generate_barcode function"""
    bcg = BarcodeGenerator()
    assert bcg.barcode is None
    bcg.generate_barcode()
    assert isinstance(bcg.barcode, PIL.EpsImagePlugin.EpsImageFile)


def test_jump_generate_barcode():
    """Test jump function will generate a barcode"""
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    assert bcg.barcode is None
    bcg.jump(1)
    assert bcg.index == 1
    assert bcg.code == "001"
    assert isinstance(bcg.barcode, PIL.EpsImagePlugin.EpsImageFile)
