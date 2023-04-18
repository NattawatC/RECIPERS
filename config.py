from sqlalchemy import URL, create_engine

URLOBJECT = URL.create(
    drivername="postgresql+psycopg2",
    username="atip",
    password="",
    host="localhost",
    port=5432,
    database="Reciper",
)

ENGINE = create_engine(
    URLOBJECT)