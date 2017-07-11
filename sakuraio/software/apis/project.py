from sakuraio.software.exceptions import SakuraIOClientUnSupportedExceptions


class ProjectMixins(object):
    def get_projects(self, name=None, sort=None):
        # validate sort option
        sort_options = [None, '', 'name', 'id', '-name', '-id']
        if sort not in sort_options:
            raise SakuraIOClientUnSupportedExceptions('sort', sort)

        return self.do('GET', 'projects',
                       query_params={'name': name, 'sort': sort}
                       )

    def create_project(self, name, datastore='light', location='false'):
        datastore_options = ['light', 'standard']
        location_options = ['false', 'true']

        if datastore not in datastore_options:
            raise SakuraIOClientUnSupportedExceptions('datastore', datastore)

        if location not in location_options:
            raise SakuraIOClientUnSupportedExceptions('location', location)

        return self.do('POST', 'projects',
                       request_params={
                           'name': name,
                           'datastore': datastore,
                           'location': location
                           }
                       )
