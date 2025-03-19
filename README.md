# Awe Wines Inventory Management
A CLI application to manage wine inventory using Python and SQLAlchemy.

## Setup
1. Install dependencies: `pipenv install`
2. Run: `pipenv run python -m lib.cli`

## Features
- Manage categories (create, delete, list, find by ID, view related wines).
- Manage wines (create, delete, list, find by ID).
- Seed initial data for testing.

## Usage
- **Main Menu**: Choose 1 for categories, 2 for wines, 3 to exit, 4 to seed data.
- **Category Menu**: Create (1), Delete (2), List All (3), Find by ID (4), View Wines (5), Back (6).
- **Wine Menu**: Create (1), Delete (2), List All (3), Find by ID (4), Back (5).
- Names must be unique for categories and wines.

## Files
### lib/cli.py
Main CLI script. Runs an interactive loop to manage inventory via menus.
- `run_cli()`: Core loop handling user input and menu navigation.

### lib/db/models.py
Defines database schema and operations using SQLAlchemy.
- `Category`: Model for wine categories with methods:
  - `create(session, name)`: Adds a new category.
  - `delete(session, id)`: Removes a category by ID.
  - `get_all(session)`: Lists all categories.
  - `find_by_id(session, id)`: Finds a category by ID.
- `Wine`: Model for wines with methods:
  - `create(session, name, category_id)`: Adds a new wine.
  - `delete(session, id)`: Removes a wine by ID.
  - `get_all(session)`: Lists all wines.
  - `find_by_id(session, id)`: Finds a wine by ID.
- `get_session()`: Returns a new database session.
- `initialize_db()`: Creates database tables.

### lib/db/seed.py
Seeds initial test data.
- `seed_data()`: Adds "Red Wine" and "White Wine" categories, plus "Merlot" and "Chardonnay" wines.

### lib/helpers.py
Utility functions for displaying menus.
- `main_menu()`: Shows main menu options.
- `category_menu()`: Shows category menu options.
- `wine_menu()`: Shows wine menu options.

### lib/debug.py
Debugging tool for inspecting the database.
- `debug_db()`: Prints all categories and wines.

## Troubleshooting
- "Name already exists": Use unique names (enforced by database constraints).
- "Invalid ID": Use numeric IDs only.