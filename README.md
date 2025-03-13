Solution to backend challenge described in [CHALLENGE.md](CHALLENGE.md).

## Requirements

- Docker
- Docker Compose

## Start server

Starts the server in development mode on background.

```bash
make up
```

Then API is served at [http://localhost:8000](http://localhost:8000).

Interactive docs are available at [http://localhost:8000/docs](http://localhost:8000/docs)

## Stop server

```bash
make down
```

## Other commands

Open logs in streaming mode.

```bash
make logs
```

Run tests

```bash
make test
```

Run linter


```bash
make lint   # just check
make fix    # autofix
```