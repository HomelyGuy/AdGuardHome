import re
import os
from shutil import copyfile

pat = re.compile("url: .*?myfilters.(.*?)$")
path = os.getcwd()
# posix or nt
platform = os.name
lines = []

copyfile("AdGuardHome.yaml", "AdGuardHome_0.yaml")
with open("AdGuardHome.yaml") as f:
    line = f.readline()
    while line:
        res = re.search(pat, line)
        if res:
            files = res.group(1)
            if platform == "posix":
                new_file = "  url: " + path + "/myfilters/" + files
            elif platform == "nt":
                new_file = "  url: " +  path + "\\myfilters\\" + files
            lines.append(new_file + '\n')
        else:
            lines.append(line)
        line = f.readline()

#generate configurate
with open("AdGuardHome.yaml", "w") as fw:
    for line in lines:
        fw.write(line)