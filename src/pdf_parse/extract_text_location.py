# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2023-06-08
# license: MIT
# description: Extract text location from pdf file.
# usage: poetry run python src/pdf_parse/extract_text_location.py -i public/attachments/pdf/whatispython.pdf
# notes:

import argparse
import json
import os
import time

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.layout import LTAnno
from pdfminer.layout import LTChar
from pdfminer.layout import LTText
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class ExtractTextLocation:
    """Extract text location from pdf file."""

    def __init__(self, pdf_file, output_path=None) -> None:
        """Pass in the path to the PDF file and output path.

        :param pdf_file: pdf file path
        :param output_path: output dir
        """
        self.pdf_file = pdf_file
        self.output_path = output_path

        self.check_file()
        self.check_out_path()

    def check_file(self):
        """Check if the file exists."""
        if not os.path.exists(self.pdf_file):
            raise FileNotFoundError(f"file {self.pdf_file} not found.")
        if not self.pdf_file.endswith(".pdf"):
            raise ValueError(f"file {self.pdf_file} is not pdf file")

    def check_out_path(self):
        """Check if the output path exists."""
        if not self.output_path:
            self.output_path = os.path.dirname(self.pdf_file)
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def set_output_path(self, output_path):
        """Set output path."""
        self.output_path = output_path
        self.check_out_path()

    def parse_char_layout(self, layout):
        """Parsing page content, letter by letter."""
        # bbox:
        # x0: the distance from the left side of the page to the left edge of the box.
        # y0: the distance from the bottom of the page to the bottom edge of the box.
        # x1: the distance from the left side of the page to the right edge of the box
        # y1: distance from the bottom of the page to the top edge of the box
        words_result = []
        for textbox in layout:
            if isinstance(textbox, LTText):
                for line in textbox:
                    char_list = []
                    for character in line:
                        # If the char is a line-break or an empty space, the word is complete
                        if isinstance(character, LTAnno) or character.get_text() == " ":
                            pass
                        elif isinstance(character, LTChar):
                            char_list.append(
                                {
                                    "char": character.get_text(),
                                    "size": round(character.size, 2),
                                    "font": character.fontname,
                                    "location": {
                                        "left": round(character.bbox[0], 2),
                                        "top": round(character.bbox[3], 2),
                                        "width": round(character.width, 2),
                                        "height": round(character.height, 2),
                                    },
                                }
                            )
                    line_dict = {
                        "words": line.get_text().strip(),
                        "location": {
                            "left": round(line.bbox[0], 2),
                            "top": round(line.bbox[3], 2),
                            "width": round(line.width, 2),
                            "height": round(line.height, 2),
                        },
                        "chars": char_list,
                    }
                    words_result.append(line_dict)
        return words_result

    def extract_text_location(self, new_pdf_file=None):
        """Extract text location from pdf file."""
        if new_pdf_file not in [None, ""]:
            self.pdf_file = new_pdf_file
            self.check_file()
            self.check_out_path()

        with open(self.pdf_file, "rb") as in_file:
            parser = PDFParser(in_file)
            doc: PDFDocument = PDFDocument(parser)  # Create a PDF document

            rsrcmgr = PDFResourceManager()  # Create a PDF resource manager to share resources
            # Create a PDF device object
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # Create a PDF interpreter object
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            # Iterate through the list and process the content of each page
            # doc.get_pages() retrieves the page list
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            # Process the content of each page in the document object
            # doc.get_pages() retrieves the page list
            # Iterate through the list and process the content of each page
            # Here, layout is an LTPage object that contains various objects parsed from this page,
            # including LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal, etc.
            # To obtain text, access the text attribute of the object

            start_time = time.time()
            print("============== pdf file: ", self.pdf_file, " processing ==============")
            pdf_name = os.path.basename(self.pdf_file).split(".")[0]
            page_list = []
            for page_index, page in enumerate(PDFPage.create_pages(doc)):
                print("================ page: ", page_index + 1, " ==================")
                interpreter.process_page(page)
                layout = device.get_result()
                # get layout width and height
                page_data = self.parse_char_layout(layout)
                page_list.append(
                    {
                        "page": page_index + 1,
                        "width": round(layout.width, 2),
                        "height": round(layout.height, 2),
                        "words": page_data,
                    }
                )
            pdf_json = {"name": pdf_name, "page_count": len(page_list), "pages": page_list}
            print("pdf_json: ", pdf_json)
            with open(os.path.join(self.output_path, pdf_name + ".json"), "w") as out_file:
                out_file.write(json.dumps(pdf_json, indent=4, ensure_ascii=False))
                print(
                    "save json file success. file: ",
                    os.path.join(self.output_path, pdf_name + ".json"),
                )
            end_time = time.time()
            print(
                "============== pdf file: ",
                self.pdf_file,
                " process success, cost time: ",
                "{:.2f} S".format(end_time - start_time),
                " ==============",
            )
        pass


root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
attachment_dir = os.path.join(root_dir, "public/attachments/pdf")
pic_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")


def test_extract_text_location():
    """Test extract text location."""
    extract_text_location = ExtractTextLocation(pic_pdf_path)
    extract_text_location.extract_text_location()
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text location from pdf file.")
    parser.add_argument("-i", "--input", help="input pdf file", required=True)

    args = parser.parse_args()
    pdf_file = args.input

    extract_text_location = ExtractTextLocation(pdf_file)
    extract_text_location.extract_text_location()
    pass
