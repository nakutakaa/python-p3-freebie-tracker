from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref # Import relationship for object relations
from sqlalchemy.ext.declarative import declarative_base

# --- Metadata Setup ---
# Defines naming conventions for foreign key constraints,
# which helps Alembic in generating migrations
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Base class from which all our ORM models will inherit
Base = declarative_base(metadata=metadata)

# --- Company Model ---
class Company(Base):
    __tablename__ = 'companies'

# Define columns for the 'companies' table
    id = Column(Integer(), primary_key=True)  # Primary key column
    name = Column(String()) # Company name
    founding_year = Column(Integer()) # Year the company was founded

    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary="freebies", viewonly=True, back_populates="companies")

    def get_devs_who_received_freebies(self):
        """Returns a list of unique Dev objects who have received freebies from this Company."""
        # Directly uses the 'devs' relationship defined above
        return self.devs

# String representation for easy debugging/printing of Company objects
    def __repr__(self):
        return f'<Company {self.name}>'

# --- Dev Model ---
class Dev(Base):
    __tablename__ = 'devs' # Maps this class to the 'devs' table

    # Defines columns for the 'devs' table
    id = Column(Integer(), primary_key=True) # Primary key column
    name= Column(String()) # Developer name

# A Dev can have many Freebies (one-to-many relationship)
    # 'back_populates' links this relationship back to the 'dev' attribute on the Freebie model
    freebies = relationship("Freebie", back_populates="dev")

     # A Dev can be associated with many Companies through Freebies (many-to-many relationship)
    # 'secondary="freebies"' specifies the intermediary table (Freebie)
    # 'viewonly=True' for reading links, not creating
    # 'back_populates' links this relationship back to the 'devs' attribute on the Company model
    companies = relationship("Company", secondary="freebies", viewonly=True, back_populates="devs")

# Implementing Methods & Aggregation
    def get_companies_they_received_from(self):
        """Returns a list of unique Company objects this Dev has received freebies from."""
        # Directly uses the 'companies' relationship defined above
        return self.companies
    
    def total_freebie_value(self):
        """Calculates and returns the total monetary value of all freebies collected by this Dev."""
         # Sums the 'value' attribute for each Freebie object associated with this Dev
        return sum(freebie.value for freebie in self.freebies)

# String representation for easy debugging/printing of Dev objects
    def __repr__(self):
        return f'<Dev {self.name}>'

# --- Freebie Model ---
class Freebie(Base):
    __tablename__ = 'freebies' # Maps this class to the 'freebies' table

# Defines columns for the 'freebies' table
    id = Column(Integer(), primary_key=True) # Primary key column
    item_name = Column(String()) # Name of the freebie item
    value = Column(Integer()) # Monetary value of the freebie

# Defines Foreign Keys
# Links to the 'devs' table using the 'id' column of the Dev model
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    # Links to the 'companies' table using the 'id' column of the Company model
    company_id = Column(Integer(), ForeignKey('companies.id'))

    # Establishes a one-to-many relationship with the Dev model
    # 'back_populates' links this back to the 'freebies' attribute on the Dev model
    dev = relationship("Dev", back_populates="freebies")

     # Establishes a one-to-many relationship with the Company model
    # 'back_populates' links this back to the 'freebies' attribute on the Company model
    company = relationship("Company", back_populates="freebies")

# String representation for easy debugging/printing of Freebie objects
    def __repr__(self):
        return f'<Freebie {self.item_name} (Value:${self.value})>'