

def getMassage(NAME="ERROR",DATA=0,i=0,NUM=0):
  MASSAGES = {
        "TEST"         :["  {DATA[i]} {NUM} {DATA[i]-NUM}"],
        "TEST2"        :[]
    }
  return MASSAGES[NAME]



def PRINT_MASSAGE(FILE="TEMPLATES",NAME="ERROR",DATA=[0],NUM=0):

  output = []
  i = 0

  for i in range(0 , len(DATA)):
    test = (getMassage(NAME=NAME,DATA=(DATA[i]),i=i,NUM=[NUM]))[0]
    # s = test.format(DATA[i],NUM)
    s = f"f'{test}'"
    s = eval(s)
    output.append(s)
  for j in range(0,len(output)):
    print(output[j])


    # for el in output[j]:
    #   print(el)
#   return getMassage(FILE=FILE,NAME=NAME,DATA=DATA[i],i=i,NUM=NUM)
PRINT_MASSAGE(NAME="TEST",DATA=[3],NUM=2)