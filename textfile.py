import os
def appendtotxt(data_list, file_name, torf):
    file1 = open(file_name, "a")
    if torf == True:
        file1.write(data_list + '\n')
    else:
        file1.write(data_list)



    print("WRITTEN TO FILE")
def read_file(file_name):

    filep = str(os.path.abspath(os.getcwd()))
    file_path = filep.split("\\")[0] + chr(92) + filep.split("\\")[1]


    file1 = open(filep + "\\" + file_name, "r").readlines()
    return file1
