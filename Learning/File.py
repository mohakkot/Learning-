def file_write(file_name):
    fw = open(file_name, 'w')
    fw.write ('This is my first program of file \n')
    fw.write ('hope it works fine')
    fw.close()

def file_read(file_name):
    fr = open(file_name, 'r')
    lines = fr.read()
    line1 = str(lines)
  # line1 = lines.split(:\\n")
    print(lines)
    print (line1)
