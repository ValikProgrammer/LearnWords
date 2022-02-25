# https://github.com/lamerman/shellpy
# https://habr.com/ru/post/277679/
def PRINT_MASSAGE(NAME):
    M = {
        "TEST" : {
            f"first option":"""
print('first')
print('first')""",

            "second option":"print('hello')"
         } ,
    }
    keys = list( M[NAME].keys() )
    for i in range(0,len(keys)):
        print(f"[{i}] : {keys[i]}")
    return M[NAME]

OPTIONS = PRINT_MASSAGE("TEST")
keys = list( OPTIONS.keys() )
key = keys [0] # """ int(input("0-1:")) """

action = OPTIONS[ key ]

eval(action)
