def replace_base_url(index, revision, path):
    '''Replace base URL at environment configuration in index.

    Keyword arguments:
        index (string): An index for requested revision.
        revision (string): An requested revision.
        path (string): A path from Ember application is served.

    Returns:
        An index with replaced `baseURL`.

    Raises:
        ValueError: When `baseURL` can not be found in index.

    '''
    base_url = base_url_for(path, revision)
    start, end = range_for(index)

    return index[:start] + base_url + index[end:]


def range_for(index):
    '''Find start and end indices where base URL should be inserted.

    Keyword arguments:
        index (string): An index to search through.

    Returns:
        A tuple of start and end indices.

    Raises:
        ValueError: When `baseURL` can not be found in index.

    '''
    base = 'baseURL%22%3A%22'

    start = index.index(base) + len(base)
    end = index.index('%22', start)

    return start, end


def base_url_for(path, revision):
    '''Create a base URL for path and requested revision.

    Keyword arguments:
        path (string): A path from Ember application is served.
        revision (string): A requested revision.

    Returns:
        A base URL.

    '''
    if revision == 'current':
        return path
    return '{0}r/{1}/'.format(path, revision)


def path_for(regex):
    '''Create path by replacing '^' with '/' in regex.

    Keyword arguments:
        regex (string): A regex from Ember application is served.

    Returns:
        A path from Ember application is served.

    '''
    return regex.replace('^', '/')
