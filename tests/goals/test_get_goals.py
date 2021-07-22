import requests
import configparser
import pytest
import headers.headers as headers


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_get_goals_expected_200(auth_login):
    headers_a = {"Authorization": "Bearer " + auth_login}

    response = requests.get(
        url=config['NEXT_GEN']['base_url'] + '/goals',
        headers=headers_a
    )

    assert response.status_code == 200

