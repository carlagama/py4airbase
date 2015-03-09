# -*- coding: utf-8 -*-
import os, csv
import pandas as pd

def read_hourly_conc(country, filename): 
    # load hourly concentration files:
    periodo = []
    concentracao = []
    flag = []
    
    with open(os.path.join(os.getcwd(),'AirBase_'+country+'_v8_rawdata',filename), 'rb') as f:
        reader = csv.reader(f, dialect='excel-tab')
        for row in reader:
            dia = dt.datetime.strptime(row[0], "%Y-%m-%d")
            hora = 0
            for i in range(1,49,2):
                hora += 1
                periodo.append( dia + dt.timedelta(hours=hora))
                concentracao.append(float(row[i]))
                flag.append(int(row[i+1]))

    conc = pd.DataFrame(zip(concentracao, flag), index=periodo, columns=['hourly conc','flag'])
    
    return conc
