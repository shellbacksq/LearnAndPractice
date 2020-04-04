import logging
# log级别,格式,保存位置
logging.basicConfig(
   level= logging.INFO,
   format = '[%(asctime)s] : [%(levelname)8s] : [%(filename)10s] : [%(funcName)10s] : \
   [%(lineno)4d]： %(message)s',# 运行时间,日志级别,日志内容.保持对齐
#    filename= "logging/test.log" #要想打印到控制台就不用这句,basicConfig下不能兼得.
)   
logger = logging.getLogger(__name__)
# 下面这些写在代码里面,可以出现在任何想出现的位置.
logger.debug('debug message')
logger.info("info message")
logger.warning('warn message')
logger.error("error message")
logger.critical('critical message')

# 更加典型的使用场景,记录错误和异常.
try:
    a=10
    b=1+a
    c=5
    result = 10 / 0

except Exception:
    logger.error('Faild to get result', exc_info=True)
logger.info('Finished')