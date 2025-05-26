

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie # Import my models
import sys

# --- Database Setup ---
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# --- CLI Functions ---
def list_all_companies():
    """Lists all companies in the database."""
    companies = session.query(Company).all()
    if not companies:
        print("No companies found.")
        return

    print("\n--- All Companies ---")
    for company in companies:
        print(f"ID: {company.id}, Name: {company.name}, Founded: {company.founding_year}")
    print("---------------------")

def list_all_devs():
    """Lists all developers in the database."""
    devs = session.query(Dev).all()
    if not devs:
        print("No developers found.")
        return

    print("\n--- All Developers ---")
    for dev in devs:
        print(f"ID: {dev.id}, Name: {dev.name}")
    print("----------------------")

def list_all_freebies():
    """Lists all freebies in the database."""
    freebies = session.query(Freebie).all()
    if not freebies:
        print("No freebies found.")
        return

    print("\n--- All Freebies ---")
    for freebie in freebies:
        print(f"ID: {freebie.id}, Item: {freebie.item_name}, Value: ${freebie.value}, Dev: {freebie.dev.name}, Company: {freebie.company.name}")
    print("--------------------")

def show_help():
    """Displays available commands."""
    print("\n--- Commands ---")
    print("companies - List all companies")
    print("devs      - List all developers")
    print("freebies  - List all freebies")
    print("help      - Show this help message")
    print("exit      - Exit the application")
    print("----------------")

# --- Main CLI Loop ---
def main():
    print("Welcome to the Freebie Tracker CLI!")
    show_help() # Show commands on startup

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "companies":
            list_all_companies()
        elif command == "devs":
            list_all_devs()
        elif command == "freebies":
            list_all_freebies()
        elif command == "help":
            show_help()
        elif command == "exit":
            print("Exiting Freebie Tracker. Goodbye!")
            session.close() # Close the database session
            sys.exit(0) # Exit the script
        else:
            print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()