# ue19-lab-05 : Application Python avec API et Docker

Ce projet est une petite application Python qui utilise la librairie `requests` pour interroger un service d'API public.
L'application interroge spécifiquement **JokesAPI** pour récupérer et afficher une blague aléatoire.

## Fonctionnalités

* Récupère une blague aléatoire en utilisant l'endpoint `https://v2.jokeapi.dev/joke/Any?type=single`.
* Affiche la blague formatée sur la console.
* Gère les erreurs de connexion et les codes de statut HTTP non réussis.
* Est conteneurisée à l'aide de Docker.

## Comment l'installer et le lancer (Localement)

### Prérequis

* Python 3.x installé.
* `pip` (gestionnaire de paquets Python).

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/lamplum/ue19-lab-05
    cd ue19-lab-05
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Lancer le programme :**
    ```bash
    python app.py
    ```

## Comment l'exécuter avec Docker (Conteneurisation)

### Prérequis

* Docker installé et en cours d'exécution.

1.  **Construire l'image Docker :**
    *(Assurez-vous d'être dans le répertoire `ue19-lab-05`)*
    ```bash
    docker build -t joke-app .
    ```

2.  **Lancer le conteneur :**
    ```bash
    docker run --rm joke-app
    ```
    *Le paramètre `--rm` supprime le conteneur après son exécution.*
