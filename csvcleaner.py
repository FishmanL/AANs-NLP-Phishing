#cleans a desired csv file with a given operation
f = open('TrainingData.csv')
contents = f.read()
f.close()
#replace operation as needed
new_contents = contents.replace('-1', '0')
f = open('TrainingData1.csv', 'w')
f.write(new_contents)
f.close()