FROM python:3.7.7

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./migrate.py ./
COPY ./src/ ./src/
COPY ./res/ ./res/

VOLUME /data_in
VOLUME /data_out

CMD [ "python", "./migrate.py" ]
