FROM python
WORKDIR /sumP
COPY . .
CMD [ "python","myapp.py" ]
