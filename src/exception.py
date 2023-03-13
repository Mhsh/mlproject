import sys
#from logger import logging


# Method returns the error message constructred which includes 
# line number, file name and error message
# sys is used to get the file name and line number
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno,str(error)
    )
    return error_message

# custom exception class that extends Exception.
# invoke the message detail method to get the error message
# return the error message from str method to print the exception.
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#             a = 1/0
#     except Exception as e:
#         logging.info("Divisible by zero error.")
#         raise CustomException(e, sys)