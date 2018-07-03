from datetime import datetime
from numbers import Number
from decimal import Decimal


	
# looking through metadata and create matrix for metadat attributes
# this has been build to take different metadata files for future

def metadata_get(outputfile):
	#open metadata file and initialise variables
	metafile = open("meta.txt")
	content = metafile.read()
	content = content.splitlines()
	i=0
	col = len(content[1].split(","))
	row = len(content)
	matrix = [[0 for x in range(col)] for y in range(row)]
	#for each heading, make an array with attributes i.e. heading, length and string
	for line in content:
		matrix[i] = line.split(",")
		index = len(matrix[i])
		#put the headings down in the resultfile and add a , or newline
		# when all headings have been printed
		outputfile.write(matrix[i][0])
		if i != index:
			outputfile.write(",")
		else:
			outputfile.write("\n")
		i = i + 1
	return matrix

#this function transposes a string to a number and checks if it's a number using
# "isinstance" function. This will fail if not a number 
def numbers(num):
	try:
		num = Decimal(num)
		return isinstance(num, Number)
	except ValueError:
		print("exception %s is not a number " % record[i])

#Main program opens datafile and calls the matrix to be created
#this has been build for future proofing i.e. more headings can be added later
metafile = open("meta.txt")
outputfile = open("result.txt","w")
matrix = metadata_get(outputfile)
headings = len(matrix)
record = [0 for x in range(headings)]
datafile = open("data.txt")

#Goes through each line of datafile and uses the matrix created to 
#get the data for the corresponding heading
for line in datafile:
	i=0
	slice = 0
	preslice = 0
	#Looks at each heading's attributes and grabs the data then verifies it
	while i<headings:
		#gets the specified data and strips all leading and ending whitespace
		slice = int(matrix[i][1]) + preslice
		temp = line[preslice:slice]
		temp = temp.lstrip()
		temp = temp.rstrip()
		record[i]=temp
		preslice = slice
		#Verifies data depending on final attribute in matrix
		if matrix[i][2] == "date":
		#transposes the string to a date type and reorders to dd/mm/yyyy
			try:
				date = datetime.strptime(record[i],"%Y-%m-%d")
				record[i] = date.strftime("%d/%m/%Y")
			except ValueError:
				print("exception %s is not a real date " % record[i])
				break
		elif matrix[i][2] == "string":
		#looks at string to make sure no numbers appear
			if True != (record[i].isalpha()):
				print("exception %s is not a real name " % record[i])
				break
		elif matrix[i][2] == "numeric":
		#calls numbers function to ensure only valid numbers can be used
			if True != (numbers(record[i])):
				print("exception %s is not a number " % record[i])
				break
				
		#appends , between fields and \n when we start a new record.
		if i != headings-1:
			outputfile.write(record[i] + ",")
		else:
			outputfile.write(record[i] + "\n")
		i=i+1
#close files
metafile.close()
datafile.close()
outputfile.close()	

