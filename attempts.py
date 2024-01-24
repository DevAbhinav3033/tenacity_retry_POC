import logging

def log_attempt_number(retry_state):
    logging.basicConfig(filename='myapp.log',filemode='a',format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%d-%m-%Y:%H:%M:%S',level=logging.INFO)
    logging.info( 'Retrying %s: attempt %s ended with: %s',
        retry_state.fn, retry_state.attempt_number, retry_state.outcome)
    # print("Attempt No: ",retry_state.attempt_number)
        