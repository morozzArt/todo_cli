def get_last_id(path):
    file_with_last_id = open(path + 'last.txt', 'r')
    id = int(file_with_last_id.read())
    file_with_last_id.close()
    return id


def set_last_id(id, path):
    f = open(path + 'last.txt', 'w')
    f.write(str(id))
    f.close()
