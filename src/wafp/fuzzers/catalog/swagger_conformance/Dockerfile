FROM python:3.8.6-slim

LABEL name="swagger-conformance"

RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/olipratt/swagger-conformance.git /app \
    && cd /app \
    && git checkout 8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f \
    && apt remove -y git \
    && apt -y autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install .

ENTRYPOINT ["python", "-m", "swaggerconformance"]
