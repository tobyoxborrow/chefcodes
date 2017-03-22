from chefshow import ChefShow
from slideshow import SlideShow


def test_init_callback(mocker):
    """Test init function sets the SlideShow callback to update_image"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    chefshow = ChefShow()

    assert chefshow.start_callback == chefshow.update_image


def test_init_title(mocker):
    """Test init function sets the SlideShow title"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    chefshow = ChefShow()

    chefshow.root.title.assert_called_once_with("ChefCodes")


def test_init_jump(mocker):
    """Test init function jumps to user specified index"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    mocker.patch("treepoem.generate_barcode")
    mocker.patch("chefshow.BarcodeGenerator")
    chefshow = ChefShow(100)

    chefshow.ccg.jump.assert_called_once_with(100)


def test_toggle_start_update_progress(mocker):
    """Test toggle_start function updates the progress label"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    mocker.patch("treepoem.generate_barcode")
    chefshow = ChefShow()

    mocker.patch("PIL.ImageTk.PhotoImage")
    mocker.patch.object(chefshow.ccg, "next", return_value="01C")
    mocker.patch.object(chefshow, "update_progress")
    mocker.patch.object(chefshow.ccg, "barcode")
    chefshow.update_image()

    chefshow.update_progress.assert_called_once_with("01C")


def test_update_progress(mocker):
    """Test update_progress calls SlideShow's update_progress"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    mocker.patch("treepoem.generate_barcode")
    chefshow = ChefShow()

    m = mocker.patch.object(SlideShow, "update_progress")
    chefshow.update_progress("01C")

    m.assert_called_once_with(0, 238328, '01C')


def test_jump_back(mocker):
    """Test toggle_start function updates the progress label"""
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    mocker.patch("treepoem.generate_barcode")
    chefshow = ChefShow(100)

    mocker.patch.object(SlideShow, "update_progress")
    mocker.patch.object(chefshow.ccg, "jump")
    chefshow.jump_back()

    chefshow.ccg.jump.assert_called_with(90)
