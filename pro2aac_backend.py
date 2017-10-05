
import pandas as pd
import numpy as np


class LoadData():
	def __init__(self):
		pass
	def fasta2sfasta(self,filepath):
		dictt={}
		dummy='kd'
		#fasta 2 sfasta conversion, 
		pass
		with open(filepath, 'r') as fin:
			fin = map(str.rstrip, fin)
			for line in fin:
				line.rstrip('')
				#print(line,end="")
				#line.strip('\n').strip('\n')
				if line.startswith('>'):
					#line=map(str.rstrip,line)
					header=line
					#print(header)
					#print(line, end='',flush=True)
					sline=''
					#dictt[line]=line
				else:
					sline += line
					#print('\n')
					#print(sline,end="")
					#print('\n')         
					dictt[header]=sline
		return dictt, dummy

		

	def sfasta2aac(self,dictsfasta):
		#input sfasta, return df with header, rownames aac.
		#pass
		df = pd.DataFrame()
		comp=[None]*20
		aa= ('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y')
		rowname=[]	
		for key, value in dictsfasta.items() :
			#print (key, value)
			key = key.replace('>', '')
			rowname.append(key)
			lenn=len(value)
			print(lenn)
			for i in range(20):
				comp[i]=0
			for c in value:
				comp[aa.index(c)] += 1
			print(type(comp))
			print(comp)
			comp[:] = [x / lenn for x in comp]
			dff=np.array(comp)			#crucial
			dff=pd.Series(dff)			#crucial
			print(type(dff))
			print(dff)
			df = df.append(dff,ignore_index=True)	#crucial
		#print(comp)
		print(rowname)
		df.columns = aa
		df.index = rowname
		df = df*100
		df = df.round(2)
		print((df))
		return df
		

	def runSVM(self):
		#ip: df with features, op: prob. score df
		pass

	def masterOUT(self):
		#ip: prob. score df, op: OUT file
		pass
	
#data = LoadData()
#
##sfasta=data.fasta2sfasta('../data/proteins.fasta')
##sfasta=data.fasta2sfasta('kd.fasta')
#sfasta=data.fasta2sfasta(sys.argv[1])
##print(sfasta)
#for key, value in sfasta.items() :
#    print (key, value)







