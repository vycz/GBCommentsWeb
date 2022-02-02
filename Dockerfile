FROM python:3.8
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
CMD gunicorn -w 2 -b 0.0.0.0:5000 app:app
