# -*- coding: utf-8 -*-
import pytest

from pdf_parse import extract_pdf_images
import test_pdf_parse as tpp


@pytest.mark.test_extract_pdf_images
def test_extract_pdf_images():
    # extract pdf images
    extract_pdf_images.ExtractPdfImage(tpp.demo_pic_pdf_path, tpp.test_dist_path).extract()
