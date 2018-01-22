from sklearn.feature_extraction import DictVectorizer


def main():
	#measurements = [{'feature1':7.0,'feature2':3.0,'feature3':2.33333333333, 'feature4':'<s>', 'feature5':'140|<s>'},
	#{'feature1':2.0,'feature2':3.0,'feature3':2.33333333333, 'feature4':'love', 'feature5':'141|<s>'},]

	
	measurements = []
	
	with open("dev.features") as f:
		l = set()
		for line in f:
			line = line.strip()
			if(len(line)>0):
				list = {}
				arr = line.split("\t")
				#for i in range(len(arr)):
				for i in range(4): #the maximum number of features I should add
					#print("hoang cuong", arr[i])
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						list['feature'+str(i)] = float(arr[i])
					else:
						list['feature'+str(i)] = (arr[i])
					if(i==3):
						if arr[i] not in l:
							l.add((arr[i]))
				#print(list)
				measurements.append(list)			
	print(len(l))
	vec = DictVectorizer()
	array = vec.fit_transform(measurements).toarray()
	print(array)
	#print(vec.get_feature_names())
	print(len(array))
	print(len(array[0]))


if __name__== "__main__":
  main()

