import json
import requests

class DataFetch:
    def __init__(self, url: str, extra_url: str="", params: dict={}, data: dict=None):
        self.__url = url + extra_url
        self.__params = params
        self.__data = data

    @property
    def url(self) -> str:
        return self.__url

    @property
    def extra_url(self) -> str:
        return self.__url

    @property
    def params(self) -> dict:
        return self.__params

    @property
    def data(self) -> dict | None:
        return self.__data

    @url.setter
    def url(self, value: str) -> None:
        self.__url = value

    @extra_url.setter
    def extra_url(self, value: str) -> None:
        self.__url = value

    @params.setter
    def params(self, value: dict) -> None:
        self.__params = value

    @data.setter
    def data(self, value: dict) -> None:
        self.__data = value

    def __validate_response(self, response) -> json:
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get(self) -> dict:
        response = requests.get(self.__url, self.__params)
        return self.__validate_response(response)

    def post(self) -> dict:
        response = requests.post(self.__url, json=self.__data)
        return self.__validate_response(response)

    def put(self) -> dict:
        response = requests.put(self.__url, json=self.__data)
        return self.__validate_response(response)

    def delete(self) -> dict:
        response = requests.delete(self.__url, json=self.__data)
        return self.__validate_response(response)
