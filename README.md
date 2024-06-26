# Email Queue Service

Project developed in Python that consumes a RabbitMQ queue, checks the messages, queries a database, and sends emails to subscribers.

## Configuration

### Prerequisites

- Docker and Docker Compose (optional)
- Python 3.x (optional, if using Docker)
- RabbitMQ 3.13.x (optional, if using Docker)
- PostgreSQL 16.x (optional, if using Docker)

### Setting up environment variables

Use the `example.env` file as an example and create a file named `.env` at the root of the project.

### Usage with Docker Compose

1. Clone this repository:

```
git clone https://github.com/your-username/newsletter-system.git
```

2. Create the containers with Docker Compose CLI:

```
docker-compose up -d
```

3. View the logs of any of the containers:

```
docker logs email_consumer-1
```

## Local Usage

1. Clone this repository:

```
git clone https://github.com/your-username/newsletter-system.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. To start the system, execute:

```
python src/__main__.py
```

## Contribution

Contributions are welcome! Feel free to send pull requests or open issues reporting problems or suggesting improvements.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).