
import json 
import re 

def hasCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def makeDictionaryFromText(text):
    forbiddenSymbols = ["(n.), (v.)","(n.)","(n.), (v.)","[]","(v.)","(phr. v.)","(adj.)","(чым-н.)","(чем-л.)","(n. phr.)","(v. phr.)"]
    dict  = {} 
    arr = text.splitlines()

    for phrase in arr:
        if  "/" and "–" in phrase: # like str is not empy and we will not crush on finding indexes
            i = phrase.index("–")
            j = phrase.rindex("/") # rindex - the last index of element . We need it when we have : stand up for smbd/dmth - постоять за / пастаяць за
            eng = phrase[:i]
            Rus = phrase[i+2:j]

            # убираем транскрипцию 
            try:
                beginOfTranscription = eng.index("[") # if we have "[" это начит что это началась трансрипция , а после транскрипции ничего полезного нету
                Eng  = eng[:beginOfTranscription-1]
            except :
                # значит что транскрипции не было
                pass

            # убираем то что в скобочках типо (v.) , (n.) (adj.)  и т.д
            for i in forbiddenSymbols:
                while i in Eng:
                    Eng = Eng.replace(i,"")

            dict [Eng.strip()] = Rus.strip()
    
    return dict


def reverseDictionary(dict):
    newDict = {}
    for eng , rus in dict.items():
        newDict[rus] = eng;
    return newDict

def makeVarietyOfAnswerForEnglishWords(dict):
    prepositionsArr = ["on smb","on sth","for smd","for sth","for smth/smb","on smth/smb","to smth/smb","to smb","to sth","for yourself","with smth","with smb","sth","smd"]
    for rus , eng in dict.items():
        if "(" and ")" in eng:
            beginIndex   = eng.index("(")
            endIndex     = eng.index(")")
            secondOption = (eng[:beginIndex] + eng[endIndex+1:]).strip()
            arrEng       = [eng,secondOption] 

            dict[rus]     = arrEng

        for prepos in prepositionsArr:
            if prepos in eng:# just checkin that it was in the end of the words , brecause if it is in the middle we should not make one more option
                beginIndexOfPrepos = eng.index(prepos)
                lenShoudBe =  beginIndexOfPrepos+len(prepos)
                if len(eng) == lenShoudBe:
                    secondOption = (eng[:beginIndexOfPrepos]).strip()
                    arrEng       = [eng,secondOption] 

                    dict[rus]     = arrEng

    return dict


def deleteEnters(text): # delete make the eng in rus together not on  different lines
    arr = text.splitlines()

    for i in range(0,len(arr)):
        if len(arr[i]) >=2 and hasCyrillic(arr[i][1]+arr[i][2]): # we need 2 symbols because belerussian "i" == english "i" and first simple cam be "("
            numberOfLinesThatRussionTranslationOccupy= 1
            while ( len(arr[i]) >=2 ) and ( hasCyrillic(arr[i][1]+arr[i][2]) ):
                if ( len(arr[i-1]) > 1 ) and ( arr[i-1][-1] == "-") :# значит что это знак переноса и мы просто его убираем (он нам не нужен)
                    # и тут arr-1 а не arr-i потомучто на каждой предыщей строке может быть перенос , а не только на самой первой с которой начинает перевод переходить на другую строку
                    # так как троки не изменяему то мы создаем новую строку без последнего символа

                    # PROBLEM : почему то не работает когда много переносов как например слово temper
                    print(i," ============DELETING -==========")
                    print("OLD STR: ",arr[i-1])
                    newStr = arr[i-1][:-1]
                    arr[i-1]= newStr
                    print("NEW STR: ",arr[i-1])


                arr[i-numberOfLinesThatRussionTranslationOccupy] += arr[i]
                arr[i] = " "
                numberOfLinesThatRussionTranslationOccupy += 1
                i+=1

    text = "\n".join(arr)
    return text

def main(text):
    text = deleteEnters(text)
    dict = makeDictionaryFromText(text)
    dict = reverseDictionary(dict)
    dict = makeVarietyOfAnswerForEnglishWords(dict)
    return json.dumps(dict,indent=4,ensure_ascii=False)
    # writeDataToFile(OUT_FILE,json.dumps(dict,indent=4,ensure_ascii=False)) # write(refresh) our SRC file

