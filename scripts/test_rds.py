"""
Module: products_db

This module provides utilities to interact with the MySQL products database hosted on AWS RDS.
It fetches credentials securely from AWS Secrets Manager and performs basic CRUD operations using SQLAlchemy ORM.

Environment Variables:
    DB_SECRET_ARN (str): ARN of the AWS Secrets Manager secret containing DB credentials.
    AWS_REGION (str, optional): AWS region for Secrets Manager client. Defaults to 'ap-southeast-2'.

Dependencies:
    boto3
    sqlalchemy
    pymysql
"""

import os
import json
import logging
import boto3

from typing import Dict
from src.common.models import Base, Product
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import (
    create_engine,
    select,
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Environment variables
DB_SECRET_ARN = os.environ["DB_SECRET_ARN"]
REGION_NAME = os.environ.get("AWS_REGION", "ap-southeast-2")


# Database credential utilities
def get_db_credentials(secret_arn: str) -> Dict[str, str]:
    """
    Fetch database credentials from AWS Secrets Manager.

    Args:
        secret_arn (str): ARN of the Secrets Manager secret.

    Returns:
        dict: Dictionary containing DB connection info (host, username, password, dbname, port).
    """
    sm_client = boto3.client("secretsmanager", region_name=REGION_NAME)
    try:
        secret_value = sm_client.get_secret_value(SecretId=secret_arn)
    except sm_client.exceptions.ResourceNotFoundException:
        logger.error("Secret not found: %s", secret_arn)
        raise
    except Exception as e:
        logger.exception("Failed to retrieve secret: %s", e)
        raise

    return json.loads(secret_value["SecretString"])


def get_db_engine(secret_arn: str):
    """
    Create a SQLAlchemy engine using credentials from Secrets Manager.

    Args:
        secret_arn (str): ARN of the Secrets Manager secret.

    Returns:
        sqlalchemy.Engine: SQLAlchemy engine instance.
    """
    creds = get_db_credentials(secret_arn)
    user = creds["username"]
    password = creds["password"]
    host = creds["host"]
    dbname = creds["dbname"]
    port = int(creds.get("port", 3306))

    connection_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(connection_url, pool_pre_ping=True)


def get_session(engine) -> Session:
    """
    Create a SQLAlchemy session.

    Args:
        engine (sqlalchemy.Engine): SQLAlchemy engine instance.

    Returns:
        sqlalchemy.orm.Session: Session object.
    """
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


# Database operations
def create_products_table(engine) -> None:
    """
    Create the 'products' table if it does not exist.

    Args:
        engine (sqlalchemy.Engine): SQLAlchemy engine instance.
    """
    Base.metadata.create_all(engine)
    logger.info("'products' table created or already exists.")


def insert_sample_product(
    session: Session,
    name: str = "Sample Product",
    description: str = "This is a test",
    status: str = "ACTIVE",
) -> None:
    """
    Insert a sample product into the database if it does not already exist.

    Args:
        session (Session): Active SQLAlchemy session.
        name (str): Product name.
        description (str): Product description.
        status (str): Product status.
    """
    existing = session.execute(
        select(Product).filter_by(name=name)
    ).scalar_one_or_none()
    if existing:
        logger.info("Product already exists: %s. Skipping insertion.", name)
        return

    product = Product(name=name, description=description, status=status)
    session.add(product)
    session.commit()
    logger.info("Inserted sample product: %s", name)


def list_products(session: Session) -> None:
    """
    Fetch and log all products from the database.

    Args:
        session (Session): Active SQLAlchemy session.
    """
    products = session.execute(select(Product)).scalars().all()
    if not products:
        logger.info("No products found.")
        return

    logger.info("Current products in DB:")
    for p in products:
        logger.info(p)


# Main execution
def main() -> None:
    """
    Main entry point to create table, insert a sample product, and list all products.
    """
    engine = get_db_engine(DB_SECRET_ARN)
    session = get_session(engine)

    try:
        create_products_table(engine)
        insert_sample_product(session)
        list_products(session)
    finally:
        session.close()
        logger.info("Database session closed.")


if __name__ == "__main__":
    main()
