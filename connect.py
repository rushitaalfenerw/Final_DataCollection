from pymongo import MongoClient

# Replace with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")

try:
    # Test the connection by listing databases
    databases = client.list_database_names()
    print("Connected successfully!")
    print("Databases:", databases)
except Exception as e:
    print("Could not connect to MongoDB:", e)
