# Streamlit To-Do App

A simple and interactive to-do list application built using Streamlit. This application allows users to add, display, and analyze their to-do items in a user-friendly interface.

## Features

- Add new to-do items with a simple input form.
- View the list of to-do items with options to mark them as complete or delete them.
- Visualize the statistics of completed and pending tasks.

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-todo-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the application, run the following command in your terminal:
```
streamlit run src/main.py
```

Open your web browser and go to `http://localhost:8501` to access the application.

## Project Structure

```
streamlit-todo-app
├── src
│   ├── main.py               # Entry point of the Streamlit application
│   ├── components             # Contains UI components for the app
│   │   ├── __init__.py
│   │   ├── todo_input.py      # Input form for adding to-do items
│   │   ├── todo_display.py     # Displays the list of to-do items
│   │   └── analytics.py        # Visualizes task statistics
│   └── utils                  # Utility functions for data handling
│       ├── __init__.py
│       └── data_handler.py     # Functions for loading and saving to-do items
├── data
│   └── todos.json            # JSON file for persistent storage of tasks
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.