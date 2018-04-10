import pypyodbc as odbc
from contextlib import contextmanager


# This is the perfered method to create a context manager.
# # There is already a module created to be used 
# # you just have to know how to use it.
# # # Much simpler syntax.
@contextmanager
def open_file(file, mode):
    print("opening file")
    try:
        myFile = open(file,mode)
        yield myFile
    finally:
        print("closing file")
        myFile.close()


# @contextmanager
# def read_line(file):
#     print("Reading file",file)
#     try:
#         myFile = open(file,"r")
#         yield read_line_gen(myFile)
#     finally:
#         print("Closing File:",file)
#         myFile.close()


def read_line(file):
    with open_file(file,"r") as fileObj:
        while True:
            data = fileObj.readline()
            if not data:
                break
            yield data


# Opening file for the first time.
# # Creating the file
with open_file("tempWrite.txt", 'w+') as outFile:
    for i in range(10):
        outFile.write("writing something: {}\n".format(i+1))

# Opening file for the second time.
# # Thought i was appending, but actually just writing over the file
with open_file("tempWrite.txt", 'w+') as outFile:
    for i in range(10):
        outFile.write("writing something: {}\n".format(i+1))

# Opening file for the third time
# # Actually appending to file
with open_file("tempWrite.txt", 'a') as outFile:
    for i in range(10):
        outFile.write("Appending something: {}\n".format(i+1))



for line in read_line("tempWrite.txt"):
    print("Print Line: {}".format(line))



# with read_line("tempWrite.txt") as lines:
#     for line in lines:
#         print("Print Line: {}".format(line))



# This didn't give me a for loop in writing lines.
# # Only slightly thought it would but expected it to break
# with read_line("tempWrite.txt") as line:
#     print("Print Line: {}".format(line))
