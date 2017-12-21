from cPickle import load, dump
import os

def main():
	pfamDict=load(open("Generated/pfamDict.cpickle","rb"))
	#outputFolder="Generated/FamilyVisualization"
	outfilename="Generated/familyCount.txt"

	sortArr=[]
	for family in pfamDict.keys():
		arr=pfamDict[family]
		sortArr.append((family,arr))
		#lenstr="%05d" % (len(arr))
		#with open(os.path.join(lenstr+"_"+outputFolder,family+".cpickle","w") as f:
			#f.write(str(pfamDict[family]))
			#dump(arr,f)

	sortArr.sort(key=lambda x:len(x[1]), reverse=True)

	#open an empty file
	open(outfilename,"w")

	#write the family count in order
	for i in range(len(sortArr)):
		arr=sortArr[i]
		family=arr[0]
		length=len(arr[1])
		with open(outfilename,"a") as f:
			f.write(str(length)+"\t"+family+"\n")


if __name__ == '__main__':
	main()