import re,sys
lst=[]
while(True):
    mail=input('enter mail:')
    f=re.search('\S+@\S',mail)
    if(f!=None):
        lst.append(mail)
        ch=input('do u want to enter another mail:(y/N)')
        if(ch.lower()=='no'):
            print('thnx')
            sys.exit
        else:
            print(lst)
    print('invalid mail')

