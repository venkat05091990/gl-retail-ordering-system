FROM python:3.9
MAINTAINER gaurav
WORKDIR /
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "app1:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD [ "python3 -m uvicorn app1:app --reload" ]
