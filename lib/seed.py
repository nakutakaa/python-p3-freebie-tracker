

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie # Imports our SQLAlchemy models

# --- Database Setup ---
# Connects to our SQLite database file named 'freebies.db'
engine = create_engine('sqlite:///freebies.db')

# Creates a configured Session class from the engine
Session = sessionmaker(bind=engine)

# Creates an actual session instance to interact with the database
session = Session()

print("--- Seeding Database ---")

# --- Clear Existing Data ---
# during development to ensure a clean slate each time seed.py is run
session.query(Freebie).delete() # Deletes all existing freebies
session.query(Dev).delete() # Deletes all existing developers
session.query(Company).delete() # Deletes all existing companies
session.commit() # Commits these deletion changes to the database
print("Cleared existing data.")

# --- Create Company Instances ---
print("Creating companies...")
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Microsoft", founding_year=1975)
company3 = Company(name="Apple", founding_year=1976)

session.add_all([company1, company2, company3]) # Adds the new company objects to the session
session.commit() # Commit to ensure they get their IDs for foreign keys
print("Companies created.")

# --- Create Dev Instances ---
print("Creating developers...")
dev1 = Dev(name="Alice Developer")
dev2 = Dev(name="Bob Coder")
dev3 = Dev(name="Charlie Hacker")

session.add_all([dev1, dev2, dev3])
session.commit() # Commit to ensure they get their IDs for foreign keys
print("Developers created.")

# --- Creating Freebie Instances ---
print("Creating freebies...")

# Freebies for Alice (dev1)
f1 = Freebie(item_name="Google T-shirt", value=30, dev_id=dev1.id, company_id=company1.id)
f2 = Freebie(item_name="Microsoft Mug", value=15, dev_id=dev1.id, company_id=company2.id)
f3 = Freebie(item_name="Apple Stickers", value=5, dev_id=dev1.id, company_id=company3.id)

# Freebies for Bob (dev2)
f4 = Freebie(item_name="Google Water Bottle", value=20, dev_id=dev2.id, company_id=company1.id)
f5 = Freebie(item_name="Microsoft Backpack", value=50, dev_id=dev2.id, company_id=company2.id)

# Freebies for Charlie (dev3)
f6 = Freebie(item_name="Apple Pen", value=10, dev_id=dev3.id, company_id=company3.id)
f7 = Freebie(item_name="Google Keychain", value=3, dev_id=dev3.id, company_id=company1.id)
f8 = Freebie(item_name="Microsoft Swag Bag", value=75, dev_id=dev3.id, company_id=company2.id)


session.add_all([f1, f2, f3, f4, f5, f6, f7, f8]) # Adds all freebie objects to the session
session.commit()  # Commits all new freebies to the database
print("Freebies created.")

print("--- Seeding Complete! ---")
session.close() # Always close the session when done.