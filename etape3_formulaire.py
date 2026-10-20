import pandas as pd
import pyautogui#importer pyautogui pour simuler les actions du clavier
import time#importer time pour gerer les delais

df = pd.read_excel("donnee.xlsx")

print("Ouvre le formulaire et clique dans le champ Nom")#afficher les instructions destinees a l'utilisateur
time.sleep(10)#laisser 10 secondes pour ouvrir le formulaire et selectionner le champ nom

for index, row in df.iterrows():#parcourir chaque contact du tableau excel
#saisir automatiquement les champs du contact
    pyautogui.write(str(row["nom"]), interval=0.05)
    pyautogui.press("tab")

    pyautogui.write(str(row["email"]), interval=0.05)
    pyautogui.press("tab")

    pyautogui.write(str(row["message"]), interval=0.05)
    pyautogui.press("tab")

    pyautogui.press("enter")

    time.sleep(2)#attendre 2 secondes avant de traiter le contact suivant