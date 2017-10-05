
import sys
from pro2aac_backend import LoadData

data = LoadData()

#sfasta=data.fasta2sfasta('../data/proteins.fasta')
#sfasta=data.fasta2sfasta('kd.fasta')
sfasta, abc = data.fasta2sfasta(sys.argv[1])
#print(sfasta)
print(type(sfasta))
for key, value in sfasta.items() :
    print (key, value)

print(abc)



#compp = data.sfasta2aac(sfasta)
aac = data.sfasta2aac(sfasta)

aac.to_csv('df.tsv',header=True,index=True,mode='w',sep='\t')


