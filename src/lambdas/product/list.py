from common.models import Product
from common.db import get_session


def lambda_handler(event, context):
    """
    AWS Lambda handler to fetch all products.

    Returns:
        list[dict]: List of products as dictionaries
    """
    with get_session() as session:
        products = session.query(Product).all()
        return [p.as_dict() for p in products]
