FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

MAINTAINER SripaadSrinivasan    "sripaad751@gmail.com"


RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
CMD ["python3"]