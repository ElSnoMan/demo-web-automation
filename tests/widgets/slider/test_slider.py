import pytest


def move_slider(py, position: str):
    slider = py.get('input.range-slider')
    py.execute_script(f'arguments[0].value = {position};', slider.webelement)
    return slider


positions = ['10', '50']


@pytest.mark.parametrize('position', positions)
def test_slider_by_input(py, position):
    py.visit('https://demoqa.com/slider')
    slider = move_slider(py, position)
    assert slider.should().have_value(position)


def test_slider_with_mouse(py):
    """ Move the slider by clicking and dragging the mouse. """
    py.visit('https://demoqa.com/slider')
    slider = py.get('.range-slider')
    slider.
