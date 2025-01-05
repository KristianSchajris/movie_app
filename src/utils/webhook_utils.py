import json
import requests

from helpers.load_env.load_env import LoadEnv

def send_to_webhook(data: dict):
    """
    Sends a dictionary of data to a specified webhook URL.

    Args:
        data (dict): The data to be sent to the webhook.
    Returns:
        int: The HTTP status code of the response.
    Raises:
        EnvironmentError: If the 'WEBHOOK_URL' environment variable is not set.
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    webhook_url = LoadEnv("WEBHOOK_URL")
    response = requests.post(webhook_url.get_value(), json=json(data))

    if response.status_code != 200:
        print("Failed to send data to webhook.")
    return response.status_code
