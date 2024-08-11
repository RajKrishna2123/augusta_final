FROM python:latest

WORKDIR /app

COPY Augusta .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    numpy \
    django \
    firebase-admin \
    tqdm \
    djangorestframework \
    pyrebase4 \
    firebase-admin \
    django-allauth \ 
    django-rest-auth 

EXPOSE 8000
EXPOSE 4000
EXPOSE 9005
EXPOSE 9199
EXPOSE 9099
EXPOSE 9005
EXPOSE 9000
EXPOSE 8085 
EXPOSE 8080 
EXPOSE 5001
EXPOSE 5000
EXPOSE 4000
EXPOSE 9299
EXPOSE 9399

CMD ["bash", "script.sh"]