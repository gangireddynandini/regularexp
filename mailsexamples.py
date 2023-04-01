import re
d="Nandini mail id 34 is nandinigagireddy@gmail.com , Dennis 78 maulid is denni23@gmail.com , Divya  67 mailid is divi@342gail.com"
sp="\S+@\S+"
mails=re.findall(sp,d)
print("mails")
for mail in mails:
    print("\t{}".format(mail))