import outlook_scanner
import json
import unittest
from typing import List

def read_data_file():
    with open('email_data.json', 'r') as f:
        return json.load(f)

def write_email_data_to_file(email_data_dict):
    with open('email_data.json', 'w') as f:
        json.dump(email_data_dict, f)


class TestOutlookScanner(unittest.TestCase):
    def setUp(self):
        self.email_data_dict = {'some_email_data':'Example Data. From Junkmail.io'}
        write_email_data_to_file(self.email_data_dict)
        
    def test_scan_spam_email(self):
        # Spam email
        self.email_data_dict['subject'] = 'Offer: Best deals on iPhone and iPad. Up to 50% '
        'off @ iMart'
        self.email_data_dict['body'] = 'Dear Com,
' + 
        'We are excited to offer our premium members exclusive discounts on some of the
' + 
        'hottest products from Apple. With savings of up to 50% off, there is no better time
' + 
        'to buy than now. Take advantage of this offer today and get the latest products
' + 
        'from Apple at unbeatable prices.
' + 
        'Sincerely,
' + 
        'iMart Team'
        write_email_data_to_file(self.email_data_dict)
        result = outlook_scanner.scan_email(self.email_data_dict)
        self.assertEqual(result, True)
        
    def test_scan_non_spam_email(self):
        # Non-spam email
        self.email_data_dict['subject'] = 'Wireless Association of Asia - Annual Convention'
        self.email_data_dict['body'] = 'Dear members,
' + 
        'We are excited to invite you to the Wireless Association of Asia annual convention.
' + 
        'This year, the convention will be held in Tokyo, Japan, from July 1st - 3rd. The
' + 
        'convention provides an excellent opportunity to meet and network with peers,
' + 
        'gain an understanding of the latest trends and developments in the industry, and
' + 
        'exchange ideas about emerging issues. For more information about the convention
' + 
        'and to register, please visit our website: www.wirelessasia.com
' + 
        'Sincerely,
' + 
        'The Wireless Association of Asia'
        write_email_data_to_file(self.email_data_dict)
        result = outlook_scanner.scan_email(self.email_data_dict)
        self.assertEqual(result, False)
        
    def tearDown(self):
        write_email_data_to_file({})


if __name__ == '__main__':
    unittest.main() 