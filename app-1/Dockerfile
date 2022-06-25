FROM python:3.9.13
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
COPY ./app-1.py /
ENTRYPOINT [ "python3" ]
CMD [ "app-1.py" ]