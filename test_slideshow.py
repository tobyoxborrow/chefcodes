from slideshow import SlideShow


def test_init_title(mocker):
    """Test init function sets title value"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    slideshow = SlideShow("ZlNLpWJUv52wgu2Y", stub)
    slideshow.root.title.assert_called_once_with("ZlNLpWJUv52wgu2Y")


def test_init_callback(mocker):
    """Test init function sets callback"""
    stub = mocker.stub()
    slideshow = SlideShow("", stub)
    assert slideshow.start_callback == stub


def test_init_geometry(mocker):
    """Test init function sets geometry values"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    slideshow = SlideShow("", stub, 500, 600)
    slideshow.root.geometry.assert_called_once_with("500x600+0+0")


def test_show(mocker):
    """Test show function calls Tk.mainloop()"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    slideshow = SlideShow("", stub)
    slideshow.show()
    slideshow.root.mainloop.assert_called_once_with()


def test_toggle_start_active(mocker):
    """Test toggle_start sets active value"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    slideshow = SlideShow("", stub)
    assert slideshow.is_active() is False
    slideshow.toggle_start()
    assert slideshow.is_active() is True


def test_toggle_start_callback(mocker):
    """Test toggle_start calls the callback function"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    slideshow = SlideShow("", stub)
    slideshow.toggle_start()
    stub.assert_called_once_with()


def test_toggle_start_buttontext(mocker):
    """Test toggle_start changes the button text"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Button")
    slideshow = SlideShow("", stub)

    slideshow.toggle_start()
    slideshow.startstop_button.config.assert_called_once_with(text="Stop")

    slideshow.toggle_start()
    slideshow.startstop_button.config.assert_called_with(text="Start")


def test_update_progress(mocker):
    """Test update_progress sets expected value"""
    stub = mocker.stub()
    mocker.patch("tkinter.Tk")
    mocker.patch("tkinter.Label")
    slideshow = SlideShow("", stub)
    slideshow.update_progress(500, 600, "gx8oN6ZDHc3lv3xy")
    slideshow.progress_label.config.assert_called_once_with(text="500 (83.33%): gx8oN6ZDHc3lv3xy")
