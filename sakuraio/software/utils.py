def validate_sort_project(value):
    sort_options = [None, '', 'name', 'id', '-name', '-id']
    if value not in sort_options:
        return False

    return True


def validate_datastore(value):
    datastore_options = ['light', 'standard']
    if value not in datastore_options:
        return False

    return True


def validate_location(value):
    location_options = ['false', 'true']
    if value not in location_options:
        return False

    return True
