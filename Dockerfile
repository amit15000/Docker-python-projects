FROM python
WORKDIR /pythonProjects/randomCatFact
COPY . .
RUN  pip install requests
CMD [ "python","api_demo.py" ]
