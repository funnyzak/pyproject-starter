# -*- coding: utf-8 -*-
import datetime
import os

from PyPDF2.generic import AnnotationBuilder
import pytest

from pdf_parse import add_pdf_annotiation
import test_pdf_parse as tpp


# test source pdf not found
def test_source_pdf_not_found():
    with pytest.raises(FileNotFoundError):
        add_pdf_annotiation.AddPdfAnnotation("tests/test_pdf_parse/test.pdf")


# test source pdf not pdf file
def test_source_pdf_not_pdf_file():
    with pytest.raises(ValueError):
        add_pdf_annotiation.AddPdfAnnotation(__file__)


# test output pdf not specified
def test_output_pdf_not_specified():
    assert os.path.exists(add_pdf_annotiation.AddPdfAnnotation(tpp.demo_pic_pdf_path).add_annotation([]))


# test output pdf specified but not exist
def test_output_pdf_specified_but_not_exist():
    output_pdf = os.path.join(
        tpp.test_dist_path, "test_output_pdf_specified_" + f"{str(int(datetime.datetime.now().timestamp()))}.pdf"
    )
    assert os.path.exists(add_pdf_annotiation.AddPdfAnnotation(tpp.demo_pic_pdf_path, output_pdf).add_annotation([]))


def test_demo():
    add_pdf_annotiation.add_pdf_annotiation_demo()


# test add annotation
def test_add_annotation():
    output_pdf = os.path.join(
        tpp.test_dist_path, f"test_add_annotation_{str(int(datetime.datetime.now().timestamp()))}.pdf"
    )

    free_txt = AnnotationBuilder.free_text(
        "Hello World\nThis is the second line!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )

    assert os.path.exists(
        add_pdf_annotiation.AddPdfAnnotation(tpp.demo_pic_pdf_path, output_pdf).add_annotation(
            [
                {
                    "page": 0,
                    "annotation": free_txt,
                },
                {
                    "page": 3,
                    "annotation": free_txt,
                },
            ]
        )
    )
