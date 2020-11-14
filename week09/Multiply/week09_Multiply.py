#-*-coding: cp950-*-
#-*-coding: utf-8-*-

import json
from ArticutAPI import ArticutAPI
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath , encoding="utf-8") as f:
        jsonFile = json.loads(f.read())
    return jsonFile

if __name__== "__main__":
    
    #tourblog.json
    jsonFilePath = "../example/tourblog.json"
    tourblogSTR = jsonTextReader(jsonFilePath)["content"]
    tourblogSTR = tourblogSTR.replace(" " , "")
    articut = ArticutAPI.Articut()
    
    #print("tourblogSTR")
    #print(tourblogSTR)
    #print(len(tourblogSTR))
    resultDICT = articut.parse(tourblogSTR , level = "lv2")
    
    #print("resultDICT")
    #print(resultDICT)
    
    resultLIST = articut.getLocationStemLIST(resultDICT)
    locLIST = []
    #print(type(resultLIST))
    #print(resultLIST)
    while resultLIST.count([]):
        resultLIST.remove([])
    #print("resultLIST")
    #print(type(resultLIST))
    #print(resultLIST)
    
    for i in resultLIST:
        if i[0][-1] not in locLIST:
            locLIST.append(i[0][-1])
    
    
    #print("locLIST")
    #print(locLIST)
    
    #print("tourblog")
    #print(locLIST)
    
    resultDICT = articut.parse(tourblogSTR , openDataPlaceAccessBOOL=True)
    resultLIST = articut.getOpenDataPlaceLIST(resultDICT)
    
    
    while resultLIST.count([]):
        resultLIST.remove([])
    
    
    openLIST = []
    
    for i in resultLIST:
        if i[0][-1] not in openLIST:
            openLIST.append(i[0][-1])
    
    #print(openLIST)
    
    jsonDICT = {"location" : locLIST , "place" : openLIST}
    #print("loc and place")
    #print(jsonDICT)
    
    #place �̦� '�j�@�I' ?
    with open('tourblog_geoinfo.json' , 'w' , encoding = 'utf-8') as f:
        json.dump(jsonDICT , f , ensure_ascii = False)    
    
    #�D�ƧP�M_106,��²,359_2017-02-21.json
    jsonFilePath = "../example/�D�ƧP�M_106,��²,359_2017-02-21.json"
    justiceSTR = jsonTextReader(jsonFilePath)["mainText"] 
    
    #justiceSTR = justiceSTR.replace("��" , "3")
    #print("justiceSTR")
    #print(justiceSTR)
    
    articut = ArticutAPI.Articut()
        
    resultDICT = articut.parse(justiceSTR , level="lv2")
    lawTK = ArticutAPI.LawsToolkit(resultDICT)
    
    resultLIST = lawTK.getCriminalResponsibility()
    #print("resultLIST")
    #print(resultLIST)
       
    resultDICT = {'liability': resultLIST}
        
    with open('justice.json' , 'w' , encoding = 'utf-8') as f:
        json.dump(resultDICT , f , ensure_ascii = False)     
    
    
    #news
    jsonFilePath = "../example/news.json"
    newsSTR = jsonTextReader(jsonFilePath)["content"] 
    articut = ArticutAPI.Articut()
    
    newsSTR = newsSTR.replace(" " , "")
    
    resultDICT = articut.parse(newsSTR , level="lv2")
    
    nameDICT = {}
    resultLIST = articut.getPersonLIST(resultDICT)
    #numName = len(nameLIST)
    
    while resultLIST.count([]):
        resultLIST.remove([])
    
    for i in resultLIST:
        if i[0][-1] not in nameDICT:
            nameDICT[i[0][-1]] = 1
        else:
            nameDICT[i[0][-1]] = nameDICT[i[0][-1]] + 1
    
    nameLIST = []
    for i in nameDICT:
        nameLIST.append((i,nameDICT[i]))
    
    #print("nameLIST")
    #print(nameLIST)
    
    
    
    articut = ArticutAPI.Articut()
    
    #print("tourblogSTR")
    #print(tourblogSTR)
    #print(len(tourblogSTR))
    
    resultDICT = articut.parse(newsSTR , level = "lv2")
    
    resultLIST = articut.getLocationStemLIST(resultDICT)
    locLIST = []
    
    while resultLIST.count([]):
        resultLIST.remove([])
    
    for i in resultLIST:
        if i[0][-1] not in locLIST:
            locLIST.append(i[0][-1])
    
    #print("locLIST")
    #print(locLIST)
        
    resultDICT = articut.parse(newsSTR , level="lv2")
    resultLIST = articut.getCurrencyLIST(resultDICT)
    
    while resultLIST.count([]):
        resultLIST.remove([])
    
    moneyLIST = []
    
    for i in resultLIST:
        if i[0][-1] not in moneyLIST:
            moneyLIST.append(i[0][-1])
    
    #print("moneyLIST")
    #print(moneyLIST)
    
    
    
    resultDICT = {"people": nameLIST , "location": locLIST , "money": moneyLIST}
                
    with open('news_info.json' , 'w' , encoding = 'utf-8') as f:
       json.dump(resultDICT , f , ensure_ascii = False)
    
    