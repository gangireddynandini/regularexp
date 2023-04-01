import re
mno=input("enter mobil number:")
if(len(mno)==10):
    res=re.search("98\d{8}",mno)
    if(res!=None):
        print("valid")
    else:
        print("dont enter strs and spl symbols")
else:
    print("invalid")
