# geeigneter als arch, schlanker
FROM python:3.12-slim 

# Working directory wird erstelle, wennn icht existent. 
WORKDIR /app   

# Copy project files das eingebundene dir toplevel bzw run build context
COPY /app . 

# Install Python deps
RUN pip install "fastapi[standard]" sqlalchemy

# mehr als info fuer devs, der wahre mount ist im run command
EXPOSE 8000  

ENTRYPOINT ["python3"]

CMD ["main.py"]
