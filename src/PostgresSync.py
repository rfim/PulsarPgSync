import pulsar
from pulsar import Function
import psycopg2
import json

class PostgresSync(Function):

    def process(self, input, context):
        error_messages = []

        context.get_logger().info(f"Received input: {input}")
        
        conn = None
        cursor = None
        
        try:
            context.get_logger().info("Trying to establish PostgreSQL connection...")
            
            conn = psycopg2.connect(
                host="localhost",
                port=5432,
                dbname="postgres",
                user="postgres",
                password="password"
            )
            cursor = conn.cursor()
            
            context.get_logger().info("Successfully established PostgreSQL connection.")
        except Exception as e:
            err_msg = f"Error while establishing connection to PostgreSQL: {e}"
            context.get_logger().error(err_msg)
            error_messages.append(err_msg)

        try:
            # Parse the content
            data = json.loads(input)
            after_data = data.get("after", {})
            
            # Extract table name and append "_destination"
            table_name = data.get("source", {}).get("table", "") + "_destination"

            # Constructing dynamic query
            columns = ", ".join(after_data.keys())
            placeholders = ", ".join(["%s"] * len(after_data))
            values = tuple(after_data.values())
            
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
            
            cursor.execute(query, values)
            conn.commit()
            
            context.get_logger().info("Successfully inserted data into PostgreSQL.")
        except Exception as e:
            err_msg = f"Error during data insertion into PostgreSQL. Data: {input}. Error: {e}"
            context.get_logger().error(err_msg)
            error_messages.append(err_msg)

        try:
            # Close the connection
            cursor.close()
            conn.close()
            context.get_logger().info("Closed PostgreSQL connection successfully.")
        except Exception as e:
            err_msg = f"Error while closing the PostgreSQL connection: {e}"
            context.get_logger().error(err_msg)
            error_messages.append(err_msg)

        return "; ".join(error_messages) if error_messages else input
