from psycopg2 import pool
import logging

logger = logging.getLogger(__name__)

connection_pool = pool.ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    database = "meu_banco",
    user = "admin",
    host="users-db",
    password = "senha123",
    port=5432
)

def init_db():
    conn = connection_pool.getconn() # pegamos uma das conexões abertas
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