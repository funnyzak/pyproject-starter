import os


def create_sub_dir(dir_name):
    # create dist folder if not exist
    dist_folder = os.path.join(os.path.dirname(__file__), dir_name)
    if not os.path.exists(dist_folder):
        os.mkdir(dist_folder)


if __name__ != "__main__":
    print("pdf_parse project")
