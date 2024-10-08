import openpyxl
words = []
book = openpyxl.open("test.xlsx",read_only=True)
sheet = book.active
mx= sheet.max_column

for row in range(1,sheet.max_row+1):
    word = sheet[row][0].value
    meaning = sheet[row][1].value
    words.append((word, meaning))

while (None, None) in words :
    words.remove((None, None))