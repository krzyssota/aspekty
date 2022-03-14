FROM python:3.8-slim-buster
COPY ["requirements.txt", "/tmp/requirements.txt"]
RUN ["pip3", "install", "-r", "/tmp/requirements.txt"]
COPY ["src/", "/opt/app_server"]
WORKDIR "/opt/app_server"
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app"]
