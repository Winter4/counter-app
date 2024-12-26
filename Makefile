install:
	pip install --no-cache-dir -r requirements.txt

build-image:
	docker image build -t counter-app  .

run-server:
	python3 app.py

compose-up:
	docker compose up -d

compose-down:
	docker compose down --volumes