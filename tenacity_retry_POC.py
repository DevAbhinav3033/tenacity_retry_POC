import mysql.connector
from mysql.connector import errorcode
from tenacity import *
from attempts import log_attempt_number
from utils.connection_db import connection



# Retrying mechanism to stop after 3 retries and also maintain a wait of 1,2,3 sec intervals
@retry(stop=stop_after_attempt(4),wait=wait_incrementing(start=1,increment=1),after=log_attempt_number)
def retry_function(rows):
  for row in rows:
        # If the status code for statement is other than 200 then retry after certain specified delay
        if row[3] != 200:
          raise Exception
        continue



def fun():
  cnx=None
  cursor=None
  try:
    # creation of cursor
    cnx=connection()
    cursor=cnx.cursor()
    # Fetch data from central db using cursor
    query='select * from statements_status limit 10'

    cursor.execute(query)
    rows = cursor.fetchall()
    
    retry_function(rows)
      
    
  # Code for handling the DB connection errors   
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  except Exception as e:
    print(e)

  finally:
    if cnx and cnx.is_connected():
      cursor.close()
      cnx.close()

if __name__=='__main__':
  fun()





