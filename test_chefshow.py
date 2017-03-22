from chefshow import ChefShow


def test_init_callback():
    """Test init function sets the SlideShow callback to update_image"""
    chefshow = ChefShow(show=False)
    assert chefshow.start_callback == chefshow.update_image


def test_init_title():
    """Test init function sets the SlideShow title"""
    chefshow = ChefShow(show=False)
    assert chefshow.root.title() == "ChefCodes"


def test_init_bcg():
    """Test init function creates a BarcodeGenerator"""
    chefshow = ChefShow(show=False)
    assert chefshow.ccg.count > 0


def test_init_jump():
    """Test init function jumps to user specified index"""
    chefshow = ChefShow(100, show=False)
    assert chefshow.ccg.index == 100
    assert chefshow.ccg.code == "01C"


def test_update_progress():
    """Test toggle_start function updates the progress label"""
    chefshow = ChefShow(99, show=False)
    code = chefshow.ccg.next(False)
    chefshow.update_progress(code)
    label_text = chefshow.progress_label.config('text')[4]
    assert label_text == "100 (0.04%): 01C"


def test_jump_back():
    """Test toggle_start function updates the progress label"""
    chefshow = ChefShow(100, show=False)
    assert chefshow.ccg.index == 100
    assert chefshow.ccg.code == "01C"
    chefshow.jump_back()
    assert chefshow.ccg.index == 90
    assert chefshow.ccg.code == "01s"
