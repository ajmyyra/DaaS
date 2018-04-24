FROM python:2.7-alpine3.7

LABEL org.label-schema.vcs-url="https://github.com/ajmyyra/DaaS"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "wsgi.py" ]
