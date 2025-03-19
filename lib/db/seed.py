from lib.db.models import get_session, Category, Wine

def seed_data():
    session = get_session()
    try:
        # Check if categories exist
        if not session.query(Category).filter_by(name="Red Wine").first():
            Category.create(session, "Red Wine")
        if not session.query(Category).filter_by(name="White Wine").first():
            Category.create(session, "White Wine")
        
        # Get category IDs
        red_wine = session.query(Category).filter_by(name="Red Wine").first()
        white_wine = session.query(Category).filter_by(name="White Wine").first()
        
        # Check if wines exist
        if not session.query(Wine).filter_by(name="Merlot").first():
            Wine.create(session, "Merlot", red_wine.id)
        if not session.query(Wine).filter_by(name="Chardonnay").first():
            Wine.create(session, "Chardonnay", white_wine.id)
        
        print("Seed data added successfully or already exists.")
    except ValueError as e:
        session.rollback()
        print(f"Error seeding data: {e}")
    except Exception as e:
        session.rollback()
        print(f"Unexpected error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()