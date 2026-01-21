d1={"albert":50,"john":40,"edward":90}
key=input("enter student's name: ")
if key in d1.keys():
     print(key,"'s mark is ",d1[key])
else:
     print("not found")

