FROM python:2.7
ENV REFRESHED_AT 2015-04-26

ENV APP_NAME admin_ddjj
ENV APP_HOME /$APP_NAME

# Requirements
ADD $PWD/requirements.txt* $APP_HOME/
WORKDIR $APP_HOME                
RUN pip install -r requirements.txt

EXPOSE 8000
VOLUME $APP_HOME

 