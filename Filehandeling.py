""" 
FOLDER
#mkdir -> to create a new folder
#rmdir ->to remove any folder/directory"""
# import os
# os.mkdir("hello")
# os.rmdir("hello")


"""
FILES
x
w
a
r
"""
#MODE 1: x ->just to create the file and if already exist it will give an error back
"""open("garba.txt","x")"""
#MODE 2: w ->we file does not exist this will create one and insert the content inside the file
""" file=open("garba.txt, "w")
file.write("khelo garba khub khelo din raat khelo")

file.write("enjoy kro job hi job hai")#again doing it then if there is any content inside file new one will replace the old one (overwrite)"""
#MODE 3: a ->add the text at last
"""file.write("khelo garba khub khelo din raat khelo")
file.write("enjoy kro job hi job hai")
file.write("/n this ,messge is deleted)"""

#MODE 4: r ->read the content inside of the file
"""file=open("garba.txt","r")
print(file.read())"""
##closing thing
"""1.file.close()->used to close file to avoide third party interference (par ese baar baar likhne hoga)
   2. with open("sample.txt","w") as file:
           file.write("this is new file")
           (es main baar baar nahi likhna open close with ke thourgh apne ap hoga)
"""
#CRUD - creat, read,update,delete
"""os.remove("garba.txt")
print("press 1 for creating a new file:")
print("press 2 for reading a new file:")
print("press 3 for updating a new file:")
print("press 4 for deleting a new file:")"""


