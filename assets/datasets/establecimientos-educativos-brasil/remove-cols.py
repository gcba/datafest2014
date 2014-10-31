import csv
creader = csv.reader(open('institucoes-brasileiras-regioes.csv'))
cwriter = csv.writer(open('institucoes-brasileiras-regioes-edit.csv', 'w'))

for cline in creader:
   new_line = [val for col, val in enumerate(cline) if col not in (0,2,3,4)]
   cwriter.writerow(new_line)