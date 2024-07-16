FROM ubuntu/python

RUN apk --update add bash vim git
 
COPY ./dependencies.txt /var/www/dependencies.txt
 
RUN pip install -r /var/www/dependencies.txt