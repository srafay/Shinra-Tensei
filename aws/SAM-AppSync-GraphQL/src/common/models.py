from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, func

# Base class that maintains a catalog of classes and tables
# All ORM models will inherit from this Base
Base = declarative_base()


class Product(Base):
    """
    SQLAlchemy ORM model for the 'products' table.

    Represents a product with the following attributes:
    - id: Primary key (auto-incrementing integer)
    - name: Product name (string, required, max length 255)
    - description: Detailed description (text field, optional)
    - status: Status of the product (e.g., 'active', 'inactive')
    - created_at: Timestamp when the record was created (defaults to NOW())

    Methods:
        __str__: Returns a readable string representation of the Product instance.
        as_dict: Returns the Product instance as a dictionary (useful for JSON serialization).
    """

    __tablename__ = "products"  # Database table name

    # Columns definition
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID
    name = Column(String(255), nullable=False)  # Product name (required)
    description = Column(Text)  # Longer text description (Optional)
    status = Column(String(50), nullable=False)  # Status (required)
    created_at = Column(
        DateTime, server_default=func.now()
    )  # Default to current timestamp

    def __str__(self):
        """
        String representation of the Product.
        Useful for debugging and logging.
        """
        return (
            f"ID: {self.id} | "
            f"Name: {self.name} | "
            f"Status: {self.status} | "
            f"Description: {self.description} | "
            f"Created At: {self.created_at}"
        )

    def as_dict(self):
        """
        Convert the Product instance into a dictionary.
        Useful for serializing to JSON (for APIs).

        Returns:
            dict: Dictionary representation of the product
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "createdAt": self.created_at.isoformat(),
        }
