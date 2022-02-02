FROM python:3.8
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip install -r requirements.py && pip install gunicorn
CMD gunicorn app:app -c gunicorn.conf
