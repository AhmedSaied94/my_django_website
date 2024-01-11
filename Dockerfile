# pull official base image
FROM alpine:latest

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev openssl-dev \
    && apk add postgresql-dev \
    && pip3 install psycopg2 \
    && apk del build-deps


# persistent / runtime deps
# RUN apk add --no-cache \
#     wkhtmltopdf \
#     xvfb \
#     ttf-dejavu ttf-droid ttf-freefont ttf-liberation \
#     fontconfig freetype ttf-ubuntu-font-family \
#     ;

# RUN chmod +x /usr/bin/wkhtmltopdf;
# RUN ln -s /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf;
# RUN chmod +x /usr/local/bin/wkhtmltopdf;
# RUN mkdir /usr/src/media
# RUN mkdir /usr/src/media/qr_codes

# install dependencies
# RUN pip install --upgrade pip
# pillow preparation
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install Pillow \
    && apk del build-deps
RUN apk update && apk add python3-dev \
    gcc \
    libc-dev \
    libffi-dev \
    libxslt-dev \
    libxml2-dev

RUN apk add --no-cache freetype-dev
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r /usr/src/app/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY ./ /usr/src/app/
RUN chmod 777 /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
RUN ["chmod", "777", "/usr/src/app/entrypoint.sh"]
RUN pip3 install debugpy==1.5.1
# copy project

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
