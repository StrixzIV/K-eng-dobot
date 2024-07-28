import serial

class ArduinoWrapper:

	def __init__(self, serial_port: str = 'COM4', braudrate: int = 9600):

		self.serialcomms = serial.Serial(
			port = serial_port,
			baudrate = braudrate,
			timeout = .1
		)


	def send_serial(self, data: str) -> None:
		self.serialcomms.write(data.encode())

	
	def close_connection(self) -> None:
		self.serialcomms.close()