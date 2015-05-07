def replace_base_url(index, revision, path):
    index = index.decode('utf-8')

    start, end = range_for(index)
    base_url = base_url_for(path, revision)

    return index[:start] + base_url + index[end:]


def range_for(index):
    base = 'baseURL%22%3A%22'

    start = index.find(base) + len(base)
    end = index.find('%22', start)

    return start, end


def base_url_for(path, revision):
    if revision == 'current':
        return path
    return '{0}r/{1}/'.format(path, revision)

def path_for(regex):
    return regex.replace('^', '/')
