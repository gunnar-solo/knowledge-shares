FROM python:3
ADD server.py requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "./server.py"]