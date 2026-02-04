# Book Store Console Application

## Overview
This project is a **console-based Book Store application written in Python** focused on demonstrating **data persistence strategies and architectural evolution**.

Rather than emphasizing complex business rules, the project explores multiple ways of storing and retrieving data, showing how the same application logic can work with:
- in-memory data structures
- flat files (CSV)
- structured files (JSON)
- a relational database (SQLite)

Each implementation follows the same interface (add, list, update, delete), allowing direct comparison between persistence approaches.

---

## Features
- Add new books with title and author
- List all stored books
- Mark books as read
- Delete books from the collection
- Persist data between executions using file storage
- Simple and clear text-based menu interface

---

## Project Evolution
The core idea of this project is to demonstrate **progressive refactoring of the persistence layer** while keeping the application behavior consistent.

### 1. In-Memory List Storage
- Used a Python list of dictionaries as the data source
- Data existed only during program execution
- Established the base CRUD logic and application flow

### 2. CSV File Persistence
- Replaced in-memory storage with a CSV file
- Each operation reads from and writes back to the file
- Boolean values are represented as `0` (unread) and `1` (read)
- Reinforced understanding of file I/O and data reconstruction

### 3. JSON File Persistence
- Migrated storage from CSV to JSON
- Enabled structured data representation using dictionaries
- Preserved native data types such as booleans
- Simplified serialization and deserialization logic

### 4. SQLite Database Storage
- Introduced SQLite using Python's `sqlite3` module
- Implemented persistent storage with SQL queries
- Used a relational schema with a primary key
- Improved robustness and scalability compared to file-based solutions

### 5. Custom Database Context Manager
- Refactored SQLite access using a custom context manager
- Centralized connection handling and transaction management
- Ensured automatic commit or rollback behavior
- Improved code readability and safety

---

## Technologies Used
- Python 3
- CSV file handling
- JSON file handling
- SQLite (`sqlite3`)
- Custom context manager for database connections
- Standard library only (no external dependencies)

---

## Design Decisions
- **Separation of concerns**: user interface logic is separated from data handling logic
- **Pluggable persistence layer**: the same application logic works with different storage backends
- **Auto-save strategy**: data is persisted immediately after write operations
- **Explicit load/save operations**: loading occurs at application start or when explicitly requested by the user
- **Type hinting**: Python type annotations are used to improve readability, correctness, and editor support
- **Context-managed database access**: a custom context manager ensures safe connection handling and transaction control

---

## How It Works
1. The application exposes the same operations regardless of storage type (add, list, mark as read, delete)
2. Each persistence implementation handles its own storage logic internally
3. File-based versions reconstruct application state from disk on each operation
4. The SQLite version delegates persistence to the database engine
5. The context manager ensures database connections are safely opened and closed

---

## Running the Application
```bash
python app.py
```
Follow the on-screen menu instructions to interact with the book store.

---

## Learning Outcomes
This project demonstrates:
- CRUD operations across multiple persistence layers
- Differences between in-memory, file-based, and database storage
- Manual serialization and deserialization of data
- SQL-based data manipulation using SQLite
- Proper resource management with custom context managers
- Practical use of Python type hints for function signatures and data structures
- Incremental refactoring without breaking application logic

---

## Possible Future Improvements
- Add unit tests
- Improve input validation
- Implement search and filtering features
- Add support for multiple users
- Convert the project into a small REST API

---

## Author
Matheus T.

---

This project was built as a learning exercise and serves as a foundation for more advanced backend and data-driven applications.

