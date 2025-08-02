import fitz    # pip install pymupdf
import re
import json

doc = fitz.open("LenderFeesWorksheetNew.pdf")

page1 = doc[0]

text = page1.get_text("text")
print(text)

loan_amount = re.search(r"\$\s*([\d,]+(?:\.\d+)?)",text)

words = page1.get_text("blocks")

bbox = page1.search_for("Loan Amount")

arr = []
arr.append({ 
        "text": ("loan_amount", loan_amount.group()),
        "bbox": bbox[0][0:4]
           })

int_rate = re.search(r"[:\s]*([0-9]+(?:\.[0-9]+)?)\s*%", text)


bbox2 = page1.search_for("Interest Rate")

int_rate_s =int_rate.group().strip()

arr.append({ 
        "text": ("Interest Rate", int_rate_s),
        "bbox": bbox2[0][0:4]
           })

filename = "my_data.json"

with open(filename, 'w') as json_file:
        json.dump(arr, json_file, indent=4)
