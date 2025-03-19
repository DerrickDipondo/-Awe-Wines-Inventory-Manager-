from lib.db.models import get_session, Category, Wine
from lib.db.models import initialize_db
from lib.helpers import main_menu, category_menu, wine_menu

initialize_db() 

# Main menu function
def main_menu():
    """Display the main menu options."""
    print("\n=== Awe Wines Inventory Management ===")
    print("1. Manage Categories")
    print("2. Manage Wines")
    print("3. Exit")
    print("4. Seed Initial Data")

# Category menu function
def category_menu():
    """Display the category menu options."""
    print("\n=== Category Menu ===")
    print("1. Create Category")
    print("2. Delete Category")
    print("3. Display All Categories")
    print("4. Find Category by ID")
    print("5. View Wines by Category")
    print("6. Back")

# Wine menu function
def wine_menu():
    """Display the wine menu options."""
    print("\n=== Wine Menu ===")
    print("1. Create Wine")
    print("2. Delete Wine")
    print("3. Display All Wines")
    print("4. Find Wine by ID")
    print("5. Back")

def run_cli():
    """Run the command-line interface for inventory management."""
    session = get_session()
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            while True:
                category_menu()
                sub_choice = input("Enter your choice (1-6): ").strip()
                
                if sub_choice == "1":
                    name = input("Enter category name: ").strip()
                    if name:
                        try:
                            Category.create(session, name)
                            print(f"Category '{name}' created.")
                        except ValueError as e:
                            print(f"Error: {e}")
                    else:
                        print("Error: Name cannot be empty.")
                
                elif sub_choice == "2":
                    id = input("Enter category ID to delete: ").strip()
                    if id.isdigit() and Category.delete(session, int(id)):
                        print(f"Category {id} deleted.")
                    else:
                        print("Error: Invalid ID or category not found.")
                
                elif sub_choice == "3":
                    categories = Category.get_all(session)
                    if categories:
                        for cat in categories:
                            print(cat)
                    else:
                        print("No categories found.")
                
                elif sub_choice == "4":
                    id = input("Enter category ID: ").strip()
                    if id.isdigit():
                        category = Category.find_by_id(session, int(id))
                        print(category if category else "Category not found.")
                    else:
                        print("Error: ID must be a number.")
                
                elif sub_choice == "5":
                    id = input("Enter category ID to view wines: ").strip()
                    if id.isdigit():
                        category = Category.find_by_id(session, int(id))
                        if category and category.wines:
                            print(f"Wines in Category {id} ({category.name}):")
                            for wine in category.wines:
                                print(wine)
                        else:
                            print("No wines found or category not found.")
                    else:
                        print("Error: ID must be a number.")
                
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif choice == "2":
            while True:
                wine_menu()
                sub_choice = input("Enter your choice (1-5): ").strip()
                
                if sub_choice == "1":
                    name = input("Enter wine name: ").strip()
                    cat_id = input("Enter category ID: ").strip()
                    if name and cat_id.isdigit():
                        category = Category.find_by_id(session, int(cat_id))
                        if category:
                            try:
                                Wine.create(session, name, int(cat_id))
                                print(f"Wine '{name}' created.")
                            except ValueError as e:
                                print(f"Error: {e}")
                        else:
                            print("Error: Category not found.")
                    else:
                        print("Error: Invalid input or category not found.")
                
                elif sub_choice == "2":
                    id = input("Enter wine ID to delete: ").strip()
                    if id.isdigit() and Wine.delete(session, int(id)):
                        print(f"Wine {id} deleted.")
                    else:
                        print("Error: Invalid ID or wine not found.")
                
                elif sub_choice == "3":
                    wines = Wine.get_all(session)
                    if wines:
                        for wine in wines:
                            print(wine)
                    else:
                        print("No wines found.")
                
                elif choice == "4":
                    from lib.db.seed import seed_data
                    seed_data()
                
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        elif choice == "4":
          from lib.db.seed import seed_data
          seed_data()
    
    session.close()

if __name__ == "__main__":
    run_cli()