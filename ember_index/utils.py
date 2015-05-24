def replace_base_url(index, revision, path):
    '''Replace base URL at environment configuration
       and optionally at base tag in index.

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

    index = replace_base_url_in_base_tag(index, base_url)
    index = replace_base_url_in_meta_tag(index, base_url)

    return index


def replace_base_url_in_base_tag(index, base_url):
    '''Replace base URL at base tag if present.

    Keyword arguments:
        index (string): An index for requested revision.
        base_url (string): A base URL to replace.

    Returns:
        An index with replaced `href` attribute at `base` tag`.

    '''
    base = '<base href="'
    start = index.find(base)

    if start is -1:
        return index

    start += len(base)
    end = index.index('"', start)

    return index[:start] + base_url + index[end:]


def replace_base_url_in_meta_tag(index, base_url):
    '''Replace base URL at environment configuration in index.

    Keyword arguments:
        index (string): An index for requested revision.
        base_url (string): A base URL to replace.

    Returns:
        An index with replaced `baseURL` at environment configuration.

    Raises:
        ValueError: When `baseURL` can not be found in index.

    '''
    base = 'baseURL%22%3A%22'
    start = index.index(base) + len(base)
    end = index.index('%22', start)

    return index[:start] + base_url + index[end:]


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
