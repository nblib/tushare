from tushare.util.exception import RequestError, UnkownError, Not200Error

from urllib.request import urlopen, Request
from urllib.error import URLError

def get(url, timeout=10):
    try:
        if isinstance(url, Request):
            request = url
        else:
            request = Request(url)
        text = urlopen(request, timeout=timeout).read()
    except URLError as er:
        raise RequestError(er)
    except Exception as er:
        raise UnkownError(er)
    if text == 'null':
        raise Not200Error("content is null")

    return text