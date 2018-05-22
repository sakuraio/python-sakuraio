from sakuraio.software.exceptions import UnSupportedExceptions
from sakuraio.software.utils import validate_sort_project, validate_datastore, validate_location


class ProjectMixins(object):
    def show_projects(self, name=None, sort=None):
        # validate sort option
        if not validate_sort_project(sort):
            raise UnSupportedExceptions('sort', sort)

        return self.do('GET', 'projects',
                       query_params={'name': name, 'sort': sort}
                       )

    def create_project(self, name, datastore='light', location='false'):
        if validate_datastore(datastore) is not True:
            raise UnSupportedExceptions('datastore', datastore)
        if validate_location(location) is not True:
            raise UnSupportedExceptions('location', location)

        return self.do('POST', 'projects',
                       request_params={
                          'name': name,
                          'datastore': datastore,
                          'location': location
                       }
                       )

    def delete_project(self, project_id):
        return self.do('DELETE', 'projects/{project_id}',
                       url_params={'project_id': project_id}
                       )

    def show_project(self, project_id):
        return self.do('GET', 'projects/{project_id}',
                       url_params={'project_id': project_id}
                       )

    def update_project(self, project_id, name, location):
        if validate_location(location) is not True:
            raise UnSupportedExceptions('location', location)

        return self.do('PUT', 'projects/{project_id}',
                       url_params={'project_id': project_id},
                       request_params={
                          'name': name,
                          'location': location
                       }
                       )
