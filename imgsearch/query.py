
def query(path):
    raw = []
    thumbnails = []
    for i in xrange(1, 10):
        raw.append('/user/hadoop/image/image000%d.jpg' % i)
    for i in xrange(1, 10):
        thumbnails.append('data/image_000%d.jpg' % i)
    return raw, thumbnails
