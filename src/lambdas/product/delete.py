from common.models import Product
from common.db import get_session
from sqlalchemy import select


def lambda_handler(event, context):
    """
    AWS Lambda handler to delete a Product by ID.

    Raises:
        ValueError: If 'id' is missing or the product does not exist.
    """

    # Extract product ID from the event
    args = event.get("arguments", {})
    product_id = args.get("id")

    if not product_id:
        raise ValueError("Product 'id' is required")

    # Open a database session using context manager
    with get_session() as session:
        # Query for the product by ID
        product = session.execute(
            select(Product).filter_by(id=int(product_id))
        ).scalar_one_or_none()

        # If product does not exist, raise error
        if not product:
            raise ValueError(f"Product with id {product_id} not found")

        # Delete the product from the database
        session.delete(product)
        session.commit()

        # Return the deleted product as a dictionary
        return product.as_dict()
