# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description:  new pdf from ocr result
# usage:
# notes:

# type: ignore
from datetime import datetime
from decimal import Decimal
import json
import os
from pathlib import Path
from typing import List

from borb.pdf import PDF  # type: ignore[import]
from borb.pdf import Alignment
from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.geometry.rectangle import Rectangle
from requests import get as requests_get


class NewPdfFromOcr:
    doc: Document = Document()
    font = None
    font_color = "#000000"

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
        :param options: options, dict, keys is: font_link, font, font_size, font_color.
        :param output_path: the output path of new pdf file.
        """
        self.output_path = output_path
        self.page_datas = page_datas
        self.options = options

        if not self.options:
            self.options = {
                "font_link": "https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts"
                + "/master/chinese/%E5%AE%8B%E4%BD%93/STSong.ttf"
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
        # read json file from ocr result
        with open(page_data.get("json_path"), "r") as f:
            ocr_result_json = json.load(f)

        if not ocr_result_json:
            return

        # Create Page.
        page: Page = Page(width=Decimal(ocr_result_json["width"]), height=Decimal(ocr_result_json["height"]))

        # Add Page to Document.
        self.doc.add_page(page)

        if not ocr_result_json.get("chars"):
            return

        for _index, _word in enumerate(ocr_result_json["chars"]):
            ocr_txt = _word["ocr_txt"]

            position: Rectangle = Rectangle(
                Decimal(_word["x"]),
                Decimal(ocr_result_json["height"]) - Decimal(_word["y"]) - Decimal(_word["h"]),
                Decimal(_word["w"]),
                Decimal(_word["h"]),
            )

            # get word width x 0.8
            try:
                Paragraph(
                    ocr_txt,
                    horizontal_alignment=Alignment.CENTERED,
                    vertical_alignment=Alignment.MIDDLE,
                    font=self.font,
                    font_color=HexColor(self.font_color) if self.font_color else HexColor("#000000"),
                    font_size=Decimal(self.options.get("font_size"))
                    if self.options.get("font_size")
                    else Decimal(_word["w"]) * Decimal(0.8),
                ).paint(page, position)
            except Exception as e:
                print(e)
                print("ocr_txt: ", ocr_txt)
                print("position: ", position)

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
            if not os.path.exists(page_data.get("json_path")):
                raise Exception("page_data json_path not exist.")

    def custom_setting(self) -> None:
        """Custom setting."""
        print("Start custom setting.")
        self.custom_font_setting()
        print("End custom setting.")

    def custom_font_setting(self) -> None:
        """Custom font setting.

        Font download link:https://fonts.google.com/.
        Font Link Example: https://github.com/google/fonts/raw/main/ofl/msmadi/MsMadi-Regular.ttf
        https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts/master/chinese/%E5%AE%8B%E4%BD%93/STSong.ttf

        :return: None
        """
        if not self.options or not isinstance(self.options, dict) or not self.options.get("font_link"):
            return

        font_link = self.options.get("font_link")

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
        """Check out_path."""
        if not self.output_path:
            self.output_path = os.path.join(
                os.path.dirname(__file__), "_cache", str(int(datetime.now().timestamp() * 1000))
            )
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


def test_new_pdf_from_ocr():  # pragma: no cover
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    json_path = os.path.join(root_dir, "public/attachments/pdf/ocr/ocr_result.json")

    page_datas = [
        {
            "json_path": json_path,
        }
    ]
    NewPdfFromOcr(page_datas=page_datas).process()


if __name__ == "__main__":  # pragma: no cover
    test_new_pdf_from_ocr()
