FROM python:3.7.7

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./migrate.py ./
COPY ./src/ ./src/
COPY ./res/ ./res/

VOLUME /data_in
VOLUME /data_out

ENV DATA_IN data_in
ENV DATA_OUT data_out

ENV DB_HOST postgres
ENV DB_PORT 5432
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_DATABASE postgres

CMD [ "python", "./migrate.py" ]
