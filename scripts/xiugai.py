import os
import re


def 禁用软件包(file):
    with open(file, "r", encoding="UTF-8") as f1, open(
        "%s.bak" % file, "w+", encoding="UTF-8", newline="\n"
    ) as f2:
        for line in f1:
            结果 = re.findall("(.*uhttpd.*)=y", line)
            if 结果:
                print(line)
                line = re.sub("^", "# ", line)
                line = re.sub("=y$", " is not set", line)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)


文件路径 = os.getenv("OPENWRT_PATH")

禁用软件包(f"{文件路径}/.config")
