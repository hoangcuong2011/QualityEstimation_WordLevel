from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils



def main():
	#measurements = [{'feature1':7.0,'feature2':3.0,'feature3':2.33333333333, 'feature4':'<s>', 'feature5':'140|<s>'},
	#{'feature1':2.0,'feature2':3.0,'feature3':2.33333333333, 'feature4':'love', 'feature5':'141|<s>'},]

	
	measurements = []
	features_dev = []
	features_train = []
	features_test = []

	for i in range(22):
		l = {}
		measurements.append(l)

	with open("dev.features") as f:
		for line in f:
			line = line.strip()
			if(len(line)>0):
				array = []
				arr = line.split("\t")
				#for i in range(len(arr)):
				for i in range(22): #the maximum number of features I should add
					#print("hoang cuong", arr[i])
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						array.append(float(arr[i]))
					else:
						if(arr[i] in measurements[i]):
							array.append(measurements[i][arr[i]])
						else:
							measurements[i][arr[i]] = len(measurements[i])
							array.append(measurements[i][arr[i]])
				#print(array)
				features_dev.append(array)

	


	with open("train.features") as f:
		for line in f:
			line = line.strip()
			if(len(line)>0):
				array = []
				arr = line.split("\t")
				#for i in range(len(arr)):
				for i in range(22): #the maximum number of features I should add
					#print("hoang cuong", arr[i])
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						array.append(float(arr[i]))
					else:
						if(arr[i] in measurements[i]):
							array.append(measurements[i][arr[i]])
						else:
							measurements[i][arr[i]] = len(measurements[i])
							array.append(measurements[i][arr[i]])
				#print(array)
				features_train.append(array)

	
	with open("test.features") as f:
		for line in f:
			line = line.strip()
			if(len(line)>0):
				array = []
				arr = line.split("\t")
				#for i in range(len(arr)):
				for i in range(22): #the maximum number of features I should add
					#print("hoang cuong", arr[i])
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						array.append(float(arr[i]))
					else:
						if(arr[i] in measurements[i]):
							array.append(measurements[i][arr[i]])
						else:
							measurements[i][arr[i]] = len(measurements[i])
							array.append(measurements[i][arr[i]])
				#print(array)
				features_test.append(array)

	

	print(features_test[1])
	print(features_train[1])
	print(features_dev[1])

	with open("test", 'w') as file:
		for i in range(len(features_test)):
			for j in range(len(features_test[i])):
				file.write(str(features_test[i][j]))
				file.write(",")
			file.write("\n")

	with open("dev", 'w') as file:
		for i in range(len(features_dev)):
			for j in range(len(features_dev[i])):
				file.write(str(features_dev[i][j]))
				file.write(",")
			file.write("\n")

	with open("train", 'w') as file:
		for i in range(len(features_train)):
			for j in range(len(features_train[i])):
				file.write(str(features_train[i][j]))
				file.write(",")
			file.write("\n")		
		

	

if __name__== "__main__":
  main()

