import responses
from web_client.some_web_client import SomeResourceClient
from datetime import datetime
import pytest

@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 11111,
        "timeDiff": 16983
    }
    responses.add(method=responses.GET, url='https://www.avito.ru/web/user/get-status/177068588',
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://www.avito.ru")

    res = some_resource_client.get_user_last_action_time(177068588)
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])


@responses.activate
def test_some_web_client_with_error():
    valid_json_answer = {
        "errors": ["Not found"],
    }
    responses.add(method=responses.GET, url='https://www.avito.ru/web/user/get-status/177068588-',
                  json=valid_json_answer, status=404)

    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient("https://www.avito.ru")
        some_resource_client.get_user_last_action_time("177068588-")
