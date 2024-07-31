# -*-coding:utf-8-*-
'''
读入一个pdb文件，将其转化成一个氨基酸序列
'''
pdb_dict =  {
    'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E',
    'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'LYS': 'K',
    'ILE': 'I', 'LEU': 'L', 'MET': 'M', 'ASN': 'N',
    'PRO': 'P', 'GLN': 'Q', 'ARG': 'R', 'SER': 'S',
    'THR': 'T', 'VAL': 'V', 'TYR': 'Y', 'TRP': 'W'
}
seq = ''
for line in open(r"D:\Pyprograms\Drugs\data\1a0q_protein.pdb"):
    if line[0:6] =="SEQRES":
       columns = line.split()
       for resname in columns[4:]:
           seq = seq + pdb_dict[resname]
print(seq)