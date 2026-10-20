import pandas as pd #importer pandas

df = pd.read_excel("donnee.xlsx")#lire le fichier excel et stocker les donnees dans df

print(df.head())#afficher les lignes