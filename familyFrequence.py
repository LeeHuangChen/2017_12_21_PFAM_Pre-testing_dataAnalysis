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
	

	for i, line in enumerate(lines):
		percent(i,len(lines),50)
		#0		1			2				3				4			5			6			7
		#PDB_ID	CHAIN_ID	PdbResNumStart	PdbResNumEnd	PFAM_ACC	PFAM_Name	PFAM_desc	eValue	
		arr=line.split("\t")
		if len(arr)>6:
			pid=arr[0]
			pfamName=arr[5]

			#add to pfam dict
			if pfamName in pfamDict.keys():
				pfamDict[pfamName].append(pid)
			else:
				pfamDict[pfamName]=[pid]
			

	#dump all info
	dump(pfamDict,open(os.path.join(outputFolder,"pfamDict.cpickle"),"w"))
	


if __name__ == '__main__':
	main()