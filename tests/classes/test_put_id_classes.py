import requests
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def test_put_classes_id(auth_login, get_last_classes_id, create_classes):
    headers= {"Authorization": "Bearer " + auth_login}
    
    response = requests.put(
        url=config['NEXT_GEN']['base_url'] + '/classes/' + get_last_classes_id,
        headers=headers,
        json=create_classes
    )

    assert response.status_code == 200
