FROM python:3.10-slim

WORKDIR /inventoryapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python", "inventory.py"]