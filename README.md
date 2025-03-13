Solution to backend challenge described in [CHALLENGE.md](CHALLENGE.md).
Below are the instructions to run the server and development notes about the implementation and further improvements that could be done.

## Requirements

- Docker
- Docker Compose

Setup a `.env` file with the following content:

```bash
SLACK_WEBHOOK_URL=<your_slack_webhook_url>
```

> [!IMPORTANT]
> Slack integration is the only implemented channel and requires a working hook.

## Usage

Once the the server is running, you can send a POST request to `/assistance-request` with the following payload:

```json
{
  "topic": "sales",
  "description": "I need help with my order"
}
```

> [!TIP]
> Use the Swagger UI interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs) to test the endpoint.

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

## Notes

### Approach

- Since channel selection is based on topic and just determines the logic/behavior, I've implemented a Strategy pattern to handle this using `ChannelRouter` class to select the right channel, any concrete implementation of `Channel`.