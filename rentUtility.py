'''
rentUtility.py

Version: .1

'''

import time


def record():

	while(True):

		timeStamp = time.strftime("%m/%d/%Y")

		timeAnswer = input('Is this an acceptable time stamp? (y/n)\n     ' + timeStamp + '\n')
		if('n' in timeAnswer):
			timeStamp = input('Please enter a valid time stamp with the format xx/mm/yyyy:\n')

		electric = input('How much is owed for electric?\n')

		gas = input('How much is owed for gas? \n')

		people = input('Who has payed you for gas so far? (separate names spaces)\n')

		car = input('Is the car payment still $60? (y/or new amount)\n')
		if('y' in car):
			car = '60'

		comcast = input('Is the comcast payment still $19? (y/or new amount)\n')
		if('y' in comcast):
			comcast = '19'

		log = open('rentLog.txt', 'r')
		oldLog = log.read()
		log.close()


		newLine = timeStamp + ' electric ' + electric + ' comcast ' + comcast + ' car ' + car + ' gas ' + gas + ' ' + people

		print('Here is what your log looks like:')
		printLog(newLine)

		redoAnswer = input('\nIs this correct? (y/n)\n')

		if('y' in redoAnswer): break

		print()


	log = open('rentLog.txt', 'w')

	log.write(oldLog + '\n' + newLine)

	log.close()


def modify():

	timeStamp = input('Give a valid time stamp for this modifications:\n')

	log = open('rentLog.txt', 'r')

	line = ''
	for line in log.readlines():
		if timeStamp in line:
			print('\nFetching this log entry:')
			printLog(line)
			break

	log.close()

	while(True):
		modification = input('\nWhat would you like to modify?\n')

		if('electric' in modification):
			newAmount = input('Enter a new electric bill value:\n')

			newLine = modifyElectric(line, newAmount)

		elif('gas' in modification):
			newAmount = input('Enter a new gas bill value:\n')

			newLine = modifyGas(line, newAmount)

		elif('people' in modification):
			newPerson = input('Enter the people who have payed you for gas (with spaces):\n')

			newLine = modifyPeople(line, newPerson)

		print('Your new log looks like this:')
		printLog(newLine)

		answer = input('\nDoes this look correct? (y/n)\n')
		if('y' in answer): break

	log = open('rentLog.txt', 'r')
	newLog = log.read().replace(line, newLine)

	log.close()
	log = open('rentLog.txt', 'w')
	log.write(newLog)
	log.close()


def modifyElectric(line, newAmount):

	newLine = ''
	count = 1

	for word in line.split():

		if(count == 3):
			newLine+= newAmount + ' '
		else:
			newLine+= word + ' '

		count+=1

	return newLine

def modifyGas(line, newAmount):

	newLine = ''
	count = 1

	for word in line.split():

		if(count == 9):
			newLine+= newAmount + ' '
		else:
			newLine+= word + ' '

		count+=1

	return newLine


def modifyPeople(line, newPeople):

	return line + ' ' + newPeople


def summary():

	log = open('rentLog.txt', 'r')
	
	for line in log.readlines():
		printLog(line)

	log.close()

def getDatedLog():

	timeStamp = input('Give a valid time stamp for this log:\n')

	log = open('rentLog.txt', 'r')

	for line in log.readlines():
		if(timeStamp in line): 
			printLog(line)
			break

	log.close()


def printLog(line):

	count = 1
	people = ''

	for word in line.split():

		if(count == 1):
			date = word
		elif(count == 3):
			electric = word
		elif(count == 5):
			comcast = word
		elif(count == 7):
			car = word
		elif(count == 9):
			gas = word
		elif(count > 9):
			people+= word

		count+=1


	print('\nDate: ' + date)
	print('    Electric: $' + electric)
	print('    Comcast: $' + comcast)
	print('    Car: $' + car)
	print('    Gas: $' + gas + '  (Payed: ' + people + ')')


def getAmountOwed():
	pass


def main():

	while(True):
		choice = input('What do you want to do?:\n    1. Record Payment\n    2. Modify Payment\n    3. Dated Log\n    4. Summary\n')

		if('r' in choice or '1' in choice): record()
		elif('m' in choice or '2' in choice): modify()
		elif('d' in choice or '3' in choice): getDatedLog()
		elif('s' in choice or '4' in choice): summary()

		keepGoing = input('\nAnything else? (y/n)\n')
		if 'n' in keepGoing: break

if __name__ == "__main__":
    main()
