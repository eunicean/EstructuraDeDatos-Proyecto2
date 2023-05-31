import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from flask import Flask,jsonify,request,render_template,redirect,url_for,session

# Load environment variables from .env file
load_dotenv()



# Access environment variables
neo4j_uri = os.getenv('NEO4J_URI')
neo4j_user = os.getenv('NEO4J_USER')
neo4j_password = os.getenv('NEO4J_PASSWORD')

# Create a driver object
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# Create a Flask application
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

# Connect to the database
with driver.session() as session:
    # Perform database operations
    result = session.run("MATCH (n) RETURN count(n) AS nodeCount")
    print(result.single()["nodeCount"])

# Close the driver
driver.close()