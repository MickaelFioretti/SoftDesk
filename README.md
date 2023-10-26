# SoftDesk
Créez une API sécurisée RESTful en utilisant Django REST

## Installation

### Installation avec Docker

### Prérequis

-   Docker
-   Docker-compose

1. Cloner le projet

```bash
git clone 
```

2. Build l'images docker

```bash
docker-compose build
```

3. Lancer les containers

```bash
docker-compose up -d
```

4. Accéder au container

```bash
docker compose exec -it softdesk bash
```

4.1. Accéder au dossier du projet

```bash
cd app
```

5. Faire les migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Lancer le projet

```bash
python3 manage.py runserver
```

## Installation

### Installation sans Docker

1. Cloner le projet

```bash
git clone
```

2. Créer un environnement virtuel

```bash
python -m venv env
```

3. Activer l'environnement virtuel

```bash
source env/bin/activate
```

4. Installer les dépendances

```bash
pip install -r requirements.txt
```

4.1. Accéder au dossier du projet

```bash
cd app
```

5. Faire les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Lancer le projet

```bash
python manage.py runserver
```

## Utilisation

### Superuser

'''text
username: admin
password: inforoot
'''