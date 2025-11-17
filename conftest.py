import pytest
from utils import CourierUtils, CourierDataGenerator


@pytest.fixture()
def courier():
    data = CourierDataGenerator.generate_fake_valid_courier_data()
    CourierUtils.create_courier(data)
    yield data
    login_response = CourierUtils.login_courier(data)
    id = CourierUtils.get_courier_id(login_response)
    CourierUtils.delete_courier(id)

@pytest.fixture()
def courier_id():
    courier_data = CourierDataGenerator.generate_fake_valid_courier_data()
    CourierUtils.create_courier(courier_data)
    login_resp = CourierUtils.login_courier(courier_data)
    courier_id = CourierUtils.get_courier_id(login_resp)
    yield courier_id
    CourierUtils.delete_courier(courier_id)

