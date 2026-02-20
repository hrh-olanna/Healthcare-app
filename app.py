from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_application"]
collection = db["user_details"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = {
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "total_income": float(request.form["income"]),
            "utilities": float(request.form.get("utilities_amt", 0) or 0),
            "entertainment": float(request.form.get("entertainment_amt", 0) or 0),
            "school_fees": float(request.form.get("school_fees_amt", 0) or 0),
            "shopping": float(request.form.get("shopping_amt", 0) or 0),
            "healthcare": float(request.form.get("healthcare_amt", 0) or 0),
            "created_at": datetime.utcnow()
        }

        collection.insert_one(user_data)
        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)