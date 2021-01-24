import re
import json

from tushare.util.exception import ParseError


def parse_fund_count(text):
    """
    解析 基金数量
    """
    try:
        text = text.decode('gbk')
        text = text.split('total_num":')[1].split(',"data":')[0]

        nums = int(text)
        return nums
    except Exception as err:
        raise ParseError(err)

def parse_fund_data(text):
    """

    """
    text = text.decode('gbk')
    text = text.split('data":')[1].split(',"exec_time"')[0]
    org_js = json.loads(text)
    return org_js