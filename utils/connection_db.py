import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Dotenv configuration for local env file
dotenv_path = join(dirname(__file__), '/Users/abhinav.yadav/Desktop/Tenacity tutorial/.env')


# MYSQL CONNECTION ESTABLISHMENT using env variables
def connection():
    load_dotenv(dotenv_path,override=True)
    cnx = mysql.connector.connect(user=os.getenv("USER"),
                                password=os.getenv("PASSWORD"),
                                host=os.getenv("HOST"),
                                port=os.getenv("PORT"),
                                database=os.getenv("DATABASE"))
    return cnx