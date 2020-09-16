import os
import time

import pytest


def wait_for_file_to_exist(file_path, timeout=5):
    attempts = 0
    while attempts < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
        attempts += 1
    raise FileNotFoundError(f'{file_path} did not exist within {str(timeout)} seconds.')


@pytest.fixture
def file_exists():
    def _file_exists(file_path):
        exists = wait_for_file_to_exist(file_path)
        yield exists
        os.remove(file_path)
    yield _file_exists


def test_upload_file(py, project_root):
    py.visit('https://demoqa.com/upload-download')
    py.get('#uploadFile').type(f'{project_root}/pylenium.json')
    assert py.get('#uploadedFilePath').should().contain_text('pylenium.json')


def test_download_file(py, project_root, file_exists):
    py.visit('https://demoqa.com/upload-download')
    py.get('#downloadButton').click()
    assert file_exists('C:/Users/ckcar/Downloads/sampleFile.jpeg')
