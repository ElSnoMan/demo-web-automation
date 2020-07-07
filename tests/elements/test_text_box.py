
def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get('#userName').type('Luca Kidman')
    py.get('#userEmail').type('yomomma@example.com')
    py.get('#currentAddress').type('37 South Yo Mommas House')
    py.get('#permanentAddress').type(py.fake.address())
    py.get('#submit').click()
    assert py.get('p[id="name"]').should().contain_text('Luca Kidman')


# refactor code


def test_submit_form_refactored(py):
    pass
