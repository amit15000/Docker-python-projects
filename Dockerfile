FROM python
WORKDIR /pythonProjects/mountBind
COPY myapp.py .
COPY servers.txt .

CMD [ "python", "myapp.py" ]
