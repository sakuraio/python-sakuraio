from sakuraio.software.exceptions import UnSupportedExceptions


class ServiceMixins(object):
    def show_servicetypes(self):
        return self.do('GET', 'servicetypes')

    def show_servicetype(self, servicetype_id):
        return self.do('GET', 'servicetypes/{servicetype_id}',
                       url_params={
                           'servicetype_id': servicetype_id
                           }
                       )

    def show_registered_service(self, servicetype=None, sort=None):
        servicetypes = [
            None, '',
            'websocket',
            'incoming-webhook',
            'outgoing-webhook',
            'mqtt',
            'mqtt.aws-iot'
            'datastore'
            ]

        sort_options = [
            None,
            'name', '-name',
            'token', '-token'
            'id', '-id'
            ]

        if servicetype not in servicetypes:
            raise UnSupportedExceptions('servicetype', servicetype)
        if sort not in sort_options:
            raise UnSupportedExceptions('sort', sort)

        return self.do('GET', 'services',
                       query_params={
                           'type': servicetype,
                           'sort': sort
                           }
                       )

    def show_service(self, service_id):
        return self.do('GET', 'services/{service_id}',
                       url_params={
                           'service_id': service_id
                           }
                       )

    def update_service(self, service_id, **kargs):
        return self.do('PUT', 'services/{service_id}',
                       url_params={
                           'service_id': service_id
                           },
                       request_params=kargs
                       )

    def delete_service(self, service_id):
        return self.do('DELETE', 'services/{service_id}',
                       url_params={
                           'service_id': service_id
                           }
                       )

    def create_websocket_service(self, name, project_id):
        return self.do('POST', 'services/?type=websocket',
                       request_params={
                           'name': name,
                           'type': 'websocket',
                           'project': project_id
                           }
                       )

    def create_outgoing_webhook_service(self, name, project_id, url, secret):
        return self.do('POST', 'services/?type=outgoing-webhook',
                       request_params={
                           'name': name,
                           'type': 'outgoing-webhook',
                           'project': project_id,
                           'url': url,
                           'secret': secret
                           }
                       )

    def create_incoming_webhook_service(self, name, project_id, url, secret):
        return self.do('POST', 'services/?type=incoming-webhook',
                       request_params={
                           'name': name,
                           'type': 'incoming-webhook',
                           'project': project_id,
                           'url': url,
                           'secret': secret
                           }
                       )

    def create_datastore_service(self, name, project_id):
        return self.do('POST', 'services/?type=datastore',
                       request_params={
                           'name': name,
                           'type': 'datastore',
                           'project': project_id
                           }
                       )

    def create_mqtt_service(self, name, project_id, hostname, port, publish_prefix, subscribe_topic,
                            username="", password="", rootca_cert="", cert="", private_key=""):
        return self.do('POST', 'services/?type=mqtt',
                       request_params={
                           'name': name,
                           'type': 'mqtt',
                           'project': project_id,
                           'hostname': hostname,
                           'port': port,
                           'publish_prefix': publish_prefix,
                           'subscribe_topic': subscribe_topic,
                           'username': username,
                           'password': password,
                           'rootca_cert': rootca_cert,
                           'cert': cert,
                           'private_key': private_key
                           }
                       )

    def create_awsiot_service(self, name, project_id, hostname, port, publish_prefix, subscribe_topic,
                              rootca_cert, cert, private_key):
        return self.do('POST', 'services/?type=mqtt.aws-iot',
                       request_params={
                           'name': name,
                           'type': 'mqtt.aws-iot',
                           'project': project_id,
                           'hostname': hostname,
                           'port': port,
                           'publish_prefix': publish_prefix,
                           'subscribe_topic': subscribe_topic,
                           'rootca_cert': rootca_cert,
                           'cert': cert,
                           'private_key': private_key
                           }
                       )

    def create_azureiot_service(self, name, project_id, shared_access_key, device_id):
        return self.do('POST', 'services/?type=azure-iot-hub',
                       request_params={
                           'name': name,
                           'type': 'azure-iot-hub',
                           'project': project_id,
                           'shared_access_key': shared_access_key,
                           'device_id': device_id
                           }
                       )
