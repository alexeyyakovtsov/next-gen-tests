import requests
import configparser


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_put_goal_id(auth_login, get_last_goal_id, create_goals):
    headers= {"Authorization": "Bearer " + auth_login}
    
    response = requests.put(
        url=config['NEXT_GEN']['base_url'] + '/goals/' + get_last_goal_id,
        headers=headers,
        json=create_goals
    )

    assert response.status_code == 200