# -*- coding: utf-8 -*-
import datetime
import os

import pytest

from pdf_parse import multi_pdf_to_multi_layer_pdf
import test_pdf_parse as tpp


def test_file_not_found():
    pdf_files = [
        "test_multi_pdf_to_multi_layer_pdf.pdf",
    ]
    output_dir = "out_dir"

    with pytest.raises(FileNotFoundError) as e:
        multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(pdf_files, output_dir)
    exec_msg = e.value.args[0]
    assert exec_msg == "file test_multi_pdf_to_multi_layer_pdf.pdf not found"


def test_file_not_pdf():
    pdf_files = [
        __file__,
    ]
    output_dir = "out_dir"

    with pytest.raises(ValueError) as e:
        multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(pdf_files, output_dir)
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


def test_multi_pdf_to_multi_layer_pdf():
    multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(
        [tpp.demo_pic_pdf_path, tpp.demo_txt_pdf_path], tpp.test_dist_path
    ).be_multi_layer()


def test_base_pdf_pages_less_than_top_pdf_page():
    multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(
        [tpp.demo_pic_pdf_path, tpp.demo_txt_pdf2_path], tpp.test_dist_path
    ).be_multi_layer()


def test_base_pdf_pages_greater_than_top_pdf_page():
    multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(
        [tpp.demo_txt_pdf2_path, tpp.demo_pic_pdf_path], tpp.test_dist_path
    ).be_multi_layer()


@pytest.mark.parametrize(
    "output_path",
    [os.path.join(tpp.test_dist_path, f"test_{str(int(datetime.datetime.now().timestamp() * 1000))}"), ""],
)
def test_output_dir_not_exist(output_path):
    multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile(
        [tpp.demo_pic_pdf_path, tpp.demo_txt_pdf_path],
        output_path,
    )


def test_pdf_files_not_specified():
    with pytest.raises(ValueError):
        multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile([], tpp.test_dist_path)


def test_pdf_files_specified_only_one():
    with pytest.raises(ValueError):
        multi_pdf_to_multi_layer_pdf.MultiPdfToMultiLayerFile([tpp.demo_pic_pdf_path], tpp.test_dist_path)


def test_demo_func():
    multi_pdf_to_multi_layer_pdf.multi_pdf_to_multi_layer_pdf_demo()
