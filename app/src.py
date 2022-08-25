from os import device_encoding
from flask import render_template
from devices.devices_service import DevicesService

def base_regestry(app):
    devices_seervice = DevicesService()

    @app.route('/')
    def index():
        devices = devices_seervice.get_all_devices()
        return render_template('index.html')
        #return render_template('index.html', devices = devices)

    return app