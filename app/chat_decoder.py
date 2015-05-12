"""
Chat Decoder Module
"""

import re
import json
import urllib2
import logging as log
from BeautifulSoup import BeautifulSoup


class ChatDecoderException(Exception):
    """
    Custom Exception.
    """

    def __init__(self, message):
        super(ChatDecoderException, self).__init__(message)
        self.value = message

    def __str__(self):
        return str(self.message)


def get_names(chat_msg):
    """
    Regex get all the words that startswith @ and stops when a non-word character found
    :param chat_msg:
    :return: list
    """
    return [name[1:] for name in (re.findall(r'@\w+', chat_msg))]

def get_emoticons(chat_msg):
    """

    :param chat_msg:
    :return: list
    """
    return [emoticon[1:-1] for emoticon in (re.findall(r'\(.*?\)', chat_msg))]


def get_links(chat_msg):
    """

    :param chat_msg:
    :return:list
    """
    urls = re.findall(r'(https?://[^\s]+)', chat_msg)
    if urls:
        return get_url_titles(urls)
    else:
        return urls


def get_url_titles(urls):
    links = []
    my_dict = {}
    for url in urls:
        try:
            html = urllib2.urlopen(url, timeout=6).read()
            soup = BeautifulSoup(html)
            title = soup.html.head.title.string
            my_dict['url'] = url
            my_dict['title'] = title
            links.append(my_dict.copy())
            my_dict.clear()
        except Exception as exc:
            log.info(ChatDecoderException("Error reading titles from the websites. "
                                          "Please check your URL or internet connection "
                                          "and try again.".format(str(exc))))
            my_dict['url'] = url
            my_dict['title'] = "Data not found"
            links.append(my_dict.copy())
            my_dict.clear()
    return links



def transform_msg(mentions, emoticons, urls):
    """

    :param mentions:
    :param emoticons:
    :param urls:
    :return:
    """
    result = dict()
    if mentions:
        result['mentions'] = mentions
    if emoticons:
        result['emoticons'] = emoticons
    if urls:
        result['links'] = urls
    if result:
        return result
    else:
        return "No mentions, emoticons, and URLs found in the chat message"


def parse_msg(chat_msg):
    """

    :param chat_msg:
    :return:
    """
    try:
        log.info("Parsing mentions in the incoming chat message")
        mentions = get_names(chat_msg)
    except Exception as exc:
        log.info(ChatDecoderException("Error parsing mentions in the incoming message".format(str(exc))))
        raise

    try:
        log.info("Parsing emoticons in the incoming chat message")
        emoticons = get_emoticons(chat_msg)
    except Exception as exc:
        log.info(ChatDecoderException("Error parsing emoticons in the incoming message".format(str(exc))))
        raise
    try:
        log.info("Parsing Urls in the incoming chat message")
        links = get_links(chat_msg)
    except Exception as exc:
        log.info(ChatDecoderException("Error parsing URLs in the incoming message".format(str(exc))))
        raise

    result = transform_msg(mentions, emoticons, links)
    log.info("Parsed string: " + str(result))
    return json.dumps(result, sort_keys=False, indent=4, separators=(',', ': '))
