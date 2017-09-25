FROM centos:7

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    pip install flask

RUN pip install redis

COPY redeye.py /redeye.py

EXPOSE 5000

# this is terrible
CMD ["python", "-u", "redeye.py"]
