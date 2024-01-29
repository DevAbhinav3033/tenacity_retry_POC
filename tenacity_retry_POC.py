import os
from os.path import join, dirname
import mysql.connector
from mysql.connector import errorcode
from tenacity import *
from attempts import log_attempt_number
from dotenv import load_dotenv


# Dotenv configuration for local env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,override=True)


try:
  # MYSQL CONNECTION ESTABLISHMENT using env variables
  cnx = mysql.connector.connect(user=os.getenv("USER"),
                                password=os.getenv("PASSWORD"),
                                host=os.getenv("HOST"),
                                port=os.getenv("PORT"),
                                database=os.getenv("DATBASE"))
  # creation of cursor
  cursor=cnx.cursor()
  

  # Retrying mechanism to stop after 3 attempts and also maintain a wait of 1,2,3 sec intervals
  @retry(stop=stop_after_attempt(4),wait=wait_incrementing(start=1,increment=1),after=log_attempt_number)
  def fun():
    # raise Exception
    # Fetch data from central db using cursor
    query='select * from statements_status limit 10'

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
      # If the status code for statement is other than 200 then retry after certain specified delay
      if row[3] != 200:
        raise Exception
      continue
        
    
    
  try:
    fun()
  except Exception as e:
    print(e)
# Code for handling the DB connection errors
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

else:
  cursor.close()
  cnx.close()


