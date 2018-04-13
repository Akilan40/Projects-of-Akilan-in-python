try:
    fh=open("Test file",'w')
    fh.write('This is test file')
except IOError:
    print'Error:can/t ind file or read data'
else:
    print"\n\n\n\n\nWritten content in the file is successfully\n\n\n\n\n\n\n\n"
    fh.close()
