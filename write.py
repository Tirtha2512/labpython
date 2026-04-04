#write()-write a single string
f=open("one.txt","w")
f.write("hello students\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun.\n")
f.close()

#example 2
f=open("one.txt","w")
f.write("new content only.\n")
f.close()

#example 3
f=open("one.txt","a")
f.write("this line is added at the end.\n")
f.close()

#writelines()-write multiple lines
f=open("one.txt","w")
line=[
    "python programing\n"
    "file handaling\n"
    "error handaling\n"
    "exception handaling\n"
]
f.writelines(line)
f.close()

