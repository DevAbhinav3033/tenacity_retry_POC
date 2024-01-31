from tenacity import *
from attempts import log_attempt_number

# Retrying mechanism to stop after 3 retries and also maintain a wait of 1,2,3 sec intervals
@retry(stop=stop_after_attempt(4),wait=wait_incrementing(start=1,increment=1),after=log_attempt_number)
def retry_function(rows):
  for row in rows:
        # If the status code for statement is other than 200 then retry after certain specified delay
        if row[3] != 200:
          raise Exception
        continue