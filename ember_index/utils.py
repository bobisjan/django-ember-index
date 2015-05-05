def extend_base_url(index, revision):
    if revision == 'current':
        return index

    index = index.decode('utf-8')

    base = 'baseURL%22%3A%22'
    ext = 'r/{0}/'.format(revision)

    idx = index.find(base)
    idx = index.find('%22', idx + len(base))

    return index[:idx] + ext + index[idx:]
