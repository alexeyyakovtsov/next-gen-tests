import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def test_get_id_classes_expected_200(auth_login, get_last_classes_id):
    headers_a = {"Authorization": "Bearer " + auth_login}

    response = requests.get(
        url=config['NEXT_GEN']['base_url'] + '/classes/' + get_last_classes_id,
        headers=headers_a
    )

    assert response.status_code == 200
    assert response.json() is not None
    assert 'category' in response.json().keys()
    assert 'name' in response.json().keys()
    assert 'language' in response.json().keys()
    assert 'created_at' in response.json().keys()
    assert 'created_by' in response.json().keys()
    assert 'updated_at' in response.json().keys()
    assert 'updated_by' in response.json().keys()
    assert 'deleted' in response.json().keys()
    assert 'id' in response.json().keys()
