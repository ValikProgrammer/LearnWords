#=========INSTRUCTION=================
# width and hiegth  must be the same (так расчитано)
# width & hiegth of digits = 5 
# width & hiegth of % = 7 

# class colors:
#     RED = '\033[31m' # red
#     GREEN = '\033[32m' # green
#     ORANGE = '\033[32m'#'\033[33m' # orange
#     BLUE = '\033[35m' # blue
#     UNDERLINED = '\033[4m'
#     BOLD = '\033[1m'
#     END = '\033[0m' # simple text (stop colourful text)

def getResult(SCORE):
    
    # ======CONSTANTS==========
    SCORE = str(SCORE)
    # SCORE = "1234567890"
    SEPERATOR = "  "

    SYMBOLS = {

        "0" : [
            "#####",
            "#   #",
            "#   #",
            "#   #",
            "#####",
            # "#####",
            # "#####",
            # "#####",
            # "#####",
            # "#####",
        ],
        "1" : [
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            # "#####",
            # "#####",
            #         "#####",
            # "#####",
            # "#####",
        ],
        "2" : [
            "#####",
            "    #",
            "#####",
            "#    ",
            "#####",
            # "#####",
            # "#####",
            #         "#####",
            # "#####",
            # "#####",
        ],
        "3" : [
            "#####",
            "    #",
            "#####",
            "    #",
            "#####"
        ],
        "4" : [
            "#   #",
            "#   #",
            "#####",
            "    #",
            "    #"
        ],
        "5" : [
            "#####",
            "#    ",
            "#####",
            "    #",
            "#####"
        ],
        "6" : [
            "#####",
            "#    ",
            "#####",
            "#   #",
            "#####"
        ],
        "7" : [
            "#####",
            "    #",
            "    #",
            "    #",
            "    #"
        ],
        "8" : [
            "#####",
            "#   #",
            "#####",
            "#   #",
            "#####"
        ],
        "9" : [
            "#####",
            "#   #",
            "#####",
            "    #",
            "#####"
        ],
        "%" : [
            # "0000/",
            # "000/ ",
            # "  /  ",
            # " /000",
            # "/0000",
            "###   /",
            "# #  / ",
            "### /  ",
            "   /   ",
            "  / ###",
            " /  # #",
            "/   ###",
        ],
    }
    


    """


    sizeOfZero = len(SYMBOLS["0"])
    sizeOfPersent = len(SYMBOLS["%"])

    standartCharSize = min (sizeOfPersent,sizeOfZero)# 5 
    anotherCharSize = max (sizeOfPersent,sizeOfZero)# 7
    standartCharSizeWithSEPERATOR = standartCharSize + len(SEPERATOR) # 5 +2 = 7
    anotherCharSizeWithSEPERATOR = anotherCharSize + len(SEPERATOR)# 7 + 2 = 9


    """



    degitsAmount = len(SCORE)

    standartCharSize = len(SYMBOLS["0"])# 5 
    anotherCharSize = len(SYMBOLS["%"])# 7
    standartCharSizeWithSEPERATOR = standartCharSize + len(SEPERATOR) # 5 +2 = 7
    anotherCharSizeWithSEPERATOR = anotherCharSize + len(SEPERATOR)# 7 + 2 = 9

    indexToStartPrintingStandartCharSize = ((anotherCharSize-standartCharSize))//2 
    indexToEndPrintingStandartCharSize = (anotherCharSize - indexToStartPrintingStandartCharSize)

    # print("indexToStartPrintingStandartCharSize,indexToEndPrintingStandartCharSize:",indexToStartPrintingStandartCharSize,indexToEndPrintingStandartCharSize)
    # print("anotherCharSize,standartCharSize:",anotherCharSize,standartCharSize)


    console = []
    MASSAGE = "Score: "
    # append lines to the result output (amount of lines == anotherCharSize)
    for i in range (0,max(anotherCharSize,standartCharSize)):
        console.append(" "*len(MASSAGE))


    # print("==============================================================================")

    # print digits in standar size lines

    # lenOfRavno = len(resultArr[0])+len(massageScore)
    


    # print("="*lenOfRavno)

    for digit in (SCORE):
        for i in range ( 0,standartCharSize):
            console[i+indexToStartPrintingStandartCharSize] += (SYMBOLS[digit][i] + SEPERATOR)

    # print BIG "%" in big size
    for i in range (0,len(console)):
        # put spaces where neccssary (where was not digits)
        if (i < indexToStartPrintingStandartCharSize or i >= indexToEndPrintingStandartCharSize ):
            console[i] += " "*(standartCharSizeWithSEPERATOR*degitsAmount)
        try:
            console[i] += (SYMBOLS["%"][i])
        except:
            continue
    # insert massage to the center ("Score: ")
    middle = len(console)//2
    copy = console[middle]
    console[middle] =  MASSAGE+copy[len(MASSAGE):] # copy[len(MASSAGE):] - in copy we have spaces and with this способ we delete them

    # ravnoAmount = len(console[0])
    # console.insert(0,("="*ravnoAmount))
    # console.append(("="*ravnoAmount))
    console.insert(0," ")
    console.append(" ")
    return console



# class colors:
#     RED = '\033[31m' # red
#     GREEN = '\033[32m' # green
#     ORANGE = '\033[32m'#'\033[33m' # orange
#     BLUE = '\033[35m' # blue
#     UNDERLINED = '\033[4m'
#     BOLD = '\033[1m'
#     END = '\033[0m' # simple text (stop colourful text)


# for i in result:
#     print(f"{colors.BOLD}{colors.BLUE}{i}")


# print(f"{colors.SOMECOLOR}text of {colors.END}")
