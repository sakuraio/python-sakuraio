from sakuraio.software.exceptions import UnSupportedExceptions


class ModuleMixins(object):
    def show_modules(self, project_id=None, serial_number=None, model=None, sort=None):
        sort_options = [
            None, '',
            'project', '-project',
            'name', '-name',
            'id', '-id',
            'selial_number', '-serial_number',
            'model', '-model'
            ]

        if sort not in sort_options:
            raise UnSupportedExceptions('sort', sort)

        return self.do('GET', 'modules',
                       query_params={
                           'project': project_id,
                           'serial_number': serial_number,
                           'model': model,
                           'sort': sort
                         }
                       )

    def register_module(self, id, password, module_name, project_id):
        return self.do('POST', 'modules',
                       request_params={
                           'register_id': id,
                           'register_pass': password,
                           'name': module_name,
                           'project': project_id

                         }
                       )

    def delete_module(self, module_id):
        return self.do('DELETE', 'modules/{module_id}',
                       url_params={
                           'module_id': module_id
                         }
                       )

    def show_module(self, module_id):
        return self.do('GET', 'modules/{module_id}',
                       url_params={
                           'module_id': module_id
                         }
                       )

    def update_module(self, module_id, module_name, project_id):
        return self.do('PUT', 'modules/{module_id}',
                       url_params={
                           'module_id': module_id
                         },
                       request_params={
                           'name': module_name,
                           'project': project_id
                         }
                       )
