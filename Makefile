up:
	docker-compose up --build -d

logs:
	docker-compose logs -f app

down:
	docker-compose down --remove-orphans

test:
	pytest --maxfail=1 --disable-warnings -q

lint:
	ruff check .
	black --check .

fix:
	ruff --fix .
	black .

stop:
	docker-compose down

logs:
	docker-compose logs -f
