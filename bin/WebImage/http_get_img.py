from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import os
import re


def download(alt, url):
    # 다운로드 함수

    outpath = "./Download/" 
    outfile = alt+".jpg"
    if not os.path.isdir(outpath):
        os.makedirs(outpath)
    urllib.request.urlretrieve(url, outpath+outfile)


def imgSearch(url):
    #  이미지 찾는 함수
    alt = list()
    res = list()
    with urllib.request.urlopen(url) as fp:
        html = fp.read()
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all("img"):
            alt.append([img.get("alt"), img.get("src")])
        for k in alt:
            if k[1].find('product') != -1 and k[1].find('.jpg') != -1:
                res.append(k) 
            
    return res

# def makeURL(data):
#     # 정규 표현식으로 URL 체킹

#     regex = ''
#     if re.compile(regex) == True:
#         return data
    
def txtReader():
    try:
        res = list()
        f = open('link.txt', 'r')

        for s in f:
            if s.find('\n') != -1: s.rstrip('\n')
            res.append('{}'.format(s))
            print("Read:{}".format(s), end='')
        
        return res

    except:
        print("Error Raised!")

    finally:
        f.close()

    
# link = [
#     'https://hukubukuro.kr/product/list.html?cate_no=93',
#     'https://hukubukuro.kr/category/tee/91/',
#     'https://hukubukuro.kr/category/mtm/229/',
#     'https://hukubukuro.kr/category/hood/230/',
#     'https://hukubukuro.kr/category/shirt/92/',
#     'https://hukubukuro.kr/category/half-zip-up/299/',
#     'https://hukubukuro.kr/category/training-set/135/',
#     'https://hukubukuro.kr/category/knit/95/'
# ]

link = txtReader()

for url in link:
    get = imgSearch(url)
    for i in get:
            print("GET:"+i[0]+".jpg")
            download(i[0],"https:"+i[1])

