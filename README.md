# LearnWords
This is Python repository with program created to help u learn some information especially English irregular verbs. 

## Add new alot of words to the dictionary 
+ get document with irrugular worbs in whitch you must have this strucure : V1 V2 V3 translation
+ than you shold to copy this document , run this programm , input your coppied document
+ than in console you will see ready object
+ copy and paste it into your programm

```javascript
let obj = {}

let arr = prompt("arr:");
let res = arr.replace(/ /g, "").split('\n')

for(let i = 0 ; i < res.length; i+=4) {
    obj[ res[i+3] ] = `${res[i]} ${res[i+1]} ${res[i+2]}`
}
console.log("+++++++++++++++++++++++++")
console.log(obj)
# 
```



## =======APP LEARN WORDS=====
- this programm was made to help you learn irregular verbs
YOU CAN ENTER DATA DIFFERENT:
+ if 3 froms of the verb is the same you can enter  "V1 = =" or "V1 V2 ="
+ if 2 and 3 from of the verb is the same you can enter  "V1 V2 ="
+ if 3 froms of the verb is different you can enter "V1 V2 V3" but
    + if this forms is different by some letters you can enter "V1 letter letter"
    + for example (stink stank stunk - вонять ) stink a u
    + for example (dream dreamt dreamt ) dream t t
    + for example (sew sewed sewn) sew sewed n
    + MY PRIDE: (sew sewed sewn) sew ed n (maiun logic in compare and comment:3 froms different)


### SOURCES
colourful text - https://habr.com/ru/post/119436/
another wariant to get colored text
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
