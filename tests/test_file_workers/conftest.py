import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open("tests/test_file_workers/test_file.txt", "w") as f_o:
        pass
