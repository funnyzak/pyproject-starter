# -*- coding: utf-8 -*-
import os

import pytest

from pdf_parse import merge_pdf


@pytest.fixture(scope="function", autouse=False)
def merge_pdf_function_scope():
    print("merge_pdf before")

    yield

    print("merge_pdf after")


def test_file_not_found():
    pdf_files = [
        "test_merge_pdf.pdf",
    ]
    output_dir = "out_dir"

    with pytest.raises(FileNotFoundError) as e:
        merge_pdf.MergePdf(pdf_files, output_dir).merge()
    exec_msg = e.value.args[0]
    assert exec_msg == "file test_merge_pdf.pdf not found"


def test_file_not_pdf():
    pdf_files = [
        os.path.join(os.path.dirname(__file__), "test_merge_pdf.py"),
    ]
    output_dir = "out_dir"

    with pytest.raises(ValueError) as e:
        merge_pdf.MergePdf(pdf_files, output_dir).merge()
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


@pytest.mark.usefixtures("merge_pdf_function_scope")
def test_merge_pdf():
    # get path top level directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    txt_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")
    output_dir = os.path.join(root_dir, "dist/pdf_parse")

    # fill pdf files
    pdf_files = [txt_pdf_path]
    merge_pdf.MergePdf(pdf_files, output_dir).merge()
