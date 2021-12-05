FROM python:3.9-alpine

WORKDIR /app

# Install dependencies.
ADD requirements.txt /app
RUN cd /app && \
    pip install -r requirements.txt

# Add actual source code.
ADD blockchain.py main.py /app

EXPOSE 5000

CMD []
ENTRYPOINT ["python", "main.py", "--port", "5000"]