#Data Processing

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["user_data"]
collection = db["users"]

# Fetch data from MongoDB
data = list(collection.find())

# Check if data was retrieved
if data:
    print("Data retrieved successfully")
else:
    print("No data found in the collection")
import pandas as pd

if data:  # Proceed if data is not empty
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Remove MongoDB's default `_id` field if it’s included
    if '_id' in df.columns:
        df = df.drop(columns=['_id'])
    
    # Save to CSV
    df.to_csv("user_data.csv", index=False)
    print("CSV file created successfully")
else:
    print("No data to save")
df = pd.read_csv("user_data.csv")
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Visualize age groups with highest income
sns.boxplot(x="age", y="income", data=df)
plt.title("Income by Age")
plt.show()

# Visualize gender distribution across spending categories
sns.barplot(x="gender", y="healthcare", data=df)
plt.title("Healthcare Spending by Gender")
plt.show()

# Export charts
plt.savefig("income_by_age.png")
plt.savefig("healthcare_spending_by_gender.png")