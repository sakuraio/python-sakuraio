class FileMixins(object):
    def show_file_configs(self, project_id):
        return self.do('GET', 'projects/{project_id}/files',
                       url_params={'project_id': project_id}
                       )

    def create_file_config(self, project_id, file_number, file_url, file_name=""):
        return self.do('POST', 'projects/{project_id}/files',
                       url_params={'project_id': project_id},
                       request_params={
                           'number': file_number,
                           'name': file_name,
                           'url': file_url
                       }
                       )

    def delete_file_config(self, project_id, file_number):
        return self.do('DELETE', 'projects/{project_id}/files/{file_number}',
                       url_params={
                           'project_id': project_id,
                           'file_number': file_number
                           }
                       )

    def show_file_config(self, project_id, file_number):
        return self.do('GET', 'projects/{project_id}/files/{file_number}',
                       url_params={
                           'project_id': project_id,
                           'file_number': file_number
                           }
                       )

    def update_file_config(self, project_id, file_number, file_url, file_name=""):
        return self.do('PUT',  'projects/{project_id}/files/{file_number}',
                       url_params={
                           'project_id': project_id,
                           'file_number': file_number
                       },
                       request_params={
                           'number': file_number,
                           'name': file_name,
                           'url': file_url
                       }
                       )
