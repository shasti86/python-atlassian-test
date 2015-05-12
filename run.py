#!/usr/bin/python

from app.chat_decoder import parse_msg
from config import LOGGING
from argparse import ArgumentParser
from logging import getLogger, getLevelName, handlers
from logging import Formatter
import logging as log


class ParseMsgException(Exception):
    """
    Custom Exception.
    """

    def __init__(self, message):
        super(ParseMsgException, self).__init__(message)
        self.value = message

    def __str__(self):
        return str(self.message)



def configure_logging():
    """ Enable logging """
    try:
        log_file = LOGGING['log_file']
    except:
        log_file = './tmp/chatmsg.log'
    try:
        log_level = LOGGING['log_level']
    except:
        log_level = log.INFO
    log.basicConfig(filename=log_file, filemode='w', level=log_level)
    log.info('Started parsing the chat msg')


def main(chat_msg):
    """
    The main function to start the application
    :return:
    """
    # Set variable constants here, if any.

    configure_logging()
    log.info('Incoming Msg: ' + chat_msg)
    print parse_msg(chat_msg)


if __name__ == '__main__':
    """ start the argument parser """
    parser = ArgumentParser(description='The Atlassian Chat Parser Service')
    parser.add_argument('-M', '--msg', help='The chat message that needs to parsed', required=True)
    args = parser.parse_args()
    main(args.msg)