#!/usr/bin/python
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a=dna.upper().count('A')
print("the number of A is",str(a))
t=dna.upper().count('T')
print("T",t)
at_content=(a+t)/len(dna)
print("at",at_content)

print("\n\nQ2\n\n")
dna2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replaceAT=dna2.replace("A","t")
replaceTA=replaceAT.replace("T","a")
replaceGC=replaceTA.replace("G","c")
replaceCG=replaceGC.replace("C","g")
dnafinal=replaceCG.upper()
print(dnafinal)

print("\n\nQ3\n\n")
dna3="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
a=dna3.find("GAATTC")
print(a)

print("cut",a+1)
len1=len(dna3[:(a+1)])
len2=len(dna3[(a+1):])
print(len1,len2)

print("\n\nQ4\n\n")
dna4="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=dna4[:63]
exon2=dna4[90:]
codeseq=exon1+exon2

print("length",len(codeseq))
print("percentage",len(codeseq)/len(dna4)*100)


intro=dna4[63:90].lower()
print(exon1+intro+exon2)

