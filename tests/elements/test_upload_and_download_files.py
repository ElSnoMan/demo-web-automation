from pylenium import Pylenium


def test_upload_file(py: Pylenium, project_root):
    py.visit('https://demoqa.com/upload-download')
    py.get('#uploadFile').type(f'{project_root}/pylenium.json')
    assert py.get('#uploadedFilePath').should().contain_text('pylenium.json')
