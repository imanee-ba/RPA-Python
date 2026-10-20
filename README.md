# RPA Python – Automatisation des tâches

## Description

Projet pratique de **Robotic Process Automation (RPA)** développé en Python. Il explore l'automatisation de tâches répétitives : lecture de données Excel, saisie de formulaires HTML et préparation d'envoi d'e-mails.

## Fonctionnalités

- Lecture et affichage des données d'un fichier Excel avec **Pandas**.
- Remplissage automatique d'un formulaire avec **PyAutoGUI**.
- Pilotage du navigateur Chrome avec **Selenium**.
- Fonction d'envoi d'e-mails personnalisés via **SMTP Gmail**.

## Technologies utilisées

- Python
- Pandas et OpenPyXL
- PyAutoGUI
- Selenium
- HTML / CSS / JavaScript
- SMTP et python-dotenv

## Structure du projet

```text
RPA Python/
├── main.py                  # Lecture d'un fichier Excel
├── etape2_lecture.py        # Affichage des contacts Excel
├── etape3_formulaire.py     # Saisie du formulaire avec PyAutoGUI
├── etape_selenium.py        # Saisie du formulaire avec Selenium
├── etape4_envoyer.py        # Fonction d'envoi d'e-mails via SMTP
└── formulaire.html          # Formulaire de contact local
```

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/UTILISATEUR/NOM-DU-DEPOT.git
   cd NOM-DU-DEPOT
   ```

2. Créer et activer un environnement virtuel (Windows) :

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Installer les dépendances :

   ```bash
   pip install pandas openpyxl pyautogui selenium python-dotenv
   ```

## Utilisation

**Préparer les données :** placer le fichier Excel attendu dans le dossier du projet. Les scripts utilisent actuellement des noms différents (`donnees.xlsx`, `donnee.xlsx`, `contacts_test_marocains.xlsx`) : adaptez-les à votre fichier réel. Les colonnes nécessaires pour la saisie sont `nom`, `email` et `message`.

**Lecture Excel :**

```bash
python main.py
```

**Remplissage avec PyAutoGUI :**

```bash
python etape3_formulaire.py
```

Ouvrez `formulaire.html` dans un navigateur et placez le curseur dans le champ *Nom* durant le délai prévu par le script.

**Remplissage avec Selenium :**

```bash
python etape_selenium.py
```

Avant l'exécution, adaptez dans le script le chemin absolu vers `formulaire.html` à votre ordinateur. Chrome doit être disponible.

**Envoi d'e-mails :** `etape4_envoyer.py` définit la fonction `envoyer_email()` avec Gmail SMTP, mais ne lance pas à lui seul une campagne complète. Pour l'utiliser, configurez les variables d'environnement `GMAIL_USER` et `GMAIL_APP_PASSWORD` et appelez la fonction depuis un script après avoir vérifié les destinataires. Ne publiez jamais vos identifiants ou votre fichier `.env`.

## Remarques

Les scripts sont des exercices indépendants d'apprentissage RPA et ne constituent pas encore une application intégrée. Les fichiers Excel ne sont pas inclus dans l'archive fournie.

## Objectif pédagogique

Apprendre à automatiser des tâches manuelles répétitives en associant traitement de données, interaction avec un navigateur et messagerie électronique.
