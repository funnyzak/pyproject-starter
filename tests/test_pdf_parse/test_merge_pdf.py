# -*- coding: utf-8 -*-
import datetime
import os

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
    # merge pdf files
    merge_pdf.MergePdf([tpp.demo_pic_pdf_path, tpp.demo_pic_pdf_path], tpp.test_dist_path).merge()


@pytest.mark.parametrize(
    "output_path",
    [os.path.join(tpp.test_dist_path, f"test_{str(int(datetime.datetime.now().timestamp() * 1000))}"), ""],
)
def test_output_dir_not_exist(output_path):
    merge_pdf.MergePdf(
        [tpp.demo_pic_pdf_path],
        output_path,
    )


# test pdf files not specified
def test_pdf_files_not_specified():
    with pytest.raises(ValueError) as e:
        merge_pdf.MergePdf([], tpp.test_dist_path).merge()
    exec_msg = e.value.args[0]
    assert exec_msg == "pdf files not specified"


def test_merge_pdf_demo_func():
    # test merge pdf def in merge_pdf
    merge_pdf.test_merge_pdf()


@pytest.mark.test_merge_pdf_main
def test_main():
    pytest.skip("skip test_main")
