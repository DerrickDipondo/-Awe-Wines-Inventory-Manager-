from lib.db.models import get_session, Category, Wine

def debug_db():
    """Print all categories and wines in the database."""
    session = get_session()
    print("Categories:", session.query(Category).all())
    print("Wines:", session.query(Wine).all())
    session.close()

if __name__ == "__main__":
    debug_db()