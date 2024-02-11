# Utilisation d'une image de base avec l'environnement Python
FROM python:3.8

# Définition du répertoire de travail
WORKDIR /app

# Copie des scripts dans le conteneur
# COPY requirements.txt .
COPY classes /app/classes
COPY data /app/data
COPY hello-world.py /app/

# install dependencies
# RUN pip install -r requirements.txt

# Exécution d'un script "hello-world" (exemple)
CMD ["python", "hello-world.py"]