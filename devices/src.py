from flask import render_template, redirect, request
from devices.devices_service import DevicesService

def devices_registry(app):
    devices_service = DevicesService()

    @app.route('/devices')
    def device(id):
        return render_template('index.html')
           
    return app