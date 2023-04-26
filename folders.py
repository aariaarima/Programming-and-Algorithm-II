import os 

#WAP to create a repository or directory.

os.mkdir("garima")
os.makedirs("C:\Users\Asus\Desktop\Python\Garima")
#if not supported you can use double slash \\

#WAP to rename an existing directory.
os.rename("garima", 'shrestha')
os.renames("garima", 'shrestha')

#WAP to delete the directory
os.rmdir("shrestha")
os.removedirs("shrestha")