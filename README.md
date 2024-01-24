
# Tenacity retry POC

It is used to introduce retry mechanism to a function in case it fails due to some error or exception


## Features

- Connect to the MYSQL database
- retry the function based on the condition and raise the exception (tenacity_retry_POC.py)
- refer to attempts.py for getting the log details
- look into the myapp.log file to see the printed logs for the output of the code


## Lessons Learned

Learned about tenacity retry with incremental waits and connection to the database using MYSQL connection object


## Run Locally

Clone the project

```bash
  git clone https://github.com/DevAbhinav3033/tenacity_retry_POC.git
```

Go to the project directory

```bash
  cd tenacity_retry_POC
```

Install dependencies

```bash
  pip install
```

Run the file

```bash
  python tenacity_retry_POC.py
```

