

k = int (input())
d = int (input())
n = int (input())
m = int (input())
l = int (input())

input = [k,d,n,m]

arr = []
for i in range(1,l+1):
  arr.append(i)

#print(arr)


for i in input :
  if (i == 1):
    arr = []
    break;
  for el in arr:
    if el % i  == 0 :
      arr.remove(el)

print(l - len(arr))



def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesBLUE = 0
  print(f"BLUE of all words:{colors.BLUE}{len(keys)}{colors.END}") 
  return [i , mistakesBLUE , keys  , arrNumbersRandomSorted]
randomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesBLUE = 0
  print(f"BLUE of all words:{colors.BLUE}{len(keys)}{colors.END}") 
  return [i , mistakesBLUE , keys  , arrNumbersRandomSorted]