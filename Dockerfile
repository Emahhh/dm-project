FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di progetto nella directory di lavoro
COPY . .

# Install Jupyter Notebook
RUN pip install --no-cache-dir jupyter

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta 8888 per Jupyter Notebook
EXPOSE 8888

# Comando per avviare Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]