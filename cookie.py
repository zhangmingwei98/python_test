import urllib.request

def main():
    url = "https://www.yaozh.com/member/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie": "acw_tc=2f624a7715613580315505579e4627022c28564f4fd80040358e0ee09f0360; PHPSESSID=7sv9421nc3lm6dhimliv3icei6; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1561358033; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1561358037; _ga=GA1.2.1702873403.1561358034; _gid=GA1.2.1558366512.1561358034; _gat=1; MEIQIA_VISIT_ID=1N55IIq3uxocYcZBSTgTaHgMX3w; MEIQIA_EXTRA_TRACK_ID=1N55IIubK2xZprVxHwUWGohFDtt; yaozh_userId=774628; UtzD_f52b_saltkey=IembZM51; UtzD_f52b_lastvisit=1561354445; UtzD_f52b_lastact=1561358603%09uc.php%09; yaozh_uidhas=1; yaozh_mylogin=1561358047; acw_tc=2f624a7715613580315505579e4627022c28564f4fd80040358e0ee09f0360; MEIQIA_VISIT_ID=1N55IIq3uxocYcZBSTgTaHgMX3w; MEIQIA_EXTRA_TRACK_ID=1N55IIubK2xZprVxHwUWGohFDtt; UtzD_f52b_ulastactivity=1561358006%7C0; _ga=GA1.1.1069582850.1561358165; _gid=GA1.1.2002682640.1561358165; yaozh_logintime=1561358602; yaozh_user=774628%09zhangmingwei98; db_w_auth=688311%09zhangmingwei98; UtzD_f52b_auth=c483rgD5NnzkMtV56y2HyNT1v5Y%2BnJ2SzEg%2Fg75XNs71rL74JOk38QZodBKNbMdpEDu2NiJbWqURy%2FDpIXspbX7cdAQ"
    }
    request = urllib.request.Request(url,headers=header)

    data = urllib.request.urlopen(request).read().decode("utf-8")
    with open("07.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()