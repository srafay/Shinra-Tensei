from common.models import Product
from common.db import get_session
from sqlalchemy import select


def lambda_handler(event, context):
    """
    AWS Lambda handler to update a Product.

    Returns:
        dict: Updated product as a dictionary

    Raises:
        ValueError: If required fields are missing or product is not found
    """
    args = event.get("arguments", {})
    product_id = args.get("id")
    name = args.get("name")
    description = args.get("description")
    status = args.get("status")

    if not product_id or not name or not status:
        raise ValueError("Missing one of the required fields: id, name, or status")

    with get_session() as session:
        # Fetch product by ID
        product = session.execute(
            select(Product).filter_by(id=int(product_id))
        ).scalar_one_or_none()

        if not product:
            raise ValueError(f"Product with ID {product_id} not found")

        # Update fields
        product.name = name
        product.description = description
        product.status = status

        # Commit changes
        session.commit()
        session.refresh(product)

        return product.as_dict()
