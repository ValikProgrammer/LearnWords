# https://github.com/lamerman/shellpy
# https://habr.com/ru/post/277679/

# def PRINT_MASSAGE(NAME):
#     M = {
#         "TEST" : {
#             f"first option":"""
# print('first')
# print('first')""",

#             "second option":"print('hello')"
#          } ,
#     }
#     keys = list( M[NAME].keys() )
#     for i in range(0,len(keys)):
#         print(f"[{i}] : {keys[i]}")
#     return M[NAME]

# OPTIONS = PRINT_MASSAGE("TEST")
# keys = list( OPTIONS.keys() )
# key = keys [0] # """ int(input("0-1:")) """

# action = OPTIONS[ key ]

# eval(action)

#=====INSTRUCTION======
# every digit has an array consisting of 5 lines (4 indexes) it is enought to draw the number of any size
# arr[0] : first line
# arr[1] : all lines before middle (but after first line) will be like that
# arr[2] :
# arr[3] : all lines after middle line (but before the last line) will be like that
# arr[4] : last line

    # print("|🌀|\n|--|")
    
# TOP : # $ % @ 0 + ^ V * < :
def test(SCORE="100",SIZE=4,CHAR="#"):
    SCORE = str(SCORE)
    middle = SIZE // 2
    sepBetweenDigits = " "*(SIZE//2)
    sepBetwenChars = " "

    # if (SIZE < 5):
    #     SIZE = 5 
    length = len(CHAR)
    IDoNotKnowHowToNameItButItMeanTheBoldOfResult = 5
    charAmount = SIZE // (length*IDoNotKnowHowToNameItButItMeanTheBoldOfResult)
    if charAmount != 0: CHAR = CHAR*charAmount

    if length < middle:

        s = CHAR * ( SIZE//length )
        t = SIZE - len(s)
        for i in range (0,t):
            s += CHAR[i]
        # s = (CHAR * ( SIZE//length )) + CHAR[(SIZE - (SIZE//length ) ) :]

        F = s                                                     # Filled (#####)
        L = CHAR + sepBetwenChars * (SIZE - (length ))            # Left   (#    )
        R = sepBetwenChars * (SIZE - length ) + CHAR              # Rght   (    #)
        E = CHAR + sepBetwenChars * (SIZE - (2*length) ) + CHAR   # Ends   (#   #)


    else:
        print(f"len of {CHAR} is too big!")
        return []

    SYMBOLS = {

    "0" : [
        f"{F}",
        f"{E}",
        f"{E}",
        f"{E}",
        f"{F}",
    ],
    "1" : [
        f"{R}",
        f"{R}",
        f"{R}",
        f"{R}",
        f"{R}",
    ],
    "2" : [
        f"{F}",
        f"{R}",
        f"{F}",
        f"{L}",
        f"{F}",
    ],
    "3" : [
        f"{F}",
        f"{R}",
        f"{F}",
        f"{R}",
        f"{F}"
    ],
    "4" : [
        f"{E}",
        f"{E}",
        f"{F}",
        f"{R}",
        f"{R}"
    ],
    "5" : [
        f"{F}",
        f"{L}",
        f"{F}",
        f"{R}",
        f"{F}",
    ],
    "6" : [
        f"{F}",
        f"{L}",
        f"{F}",
        f"{E}",
        f"{F}",
    ],
    "7" : [
        f"{F}",
        f"{R}",
        f"{R}",
        f"{R}",
        f"{R}",
    ],
    "8" : [
        f"{F}",
        f"{E}",
        f"{F}",
        f"{E}",
        f"{F}",
    ],
    "9" : [
        f"{F}",
        f"{E}",
        f"{F}",
        f"{R}",
        f"{F}",
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
    
    console = []
    for i in range (0,SIZE+2):
        console.append("")

    # print digits in standar SIZE lines
    for digit in (SCORE):
    # digit = SCORE
        
        if digit == "%":
            arr = test(SCORE=0,SIZE=SIZE//2,CHAR="#")
            print(arr)
            m = (SIZE//2) //2
            print(m,len(arr),SIZE//2)

            for i in range(0,len(arr)):
                print(i)
                char = "/"
                template = f"{arr[i]}{sepBetwenChars * (m-length-i)}{char}"
                console[i] += template
                # print(template)
                # console[len(console)-1-i] += template[::-1]
            # for i in range(len(arr),len(console)):
            #     print(i)
            #     char = "/"
            #     template = f"{arr[middle-i]}{sepBetwenChars * (middle-length-i)}{char}"
            #     console[i] += template
                
                #console += ( arr[i] )#+ sepBetwenChars * (middle-length-1) + CHAR)
            print("=====")
        else:
            for i in range (0,SIZE):

                    if i == 0 : # first line
                        index = 0
                    elif i == middle: # middle line
                        index = 2
                    elif i == (SIZE-1): # last line
                        index = 4

                    elif i < middle: # (firstLine ; middle)
                        index = 1
                    elif i > middle:# ( middle ; lastLine)
                        index = 3
                    console[i] += ((SYMBOLS[digit][index]) + sepBetweenDigits)
    return console

INCORRECT = '\033[31m' # red
CORRECT = '\033[32m' # green
WARNING = '\033[33m'#'\033[33m' # orange
BLUE = '\033[35m' # blue
UNDERLINED = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m' # simple text (stop colourful text)

 # TOP 🌀
# char = input("enter some char : ")
# size = int(input("enter size : "))


# hi = ("✋")
# print("len c :",sys.getsizeof(hi) - sys.getsizeof(""))
# console = test(SIZE=8,SCORE="%",CHAR="#")
console = test(SIZE=15,SCORE="10",CHAR="oskar" )
for line in console:
    print(f"{BOLD}{CORRECT}{line}{END}")

# arr = [1,2,3,4,5,6,7,8,9,0]
# t = 5
# print(arr[0-5])


# arr = input().split(" ")
# # print(arr)
# import sys
# for el in arr:
#     print(f"{el} | {sys.getsizeof(el)}")

# # import sys
# # arr = input().split(" ")
# arr = ['🔥', '💣', '💥', '♻', '🧨', '🤔', '⚠', '🔎', '😘', '❌', '📈', '🍿', '☑', '✅', '🖤', '🧠', '❓', '❗', '®', '✉', '🔒', '§', '©', '☯', '☭', '📹', '🔱', '🎁', '🧢', '📊', '💕', '🤍', '🥱', '🛒', '🦠', '⚡', '🐳', '💰', '🥇', '❤', '️', '🤙', '💪', '😤', '🍋', '😿', '🍒', '🗝', '️', '⌛', '⏳', '🕗', '⌚', '❎']

# arr2 = ['☜', '☞', '☝', '☟', '✍', '☺', '☹', '☻', '😁', '😂', '😃', '😆', '😇', '😈', '😉', '😊', '😋', '😌', '😍', '😎', '😏', '😐', '😒', '🚤', '😓', '😔', '😖', '😘', '😚', '😜', '😝', '😞', '😠', '😡', '😢', '😣', '😤', '😥', '😨', '😩', '😪', '😫', '😭', '😰', '🌏', '🍀', '😱', '😲', '😳', '😵', '😶', '😷', '😸', '😹', '😺', '😻', '😼', '😽', '😾', '😿', '🙀', '🙅', '🙆', '🙇', '🙈', '🙉', '🙊', '🙋', '🙌', '🙍', '🙎', '✋', '✋', '🐲', '👀', '🐝', '💢', '☘', '✌', '∞', '©', '🐾', '💋', '👣', '🚗', '☠', '🚀', '🚃', '🚄', '🚅', '🚇', '🚉', '🚌', '🚏', '🚑', '🚒', '🚓', '🚕', '😄', '😅', '🚙', '🚚', '🚢']
# for el in arr :
#     print(f"{el} | {sys.getsizeof(el)}")
# print("========")
# for el in arr2 :
#     print(f"{el} | {sys.getsizeof(el)}")




# print("=============")

# print(f"|{hi}|\n|--|")
# print(sys.getsizeof(hi))
# print(sys.getsizeof("❎"))

# если больше 76 то это уже как 2 символа почти всегда так работает
# ну если больше 80 то точно 2 символа
