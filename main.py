from dobot_utils import DobotWrapper

if __name__ == '__main__':
	
	bot = DobotWrapper()

	bot.dashboard.EnableRobot()
	bot.dashboard.SpeedFactor(10)

	bot.motion.MovL()
	bot.motion.MovJ()