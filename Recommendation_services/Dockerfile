FROM python:3.9
MAINTAINER Bharat
WORKDIR /
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "app1:app", "--host", "0.0.0.0", "--port", "8000"]
