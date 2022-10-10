# class myWord:
#     def __init__(self,pw,pt):
#         self.pw = pw
#         self.pt = pt
#         # self.ut = ut

#     def compare (self):
#         print(f"compare : {self.pw} , {self.pt} , {self.ut}")
#         # print(attr12)
#         if self.pt.lower().strip() ==  self.ut.lower().strip():
#             return "YES"
#         return "NO"

    

# def func1(pw,pt):
#     global word
#     word = myWord(pw,pt)
#     print("func1 Ended")

# def func2():
#     ut = "bla-bla"
#     word.ut = ut
#     res = word.compare()
#     print("res = ",res)

# def main() :
#     for i in range(0,3):
#         func1(f"programmword{i}",f"programmTrans{i}")
#         func2()


# main()




for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"

def func():
    print(variable12)

func()