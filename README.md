# Flask Weather API

This Flask application provides weather data for cities. The weather data is stored in memory as a Python dictionary, and the application follows the Test-Driven Development (TDD) approach.

## Features

- Retrieve weather information for a given city.
- Add new weather data for a city.
- Update weather data for a city.
- Delete weather data for a city.

## Requirements

- Python 3.x
- Flask
- pytest

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/DishaGup/Flask-Test-Driven-Development-TDD-.git
   ```

3. Create and activate a virtual environment:

   - For Windows:

     ```
     python -m venv env
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     python3 -m venv env
     source env/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```
   python app.py
   ```

2. The application is now running on http://localhost:5000.

3. Endpoints:

   - **GET** `/weather/<string:city>`: Retrieve weather information for a given city.
   - **POST** `/weather`: Add new weather data for a city.
   - **PUT** `/weather/<string:city>`: Update weather data for a city.
   - **DELETE** `/weather/<string:city>`: Delete weather data for a city.

   Note: Replace `<string:city>` with the actual name of the city.

## Testing

1. To run the tests, make sure the Flask server is not running.

2. In the project directory, run the following command:

   ```
   pytest
   ```

   This will execute all the tests and display the results.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
