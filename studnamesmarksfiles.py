import re
with open("namesmarklistex.py","r") as fp:
    filedata=fp.read()

    names=re.findall("[A-Z][a-z]+",filedata)
    marks=re.findall("\d{2}",filedata)
    print("\tName\tmarks")

    for n,m in zip(names,marks):
        print("\t{}\t.format(n,m)")


