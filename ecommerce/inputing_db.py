import csv
from cs50 import SQL
db = SQL("sqlite:///items.db")
table={}
with open(r"C:\Users\USERPC\Documents\sample.csv") as file:
    reader = csv.DictReader(file)
    for i in reader:
        db.execute("INSERT INTO items (name, path, price, quantity, description) VALUES(?,?,?,?,?)",
                   i["Name"], i["Address"], i["Price"], i["Quantity"], i["Description"])