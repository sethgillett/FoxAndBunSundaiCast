# FoxAndBunSundaiCast

### Running Locally
- `cp .env.example .env`
- Fill in .env file with open ai and lemon fox ai keys
- Run the following commands:
- `docker build . -t sundaicast`
- `docker run --rm -v ./output:/app/output sundaicast python3 /app/main.py 14`
    - Replace 14 with the number of previous days you want to include
