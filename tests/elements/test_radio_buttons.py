
def test_yes_radio_button_shows_yes(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('#yesRadio').click()
    assert py.get('.text-success').should().have_text('Yes')


def test_impressive_radio_button_is_selected(py):
    py.visit('https://demoqa.com/radio-button')
    checkbox = py.get('#impressiveRadio')
    checkbox.click(force=True)
    assert checkbox.is_selected()


def test_inject_javascript_to_enable_no_radio_button(py):
    py.visit('https://demoqa.com/radio-button')
    no_no_square = py.get('#noRadio')
    py.execute_script('arguments[0].disabled = false', no_no_square.webelement)
    no_no_square.click(force=True)
    assert no_no_square.is_selected()
