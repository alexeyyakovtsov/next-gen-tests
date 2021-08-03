import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def test_post_classes_expected_200(auth_login, create_classes):
    headers_a = {"Authorization": "Bearer " + auth_login}

    response = requests.post(
        url=config['NEXT_GEN']['base_url'] + '/classes',
        headers=headers_a,
        json=create_classes
    )

    assert response.status_code == 200
    assert 'id' in response.json().keys()
