import sender_stand_request
import data


def positive_assert():
    """
    Функция проверки позитивных тест-кейсов
    Args:
    """
    track_number = sender_stand_request.post_new_order(data.order_body)
    status_code = sender_stand_request.get_status_code_order_by_track(track_number)
    assert status_code == 200
