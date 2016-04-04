from bs4 import BeautifulSoup
import urllib
import shutil
import os

def getSynUnicodes(word):
    synCodes = []
    url = "http://tangorin.com/kanji/"+word
    markup = urllib.urlopen(url)
    soup = BeautifulSoup(markup, "html5lib")
    entries = soup.find_all("div",attrs={"class":"entry"})
    for entry in entries:
        try:
            bs = entry.dd.find("p", attrs={"class":"k-meaning"}).find("span",attrs={"class":"k-lng-en"})
        except: continue
        for b in bs.find_all('b'):
            if (b.string == word):
                # found!
                codeTr = entry.dd.find("div",attrs={"class":"k-codes"}).find("tr")
                print entry.dt.h2.string, ":", codeTr.td.string
                resCode = codeTr.td.string
                synCodes.append(resCode.encode("utf-8"));
    return synCodes

def codeSvgExists(codes,word):
    for code in codes:
        filename = "0"+code+".svg"
        kanjiFilePath = os.path.join("/Users/chelseakwong/Downloads/kanji",filename)
        saveFolder = os.path.join("/Users/chelseakwong/Documents/sketch-rnn-master/save",word)
        if not os.path.exists(saveFolder):
            os.makedirs(saveFolder)
        boolean = os.path.exists(kanjiFilePath)
        print (code, " file exists: ", boolean)
        if (boolean):
            # copy it to sketch-rnn folder, data/word
                newFolderPerCode = os.path.join("/Users/chelseakwong/Documents/sketch-rnn-master/data","negative",word,code)
                if not os.path.exists(newFolderPerCode):
                    os.makedirs(newFolderPerCode)
                for x in range(100):
                    tempNewFileName=os.path.join("/Users/chelseakwong/Documents/sketch-rnn-master/data","negative",word,code,str(x)+'.svg')
                    shutil.copy2(kanjiFilePath,tempNewFileName)

def findAndShow(word):
    codes = getSynUnicodes(word)
    codeSvgExists(codes,word)

findAndShow("need")
