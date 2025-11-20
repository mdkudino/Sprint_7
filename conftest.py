import pytest
from utils import CourierUtils, CourierDataGenerator


@pytest.fixture()
def courier():
    data = CourierDataGenerator.generate_fake_valid_courier_data()
    CourierUtils.create_courier(data)
    login_response = CourierUtils.login_courier(data)
    id = CourierUtils.get_courier_id(login_response)
    yield [data, id]
    CourierUtils.delete_courier(id)

