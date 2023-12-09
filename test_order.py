# Дубров Ярослав, 11-я когорта - Финальный проект. Инженер по тестированию плюс.

import configuration
import requests
import data


def test_order_track():
    # Выполняем запрос на создание заказа
    create_order_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
    assert create_order_response.status_code == 201

    # Сохраняем номер трека заказа
    order_track_number = create_order_response.json()['track']

    # Выполняем запрос на получение заказа по треку заказа
    get_order_response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(order_track_number))
    assert get_order_response.status_code == 200
