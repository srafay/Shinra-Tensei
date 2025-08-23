"""
db.py - Database utilities for RDS MySQL using SQLAlchemy

Responsibilities:
- Fetch DB credentials securely from AWS Secrets Manager
- Create SQLAlchemy engine and session
- Initialize DB tables from models
"""

import os
import json
import logging
from typing import Generator
import boto3
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .models import Base

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Environment variables
DB_SECRET_ARN = os.environ["DB_SECRET_ARN"]
REGION_NAME = os.environ.get("AWS_REGION", "ap-southeast-2")


def get_db_credentials(secret_arn: str) -> dict:
    """
    Fetch database credentials from AWS Secrets Manager.
    """
    sm_client = boto3.client("secretsmanager", region_name=REGION_NAME)
    try:
        secret_value = sm_client.get_secret_value(SecretId=secret_arn)
        creds = json.loads(secret_value["SecretString"])
    except sm_client.exceptions.ResourceNotFoundException:
        logger.error("Secrets Manager: Secret not found [%s]", secret_arn)
        raise
    except Exception as e:
        logger.exception("Failed to retrieve DB secret: %s", e)
        raise

    return creds


def get_engine():
    """
    Create SQLAlchemy engine using credentials from Secrets Manager.
    """
    creds = get_db_credentials(DB_SECRET_ARN)
    user = creds["username"]
    password = creds["password"]
    host = creds["host"]
    db_name = creds["dbname"]
    port = int(creds.get("port", 3306))

    if not host:
        raise RuntimeError("Database host not found in Secrets Manager secret.")

    connection_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    logger.info("Creating DB engine for host: %s, db: %s", host, db_name)
    return create_engine(connection_str, pool_pre_ping=True)


# Global session factory
SessionLocal = sessionmaker(bind=get_engine())


@contextmanager
def get_session() -> Generator[Session]:
    """
    Provide a transactional scope around a series of operations.
    Usage:
        with get_session() as db:
            db.query(Product).all()
    """
    session: Session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        logger.exception("Session rollback due to exception")
        raise
    finally:
        session.close()


def init_db():
    """
    Initialize database: create tables if they do not exist.
    """
    engine = get_engine()
    Base.metadata.create_all(engine)
    logger.info("Database tables created or already exist.")


# Init db
init_db()
