FROM python
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python","-u", "app.py"]