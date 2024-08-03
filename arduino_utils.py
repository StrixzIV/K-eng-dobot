import serial

class ArduinoWrapper:

	def __init__(self, serial_port: str = 'COM3', braudrate: int = 9600):
     
		print(f'Connecting to Arduino on {serial_port}...')

		try:
			self.serialcomms = serial.Serial(
				port = serial_port,
				baudrate = braudrate,
				timeout = .1
			)
   
		except Exception as e:
			print('Connection Failed.')
			raise e


	def send_serial(self, data: str) -> None:
		self.serialcomms.write(data.encode())

	
	def close_connection(self) -> None:
		self.serialcomms.close()