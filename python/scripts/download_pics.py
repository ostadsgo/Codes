import re
from os import system

wall_path = "/home/saeed/docs/code/python/scripts"
# url = "https://github.com/linuxdotexe/nordic-wallpapers/tree/master/wallpapers"
# html_page = system(f"wget -O index.html {url}") 

# html file
f = open(f"{wall_path}/index.html", 'r')
html_content = f.read()
f.close()

matches = re.findall(r"(\w+-?\w+\.(png|jpg|jpeg))<\/a>", html_content)
i = 0
for match in matches:
    name = match[0]
    url = f"https://github.com/linuxdotexe/nordic-wallpapers/raw/master/wallpapers/{name}"
    # system(f"axel '{url}'")
    i += 1
    print(name, i)
