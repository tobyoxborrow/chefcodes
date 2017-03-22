import treepoem

from barcode_generator import BarcodeGenerator


def test_init():
    """Test init function populates its internal list of codes"""
    bcg = BarcodeGenerator()
    assert bcg.count > 0


def test_next(mocker):
    """Test next function moves index by 1"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.next()
    assert bcg.index == 1
    assert bcg.code == "001"


def test_jump_1(mocker):
    """Test jump function with argument of 1"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(1)
    assert bcg.index == 1
    assert bcg.code == "001"


def test_jump_10(mocker):
    """Test jump function with argument of 10"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(10)
    assert bcg.index == 10
    assert bcg.code == "00a"


def test_jump_100(mocker):
    """Test jump function with argument of 100"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    bcg.jump(100)
    assert bcg.index == 100
    assert bcg.code == "01C"


def test_generate_barcode(mocker):
    """Test generate_barcode function"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.barcode is None
    bcg.generate_barcode()
    assert treepoem.generate_barcode.called is True


def test_jump_generate_barcode(mocker):
    """Test jump function will generate a barcode"""
    mocker.patch("treepoem.generate_barcode")
    bcg = BarcodeGenerator()
    assert bcg.index == 0
    assert bcg.barcode is None
    bcg.jump(1)
    assert bcg.index == 1
    assert bcg.code == "001"
    assert treepoem.generate_barcode.called is True
