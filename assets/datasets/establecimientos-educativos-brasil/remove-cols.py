import csv
with open("institucoes-brasileiras-regioes.csv","rb") as source:
   rdr= csv.reader( source, delimiter=';' )
   with open("institucoes-brasileiras-regioes-edit.csv","wb") as result:
       wtr= csv.writer( result )
       for r in rdr:
           wtr.writerow((r[2], r[5], r[11], r[15], r[16], r[26], r[27]) )