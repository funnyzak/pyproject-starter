# -*- coding: utf-8 -*-
import os


project_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
project_attachment_dir = os.path.join(project_root_dir, "public/attachments")

demo_pic_pdf_path = os.path.join(project_attachment_dir, "samplepic.pdf")
demo_txt_pdf_path = os.path.join(project_attachment_dir, "whatispython.pdf")
test_dist_path = os.path.join(project_root_dir, "dist/pdf_parse")

# if test dist path not exist, create it
if not os.path.exists(test_dist_path):
    os.makedirs(test_dist_path)
