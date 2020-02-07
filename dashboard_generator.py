import pandas
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
OPTION C: use the os module to detect the names of all CSV files which exist in the "data" directory, 
then display this list to the user and prompt the user to input their selection.
"""


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71


# Look at all of the different files in the directory, determine which are CSV, list them.
fileNames = os.listdir(path=".")
csvNames = []

# Get a list of file names
for fileName in fileNames:
    if(len(fileName.split(".")) > 1):
        if(fileName.split(".")[1] == "csv"):
            csvNames.append(fileName)

# List all of the files that are available and associate a number to them
print("Enter the number of file you would like to process: ")
i = 0
while i < len(csvNames):
    print("   " + str(i) + ": " + csvNames[i])
    i += 1

selectedFileIndexInput = 'a'  # making it a character so the while loop runs
selectedFileIndex = -1  # same as above

# Error checking for input selection. Making sure it is a digit and within range
while not selectedFileIndexInput.isdigit() or selectedFileIndex < 0 or selectedFileIndex > len(csvNames)-1:
    selectedFileIndexInput = input("Selection: ")

    if(selectedFileIndexInput.isdigit()):
        selectedFileIndex = int(selectedFileIndexInput)
        if(selectedFileIndex >= 0 and selectedFileIndex < len(csvNames)-1):
            break
        else:
            print("Please enter a valid digit.")
    else:
        print("Please enter a valid digit.")

# Take the index and create a pandas csv object
selectedFile = pandas.read_csv(os.path.join(
    os.getcwd(), csvNames[selectedFileIndex]), parse_dates=['date'])

# Extract month and year from the first item in the CSV file
MONTH = selectedFile['date'].tolist()[0].strftime("%B")
YEAR = str(selectedFile['date'].tolist()[0].year)

# Title
print("-----------------------")
print("REPORTING PERIOD: " + MONTH + " " + YEAR)

# Total monthly sales
print("Total Revenue: ", to_usd(selectedFile['sales price'].sum()))

print("-----------------------")
print("CRUNCHING THE DATA... \n")

# Calculation
topProducts = selectedFile.groupby(['product']).sum().sort_values(
    ['sales price'], ascending=False).reset_index().drop(['unit price', 'units sold'], 1).head(5)

# Create a copy to preserve pricing data for viz
topProductsViz = topProducts.copy()

topProducts['sales price'] = topProducts['sales price'].map(
    lambda a: to_usd(float(a)))  # Change Sales Price into USD

template = "|{0:<30}|{1:<30}"
print("TOP 5 SALES FOR", MONTH, YEAR)
print(template.format("PRODUCT", "PRICE"))

for index, row in topProducts.iterrows():
    print(template.format(str(int(index) + 1) + ") " +
                          row['product'], row['sales price']))

print('\n VISUALIZATION OF TOP SALES')

# Create the plot and give it a title
topProductPlot = topProductsViz.plot.bar(
    x="product", y="sales price", title="Monthly Sales for " + MONTH + " " + YEAR)

# Format the ticks so that they are USD instead of just plain numbers  
topProductPlot.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%1.2f'))
topProductPlot.tick_params(labelrotation=0.5, grid_alpha=0.3)

#Maximize the window
plt.grid()
plt.show()

# Chart[Stacked Bar Chart]y

# Determine Top 5 selling products overall
# Determine sale amount for each month
# Chart with top selling products of the entire period [Bar Chart]
# Plot each item as a line over the months [Line Graph]


# print("-----------------------")
# print("TOTAL MONTHLY SALES: $12,000.71")

# print("-----------------------")
# print("TOP SELLING PRODUCTS:")
# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# print("-----------------------")
# print("VISUALIZING THE DATA...")
