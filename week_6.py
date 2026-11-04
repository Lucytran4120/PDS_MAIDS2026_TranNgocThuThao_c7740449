file1 = open(r"MyFile1.txt","a")
with open("MyFile1.txt","r") as f:
    data=f.read()
    print(data)
# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
file1 = open("myfile.txt","r+")
print("Output of Read function is ")
print(file1.read())
print()
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
print( "Output of Readline function is ")
print(file1.readline())
print()
file1.seek(0)
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()
# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Today \n")
file1.close()
file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()
# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()
import pandas as pd
import pandas as pd

df = pd.DataFrame({
    'name': ['An', 'Binh', 'Chi', 'Dung', 'Em'],
    'age': [20, 21, 19, 22, 20],
    'class': ['MAIDS1', 'MAIDS1', 'MAIDS2', 'MAIDS2', 'MAIDS1'],
    'math': [8.5, 7.0, 9.2, 6.8, 5.5],
    'english': [9.0, 8.0, 7.5, 6.0, 7.0]
})

print(df)

df.to_excel('data.xlsx', index=False)
print("Saved data.xlsx")

df.to_csv('data.csv')
df = pd.read_csv('data.csv', index_col=0)
df

df.to_excel('data.xlsx')
df = pd.read_excel('data.xlsx', index_col=0)
df


