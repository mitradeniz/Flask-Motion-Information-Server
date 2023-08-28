# Motion Information Server with Flask and Socket

This repository contains code for a simple server that receives motion information from a client using both Flask and Socket programming. The server listens for incoming data over a socket connection and communicates with clients using the Flask framework.

## Features

- Listens for motion data from clients over a socket connection.
- Provides an API endpoint to retrieve motion information using Flask.

## Requirements

- Python 3.x
- Flask library (`pip install flask`)

## Usage

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the Flask library if you haven't already by running `pip install flask`.
4. Open a terminal and navigate to the repository directory.
5. Run the server by executing the `server.py` file using Python: `python server.py`.
6. The server will start and listen on port 8081.

## API Endpoint

You can access the motion information using the following endpoint:


## Notes

- The server listens on all available IP addresses (0.0.0.0) on port 8081.
- The code demonstrates the usage of Flask to create an API endpoint and Socket programming for communication with clients.
- The server waits for incoming connections over the socket connection, receives motion data, and responds accordingly.

## Author

mitradeniz

## License

This project is licensed under the [MIT License](LICENSE).

For more details, please refer to the [GitHub repository:] [(https://github.com/mitradeniz/Flask-Motion-Information-Server)].

