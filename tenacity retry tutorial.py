# from tenacity import *
# import sys
# Basic retry

# @retry
# def exception_function():
#     print("From exception function")
#     raise Exception

# Stopping_Attempt

# @retry(stop=stop_after_attempt(7))
# def exception_function():
#     print("From exception function, stop after 7 attempts")
#     raise Exception

# Time limit for retrying

# @retry(stop=stop_after_delay(10))
# def exception_function():
#     print("From exception function with dealy of 10s ")
#     raise Exception


# ----------------------------------------------------------------------------------------------
# Wait b/w retries

# @retry(wait=wait_fixed(2),stop=stop_after_attempt(7))
# def exception_function():
#     print("From exception function after delay of 2s ")
#     raise Exception


# @retry(wait=wait_fixed(2)+wait_random(min=1, max=2),stop=stop_after_attempt(7))
# def exception_function():
#     print("wait 2 seconds fixed and then add randomly seconds b/w 1 and 2  to the wait time")
#     raise Exception


# @retry(wait=wait_exponential(multiplier=1,min=4,max=10),stop=stop_after_attempt(7))
# def exception_function():
#     print("Wait 2^x * 1 second between each retry starting with 4 seconds, then up to 10 seconds, then 10 seconds afterwards")
#     raise Exception

# exception_function()

# ----------------------------------------------------------------------------------------------
# Getting the logging info of the invocations

# import logging
# import sys

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# logger = logging.getLogger(__name__)

# class MyException():
#     def __init__(self,val) -> None:
#         print(val)

# @retry(stop=stop_after_attempt(3),before=before_log(logger, logging.DEBUG))
# def raise_my_exception():
#     raise MyException("Fail")

# try:
#     raise_my_exception()
# except Exception:
#     pass

# print(raise_my_exception.retry.statistics) # Statistics of the retry for the function


# ----------------------------------------------------------------------------------------------

# Retry  with custom callbacks
# import logging

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# logger = logging.getLogger(__name__)

# class MyException():
#     def __init__(self,val) -> None:
#         print(val)

# # Custom callback function
# def my_before_sleep(retry_state):
#     if retry_state.attempt_number < 1:
#         loglevel = logging.INFO
#     else:
#         loglevel = logging.WARNING
#     logger.log(
#         loglevel, 'Retrying %s: attempt %s ended with: %s',
#         retry_state.fn, retry_state.attempt_number, retry_state.outcome)
# # Custom callback parameter => before_sleep
# @retry(stop=stop_after_attempt(3), before_sleep=my_before_sleep)
# def raise_my_exception():
#     raise MyException("Fail")

# try:
#     raise_my_exception.retry_with(stop=stop_after_attempt(4))()   #Changing parameters at runtime
# except RetryError:
#     pass


# ----------------------------------------------------------------------------------------------

# Using Retrying mechanism without retry decorater

# from tenacity import Retrying, RetryError, stop_after_attempt
# class Retry:
#     attempt_no=1
#     try:
#         for attempt in Retrying(stop=stop_after_attempt(3)):
#             with attempt:
#                 print("Retrying attempt_no: ",attempt_no)
#                 attempt_no+=1
#                 raise Exception('My code is failing!')
#     except RetryError:
#         pass