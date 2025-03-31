import requests
from zipfile import ZipFile
import json
from openpyxl import Workbook
from openpyxl.worksheet.table import Table

BOOTSTRAP_VERSION = "1.11.3"
BOOTSTRAP_URL = f"https://github.com/twbs/icons/releases/download/v{BOOTSTRAP_VERSION}/bootstrap-icons-{BOOTSTRAP_VERSION}.zip"

r = requests.get(BOOTSTRAP_URL)
with open("bootstrap_icons.zip", "wb") as f:
    f.write(r.content)

contents = []
with ZipFile("bootstrap_icons.zip") as zip:
    with zip.open(f"bootstrap-icons-{BOOTSTRAP_VERSION}/font/bootstrap-icons.json") as file:
        contents = json.load(file).keys()


wb = Workbook()
ws = wb.active

data = []
header = ["name", "svg", "library", "library_version"]
ws.append(header)
with ZipFile("bootstrap_icons.zip") as zip:
    for icon_name in contents:
        with zip.open(f"bootstrap-icons-{BOOTSTRAP_VERSION}/{icon_name}.svg") as file:
            data.append([icon_name, file.read(), "bootstrap", BOOTSTRAP_VERSION])

for row in data:
    ws.append(row)

table = Table(displayName="bootstrap", ref=f"A1:D{len(data) + 1}")
ws.add_table(table)
wb.save("icons.xlsx")
