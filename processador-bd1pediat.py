import pandas as pd
import numpy as np
import scipy.stats
pip install xlrd==1.2.0

data = pd.read_excel(r'./BD1Pediat.xls', usecols = ['T_GEST', 'PESO', 'ESTATURA', 'PC', 'PT', 'SEXO', 'SANGUE', 'RH', 'ANOMALIA'])

def calculaIntervaloConfiancaQuantitativa(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def printInformacoesQuantitativas(data):
  # Média encontrada para a coluna quantitativa passada por referência
  print("Média encontrada: ", np.average(data))
  # Desvio Padrão para a coluna quantitativa passada por referência
  print("Desvio padrão encontrado", np.std(data))
  # Confiança de 95% para para a coluna quantitativa passada por referência
  print("Intervalo de confiança 95% encontrado: ", calculaIntervaloConfiancaQuantitativa(data))

def calculaFrequenciaRelativa(list_of_chars):
    #find relative frequency
    calculaFrequenciaRelativa = {}
    for char in list_of_chars:
        if char in calculaFrequenciaRelativa:
            calculaFrequenciaRelativa[char] += 1
        else:
            calculaFrequenciaRelativa[char] = 1
    for char in calculaFrequenciaRelativa:
        calculaFrequenciaRelativa[char] = calculaFrequenciaRelativa[char]/len(list_of_chars)
    return calculaFrequenciaRelativa

print("Informações sobre T_GEST (Tempo de gestação, em dias)")
printInformacoesQuantitativas(data['T_GEST'])

print("Informações sobre PESO (Peso do recem anscido, em kg)")
printInformacoesQuantitativas(data['PESO'])

print("Informações sobre ESTATURA (Altura do recém nascido, em cm)")
printInformacoesQuantitativas(data['ESTATURA'])

print("Informações sobre PC (perímetro da cabeça ao nascer, em cm)")
printInformacoesQuantitativas(data['PC'])

print("Informações sobre PT (perímetro do tórax ao nascer, em cm)")
printInformacoesQuantitativas(data['PT'])

print("Informações sobre SEXO (M para Masculino ou F para Feminino)")
calculaFrequenciaRelativa(data['SEXO'])
print("Ocorrências:\n", pd.Series(data['SEXO']).value_counts())

print("Informações sobre SANGUE (O, A, B, AB)")
print(calculaFrequenciaRelativa(data['SANGUE']))
print("Ocorrências:\n", pd.Series(data['SANGUE']).value_counts())

print("Informações sobre RH (POS ou NEG)")
print(calculaFrequenciaRelativa(data['RH']))
print("Ocorrências:\n", pd.Series(data['RH']).value_counts()) 

print("Informações sobre ANOMALIA (SIM ou NÃO)")
print(calculaFrequenciaRelativa(data['ANOMALIA']))
print("Ocorrências:\n", pd.Series(data['ANOMALIA']).value_counts())