from main import db
from devices.devices_model import Device

class DevicesService():
    def __init__(self):
        self.Device = Device

    def get_all_devicess(self):
        devices = self.Device.query.order_by(Device.price).all()
        return devices

    def create_device(self, device_title, description, category_id, brand_id, price):
        device = self.Device(device_title = device_title, description = description, category_id = category_id,  brand_id = brand_id, price = price)
        try:
            db.session.add(device)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False
