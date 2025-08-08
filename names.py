import secrets
import string
#get names from file

with open("cool_name.txt","r+") as f :
    global strlist
    strlist=[]
    for line in f.readlines():
        str_filter=str(line.replace("\n",""))
        strlist.append(str_filter)


 
 
int_ran=secrets.randbelow(999)

#print(int_ran)
#gen cool name
strlist.sort()
ran_names=secrets.choice(strlist)
ran_names2=secrets.choice(strlist)
print(ran_names,ran_names2,int_ran)