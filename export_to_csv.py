import csv
from pymongo import MongoClient
from models import User

client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_application"]
collection = db["user_details"]

output_path = r"C:\Projects\Flask Healthcare Application\data\healthcare_data.csv"

with open(output_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Age", "Gender", "TotalIncome",
        "Utilities", "Entertainment",
        "SchoolFees", "Shopping", "Healthcare"
    ])

    for doc in collection.find():
        user = User(
            doc.get("age"),
            doc.get("gender"),
            doc.get("total_income"),
            doc.get("utilities"),
            doc.get("entertainment"),
            doc.get("school_fees"),
            doc.get("shopping"),
            doc.get("healthcare")
        )
        writer.writerow(user.to_list())

print("CSV Export Completed.")
