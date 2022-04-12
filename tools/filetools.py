#encoding=utf-8
import logging
import os
import six
logging.basicConfig(level=logging.DEBUG)

class FileTools:
    """
    function:read and write file
    """
    def __init__(self,bytes_num):
        self.fragment_size=bytes_num

    def get_file_size(self,src_file):
        return os.path.getsize(src_file)

    def get_fragment_size(self):
        return self.fragment_size

    def read(self,src_file):
        fragments=[]
        try:
            with open(src_file,'rb') as f:
                while True:
                    fragment=f.read(self.fragment_size)
                    if not fragment:
                        break
                    fragments.append(fragment)
                return fragments
        except:
            logging.error("{} file not found.".format(src_file))

    def write(self,target_file,fragments):
        with open(target_file,'wb') as f:
            for fragment in fragments:
                f.write(six.int2byte(fragment))


if __name__=="__main__":
    src_file= "../text_editor/test_file/srcfile"
    target_file="test_file/targetfile"
    filetools=FileTools(4)
    file_size=filetools.get_file_size(src_file)
    print("文件的大小为:{}".format(file_size))
    fragments=filetools.read(src_file)
    for fragment in fragments:
        print(fragment)
    filetools.write(target_file,fragments)