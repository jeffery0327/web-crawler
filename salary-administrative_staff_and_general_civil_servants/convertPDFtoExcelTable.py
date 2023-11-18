from PyPDF2 import PdfReader
import pandas as pd

# Read PDF to String
reader = PdfReader("./web-crawler/salary-administrative_staff_and_general_civil_servants/testData1.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

# print(text)

# Convert String to DataFrame
convert_text = text.split("\n")

COLUMN_NAME = ""
DATA = pd.DataFrame(columns=["類別","職等職稱","月支數額"])
for i,text in enumerate(convert_text):
    if i<2:
        continue
    if text.startswith("註"):
        break
    text = text.lstrip()
    text = text.rstrip()
    data_row = text.split(" ")
    if len(data_row)>2:
        COLUMN_NAME = text.replace(" ","")
        continue
    new_raw = pd.DataFrame({"類別": COLUMN_NAME, "職等職稱": data_row[0], "月支數額": data_row[1]}, index=[i])
    DATA = pd.concat([new_raw,DATA])
print(DATA)

# Write DataFrame to Excel