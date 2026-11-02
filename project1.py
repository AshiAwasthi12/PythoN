#CRUD - create, read,update,delete
from pathlib import Path  #pathlib is a library
import os
def create_folder():
    name=input("tell your folder name:-")
    p=Path(name)

    if p.exists():
        print("this folder name already exist please try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully!")

def read_folder():
    p=Path("") #empty string gives path of folder you are currently using
    names=list(p.rglob("*"))

    for i in range(len(names)):
        print(f"{i+1}:{names[i]}")

def update_folder():
    read_folder()
    name=input("which folder you want to update:-")
    old_p=Path(name)

    if old_p.exists():
        new_name=input("tell new folder name:-")
        new_p=Path(new_name)
        old_p.rename(new_p)
        print("folder name changed succsessfully")
    else:
        print("no such folder exist please try again")
        update_folder

def delete_folder():
    name=input("tell your folder name:-")
    p=Path(name)

    if p.exists():
       p.rmdir()
       print("folder deleted successfully")
    else:
       print("no such folder exists please try again")
       delete_folder

def create_file():
    name=input("tell your file name with extension")
    p=Path(name)
    if p.exists():
        print("this folder name alredy exists please try again")
        create_file
    else:
        with open(p,"w") as file:
            data=input("write anything you want")
            file.write(data)
            print("succeseefly")

def read_file():
    name=input("tell your file name with extension")
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data=file.read()
            print("/n/n/nYour file data is/n/n/n")
            print(data)

def delete_file():
    name=input("tell your file name with extension")
    p=Path(name)

    if p.exists():
        os.remove(p)
        print("file deleted successefully")
    else:
        print("no such file exists please try again")
        delete_file()

    

print("press 1 for creating a new folder:")
print("press 2 for reading a new folder:")
print("press 3 for updating a new folder:")
print("press 4 for deleting a new folder:")
print("press 5 for creating a new file:")
print("press 6 for reading a new file:")
print("press 7 for updating a new file:")
print("press 8 for deleting a new file:")
res =int(input("tell your response:-"))
if res==1:
    create_folder()

if res==2:
    read_folder()

if res==3:
    update_folder()
if res==4:
    delete_folder()
if res==5:
    create_file()
if res==6:
    read_file()
if res==8:
    delete_file()

