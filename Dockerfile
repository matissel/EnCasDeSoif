FROM alpine:3.9.4

RUN mkdir -p /var/EnCasDeSoif
WORKDIR /var/EnCasDeSoif

COPY . /var/EnCasDeSoif
RUN apk update && apk add --no-cache \
        python3 && pip3 install -r requirements.txt

EXPOSE 8000 

CMD [ "sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python manage.py loaddata users pointsEau  &&  python3 manage.py runserver 0.0.0.0:8000 --insecure" ]
