import requests
import configparser
import pytest


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_get_goal_id(auth_login, get_last_goal_id):
    headers= {"Authorization": "Bearer " + auth_login}
    
    response = requests.get(
        url=config['NEXT_GEN']['base_url'] + '/goals/' + get_last_goal_id,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json() != None
    assert 'owner' in response.json().keys()
    assert 'name' in response.json().keys()
    assert 'due_date' in response.json().keys()
    assert 'completed' in response.json().keys()
    assert 'created_at' in response.json().keys()
    assert 'created_by' in response.json().keys()
    assert 'updated_at' in response.json().keys()
    assert 'updated_by' in response.json().keys()
    assert 'deleted' in response.json().keys()
    assert 'id' in response.json().keys()
