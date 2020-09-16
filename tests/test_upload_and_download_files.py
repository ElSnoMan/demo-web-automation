import os
import time


def test_upload_file(py, project_root):
    py.visit('https://demoqa.com/upload-download')
    py.get('#uploadFile').type(project_root + '/pylenium.json')
    assert py.get('#uploadedFilePath').should().contain_text('pylenium.json')


def wait_for_file_to_exist(file_path, timeout=5):
    attempts = 0
    while attempts < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
        attempts += 1
    return False


def test_download_file(py):
    py.visit('https://demoqa.com/upload-download')
    py.get('#downloadButton').click()
    assert wait_for_file_to_exist('C:/Users/ckcar/Downloads/sampleFile.jpeg')
