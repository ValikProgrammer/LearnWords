# Get started
```bash
git clone https://github.com/ValikProgrammer/LearnWords
cd LearnWords/console
python3 main.py
```
# APP LEARN WORDS
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
## To Do
+ в файле writeData добавить возможность нескольких ответов 
    + так же прописать это в коде в repeatWords (programmWord это будет массив а не слово и программа должна пробегаться по массиву и сравнивать каждый раз)
    + например возможные ответы:
        + 65
        + 65%
+ везде где есть выбор нужно добавить цикл  while который будет проверять реально ли можно выполнить эту опцию или это ошибка
    + возможно еще нужно будет добавить try , except
    + ```python
        choose = input("Some text")
        try :
            choose = int(choose)
        except:
            print("you entered wrong number. try againg")

    ```
--------
+ создать обьект с принтами там будет ключи и значения Напримр
	+ inputDictionary : Choose dictionary ,,,,,,,
+ подкорректировать print() там где просто написано [0-num] ghbdzpfnm 'nj r lkbyyt vfccbdf'
+ печататьть числа по размерам
+ clear console - https://www.delftstack.com/howto/python/python-clear-console/
+ [***VERY inportant***] to know how to change the version of the project and how to name this version for exfmple "Repeating And Writing Is working"

## GITHUB
## Github push

<!--+ git clone https://github.com/ValikProgrammer/LearnWords   -->
+ git pull (very important - to get changes from github)
+ git add . 
+ git commit
    + to the end of the file
    + press ctrl+O (letter "o")
    + press enter
    + press ctrl+x
+ git push
    + username
    + token

### Sumoory

## tutorial of github 
+ SOURCE : https://itproger.com/course/git/
### git config
-- global это глабально , если ничего не писать то быдет локально
```bash

~ ❯ git config --global user.name ValikProgrammer                                                                 17:09:54
~ ❯ git config --global user.email ValikProgrammer@gmail.com                                                      17:10:34
~ ❯ git config user.name                                                                                          17:11:04
ValikProgrammer
~ ❯ git config user.email                                                                                         17:11:15
ValikProgrammer@gmail.com
~ ❯     

```
### .gitignore
+ add file .gitignore and write files that will be ignored in git add command
```
moNotes.md
*.txt
folder/ - игнорирование всей дирректории
```


### commands
#### working with files
+ git add - добавление файлов в стадию ожидания;
    + чтоб добавить сразу все пиши git add . или git add -A
    + что добавить файлы с определенным разрешением git add *.html
+ git restore [file] - restore changes (get changes from remote repository)
+ git rm - отмена действий.
    + -cached "file"

#### Versions
+ git log --oneline - получить список всех коммитов
+ git checkout [id] - посмотреть проект на стадии кокого -то комита

+ git revert id - отменить коммит
+ git reset id --hard - удалить коммит

#### Branches
+ git branch [name] - create a branch
+ git checkout [name] - switch to branch with 
    + git checkout master - switch to main branch

#### Working with remove repository
+ git remote add origin [url] - связываем локальныйф репозиторий с удаленным
+ git push [имя удаленного репозитория] [branch name]
    + git push origin master

+ git pull [имя удаленного репозитория] [branch name] - information about changes
    + git pull origin master

+  git clone [url] - clone repository
#### Other
+ git status - get status
+ git commit - добавление файлов в локальное хранилище
    + -m "comment"



##### USUAL Set

<!--+ git clone https://github.com/ValikProgrammer/LearnWords   -->
+ git pull (very important - to get changes from github)
+ git add . 
+ git commit
    + to the end of the file
    + press ctrl+O (letter "o")
    + press enter
    + press ctrl+x
+ git push
    + username
    + tocken
    + 
### SOURCES
colourful text - https://habr.com/ru/post/119436/
another wariant to get colored text
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
