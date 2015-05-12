from mock import patch
from unittest import TestCase
from utils import open_file, open_dict
from app import chat_decoder


class ChatDecoderTests(TestCase):
    """
    Test cases for chat message decoder
    """
    def setUp(self):
        self.mentions = open_file('chat_test_mentions_valid.txt')
        self.mentions_list = ['Bob', 'John', 'Jack']
        self.emoticons = open_file('chat_test_emoticons_valid.txt')
        self.emoticons_list = ['megusta', 'coffee']
        self.urls = open_file('chat_test_urls_valid.txt')
        self.urls_dict = open_dict('chat_result_urls_valid.json')
        self.urls_negative_test = "This is a chat msg with no urls"
        self.urls_negative_result = []
        self.invalid_url = ['http://goo']
        self.invalid_url_result = open_dict('chat_invalid_url_result.json')
        self.transform_msg_result = open_dict('chat_transformed_msg_result.json')
        self.chat_msg = open_file('test_parse_msg.txt')
        self.test_parse_msg_result = open_file('test_parse_msg_result.txt')

    def test_get_names(self):
        response = chat_decoder.get_names(self.mentions)
        self.assertEqual(response, self.mentions_list)

    def test_get_emoticons(self):
        response = chat_decoder.get_emoticons(self.emoticons)
        self.assertEqual(response, self.emoticons_list)

    def test_get_links(self):
        response = chat_decoder.get_links(self.urls)
        self.assertEqual(response, self.urls_dict)

    def test_get_links_negative_test(self):
        response = chat_decoder.get_links(self.urls_negative_test)
        self.assertEqual(response, self.urls_negative_result)

    def test_get_url_titles_test(self):
        response = chat_decoder.get_url_titles(self.invalid_url)
        self.assertEqual(response, self.invalid_url_result)

    def test_transform_msg(self):
        response = chat_decoder.transform_msg(self.mentions_list, self.emoticons_list, self.urls_dict)
        self.assertEqual(response, self.transform_msg_result)

    def test_transform_msg_empty(self):
        response = chat_decoder.transform_msg([], [], [])
        self.assertEqual(response, "No mentions, emoticons, and URLs found in the chat message")

    @patch('app.chat_decoder.get_names')
    @patch('app.chat_decoder.get_emoticons')
    @patch('app.chat_decoder.get_links')
    @patch('app.chat_decoder.get_url_titles')
    @patch('app.chat_decoder.transform_msg')
    def test_parse_msg(self, transform_msg, url_dict, urls, emoticons, mentions ):
        mentions.return_value = ['Bob', 'John', 'Jack']
        emoticons.return_value = ['megusta', 'coffee']
        urls.return_value = self.urls
        url_dict.return_value = self.urls_dict
        transform_msg.return_value = self.transform_msg_result
        response = chat_decoder.parse_msg(self.chat_msg)
        self.assertEqual(response, self.test_parse_msg_result)





