FROM python:3.12-slim 

# Working directory
WORKDIR /app   

# Copy project files
COPY . .    

# Install Python deps
RUN pip install -r requirements.txt

EXPOSE 8000  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
