__author__ = 'Kaiqun'

import xlrd
from os import listdir
from os.path import isfile, join
import datetime


def BatchOperator(inputPath):
	onlyfiles = [inputPath + '\\' + f for f in listdir(inputPath) if isfile(join(inputPath, f))]

	for file in onlyfiles:
		onefileoperate(file)


def onefileoperate(filedir):
	currentYear = datetime.datetime.now().strftime('%Y')
	currentDateTime = ''

	onefile = filedir.split('\\')[-1:][0]
	currentDate = currentYear + '-' + onefile.split('_')[-1:][0][:2] + '-' + onefile.split('_')[-1:][0][2:4]
	StationID = onefile.split('_')[-2:][0]

	workbook = xlrd.open_workbook(filedir)
	worksheet = workbook.sheet_by_name('Sheet1')
	num_rows = worksheet.nrows - 1

	curr_row = 3
	channelIndex = 0

	while curr_row < num_rows:
		curr_row += 1

		# Break loop if is at bottom
		if worksheet.cell_value(curr_row, 1) == 'Total':
			break

		# Skip Class heading row and Totals
		if worksheet.cell_type(curr_row, 1) == 0 and worksheet.cell_type(curr_row, 2) == 0:
			continue
		if worksheet.cell_value(curr_row, 2) == 'Total':
			continue

		# Counting Channels
		if worksheet.cell_type(curr_row, 1) == 1 and worksheet.cell_value(curr_row, 2) == 'Channel 1':
			currentDateTime = currentDate + ' ' + "%02d" % (int(worksheet.cell_value(curr_row, 1).split(':')[0]) - 1) + ':00:00'
			print currentDateTime
			channelIndex = 1
		else:
			channelIndex += 1

		print [int(worksheet.cell_value(curr_row, i)) for i in range(3, 20) if worksheet.cell_value(curr_row, i) != '']
		# print currentDateTime + '  ' + StationID + '  ' + onefile


# BatchOperator('D:\\Software\\LoopsInsert\\testingData\\Class\\2015\\000000000001')