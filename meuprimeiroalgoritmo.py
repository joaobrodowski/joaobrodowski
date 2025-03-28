import pandas as pd
import matplotlib.pyplot as plt

dados = {
   "EMPRESA" : ['A', 'B', 'C'],
   "FATURAMENTO" : [23, 35, 64]

         
    }

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 5))
plt.bar(df['EMPRESA'], df ['FATURAMENTO'], 
        color = 'blue', alpha = 0.8)



plt.title ('faturamento mensal' )
plt.xlable ('EMPRESAS')
PLT.YLABLE ('FATURAMENTO')

plt.show()