from cPickle import dump
import os

def percent(i,length,numberNotification, header="", footer="",percentRange=(0,100)):
	scale=length/numberNotification
	if scale>0:
		if(i%scale==0):
			progress=str(percentRange[0]+int(float(i)/float(length)*(percentRange[1]-percentRange[0])*100)/float(100))+"%"
			write=header+progress+footer
			print write


def main():
	pamMappings=open("pamMappings/pdb_pfam_mapping.txt","r").read()
	outputFolder="Generated"


	lines=pamMappings.split("\n")


	pfamDict={}
	famToNum={}
	famCount={}

	tempFamNum=0

	for i, line in enumerate(lines):
		percent(i,len(lines),100)
		#0		1			2				3				4			5			6			7
		#PDB_ID	CHAIN_ID	PdbResNumStart	PdbResNumEnd	PFAM_ACC	PFAM_Name	PFAM_desc	eValue	
		arr=line.split("\t")
		pid=arr[0]
		pfamAcc=arr[4]

		#add to pfam dict
		if pfamAcc in pfamDict.keys():
			pfamDict[pfamAcc].append(pid)
		else:
			pfamDict[pfamAcc]=[pid]

		#add to famToNum
		histNum=None
		if pfamAcc in famToNum.keys():
			histNum=famToNum[pfamAcc]
		else:
			famToNum[pfamAcc]=tempFamNum
			histNum=tempFamNum
			tempFamNum+=1

		#add to famCount
		if pfamAcc in famCount.keys():
			
		famCount.append(histNum)


	#dump all info
	dump(pfamDict,open(os.path.join(outputFolder,"pfamDict.cpickle")))
	dump(famToNum,open(os.path.join(outputFolder,"famToNum.cpickle")))
	dump(famCount,open(os.path.join(outputFolder,"famCount.cpickle")))


if __name__ == '__main__':
	main()