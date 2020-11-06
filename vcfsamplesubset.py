#! /bin/python3.7
import sys
input1 = sys.argv[1]
input2 = sys.argv[2]
outfile = sys.argv[3]
vcffile=open(input1,'r')
chrfile=open(input2,'r')
outfile=open(outfile,'w')

linenumber=0
search_filters=[]
indexes = []
for line1 in chrfile:
	line1=line1.strip().split('\t')
	search_filters.append(line1[0])
firstNlines = vcffile.readlines()[0:26]
outfile.write(''.join([str(elem) for elem in firstNlines]))
vcffile.close()

vcffile=open(input1,'r')
for line in vcffile:
	line=line.strip('\n')
	if line[0] == '#' and line[1]=='#':
		continue
	columns = line.split('\t')
	if line[0] =='#':
		for filters in search_filters:
			idx=columns.index(filters)
			if idx >=0:
				indexes.append(idx)
	for outindex in indexes:
		outfile.write(columns[outindex]+ '\t')
	outfile.write('\n')
	
vcffile.close()
chrfile.close()
outfile.close()

# Python3 vcfssamplesubset.py ALL.chrY.phase1_samtools_si.20101123.snps.low_coverage.genotypes.vcf samplelist.txt samplesubset.vcf