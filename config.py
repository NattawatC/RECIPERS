from sqlalchemy import URL, create_engine

URLOBJECT = URL.create(
    drivername="postgresql",
    username="atip",
    password="",
    host="192.168.1.55",
    port=5432,
    database="Reciper",
)

ENGINE = create_engine(
    URLOBJECT)