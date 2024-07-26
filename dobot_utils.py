from dobotlib import dobot_api

class DobotWrapper:

	def __init__(self, address: str = '192.168.1.6'):

		self.address = address
		self.DASHBOARD_PORT = 29999
		self.MOTION_PORT = 30003
		self.FEED_PORT = 30004

		try:
			print('Connecting to dobot...')
			self.connect()

		except Exception as e:
			print('Connection failed.')
			raise e

		print('Successfully connected to dobot.')


	def connect(self) -> None:
		self.dashboard = dobot_api.DobotApiDashboard(self.address, self.DASHBOARD_PORT)
		self.motion = dobot_api.DobotApiMove(self.address, self.MOTION_PORT)
		self.feed = dobot_api.DobotApi(self.address, self.FEED_PORT)