def replace_base_url(index, revision, path):
    base_url = base_url_for(path, revision)
    start, end = range_for(index)

    return index[:start] + base_url + index[end:]


def range_for(index):
    base = 'baseURL%22%3A%22'

    start = index.index(base) + len(base)
    end = index.index('%22', start)

    return start, end


def base_url_for(path, revision):
    if revision == 'current':
        return path
    return '{0}r/{1}/'.format(path, revision)

def path_for(regex):
    return regex.replace('^', '/')
