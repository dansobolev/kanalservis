FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# create directory for the app user
RUN mkdir -p /home/danii

# create the app user
RUN addgroup --system danii && adduser --system --group danii

# create the appropriate directories
ENV HOME=/home/danii
ENV APP_HOME=/home/danii/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y ncat
RUN python -m pip install --upgrade pip
COPY ../requirements.txt .
RUN python -m pip install -r requirements.txt

# copy project
COPY .. $APP_HOME

# chown all the files to the app user
RUN chown -R danii:danii $APP_HOME

# change to the app user
USER danii
