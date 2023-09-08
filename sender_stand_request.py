import configuration
import requests


def post_new_order(body):
    """
    Отправка запроса на создание нового заказа
    Args:
        body: Тело запроса на создание заказа

    Returns: Номер трека заказа
    """
    response = requests.post(configuration.SERVER_URL + configuration.CREATE_ORDER,
                             json=body).json()
    return response['track']


def get_status_code_order_by_track(track_number):
    """
    Отправка запроса на получение заказа по его трек номеру
    Args:
        track_number: Трек номер заказа

    Returns: Статус код выполнения запроса
    """
    return requests.get(configuration.SERVER_URL + configuration.GET_ORDER_BY_TRACK_NUMBER,
                        params={"t": track_number}).status_code
