import sys
from datetime import datetime

#run 
def main():
	current = datetime.now()

	hour = current.hour % 12
	minute = current.minute

	goal = sys.argv[1]
	goal_hour, goal_minute = sys.argv[1].split(":")

	print(int(hour))
	print(int(minute))

	print(int(goal_hour))
	print(int(goal_minute))

	while (int(goal_hour) != int(hour)) or (int(minute) != int(goal_minute)):
		#print("haha")
		current = datetime.now()
		hour = current.hour % 12
		minute = current.minute
		#print(int(hour))
		#print(int(minute))

if __name__ == '__main__':
	main()