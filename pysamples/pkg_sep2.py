f = open("pkgs.txt")
content = f.read()
f.close()


pkgs_list = content.split("\n")
pkgs_list = pkgs_list[1:-1]

import re
patt = r"^(\w*-){1,4}"
pkgs_name = []
for line in pkgs_list:
    match = re.search(patt, line)
    if match is not None:
        start = match.start()
        end = match.end()
        pkgs_name.append(line[start:end-1])

print(" ".join(pkgs_name[3:20]))
        
