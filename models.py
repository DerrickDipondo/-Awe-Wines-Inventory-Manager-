from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# Setup SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

# Model: Category
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    wines = relationship("Wine", back_populates="category")

    @classmethod
    def create(cls, session, name):
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
        category = cls.find_by_id(session, id)
        if category:
            session.delete(category)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

# Model: Wine
class Wine(Base):
    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="wines")

    @classmethod
    def create(cls, session, name, category_id):
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
        wine = cls.find_by_id(session, id)
        if wine:
            session.delete(wine)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def __repr__(self):
        return f"<Wine(id={self.id}, name={self.name}, category_id={self.category_id})>"