from common.models import Product
from common.db import get_session


def lambda_handler(event, context):
    """
    AWS Lambda handler to fetch a single Product by ID.

    Raises:
        ValueError: If 'id' is missing from arguments.
    """

    # Extract product ID from event arguments
    product_id = event.get("arguments", {}).get("id")
    if not product_id:
        raise ValueError("Product ID is required")

    # Open a database session
    with get_session() as session:
        # Query for the product by ID
        product = session.query(Product).filter(Product.id == int(product_id)).first()

        # If no product is found, return empty
        if not product:
            return {}

        # Return the product as a dictionary
        return product.as_dict()
