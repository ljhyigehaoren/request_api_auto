import os,time,logging
import threading
path=os.getcwd()
class log_message():
	_instance_lock = threading.Lock()

	def __init__(self,title):
		# 日志模块标题
		title = title
		# 获取时间作为日志名称
		day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
		# 获取项目执行路径
		pad = os.getcwd()
		# 拼接出完整的日志文件路径
		file_dir = pad + '\\logs'
		file = os.path.join(file_dir, (day + '.log'))
		self.logger = logging.Logger(title)
		self.logger.setLevel(logging.INFO)
		self.logfile = logging.FileHandler(file)
		self.logfile.setLevel(logging.INFO)
		self.control = logging.StreamHandler()
		self.control.setLevel(logging.INFO)
		self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.logfile.setFormatter(self.formater)
		self.control.setFormatter(self.formater)
		self.logger.addHandler(self.logfile)
		self.logger.addHandler(self.control)
	@classmethod
	def instance(cls, *args, **kwargs):
		with log_message._instance_lock:
			if not hasattr(log_message, "_instance"):
				log_message._instance = log_message(*args, **kwargs)
			log_message._instance.logger.name=args[0]
		return log_message._instance

	def debugInfo(self, message):
		self.logger.debug(message)

	def info_log(self, message):
		self.logger.info(message)

	def ware_log(self, message):
		self.logger.warn(message)

	def error_log(self, message):
		self.logger.error(message)