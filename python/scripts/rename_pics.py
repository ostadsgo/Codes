from os import listdir, rename

base = "/home/saeed/docs/code/python/scripts/wallpapers"
images = listdir(base)
for index, name in enumerate(images, 1):
    imgname, ext = name.split('.')
    src = f"{base}/{name}"
    dst = f"{base}/w{index:03}.{ext}"
    try:
        print(src, '->', dst)
        # print(name, '->', 'w'+str(index))
        rename(src, dst)
    except Exception:
        print(f"Erro on {src}")
