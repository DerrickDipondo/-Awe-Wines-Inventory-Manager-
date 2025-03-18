from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# Setup SQLAlchemy database connection
Base = declarative_base()
engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    """Return a new SQLAlchemy session for database operations."""
    return Session()

def initialize_db():
    """Create tables in the database if they don’t exist."""
    Base.metadata.create_all(engine)

# Model: Category representing wine categories
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Unique category names
    wines = relationship("Wine", back_populates="category")

    @classmethod
    def create(cls, session, name):
        """Create a new category with the given name."""
        category = cls(name=name)
        session.add(category)
        try:
            session.commit()
            return category
        except IntegrityError:
            session.rollback()
            raise ValueError("Category name already exists.")

    @classmethod
    def delete(cls, session, id):
        """Delete a category by ID if it exists."""
        category = cls.find_by_id(session, id)
        if category:
            session.delete(category)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        """Return all categories."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        """Find a category by ID."""
        return session.query(cls).filter_by(id=id).first()

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

# Model: Wine representing individual wines
class Wine(Base):
    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Unique wine names
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="wines")

    @classmethod
    def create(cls, session, name, category_id):
        """Create a new wine with the given name and category ID."""
        wine = cls(name=name, category_id=category_id)
        session.add(wine)
        try:
            session.commit()
            return wine
        except IntegrityError:
            session.rollback()
            raise ValueError("Wine name already exists.")

    @classmethod
    def delete(cls, session, id):
        """Delete a wine by ID if it exists."""
        wine = cls.find_by_id(session, id)
        if wine:
            session.delete(wine)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        """Return all wines."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        """Find a wine by ID."""
        return session.query(cls).filter_by(id=id).first()

    def __repr__(self):
        return f"<Wine(id={self.id}, name={self.name}, category_id={self.category_id})>"