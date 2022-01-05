def read_file(filename):
    with open(filename) as f:
        return f.read()


def sep_pkgs(s):
    pkgs_list = s.split(" ")
    pkgs = [pkg for pkg in pkgs_list if pkg != ""]
    return pkgs

def get_pkg_name(pkgs):
    pkgs_list = []
    for pkg in pkgs[:10]:
        index = pkg.find('.')
        pkg_name = pkg[:index-2]
        pkgs_list.append(pkg_name)
    return pkgs_list


s = read_file("pkgs.txt")
pkgs = sep_pkgs(s)
names = get_pkg_name(pkgs)
for pkg in pkgs:
    print(pkg)
