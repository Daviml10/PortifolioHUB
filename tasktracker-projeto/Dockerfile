# Imagem oficial do Python, versão leve.
FROM python:3.11-slim

# Define a pasta de trabalho dentro do contêiner.
WORKDIR /app

# Faz os prints aparecerem imediatamente no terminal.
ENV PYTHONUNBUFFERED=1

# Copia o código-fonte para dentro da imagem.
COPY src/ ./src/

# Inicia o menu interativo do TaskTracker.
CMD ["python", "src/main.py"]
