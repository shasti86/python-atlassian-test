import simplejson as json
import os


def get_path(filename):
    cwd = os.getcwd()
    path = cwd + '/tests/samples/' + filename
    test_path = cwd + '/samples/' + filename
    return (path, test_path)


def open_file(filename):
    (path, test_path) = get_path(filename)
    try:
        data = open(path)
    except Exception, exc:
        try:
            data = open(test_path)
        except Exception, exc:
            print exc
            raise
    message_str = data.read()
    data.close()
    return message_str


def open_dict(filename):
    (path, test_path) = get_path(filename)
    try:
        data = open(path)
    except Exception, exc:
        try:
            data = open(test_path)
        except Exception, exc:
            print exc
            raise
    message_dict = json.load(data)
    data.close()
    return message_dict
