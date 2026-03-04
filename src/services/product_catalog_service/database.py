from psycopg2 import pool
import logging

logger = logging.getLogger(__name__)

connection_pool = None

def init_db():
    try:
        global connection_pool
        connection_pool = pool.ThreadedConnectionPool(

        )
        conn = connection_pool.getconn()
    except Exception as E:
        logger.error(f"Connection to DB failed: {E}")
    try:
        cursor = conn.cursor()
        logger.info("Creating products table")
        cursor.execute(
            """
                CREATE TABLE if not exists products (
                    name varchar,
                    price number
                )
            """
        )
        conn.commit()
        cursor.close()
    except Exception as E:
        logger.error(f"Error while creating products table: {E}")
    finally:
        connection_pool.putconn(conn=conn)

    