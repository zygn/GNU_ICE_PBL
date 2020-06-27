import glob, random, copy
import bin.weather as we
import bin.model as mod
from PIL import Image

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4822034000"

imgDic = "./sample/Image"

def findPicture(prefix, img):
    # print("AFTER", prefix)

    hat = []
    hood = []
    jean = []
    longT = []
    padding = []
    shortbottom =[]
    shortT = []
    slacks = []

    result = []

    splitParam = "/"
    # if OS POSIX: "/"
    # if OS NT Kernel: "\\"

    for filename in glob.iglob('{}/**/*.jpg'.format(img), recursive=True):

        if filename[len(img)+1:].split(splitParam)[0] == "hat":
            hat.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "hood":
            hood.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "jean":
            jean.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "longT":
            longT.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "padding":
            padding.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "shortbottom":
            shortbottom.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "shortT":
            shortT.append(filename)
        elif filename[len(img)+1:].split(splitParam)[0] == "slacks":
            slacks.append(filename)

    for i in prefix:
        if i == "hat":
            s = hat
            result.append(s[random.randint(0,len(s))])

        elif i == "hood":
            s = hood
            result.append(s[random.randint(0,len(s))])

        elif i == "jean":
            s = jean
            result.append(s[random.randint(0,len(s))])

        elif i == "longT":
            s = longT
            result.append(s[random.randint(0,len(s))])

        elif i == "padding":
            s = padding
            result.append(s[random.randint(0,len(s))])

        elif i == "shortbottom":
            s = shortbottom
            result.append(s[random.randint(0,len(s))])

        elif i == "shortT":
            s = shortT
            result.append(s[random.randint(0,len(s))])
        
        elif i == "slacks":
            s = slacks
            result.append(s[random.randint(0,len(s))])

    return result


b = we.WeatherSystem(url)
prefix = copy.deepcopy(b.decideCloth())
print('추천 목록:', prefix)
print('가중치:', b.weight)

pl = findPicture(prefix, imgDic)
print('사진 경로', pl)
for i in pl:
    img = Image.open(i)
    img.show()