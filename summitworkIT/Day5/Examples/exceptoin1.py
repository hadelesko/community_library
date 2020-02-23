try:
    #fh = open("testfile1", "r")
    #fh.write("This is my test file for exception handling!!")
    print("hello")
except IOError:
    print("Error: can\'t find file or read data")
    # we can convery , handle the exception
    # we can rollback(), update 
else:
    print("Written content in the file successfully")
    #fh.close()
print("hello, i am last line of the program")