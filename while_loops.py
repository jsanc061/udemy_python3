num=1
while num<=5:
    print(num)
    num=num+1
    
# allow user to quit input entry
txt="This is a parrot program\n"
txt=txt+ "Enter 'end' to quit the program."
msg=""
while msg != 'end':
    msg=input(txt)
if msg != 'end':
    print(msg)
    
# using a flag variable
txt="This is a parrot program\n"
txt=txt+ "Enter 'end' to quit the program."
flag=True
while flag:
    msg=input(txt)
    if msg=='end':
        flag=False
    else:
        print(msg)