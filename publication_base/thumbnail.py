try:
    import PythonMagick as pymag
    import os

    def is_python_magick():
        return True

    def create_pdf_thumbnail2(full_pdf_file_path):
        file_path, pdf_file_name = os.path.split(full_pdf_file_path)
        create_pdf_thumbnail(file_path, pdf_file_name)

    def create_pdf_thumbnail(file_path, pdf_file_name):
        try:
            if type(file_path) is unicode:
                file_path = str(file_path)
            if type(pdf_file_name) is unicode:
                pdf_file_name = str(pdf_file_name)

            pdf_full_file_path = os.path.join(file_path, pdf_file_name)
            file_without_ext, ext = os.path.splitext(pdf_file_name)
            tmp_file = os.path.join(file_path, file_without_ext + ".jpeg")
            thumbnail_file = os.path.join(file_path, file_without_ext + ".jpg")
            if os.path.isfile(tmp_file):
                os.remove(tmp_file)
            if os.path.isfile(thumbnail_file):
                os.remove(thumbnail_file)

            img = pymag.Image()
            img.density("150")
            img.magick("JPEG")
            img.read(pdf_full_file_path)
            img.write(tmp_file)

            img2 = pymag.Image(tmp_file)
            img2.magick('JPEG')
            img2.scale('160x')
            img2.write(thumbnail_file)

        finally:
            if os.path.isfile(tmp_file):
                os.remove(tmp_file)

    def test_pymagick():
        file_path = "D:\\workspace\\article_info_extractor\\Docs\\2012\\1"
        lst = os.listdir(file_path)
        for file_name in lst:
            name, ext = os.path.splitext(file_name)
            if ext.lower() == ".pdf":
                create_pdf_thumbnail(file_path, file_name)
                print file_name


    #     img2 = pymag.Image(outfile)
    #     img2.magick('JPEG')
    #     img2.scale('160x')
    #     img2.write(thumbnail_file)
except ImportError as e:

    def is_python_magick():
        return False

    def create_pdf_thumbnail2(full_pdf_file_path):
        # print "create_pdf_thumbnail2"
        pass

    def create_pdf_thumbnail(file_path, pdf_file_name):
        # print "create_pdf_thumbnail"
        pass

if __name__ == "__main__":
    create_pdf_thumbnail(r"D:\!", "fiz_mat_3_2012.pdf")
    # test_pymagick()

