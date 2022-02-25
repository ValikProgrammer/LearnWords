def getResult(SCORE,MASSAGE="Score: ",):
    
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
        ],
        "1" : [
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
        ],
        "2" : [
            "#####",
            "    #",
            "#####",
            "#    ",
            "#####",
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
            "###   /",
            "# #  / ",
            "### /  ",
            "   /   ",
            "  / ###",
            " /  # #",
            "/   ###",
        ],
    }
    
    degitsAmount = len(SCORE)

    standartCharSize = len(SYMBOLS["0"])# 5 
    anotherCharSize = len(SYMBOLS["%"])# 7

    indexToStart = 1
    indexToEnd = max(anotherCharSize,standartCharSize) - indexToStart # 6
    console = []

    # append lines to the result output (amount of lines == anotherCharSize)
    middle = anotherCharSize//2
    for i in range (0,max(anotherCharSize,standartCharSize)):
        if (i == middle):
            console.append(MASSAGE)
            continue
        console.append(" "*len(MASSAGE))

    # print digits in standar size lines
    for digit in (SCORE):
        for i in range (0,standartCharSize):
            console[i+indexToStart] += (SYMBOLS[digit][i] + SEPERATOR)

    # print BIG "%" in big size
    for i in range (0,len(console)):
        # put spaces where neccssary (where was not digits)
        if (i < indexToStart or i >= indexToEnd ):
            console[i] += " "*( ( standartCharSize + len(SEPERATOR) ) *degitsAmount)
        console[i] += (SYMBOLS["%"][i])
    console.append("")
    # for line in console:
    #     print(line)
    return console

