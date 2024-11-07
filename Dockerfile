# Usa l'immagine di base di Jupyter con Python 3
FROM jupyter/scipy-notebook:latest

# Imposta la directory di lavoro
WORKDIR /home/jovyan/work

# Copia i file di progetto nella directory di lavoro
COPY . .

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta 8888 per Jupyter Notebook
EXPOSE 8888

# Comando per avviare Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''"]