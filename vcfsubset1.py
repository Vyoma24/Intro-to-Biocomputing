#! /bin/python3.7
import sys
import gzip
input1 = sys.argv[1]
input2 = sys.argv[2]
outfile = sys.argv[3]
vcffile=open(input1,'r')
chrfile=open(input2,'r')
outfile=open(outfile,'w')
linenumber=0
search_Chr=[]
search_Pos=[]
for line1 in chrfile:
	line1=line1.strip().split('\t')
	search_Chr.append(line1[0])
	search_Pos.append(line1[1])

firstNlines = vcffile.readlines()[0:26]
outfile.write(''.join([str(elem) for elem in firstNlines]))
vcffile.close()

vcffile=open(input1,'r')
# print(firstNlines)

for line in vcffile:
	
	
	line=line.strip('\n')
	if line[0] == '#':
		continue
	columns = line.split('\t')
	Chr=columns[0]
	Pos=columns[1]
	Ref=columns[3]
	Alt=columns[4]

	if Chr in search_Chr and Pos in search_Pos:
		outfile.write(line+'\n')
vcffile.close()
chrfile.close()
outfile.close()

# Python3 vcfsubset1.py ALL.chrY.phase1_samtools_si.20101123.snps.low_coverage.genotypes.vcf variantlist.txt variantsubset.vcf 