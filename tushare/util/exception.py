class ParseError(Exception):
    """
    解析响应内容异常
    """
    pass


class RequestError(Exception):
    """
    请求超时,地址有问题等,此错误应该重试
    """
    pass


class Not200Error(Exception):
    """
    非200响应,或响应内容为空
    """
    pass

class UnkownError(Exception):
    """
    未知异常,建议抛出不进行处理,方便定位错误
    """
    pass
