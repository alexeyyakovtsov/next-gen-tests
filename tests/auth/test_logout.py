import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def test_auth_logout_expected_200(auth_login):
    headers= {"Authorization": "Bearer " + auth_login}

    response = requests.post(
                url=config['NEXT_GEN']['base_url'] + '/auth/logout',
                headers=headers
    )

    assert response.status_code == 200


def test_auth_logout_expected_403():
    response = requests.post(
                url=config['NEXT_GEN']['base_url'] + '/auth/logout',
    )

    assert response.status_code == 403
