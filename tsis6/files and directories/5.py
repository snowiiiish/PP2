list1 = ['Alina', 'Mango', 'Banana', 'PP','KBTU']
path = 'b.txt'
with open(path, 'w') as wr:
    wr.writelines(f'{list1}\t')
wr.close()