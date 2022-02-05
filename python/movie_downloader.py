
from urllib import request

base_url = ("https://fh.bia2anime.site/Series/Anime/"
       "Code.Geass/Code.Geass.Hangyaku.no.Lelouch.R2/"
       "Code.Geass.Hangyaku.no.Lelouch.R2.{}.Uncen.720p.Bia2Anime.mkv")


for count in range(1, 26):
    episode = f"0{count}" if count < 10 else f"{count}" 
    filename = f"Code_Geass_R2_{episode}.mkv"
    url = base_url.format(episode)
    request.urlretrieve(url, filename)
    print(filename, "downloaded sucessfuly.")


