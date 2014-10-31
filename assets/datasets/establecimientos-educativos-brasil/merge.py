fout=open("institucoes-brasileiras-regioes.csv","a")
for num in range(1,8):
    for line in open(str(num)+".csv"):
         fout.write(line)    
fout.close()