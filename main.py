
import bin.weather as we
import bin.model as mod 

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4822034000"

modelDic = "C:/Users/Yundo/Documents/GitHub/GNU_ICE_PBL/SampleCase/50md.h5"
imgDic = "C:/Users/Yundo/Documents/GitHub/GNU_ICE_PBL/SampleCase/01.jpg"

b = we.WeatherSystem(url)
print(b.decideCloth())

m = mod.modelReturn()
print(m)