## Weather App
This is a simple application that fetches weather data for Kraków using the OpenWeatherMap API and logs the temperature and weather description.

## Getting Started
To run this application, you will need an API key from OpenWeatherMap.

## Clone the repository:

```
git clone https://github.com/KamilWardyla/actions-weather
```

## Install the required dependencies:

```
pip install requests
```

## Logging
The application logs the weather information to a file named weather.log. The log file is encoded in UTF-8, and it includes the timestamp, logger name, log level, and log message.

## GitHub Actions
This repository includes a GitHub Actions workflow that can be used to automate the execution of the application. The workflow is triggered on every push event to the main branch.

The workflow executes the following steps:

Set up Python environment.
Install dependencies.
Run the application.
The workflow also sets the API_KEY environment variable from the repository's secrets to ensure that the API key is securely passed to the application.

## To use GitHub Actions with this repository:

Generate an API key from OpenWeatherMap.

Create a new secret in your GitHub repository with the name API_KEY and paste the API key as the value.

Push your changes to the main branch, and the workflow will automatically execute.

You need to have the permissions to set up secrets and enable GitHub Actions for your repository.

