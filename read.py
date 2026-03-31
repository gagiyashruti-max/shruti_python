src=open("1.txt","r")
data=src.read()
src.close()

dst=open("bit.txt","w")
dst.write(data)
dst.close()
print("file copied succesfully.")
