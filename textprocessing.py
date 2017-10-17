
import os
import string



class docdata:
    
    fulldict = {}
    
    def __init__ (self):
        self.wordlist = []
        self.worddict = {}
        self.size = 0






foldername = "./transcripts"
delStr = str.maketrans(dict.fromkeys(string.punctuation + string.digits))


docnames = os.listdir(foldername)
doclist = []


for filename in docnames :
    docdir = foldername+"/"+filename
    docfile = open(docdir,encoding='utf_8',errors='ignore')
    #print(filename)
    textstr = docfile.read()
    textstr = textstr.replace(u'\ufeff','')
    textstr = textstr.translate(delStr)
    textstr = textstr.lower()
    textstr = textstr.split()

    doclist.append(textstr)    
    docfile.close()

print(doclist[15])
indexedDoc = []
sortedfulldict = []
databasesize = 0
    
for doc in doclist:
    data = docdata()
    data.size = len(doc)
    databasesize += data.size
    data.wordlist = doc
        
    for word in doc:
        
        if word in data.worddict.keys():
            data.worddict[word] = data.worddict[word] + 1            
        else:
            data.worddict[word] = 1
            
            
        if word in data.fulldict.keys():
            data.fulldict[word] = data.fulldict[word] +1
        else:
            data.fulldict[word] = 1
                
    
    data.wordlist = sorted(data.worddict.items(),key= lambda d:d[1],reverse = True)    
    indexedDoc.append(data)

sortedfulldict = sorted(data.fulldict.items(),key= lambda d:d[1],reverse = True)
#print (indexedDoc[1].worddict)
i = 0
mostfrewords = []
oncewords = []

for key in sortedfulldict:
    mostfrewords.append(key[0])
    i += 1
    if i == 30:
        break

for key in sortedfulldict:
    if key[1] == 1:
        oncewords.append(key[0])

print("Q1-Q3")
print(databasesize)
print(len(sortedfulldict))
print(oncewords)

print(mostfrewords)
tfdict = {}
idfdict = {}
tfidfdict = {}
possibilitydict = {}
for query in mostfrewords:
    tfdict[query] = data.fulldict[query]
    possibilitydict[query] = data.fulldict[query]/databasesize
    
    idfdict[query] = 0
    for doc in indexedDoc:        
        if query in doc.worddict.keys():
            idfdict[query] += 1
    idfdict[query] /= len(indexedDoc)
    tfidfdict[query] = tfdict[query]*idfdict[query]

print("Q4")
print(tfdict)
print(idfdict)
print(tfidfdict)
print(possibilitydict) 

print("Q5")
print(databasesize/len(docnames))    

            
            
        

