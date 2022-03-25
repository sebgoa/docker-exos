FROM centos:7

RUN curl "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    pip install flask

RUN pip install redis

COPY bank.py /bank.py

EXPOSE 5000

# this is terrible
CMD ["python", "-u", "bank.py"]
