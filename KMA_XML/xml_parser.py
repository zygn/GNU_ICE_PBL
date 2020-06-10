import urllib.request, re

url = 'http://www.kma.go.kr/wid/'\
      'queryDFSRSS.jsp?zone=4822034000'

ufile = urllib.request.urlopen(url)
contents = ufile.read().decode('utf-8')

item = re.findall(r'<item>.+?</item>', contents, re.DOTALL)
description = re.findall(r'<description>.+?</description>', contents, re.DOTALL)
header = re.findall(r'<header>.+?</header>', contents, re.DOTALL)
body = re.findall(r'<body>.+?</body>', contents, re.DOTALL)
data = re.findall(r'<data seq="0">.+?</data>', contents, re.DOTALL)

for loc in item:
      location = re.search(r'<category>(.+)</category>', loc, re.DOTALL)
      print(location.group(1))

for hea in header:
      tm = re.search(r'<tm>(.+)</tm>', hea, re.DOTALL)
      for dat in data:
            temp = re.search(r'<temp>(.+)</temp>', dat, re.DOTALL)
            wfKor = re.search(r'<wfKor>(.+)</wfKor>', dat, re.DOTALL)
            ws = re.search(r'<ws>(.+)</ws>', dat, re.DOTALL)

print('     ', 'YYYYMMDDHHmm :', tm.group(1))
print('     ', '기온 :', temp.group(1))
print('     ', '날씨 :', wfKor.group(1))
print('     ', '풍속(m/s) :', ws.group(1))