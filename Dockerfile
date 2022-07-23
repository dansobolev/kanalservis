FROM python:3.8

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
