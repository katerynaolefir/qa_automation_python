FROM python:3.12

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium

CMD ["pytest", "tests/db/test_db.py", "-v"]