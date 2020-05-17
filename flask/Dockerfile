FROM python:3.8.3
RUN flaskuser --create-home flaskuser
WORKDIR /home/flaskuser
USER flaskuser
ENV PATH="/home/flaskuser/.local/bin:${PATH}"
COPY --chown=flaskuser requirements.txt /home/flaskuser/requirements.txt
RUN python -m pip install --user --no-cache-dir --trusted-host pypi.python.org -r /home/flaskuser/requirements.txt
COPY --chown=flaskuser . /home/flaskuser
ADD . /home/flaskuser/app
CMD ["uwsgi", "app.ini"]