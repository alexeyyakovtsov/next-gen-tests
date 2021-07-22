import requests
import configparser
import pytest
import headers.headers as headers


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_post_goals_expected_200(auth_login, create_goals):
    headers_a = {"Authorization": "Bearer " + auth_login}

    response = requests.post(
        url=config['NEXT_GEN']['base_url'] + '/goals',
        headers=headers_a,
        json=create_goals
    )

    assert response.status_code == 200
    assert 'id' in response.json().keys()

