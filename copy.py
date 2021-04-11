import os
import shutil
import sys
import subprocess
import re
import uuid
import random
import string

altium_temp_dir = "C:\\Users\\Public\\Documents\\Altium\\AD18\\Templates\\"

top = os.path.dirname(os.path.realpath(__file__))

print(top)


def copy():
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            if root.find(".git") < 0 and name.endswith(".SchDot"):
                scr = os.path.join(root, name)
                dst = os.path.join(altium_temp_dir, name)
                shutil.copyfile(scr, dst)
                print("copy: %s" % dst)


copy()
