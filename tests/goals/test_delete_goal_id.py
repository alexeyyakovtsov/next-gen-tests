import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def test_delete_goal_id(auth_login, get_last_goal_id):
    headers= {"Authorization": "Bearer " + auth_login}

    response = requests.delete(
        url=config['NEXT_GEN']['base_url'] + '/goals/' + get_last_goal_id,
        headers=headers
    )

    assert response.status_code == 200
