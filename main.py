import os
import re

re_str = input("regex>")
replacement = input("replacement>")
dir = input("dir>")
for filename in os.listdir(dir):
    new_name = re.sub(re_str, replacement, filename)
    os.rename(dir+"/"+filename, dir+"/"+new_name)