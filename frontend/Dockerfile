FROM python:3.8.16

WORKDIR /frontend

COPY ./requirements.txt /frontend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /frontend/requirements.txt

COPY . /frontend

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
