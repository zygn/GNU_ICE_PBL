import urllib.request, re, random

class WeatherSystem:
      def __init__(self, url):
            self.url = url
            self.data = None
            self.weight = 0.0 #0 추울때 ~ 90 더울때
            self.weightBottom = 0
            self.weightTop = 90 


            self.hood = [20,30, "hood"]
            self.jean = [0,50, "jean"]
            self.longT = [30,50, "longT"]
            self.padding = [0,6, "padding"]
            self.shortbottom = [50,90, "shortbottom"]
            self.shortT = [50,90, "shortT"]
            self.slacks = [30,50, "slacks"]
      

      def weatherStateFounder(self):
            if self.data['weatherstate'] == "맑음":
                  self.weight += 4.0
                  
            elif self.data['weatherstate'] == "구름 많음":
                  self.weight += 2.0

            elif self.data['weatherstate'] == "흐림":
                  self.weight -= 4.0

            elif self.data['weatherstate'] == "흐리고 비":
                  self.weight -= 6.0

            elif self.data['weatherstate'] == "눈":
                  self.weight -= 10.0

            elif self.data['weatherstate'] == "소나기":
                  self.weight += 0.0


      def seasonFounder(self):
            if self.data['airtemp'] >= 25.0:
                  self.weight += self.data['airtemp'] * 2.0 # SUMMER

            elif self.data['airtemp'] <= 5.0:  # WINTER
                  if self.data['airtemp'] <= 0.0: wb = 0
                  else: wb = self.data['airtemp'] * 2.0
                  self.weight += wb
                 
            elif self.data['airtemp'] >= 5.0 and self.data['airtemp'] <= 25.0: # SPRING AND FALL
                  self.weight += self.data['airtemp'] * 2.0 


      def takeWeather(self):
            url = self.url
            ufile = urllib.request.urlopen(url)
            contents = ufile.read().decode('utf-8')
            item = re.findall(r'<item>.+?</item>', contents, re.DOTALL)
            description = re.findall(r'<description>.+?</description>', contents, re.DOTALL)
            header = re.findall(r'<header>.+?</header>', contents, re.DOTALL)
            body = re.findall(r'<body>.+?</body>', contents, re.DOTALL)
            data = re.findall(r'<data seq="0">.+?</data>', contents, re.DOTALL)
            for loc in item:
                  location = re.search(r'<category>(.+)</category>', loc, re.DOTALL)
                  #print(location.group(1))
            for hea in header:
                  tm = re.search(r'<tm>(.+)</tm>', hea, re.DOTALL)
                  for dat in data:
                        temp = re.search(r'<temp>(.+)</temp>', dat, re.DOTALL)
                        wfKor = re.search(r'<wfKor>(.+)</wfKor>', dat, re.DOTALL)
                        ws = re.search(r'<ws>(.+)</ws>', dat, re.DOTALL)
            # print('     ', 'YYYYMMDDHHmm :', tm.group(1))
            # print('     ', '기온 :', temp.group(1))
            # print('     ', '날씨 :', wfKor.group(1))
            # print('     ', '풍속(m/s) :', ws.group(1))
            self.data = {
                  'locationhere' : location.group(1),
                  'airtemp' : float(temp.group(1)),
                  'weatherstate' : wfKor.group(1),
                  'windspeed' : float(ws.group(1))
            }


      def decideCloth(self):

            self.takeWeather()
            self.seasonFounder()
            self.weatherStateFounder()

            res = []

            hatRandomize = random.randint(0,1)
            if hatRandomize == 0:
                  pass
            else: res.append("HAT") 
            
            arr = [self.hood, self.jean, self.longT, self.padding, self.shortbottom, self.shortT, self.slacks]
            for i in arr:
                  if self.weight >= i[0] and self.weight <= i[1]:
                        res.append(i[2])
            return res



# b = WeatherSystem(weather(url))
# print(b.decideCloth())