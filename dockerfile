FROM python:3.11.4-slim as builder
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.11.4-slim as dev
WORKDIR /usr/src/app
COPY --from=builder /root/.local /root/.local
COPY src/ ./src
ENV PATH=/root/.local/bin:$PATH
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]