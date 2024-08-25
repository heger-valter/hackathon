#! /usr/bin/env python
import math
import csv
def run( filename):
	print "reformatting "
	print filename 
	with open(filename, "rb") as fileHandleReader:
		csv_reader = csv.reader(fileHandleReader)
		fileHandleWriter = open("/home/wheger/hackathon/sine/model_0/inference/test.csv", "w")
		output=csv.writer(fileHandleWriter)

		csv_reader.next()
		csv_reader.next()
		csv_reader.next()
		csv_reader.next()

		for row in csv_reader:
			output.writerow( [row[1], row[2], row[7] ] )

		fileHandleWriter.close()
		fileHandleReader.close()

if __name__ == "__main__":
		print " main "
		run("/home/wheger/hackathon/sine/model_0/inference/DefaultTask.TemporalAnomaly.predictionLog.csv")

