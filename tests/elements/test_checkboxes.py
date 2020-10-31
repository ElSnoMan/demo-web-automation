from pylenium.element import Element


def get_checkbox(py, name) -> Element:
    name = name.lower()
    return py.get(f"[for='tree-node-{name}'] > input")


def get_toggle(py, name) -> Element:
    name = name.lower()
    return py.get(f"[for='tree-node-{name}']").siblings()[0]


def test_basic_challenge(py):
    get_toggle(py, 'Home').click(force=True)
    get_toggle(py, 'Desktop').click()

    commands = get_checkbox(py, 'Commands')
    commands.click()

    assert commands.is_checked()
    assert 'half-check' in get_checkbox(py, 'Home').get_attribute('class')
    assert 'half-check' in get_checkbox(py, 'Desktop').get_attribute('class')
