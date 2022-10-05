# -*- coding: utf-8 -*-
import pytest

from pdf_parse import merge_pdf
import test_pdf_parse as tpp


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
        __file__,
    ]
    output_dir = "out_dir"

    with pytest.raises(ValueError) as e:
        merge_pdf.MergePdf(pdf_files, output_dir).merge()
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


@pytest.mark.usefixtures("merge_pdf_function_scope")
def test_merge_pdf():
    # fill pdf files
    merge_pdf.MergePdf([tpp.demo_pic_pdf_path, tpp.demo_pic_pdf_path], tpp.test_dist_path).merge()


def test_merge_pdf_demo_func():
    # test merge pdf def in merge_pdf
    merge_pdf.test_merge_pdf()
