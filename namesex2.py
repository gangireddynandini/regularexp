import re
with open("mailsexamples.py","r") as fp:
    filedata=fp.read()
    mails=re.findall("\S+@\S+",filedata)
    names=re.findall("[A-Z][a-z]+",filedata)
    print("\tNames\tmails")
    for name,mail in zip(names,mails):
        print("\t{}\t{}".format(name,mail))