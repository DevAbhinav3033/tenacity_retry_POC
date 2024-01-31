import mysql.connector
from mysql.connector import errorcode
from utils.connection_db import connection
from utils.retry_function import retry_function





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





