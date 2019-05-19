FROM alpine:3.9.4

RUN mkdir -p /var/EnCasDeSoif
WORKDIR /var/EnCasDeSoif

COPY . /var/EnCasDeSoif
RUN apk update && apk add --no-cache \
        python3 && pip3 install -r requirements.txt

EXPOSE 8000 

ENTRYPOINT [ "python", "manage.py", "runserver" ]