from common.models import Product
from common.db import get_session


def lambda_handler(event, context):
    """
    AWS Lambda handler to add a new Product to the database.

    Raises:
        ValueError: If required fields (name, status) are missing.
    """

    # Extract arguments from the event
    args = event.get("arguments", {})
    name = args.get("name")
    description = args.get("description")
    status = args.get("status")

    # Validate required fields
    if not name or not status:
        raise ValueError("Name and status are required")

    # Open a database session using context manager
    with get_session() as session:
        # Create a new Product ORM instance
        product = Product(name=name, description=description, status=status)

        # Stage the product for insert
        session.add(product)

        # Commit the transaction
        session.commit()

        # Refresh the instance so auto-generated fields (id, created_at) are populated
        session.refresh(product)

        # Return the product as dictionary
        return product.as_dict()
