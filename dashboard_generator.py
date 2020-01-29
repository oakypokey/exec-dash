import pandas
import os
import csv

"""
OPTION C: use the os module to detect the names of all CSV files which exist in the "data" directory, 
then display this list to the user and prompt the user to input their selection.
"""

#Look at all of the different files in the directory, determine which are CSV, list them.
fileNames = os.listdir(path=".")
csvNames = []

#Get a list of file names
for fileName in fileNames:
    if(len(fileName.split(".")) > 1):
        if(fileName.split(".")[1] == "csv"):
            csvNames.append(fileName)

#List all of the files that are available and associate a number to them
print("Enter the number of file you would like to process: ")
i = 0
while i < len(csvNames):
    print("   " + str(i) + ": " + csvNames[i])
    i += 1

selectedFileIndexInput = 'a' #making it a character so the while loop runs
selectedFileIndex = -1 #same as above

#Error checking for input selection. Making sure it is a digit and within range
while not selectedFileIndexInput.isdigit() or selectedFileIndex < 0 or selectedFileIndex > len(csvNames)-1:
    selectedFileIndexInput = input("Selection: ")

    if(selectedFileIndexInput.isdigit()):
        selectedFileIndex = int(selectedFileIndexInput)
        if(selectedFileIndex > 0 and selectedFileIndex < len(csvNames)-1):
            break
        else:
            print("Please enter a valid digit.")
    else:
        print("Please enter a valid digit.")

#Take the index and create a pandas csv object
selectedFile = pandas.read_csv(os.path.join(os.getcwd(), csvNames[selectedFileIndex]))

#Printing the object for testing
print(selectedFile)

# print("-----------------------")
# print("MONTH: March 2018")

# print("-----------------------")
# print("CRUNCHING THE DATA...")

# print("-----------------------")
# print("TOTAL MONTHLY SALES: $12,000.71")

# print("-----------------------")
# print("TOP SELLING PRODUCTS:")
# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# print("-----------------------")
# print("VISUALIZING THE DATA...")