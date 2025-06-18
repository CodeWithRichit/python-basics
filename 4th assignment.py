#Task1:Read a file and handle errors
file1=open('sample.txt','w')
file1.write("This is a sample text file. \nIt contains multiple lines. \n")
file1.close()

file=open('sample.txt','r')
content=file.read()
print(content)
file.close()
try:
    file2=open('sample.tx','r')
    Content=file2.read()
    print(Content)
    file2.close()

except FileNotFoundError:
    print('Error:The file does not exist')
finally:print('Continue,ahead')

#Task2:Write and Append data to a file
command=input('Enter something to write in the file: ')
file3=open('output.txt','w')
value=file3.write(command+'\n')
file3.close()
order=input('enter additional text to append: ')
file3=open('output.txt','a')
value1=file3.write(order+'\n')
file3.close()
file3=open('output.txt','r')
val=file3.read()
print(val)
file3.close()

