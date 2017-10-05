
import sys
from pro2aac_backend import LoadData

#class LoadData():
#	def __init__(self):
#		pass
#	def fasta2sfasta(self,filepath):
#		dictt={}
#		#fasta 2 sfasta conversion, 
#		pass
#		with open(filepath, 'r') as fin:
#			fin = map(str.rstrip, fin)
#			for line in fin:
#				line.rstrip('')
#				#print(line,end="")
#				#line.strip('\n').strip('\n')
#				if line.startswith('>'):
#					#line=map(str.rstrip,line)
#					header=line
#					#print(header)
#					#print(line, end='',flush=True)
#					sline=''
#					#dictt[line]=line
#				else:
#					sline += line
#					#print('\n')
#					#print(sline,end="")
#					#print('\n')         
#					dictt[header]=sline
#		return dictt			
#
#		
#
#	def sfasta2aac(self):
#		#input sfasta, return df with header, rownames aac.
#		pass
#	
#	def runSVM(self):
#		#ip: df with features, op: prob. score df
#		pass
#
#	def masterOUT(self):
#		#ip: prob. score df, op: OUT file
#		pass
#	
data = LoadData()

#sfasta=data.fasta2sfasta('../data/proteins.fasta')
#sfasta=data.fasta2sfasta('kd.fasta')
sfasta, abc = data.fasta2sfasta(sys.argv[1])
#print(sfasta)
print(type(sfasta))
for key, value in sfasta.items() :
    print (key, value)

print(abc)





