import requests
import configparser
import pytest
import randomaizer


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_put_goal_id(auth_login, get_last_goal_id):
    headers= {"Authorization": "Bearer " + auth_login}

    random_data = randomaizer.RandomData()
    random_word = random_data.generate_word(5)
    
    response = requests.patch(
        url=config['NEXT_GEN']['base_url'] + '/goals/' + get_last_goal_id,
        headers=headers,
        json= {
            "name": random_word
        }
    )

    assert response.status_code == 200
    assert 'id' in response.json().keys()
