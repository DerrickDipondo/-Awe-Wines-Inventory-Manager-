# Awe Wines Inventory Management
A CLI application to manage wine inventory using Python and SQLAlchemy.

## Setup
1. Install dependencies: `pipenv install`
2. Run: `pipenv run python inventory.py`

## Features
- Manage categories (create, delete, list, find by ID, view related wines).
- Manage wines (create, delete, list, find by ID).
- Seed initial data for testing.

## Usage
- **Main Menu**: Choose 1 for categories, 2 for wines, 3 to exit, 4 to seed data.
- **Category Menu**: Create (1), Delete (2), List All (3), Find by ID (4), View Wines (5), Back (6).
- **Wine Menu**: Create (1), Delete (2), List All (3), Find by ID (4), Back (5).
- Names must be unique for categories and wines.

## Troubleshooting
- Error: "Name already exists" - Ensure unique names.
- Invalid ID - Use numeric IDs only.