import logging
from logging.handlers import HTTPHandler,SMTPHandler
import sys
import core

logger = logging.getLogger('main') # Logger
logger.setLevel(level=logging.INFO)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('logging/full_output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('[%(asctime)s] : [%(levelname)8s] : [%(filename)10s] : [%(funcName)10s] : \
   [%(lineno)4d]： %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HTTPHandler
# http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
# logger.addHandler(http_handler)

# SMTPHandler
# smtp_handler=SMTPHandler(mailhost=("smtp.163.com", 25), fromaddr='sunqiang42@163.com',
#                                   toaddrs=['sq11235@163.com',],
#                                   subject="logging to email test",
#                                   credentials=('sunqiang42@163.com', '***'),
#                                   )
# logger.addHandler(smtp_handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')

core.run()