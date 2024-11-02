Healthcare User Data Collection and Analysis

Project Overview

This Python project offers a web application designed to collect user data on income and spending habits in the healthcare sector. The collected information is stored in a MongoDB database, processed for further analysis, and finally visualized using Matplotlib and Seaborn libraries.

Project Structure

FlaskApp.py: Defines a Flask web application to collect user data through a web form.
Connect.py: Establishes a connection to the MongoDB database and verifies its functionality.
Dataform.html: Provides the HTML template for the data collection web form.
Dataprocess.py: Handles retrieving data from MongoDB, converting it to a Pandas DataFrame, creating a CSV file, and generating basic data visualizations.
Prerequisites

Python 3.x (with Flask, pymongo, pandas, matplotlib, and seaborn libraries installed)
MongoDB database (installed and running locally or on a remote server)
Setting Up

Install Required Libraries:
Use pip install flask pymongo pandas matplotlib seaborn in your terminal.

Configure MongoDB Connection (FlaskApp.py):
Replace mongodb://localhost:27017/ with your actual MongoDB connection string, including the hostname, port number, database name, and authentication credentials (if required).

Start the Application:
Navigate to the project directory in your terminal and run python FlaskApp.py. This launches the web application at http://localhost:5002 (default port).

Using the Application

Access the Web Form:
Open the web application in your browser at http://localhost:5002.

Fill Out the Form:
Enter the user's age, gender, income, and individual spending categories (utilities, entertainment, school fees, shopping, healthcare).

Submit Data:
Click the "Submit" button to save the user's data to the MongoDB database.

Data Processing and Visualization (Dataprocess.py):

Running Dataprocess.py:
Execute python Dataprocess.py from your command line to retrieve data from MongoDB, create a CSV file, and perform basic visualizations.

CSV File:
The script will generate a CSV file named user_data.csv containing the collected user data.

Visualizations:
The script creates two visualizations:

income_by_age.png: Shows income distribution across age groups (boxplot).
healthcare_spending_by_gender.png: Visualizes healthcare spending based on gender (bar chart).