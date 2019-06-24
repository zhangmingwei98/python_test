import urllib.request
import urllib.parse
import string

def main():
    # base url
    url = "http://www.baidu.com/s?wd="
    print(url)

    # string append
    name = "数据库"
    url += name
    #url += ""
    print(url)
    # 中文 -> ascii
    url = urllib.parse.quote(url,safe=string.printable)
    print(url)

    # open url,return response
    resp = urllib.request.urlopen(url)
    print(resp)
    #read从resp中读取数据（bytes）,decode: byte -> string
    data = resp.read().decode("utf-8")

    print(resp)
    print(data)
    name += ".html"
    with open("01.html","w") as f:
        f.write(data)



if __name__ == "__main__":
    main()