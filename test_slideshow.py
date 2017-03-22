from slideshow import SlideShow


def test_init():
    """Test init function sets expected values"""
    def samplefunction():
        """Sample function for start_callback"""
        pass
    slideshow = SlideShow("ZlNLpWJUv52wgu2Y", samplefunction)
    assert slideshow.root.title() == "ZlNLpWJUv52wgu2Y"
    assert slideshow.start_callback == samplefunction


def test_update_progress():
    """Test update_progress sets expected value"""
    def samplefunction():
        """Sample function for start_callback"""
        pass
    slideshow = SlideShow("sampletitle", samplefunction)
    slideshow.update_progress(500, 1000, "gx8oN6ZDHc3lv3xy")
    label_text = slideshow.progress_label.config('text')[4]
    assert label_text == "500 (50.00%): gx8oN6ZDHc3lv3xy"


def test_toggle_start_active():
    """Test toggle_start sets active value"""
    def samplefunction():
        """Sample function for start_callback"""
        pass
    slideshow = SlideShow("sampletitle", samplefunction)
    assert slideshow.is_active() is False
    slideshow.toggle_start()
    assert slideshow.is_active() is True


def test_toggle_start_callback():
    """Test toggle_start calls the callback function"""
    def samplefunction():
        """Sample function for start_callback"""
        samplefunction.counter += 1
    samplefunction.counter = 0
    slideshow = SlideShow("sampletitle", samplefunction)
    slideshow.toggle_start()
    assert samplefunction.counter == 1


def test_toggle_start_buttontext():
    """Test toggle_start changes the button text"""
    def samplefunction():
        """Sample function for start_callback"""
        pass
    slideshow = SlideShow("sampletitle", samplefunction)

    slideshow.toggle_start()
    button_text = slideshow.startstop_button.config('text')[4]
    assert button_text == "Stop"

    slideshow.toggle_start()
    button_text = slideshow.startstop_button.config('text')[4]
    assert button_text == "Start"
