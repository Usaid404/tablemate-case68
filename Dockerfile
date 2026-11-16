FROM python:3.12-slim
RUN useradd -m app
WORKDIR /app
COPY waitlist.py service.py helpers.py ./
COPY tests ./tests
USER app
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
