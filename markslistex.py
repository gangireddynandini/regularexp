import re
d="Nandini mail id 34 is marks, Dennis 78 marks, Divya  675 ,divya got 56 marks"
sp="\d{2}"
marks=re.findall(sp,d)
print("marks")
for m in marks:
    print("\t{}".format(m))