from psycopg2 import pool
import logging
import os

logger = logging.getLogger(__name__)

connection_pool = None

def init_db():
    try:
        global connection_pool
        connection_pool = pool.ThreadedConnectionPool(
            minconn=1,
            maxconn=10,
            database=os.getenv("DB_NAME", "meu_banco"),
            user=os.getenv("DB_USER", "admin"),
            host=os.getenv("DB_HOST", "localhost"),
            password=os.getenv("DB_PASSWORD", "senha123"),
            port=int(os.getenv("DB_PORT", 5432))
        )
        conn = connection_pool.getconn() # pegamos uma das conexões abertas
    except Exception as E:
        logger.error(f"Connection to DB failed: {E}")
    try:
        cursor = conn.cursor() # cursor é o que utilizamos para executar queries na conexão aberta
        logger.info("Looking for users table")
        cursor.execute(
            """CREATE TABLE if not exists users (
                name varchar,
                password varchar
            )"""
            ) # executa querie
        conn.commit() # salva o que foi feito
        cursor.close() # finaliza o cursor
    except:
        logger.error("Error to start user table!")
    finally:
        logger.info("Users table working!")
        connection_pool.putconn(conn) # devolve a conexão emprestada
        
def login(username: str, password: str) -> bool:
    conn = connection_pool.getconn()
    try:
        cursor = conn.cursor()
        logger.info("Looking for user in database")
        cursor.execute(
            f"""
                SELECT 1 FROM users WHERE name = %s and password = %s
            """, (username, password)
        )
        result = cursor.fetchone()
        cursor.close()
        return result
    except Exception as E:
        logger.error(f"Error at searching for user: {E}")
        return False
    finally:
        connection_pool.putconn(conn=conn)
        
def register(username: str, password: str) -> bool:
    conn = connection_pool.getconn()
    try:
        cursor = conn.cursor()
        logger.info("Creating new user")
        cursor.execute(
            f"""
                INSERT INTO users (name, password) VALUES (%s, %s)
            """, (username, password)
        )
        conn.commit()
        cursor.close()
        return True
    except Exception as E:
        logger.error(f"Error creating new user: {E}")
        return False
    finally:
        connection_pool.putconn(conn=conn)