import pytest


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/dynamic-properties')


def test_element_with_dynamic_id_has_text(py, demo_qa):
    assert py.contains('This text has random Id')


def test_element_with_dynamic_id_2(py, demo_qa):
    assert py.get('p').should().contain_text('This text has random Id')


def test_element_is_visible_after_5_seconds(py, demo_qa):
    assert py.get('#visibleAfter').should().be_visible()


def test_element_enabled_after_5_seconds(py, demo_qa):
    assert py.get('#enableAfter').should().not_have_attr('disabled')


def test_element_changes_text_color_to_red(py, demo_qa):
    button = py.get('#colorChange')
    assert py.wait().until(lambda _: 'danger' in button.get_attribute('class'))
