import os

# new_dir=os.mkdir("Practice")

# os.rmdir("NVIT")

file=open("demo1.txt","r+")
file.seek(0)
file.truncate()
file.close