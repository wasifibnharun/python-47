file1=open("demo1.txt","w")
file1.write("Wasif Ibn Harun")
file1.close()


file1=open("demo1.txt","a")
file1.write(" is my name")
file1.close


file2=open("demo1.txt","r")
read_content=file2.read()
print(read_content)
file2.close