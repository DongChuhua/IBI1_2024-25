import re 

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file, open('tata_genes.fa', 'w') as out:
    seq = ''
    gene_name = ''
    
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            # 处理前一个基因的序列
            if gene_name and re.search(r'TATA[AT]A[AT]', seq):
                out.write(f'>{gene_name}\n{seq}\n')
            # 提取当前基因名
            match = re.search(r'gene:(\S+)', line)
            gene_name = match.group(1) if match else None
            seq = ''  # 重置序列
        else:
            seq += line
    
    # 循环结束后检查最后一个基因
    if gene_name and re.search(r'TATA[AT]A[AT]', seq):
        out.write(f'>{gene_name}\n{seq}\n')