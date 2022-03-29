FROM python:3.9
MAINTAINER gaurav
WORKDIR /
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
