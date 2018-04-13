try:
    fh=open("Test file",'w')
    fh.write('This was created by Akilan ,so say thanks to Akilan')
    fh.write('\n\nThank you Akilan :)')
except IOError:
    print'Error:can/t ind file or read data'
else:
    print"\n\n\n\n\nWritten content in the file is successfully\n\n\n\n\n\n\n\n"
    fh.close()
