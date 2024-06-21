# REMBG - Background Remover

[REMBG](https://hub.docker.com/r/ryuga64/bg-rem) is a background remover tool that uses the U2 Net model to remove backgrounds from PNG images using AI. This project provides a simple Flask application to interact with the background removal functionality and includes a Docker setup for containerization.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [To-Do](#to-do)
- [Contributing](#contributing)
- [License](#license)

## Introduction

REMBG is a powerful tool that leverages the U2 Net model to remove backgrounds from PNG images with high accuracy. This project includes a Flask application for easy interaction and a Docker setup to ensure a consistent and reproducible environment.

## Features

- Background removal using the U2 Net model.
- Simple Flask application for easy interaction.
- Dockerized for consistent and reproducible environments.

## Requirements

- Python 3.7+
- Docker (optional for containerization)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rembg.git
   cd rembg
2. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the Flask application:
   ```bash
   python basic.py
2. Open your browser and navigate to http://127.0.0.1:5000 to interact with the application.

## Docker


### Building the Docker Image
1. Ensure you have Docker installed on your system.
2. Navigate to the project directory.
3. Build the Docker image:
   ``` bash
   docker build -t rembg .
### Running the Docker Container
1. Run the Docker container with port mapping:

   ```bash
	docker run -p 5000:5000 rembg
2. Open your browser and navigate to http://127.0.0.1:5000 to interact with the application.

## To-Do

 - Deployment of the Flask application on [Vercel](https://vercel.com) app pending.
 - Deployment of the Docker container on [Google Cloud Run](https://cloud.google.com/run?hl=en) or [Amazon Elastic Services](https://aws.amazon.com/ecs/).
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Clone the Repository 
> git clone https://github.com/heroaks/rembg.git

### Pull the Docker Image
> docker pull ryuga64/bg-rem