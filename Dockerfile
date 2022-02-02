FROM python:3.8
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip install -r requirements.py && pip install gunicorn
CMD gunicorn -w 2 -b 127.0.0.1:5000 app:app --daemon 
