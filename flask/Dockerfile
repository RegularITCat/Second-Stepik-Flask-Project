FROM python:3.7.5
RUN useradd -ms /bin/bash flaskuser
WORKDIR /home/flaskuser/app
ADD . /home/flaskuser/app
RUN chmod 755 /home/flaskuser/app
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
USER flaskuser
CMD ["uwsgi", "app.ini"]