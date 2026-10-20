from selenium import webdriver #importer selenium pour piloter le navigateur
from selenium.webdriver.common.by import By#importer By pour retrouver les elements HTML par identifiant
import pandas as pd #importer pandas pour lire les donnees du fichier Excel
import time#importer time pour ajouter des pauses

# Lire le fichier Excel
df = pd.read_excel("donnee.xlsx")

# Ouvrir le navigateur Chrome et demarrer une session automatisee de chrome
driver = webdriver.Chrome()

# Ouvrir la formulaire HTML local
driver.get(r"C:\Users\Desktop\tp_rpa\formulaire.html")

time.sleep(2)#attendre 2 secondes pour laisser le temps a la page de s'afficher
#parcourir chaque ligne du taleau Excel
for index, row in df.iterrows():

    # Récupérer les champs du formulaire
    nom = driver.find_element(By.ID, "nom")
    email = driver.find_element(By.ID, "email")
    message = driver.find_element(By.ID, "message")

    # Remplir le formulaire
    nom.send_keys(str(row["nom"]))
    email.send_keys(str(row["email"]))
    message.send_keys(str(row["message"]))

    time.sleep(2)#attendre deux secondes pour laisser le temps a la page de s'afficher 

    # Vider les champs avant la ligne suivante
    nom.clear()
    email.clear()
    message.clear()

time.sleep(5)#attendre 5 secondes avant de fermer le navigateur 

driver.quit()#fermer chrome et terminer la session Selenium