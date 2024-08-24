# FastAPI QuickStart

FastAPI QuickStart is a tool to quickly set up a basic structure for a FastAPI application.

## Installation

```
pip install fastapi-quickstart-genesis
```

## Usage

To create a new FastAPI project structure:

```
python -m fastapi_quickstart my_app
```

or

```
fastapi_quickstart my_app
```

This will create a new directory `my_app` with a basic FastAPI application structure.

## Project Structure

The generated project will have the following structure:

```
my_app/
├── app/
│   ├── main.py
│   └── models.py
├── tests/
└── requirements.txt
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install development dependencies: `pip install -r requirements.txt`
5. Install the package in editable mode: `pip install -e .`

## License

This project is licensed under the MIT License.
