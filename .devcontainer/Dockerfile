FROM mcr.microsoft.com/vscode/devcontainers/python

RUN apt update 

RUN apt install -y bash vim git curl postgresql

RUN curl -o lcbo.tgz https://heycarsten.s3.amazonaws.com/lcboapi-2019-01-21.tgz && tar -zxvf lcbo.tgz

RUN service postgresql start

RUN sudo su postgres sh -c 'createdb lcbo'

RUN sudo su postgres sh -c 'psql lcbo </workspaces/monitoring-logging/lcboapi-2019-01-21.sql'
