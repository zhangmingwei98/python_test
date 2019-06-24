import urllib.request
form http import cookiejar
from urllib import parse

def main():
    header = {
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    login_url = "https://www.yaozhi.com/login"
    login_from_data = {
        "username":"zhangmingwei98",
        "pwd":"zmw981111",
        "formhash":"99D101779B",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    cook = cookiejar.CookieJar()

    handler = urllib.request.HTTPCookieProcessor(cook)

    openr = urllib.request.build_opener(handler)

    login_str = parse.urlencode(login_form_data).encode("utf-8")
    login_request = urllib.request.Request(login_url, headers=header, data=login_str)

    resp = opener.open(login_request)
    print(resp)
    data = resp.read().decode("utf-8")
    # print(data)

    member_url = "https://www.yaozh.com/member/"
    member_request = urllib.request.Request(member_url, headers=header)
    data = opener.open(member_request).read().decode("utf-8")
    with open("08.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()