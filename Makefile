up:
	docker-compose up --build -d

logs:
	docker-compose logs -f app

down:
	docker-compose down --remove-orphans

test:
	pytest --maxfail=1 --disable-warnings -q

lint:
	docker-compose run --rm app ruff check /app
	docker-compose run --rm app black --check /app

fix:
	docker-compose run --rm app ruff check --fix /app
	docker-compose run --rm app black /app

stop:
	docker-compose down
