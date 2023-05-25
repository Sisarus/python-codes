class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        

kissa = analysedText("Suomen Nato-prosessi tulee päätökseen tänään tiistaina, kun Suomi hyväksytään osaksi kansainvälistä sotilasliittoa. Suomen ulkoministeri Pekka Haavisto (vihr) matkusti eilen Brysseliin Suomen Nato-dokumentit salkussaan. Paikan päällä on luonnollisesti myös Suomen presidentti Sauli Niinistö. Iltalehti seuraa Nato-prosessin viimeisiä askelia paikan päällä. Paikalla ovat toimittajamme Lauri Nurmi ja kuvaajamme Elle Laitila. Tästä jutusta löydät tärkeät kellonajat.")

print(kissa.freqAll())

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()


x="Go"

if(x=="Go"):

  print('Go ')

else:

  print('Stop')

print('Mike')

def add(a, b):
    return(a+b)

for i,x in enumerate(['A','B','C']):
    print(i,2*x)