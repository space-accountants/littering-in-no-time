import glob
import os

import xml.etree.ElementTree as ElementTree


def get_root_of_table(path: str,
                      fname: str = None) -> ElementTree:
    if fname is None:
        full_name = path
    else:
        full_name = os.path.join(path, fname)
    if '*' not in full_name:
        assert os.path.isfile(full_name), \
            ('please provide correct path and file name')
    dom = ElementTree.parse(glob.glob(full_name)[0])
    root = dom.getroot()
    return root