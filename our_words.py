import openpyxl
words = []
book = openpyxl.open("dictionary1.xlsx",read_only=True)
sheet = book.active
mx= sheet.max_column

for row in range(1,sheet.max_row+1):
    word = sheet[row][0].value
    meaning = sheet[row][1].value
    link = sheet[row][2].value
    words.append((word, meaning, link)) 

while (None, None, None) in words :
    words.remove((None, None, None))
