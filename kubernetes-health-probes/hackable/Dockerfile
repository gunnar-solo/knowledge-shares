FROM python:3
ADD server.py requirements.txt DATABASE.db /
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "./server.py"]