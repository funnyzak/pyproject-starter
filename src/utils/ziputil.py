#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import zipfile

import utils.util as util


class ZipUtil:
    @classmethod
    def zip_single_file(cls, zip_path, file_path):
        """单个文件添加到压缩包.

        :param zip_path: 压缩包路径
        :param file_path: 文件路径
        :return:
        """
        with zipfile.ZipFile(zip_path, "w") as z:
            z.write(file_path, os.path.split(file_path)[1])
        pass

    @classmethod
    def unzip_files(cls, zip_path, unzip_target_path, pwd=None):
        """解压缩.

        :param zip_path: 压缩包路径
        :param unzip_target_path: 解压到目标目录
        :param pwd:
        :return:
        """
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(path=unzip_target_path, pwd=pwd)
        pass

    @classmethod
    def zip_files_view(cls, zip_path):
        """查看压缩包所有文件.

        :param zip_path: 压缩包路径
        :return:
        """
        with zipfile.ZipFile(zip_path, "r") as z:
            return z.namelist()
        pass

    @classmethod
    def add_files_to_zip(cls, zip_path, dir_path, recursive=False):
        """把文件添加到压缩包.

        :param zip_path: 压缩包地址
        :param dir_path: 可以是文件路径或文件夹路径，如为文件夹路径则添加该文件夹下的所有文件（不包含子目录）
        :param recursive: 如果是文件夹 压缩是否包含该文件夹名称
        """
        if not os.path.exists(dir_path):
            return False

        if os.path.isfile(dir_path):
            with zipfile.ZipFile(zip_path, "a") as z:
                z.write(dir_path)
                return True
        else:
            with zipfile.ZipFile(zip_path, "a") as z:
                all_files = util.search_files(dir_path, "*")
                for single_file in all_files:
                    if single_file != zip_path:
                        z.write(
                            single_file["full_path"],
                            single_file["full_path"].replace(
                                dir_path if not recursive else os.path.split(dir_path)[0], ""
                            ),
                        )
                return True
        return False
        pass
