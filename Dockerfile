FROM python
COPY . /webshop
WORKDIR /webshop
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
