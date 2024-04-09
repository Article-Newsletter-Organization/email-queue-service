FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY requirements.txt ./

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .

ENTRYPOINT python src/__main__.py


