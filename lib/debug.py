

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie # Import our SQLAlchemy models

# This block runs only when debug.py is executed directly
if __name__ == '__main__':
    
    # --- Database Setup ---
    # Connects to our SQLite database file named 'freebies.db'
    engine = create_engine('sqlite:///freebies.db')
    # Creates a configured Session class from the engine
    Session = sessionmaker(bind=engine)
    # Creates an actual session instance to interact with the database
    session = Session() 

# Inform the user how to use the debugger
    print("Debugger active. Use 'session' to query data, and 'Company', 'Dev', 'Freebie' for models.")
    print("For example: google = session.query(Company).filter_by(name='Google').first()")
    print("Type 'c' or 'continue' to exit the debugger if needed, or 'exit()' to quit directly.")

# --- Start Debugger ---
    # Imports ipdb and starts the interactive debugger at this point
    import ipdb; ipdb.set_trace() #  starts the debugger

    # Closes the session when done (will happen when debugger exits)
    session.close()