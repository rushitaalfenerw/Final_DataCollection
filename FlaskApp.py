from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  
db = client["user_data"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect user data from the form
        age = request.form["age"]
        gender = request.form["gender"]
        income = request.form["income"]
        expenses = {}
        for category in ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]:
            expenses[category] = request.form[category]
        
        # Insert data into MongoDB
        user_data = {
            "age": age,
            "gender": gender,
            "income": income,
            "expenses": expenses
        }
        collection.insert_one(user_data)
        
        # Redirect to a success page or display a confirmation message
        return "Data submitted successfully!"
    
    return render_template("dataform.html")

if __name__ == "__main__":
    app.run(debug=True, port=5002)





