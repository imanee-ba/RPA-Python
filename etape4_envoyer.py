import os#importer os pour acceder aux variables d'environnement
import time#importer le module de gestion du temps 
import smtplib#importer le module SMTP pour envoyer des e-mails 
from pathlib import Path#importer pour construire le chemin du formulaire
from email.mime.text import MIMEText#importer pour creer un contenu de message texte
from email.mime.multipart import MIMEMultipart#importer pour construire un email structure

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


# ---------- CONFIG ----------
FICHIER_EXCEL = "contacts_test_marocains.xlsx"
FORMULAIRE = Path("formulaire.html").resolve().as_uri()
email_expediteur = os.getenv("GMAIL_USER")  # adresse email de l'expéditeur
mot_de_passe = os.getenv("GMAIL_APP_PASSWORD")   # mot de passe d'application Gmail
ENVOYER_EMAILS = True    #indiquer si l'envoi est autorise        
#fonction qui envoie un e mail a destinataire
def envoyer_email(destinataire, nom, message):
    #creer le conteneur du message electronique
    msg = MIMEMultipart()
    msg["From"] = email_expediteur
    msg["To"] = destinataire
    msg["Subject"] = f"Bonjour {nom}, nous avons bien reçu votre message"
#construire le corps du message avec le nom et le texte recu
    corps = (
        f"Bonjour {nom},\n\n"
        f"Merci pour votre message :\n\"{message}\"\n\n"
        f"Nous reviendrons vers vous très prochainement.\n\n"
        f"Cordialement,\nL'équipe"
    )
    
    msg.attach(MIMEText(corps, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
        serveur.login(email_expediteur, mot_de_passe)
        serveur.send_message(msg)#transmettre l'email au serveur SMTP





