# created by: leon<silenceace at gmail dot com>
# date: 2022-10-02
# license: MIT
# description: Merge pdf files
# usage: poetry run python src/pdf_parse/merge_pdf.py
# notes:

from datetime import datetime
import os

from PyPDF2 import PdfMerger

from pdf_parse import create_sub_dir


attachment_root = os.path.join(os.path.dirname(__file__), "attachments")
txt_pdf_path = os.path.join(attachment_root, "whatispython.pdf")
pic_pdf_path = os.path.join(attachment_root, "samplepic.pdf")
merge_pdf_path = os.path.join(os.path.dirname(__file__), "dist", f"merge_{str(int(datetime.now().timestamp()))}.pdf")

merger = PdfMerger()

input1 = open(pic_pdf_path, "rb")
input2 = open(txt_pdf_path, "rb")
input3 = open(txt_pdf_path, "rb")

# add the first 1 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 1))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position=0, fileobj=input2, pages=(0, 1))

# append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open(merge_pdf_path, "wb")
merger.write(output)

print(f"Merge PDF written to {merge_pdf_path}")

# Close File Descriptors
merger.close()
output.close()
