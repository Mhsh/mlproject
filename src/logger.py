import logging
import os
import datetime

# this code will invoke as soon as the logger is run.
# Generates the log folder and file at current working directory.
# extis_ok - does not raise exception if folder is already present.
LOG_FILE=f"{datetime.datetime.now().strftime('%m_%d_%Y_%H')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
# config object for logger.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)
# Test code for logger.
# if __name__=="__main__":
#     logging.info("Logs started")