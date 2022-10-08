# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description:  new pdf from ocr result
# usage:
# notes:

from datetime import datetime
from decimal import Decimal
import json
import os
from pathlib import Path
from typing import List

from borb.pdf import PDF  # type: ignore [import]
from borb.pdf import Alignment
from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import Image
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont  # type: ignore [import]
from borb.pdf.canvas.geometry.rectangle import Rectangle  # type: ignore [import]
from requests import get as requests_get  # type: ignore [import]


# from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation


class NewPdfFromOcr:
    doc: Document = Document()
    font = None
    font_color = "#ffffff"

    time_start = datetime.now()

    def __init__(
        self,
        page_datas: List[dict],
        options: dict = None,
        output_path=None,
    ) -> None:
        """New pdf from ocr result.

        :param page_datas: ocr result page info data, page_datas is list, each item is dict,
        dict keys is: origin_img, json_path.
        :param options: options, dict, keys is: font_link, font, font_color.
        :param output_path: the output path of new pdf file.
        """
        self.output_path = output_path
        self.page_datas = page_datas
        self.options = options

        if not self.options:
            self.options = {
                "font_link": "https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts"
                + "/master/chinese/%E6%A5%B7%E4%BD%93/Kaiti.ttf"
            }

        self.check_page_datas()
        self.check_out_path()

    def process(self) -> str:
        """Process all pages and export pdf file."""
        self.time_start = datetime.now()

        print("Start time: ", self.time_start)

        self.custom_setting()

        print("Start process all pages.")

        output_pdf_path = os.path.join(self.output_path, f"ocr_pdf_{str(int(datetime.now().timestamp() * 1000))}.pdf")

        for page_data in self.page_datas:
            self.process_page(page_data)

        # store
        with open(output_pdf_path, "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, self.doc)
            # Display the PDF path with color.
            print("The output pdf path is -> ", f"\033[1;32m{output_pdf_path}\033[0m")

        print(f"End process all pages. \nEnd time: {datetime.now()} \nTotal time: ", datetime.now() - self.time_start)

        return output_pdf_path

    def process_page(self, page_data: dict) -> None:
        """Process single page and add to doc."""
        ocr_result_json = None

        json_path = str(page_data.get("json_path"))
        origin_img = str(page_data.get("origin_img")) if page_data.get("origin_img") else None

        # read json file from ocr result
        with open(json_path, "r") as f:
            ocr_result_json = json.load(f)

        if not ocr_result_json or not ocr_result_json.get("chars"):
            return

        page_width = Decimal(ocr_result_json.get("width"))
        page_height = Decimal(ocr_result_json.get("height"))

        # Create Page.
        page: Page = Page(width=page_width, height=page_height)

        # Add Page to Document.
        self.doc.add_page(page)

        # Add pic to page.
        if origin_img and os.path.exists(origin_img):
            bg_img_position: Rectangle = Rectangle(
                0,
                0,
                page_width,
                page_height,
            )

            # add an Image
            Image(
                Path(origin_img),
                width=page_width,
                height=page_height,
                padding_bottom=0,
                padding_top=0,
                padding_left=0,
                padding_right=0,
                margin_bottom=0,
                margin_top=0,
                margin_left=0,
                margin_right=0,
            ).paint(page, bg_img_position)

        def_char = "|"

        for _index, _word in enumerate(ocr_result_json["chars"]):
            ocr_char = _word["ocr_txt"]
            char_pos_x = Decimal(_word["x"])
            char_pos_y = Decimal(_word["y"])
            char_width = Decimal(_word["w"])
            char_height = Decimal(_word["h"])

            char_pdf_position: Rectangle = Rectangle(
                Decimal(char_pos_x),
                page_height - Decimal(char_pos_y) - Decimal(char_height),
                Decimal(char_width),
                Decimal(char_height),
            )

            # page.add_annotation(SquareAnnotation(char_pdf_position, stroke_color=HexColor("#ff0000")))

            p_font_size = (char_width if char_width > char_height else char_height) * Decimal(0.97)

            def paint_char(_ocr_txt, _char_pdf_position, _p_font_size):
                Paragraph(
                    _ocr_txt,
                    horizontal_alignment=Alignment.CENTERED,
                    vertical_alignment=Alignment.MIDDLE,
                    text_alignment=Alignment.CENTERED,
                    font=self.font,
                    font_color=HexColor(self.font_color) if self.font_color else HexColor("#ffffff"),
                    font_size=_p_font_size,
                ).paint(page, _char_pdf_position)

            try:
                paint_char(ocr_char, char_pdf_position, p_font_size)
            except Exception as e:
                print(f"paint char {ocr_char} error: ", e)
                print(f"will paint default char {def_char} replace {ocr_char}")
                paint_char(def_char, char_pdf_position, p_font_size)

    def check_page_datas(self) -> None:
        """Check page_datas."""
        if not self.page_datas:
            raise Exception("page_datas is empty.")
        if not isinstance(self.page_datas, List):
            raise Exception("page_datas is not list.")
        for page_data in self.page_datas:
            if not isinstance(page_data, dict):
                raise Exception("page_data is not dict.")
            if not page_data.get("json_path"):
                raise Exception("page_data json_path is empty.")
            if not os.path.exists(str(page_data.get("json_path")) if page_data.get("json_path") else ""):
                raise Exception("page_data json_path not exist.")

    def custom_setting(self) -> None:
        """Custom setting."""
        print("Start custom setting.")
        self.custom_font_setting()
        print("End custom setting.")

    def custom_font_setting(self) -> None:
        """Custom font setting.

        Font download link:https://fonts.google.com/.
        Font Link Example: 宋体 https://github.com/google/fonts/raw/main/ofl/msmadi/MsMadi-Regular.ttf
        https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts/master/chinese/%E5%AE%8B%E4%BD%93/STSong.ttf
        楷体： https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts/master/chinese/%E6%A5%B7%E4%BD%93/Kaiti.ttf

        :return: None
        """
        if not self.options or not isinstance(self.options, dict) or not self.options.get("font_link"):
            return

        font_link = str(self.options.get("font_link"))

        # If font_link is not empty, then download font and set font.
        if font_link and isinstance(font_link, str) and font_link.startswith("http"):
            # Set font download path.
            font_path = os.path.join(os.path.dirname(__file__), "_cache", "fonts")
            if not os.path.exists(font_path):
                os.makedirs(font_path)
            # Font file save name.
            font_file_name = os.path.join(font_path, font_link.split("/")[-1])

            if not os.path.exists(font_file_name):
                print(f"Start download font file: {font_link}.")

                with open(font_file_name, "wb") as font_file_handle:
                    font_file_handle.write(requests_get(font_link, stream=True).content)

            self.font = TrueTypeFont.true_type_font_from_file(Path(font_file_name))
        elif os.path.exists(font_link):
            self.font = TrueTypeFont.true_type_font_from_file(Path(font_link))

    def check_out_path(self) -> None:
        if not self.output_path:
            self.output_path = os.path.join(
                os.path.dirname(__file__), "_cache", str(int(datetime.now().timestamp() * 1000))
            )
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


def test_new_pdf_from_ocr():  # pragma: no cover
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    json_path = os.path.join(root_dir, "public/attachments/pdf/ocr/ocr_result.json")
    origin_img_path = os.path.join(root_dir, "public/attachments/pdf/ocr/test2.jpeg")

    page_datas = [{"json_path": json_path, "origin_img": origin_img_path}]
    NewPdfFromOcr(page_datas=page_datas).process()


if __name__ == "__main__":  # pragma: no cover
    test_new_pdf_from_ocr()
