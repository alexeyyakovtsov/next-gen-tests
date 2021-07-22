import requests
import configparser
import randomaizer as randomaizer
import headers.headers as headers


config = configparser.ConfigParser()
config.read('../../config.ini')


def test_auth_login_expected_200():
    data = {
        "email": config['NEXT_GEN']['email'],
        "password": config['NEXT_GEN']['password']
    }

    response = requests.post(
                url=config['NEXT_GEN']['base_url'] + '/auth/login', 
                json=data,
                headers=headers.HEADERS
    )
    assert response.status_code == 200
    assert response.json() != None


def test_auth_login_expected_422():
    random_data = randomaizer.RandomData()
    random_word = random_data.generate_word(5)


    data = {
        "email": random_word,
        "password": random_word
    }

    response = requests.post(
                url=config['NEXT_GEN']['base_url'] + '/auth/login', 
                json=data,
                headers=headers.HEADERS
    )
    assert response.status_code == 422