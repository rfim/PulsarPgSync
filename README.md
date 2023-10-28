# `PostgresSync` - Debezium to PostgreSQL Syncing Function

This repository contains the `PostgresSync` function, a Pulsar function designed to synchronize data from a Debezium source to a PostgreSQL database.

## Overview

`PostgresSync` listens to events produced by Debezium, processes the incoming records, and writes the transformed data to a PostgreSQL database. It's designed to be efficient, robust, and scalable.

## Prerequisites

- Apache Pulsar setup and running
- PostgreSQL database setup and running
- Debezium connector setup with a source (e.g., MySQL, MongoDB, etc.)

## Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies:**
    Ensure you have `pip` installed:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configure Debezium:**
    Ensure your Debezium connector is correctly configured and is publishing events to a Pulsar topic.

2. **Run the `PostgresSync` Function:**

    ```bash
    ./bin/pulsar-admin functions localrun \
        --classname PostgresSync \
        --py test_postgres_sync.py \
        --inputs <YOUR-DEBEZIUM-TOPIC> \
        --output <YOUR-OUTPUT-TOPIC> \
        --tenant public \
        --namespace default \
        --name PostgresSyncFunction
    ```

3. **Monitor Logs:**
    Monitor the function logs to ensure data is being processed and inserted into PostgreSQL.

## Troubleshooting

- **Connection Issues:** Ensure PostgreSQL and Debezium are both running and accessible.
- **Schema Issues:** Make sure the schema of the incoming data matches the expected schema.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
