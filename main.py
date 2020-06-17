import KMA_XML.xml_parser as kma
import Model.model as md

globSeason = None

url = 'http://www.kma.go.kr/wid/'\
      'queryDFSRSS.jsp?zone=4822034000'
tempdir = "C:/Users/Yundo/Documents/GitHub/GNU_ICE_PBL/SampleCase/"

loc = kma.weather(url)
model = md.modelReturn(tempdir+"01.jpg",tempdir+"md.h5")
print(loc, model)

if float(loc['airtemp']) > 25.0 and loc['weatherstate'] == "맑음":
    globSeason = "SUMMER"

print(globSeason)
