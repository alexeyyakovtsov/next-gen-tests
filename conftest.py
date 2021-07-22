import pytest
import requests
import configparser
import headers.headers as headers
import randomaizer
from json import loads, dumps


config = configparser.ConfigParser()
config.read('../../config.ini')


@pytest.fixture
def auth_login():
    data = {
        "email": config['NEXT_GEN']['email'],
        "password": config['NEXT_GEN']['password']
    }

    response = requests.post(
        url=config['NEXT_GEN']['base_url'] + '/auth/login', 
        json=data,
        headers=headers.HEADERS
    )

    assert response.status_code == 200
    assert response.json() is not None
    return response.json()["token"]


@pytest.fixture
def create_goals():
    random_data = randomaizer.RandomData()
    random_word = random_data.generate_word(5)

    data = {
        "name": random_word,
        "due_date": "2022-12-10T00:00:00.000Z"
    }

    return data


@pytest.fixture
def get_last_goal_id(auth_login):
    headers_a = {"Authorization": "Bearer " + auth_login}

    response = requests.get(
        url=config['NEXT_GEN']['base_url'] + '/goals',
        headers=headers_a
    )

    return response.json()[-1]["id"]
