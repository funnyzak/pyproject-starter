# -*- coding: utf-8 -*-
import pytest

from pdf_parse import extract_text_location


def test_pdf_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        extract_text_location.ExtractTextLocation("test.pdf")
    exec_msg = e.value.args[0]
    assert exec_msg == "file test.pdf not found."


def test_not_pdf_file():
    with pytest.raises(ValueError) as e:
        extract_text_location.ExtractTextLocation(__file__)
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


def test_extract_text_location():
    extract_text_location.test_extract_text_location()
