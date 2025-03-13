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

- Since channel selection is based on topic and just determines the logic/behavior, I've implemented a Strategy pattern to handle this using `ChannelRouter` class to select the right channel, which must be a concrete implementation of `Channel` (later renamed to `BaseChannel`).
- Added a working endpoint `POST /assistance-requests` with some basic integration tests (`tests/test_app.py`) that already covers the challenge functionality requirements.
- Now that it's working let's do some refactor so I can unit test each part without the need of the whole server running or perform actual requests to Slack.
  - **Note:** as Slack channel it's implemented a side effect of integration tests is it actually send messages to slack each time.
- Added `ChannelRouter` as dependency of the endpoint and mocked it in tests. Now `tests/test_app.py` is a unit test suite that doesn't perform any actual request to Slack. It just tests that endpoint uses the channel provided by the router. This makes the test faster and more flexible to small changes, we could add more topics and/or channels without having to modify the test.
  - **Note:** I removed all integration tests but might be interesting to keep them as well to be able to test the whole flow.
- Added unit tests for `ChannelRouter` in `tests/test_channel_router.py`.
- Now that we have everything working with a good test coverage, let's reorganize folders and files (including renaming) to make it more readable and maintainable. Since this is a very small project, I would rule out using DDD or hexagonal architectures because they might be too complex, although they can be a good option to iterate on as the project scales. For the exercise, I think a ***screaming architecture*** approach is more appropriate.
Changed project structure from

```
.
├── app
│   ├── api
│   │   └── routes.py
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   ├── models.py
│   └── services
│       ├── channel.py
│       ├── channel_router.py
│       ├── email.py
│       └── slack.py
├── CHALLENGE.md
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
└── tests
    ├── test_app.py
    └── test_channel_router.py

```

to

```
.
├── app
│   ├── assistance_request
│   │   ├── api_routes.py
│   │   ├── channels
│   │   │   ├── base_channel.py
│   │   │   ├── channel_router.py
│   │   │   ├── email.py
│   │   │   └── slack.py
│   │   └── models.py
│   ├── core
│   │   ├── logger.py
│   │   └── settings.py
│   └── main.py
├── CHALLENGE.md
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
└── tests
    ├── test_app.py
    └── test_channel_router.py

```
