# -*- coding: utf-8 -*-
__author__ = 'cemkiy'
import splinter

class splinter_process:
    def __init__(self):
        self.browser = splinter.Browser()
        self.your_account = {'username': 'your_email', 'password': 'your_password'}


    def login_with_your_account(self):
        try:
            url = 'https://koinim.com/account/login/'
            self.browser.visit(url)
            self.browser.fill('username', self.your_account['username'])
            self.browser.fill('password', self.your_account['password'])
            button = self.browser.find_by_value('Giriş Yap')
            # Interact with elements
            button.click()
        except Exception as e:
            print e


    def get_btc_value(self):
        try:
            url = 'https://koinim.com/'
            self.browser.visit(url)
            return self.browser.find_by_tag('strong').first.value
        except Exception as e:
            print e


    def get_ltc_value(self):
        try:
            url = 'https://koinim.com/'
            self.browser.visit(url)
            return self.browser.find_by_tag('strong')[1].value
        except Exception as e:
            print e

    #needs login_with_your_account
    def get_send_urls_btc(self, index):#Get payment url by index
        try:
            self.login_with_your_account()
            self.browser.click_link_by_href('/deposit/bitcoin/')
            return self.browser.find_by_tag('code')[index].value
        except Exception as e:
            print e

    #needs login_with_your_account
    def generate_new_send_btc_url(self):#Generate new payment url
        try:
            self.login_with_your_account()
            self.browser.click_link_by_href('/deposit/bitcoin/')
            button = self.browser.find_by_tag('button')
            button.click()
        except Exception as e:
            print e
            return False


    #needs login_with_your_account
    def get_transactions(self, index):
        if index == 0:
            index = 0
        else:
            index = index * 5
        try:
            self.login_with_your_account()
            self.browser.click_link_by_href('/transactions/')
            transactions = {'history': self.browser.find_by_tag('td')[index].value,
                            'trans': self.browser.find_by_tag('td')[index+1].value,
                            'amount': self.browser.find_by_tag('td')[index+2].value,
                            'price': self.browser.find_by_tag('td')[index+3].value,
                            'total': self.browser.find_by_tag('td')[index+4].value}
            return transactions
        except Exception as e:
            print e
            return False

    #needs login_with_your_account
    def set_bitcoin(self, adress, amount_integer, amount_decimal=0):
        try:
            self.login_with_your_account()
            self.browser.click_link_by_href('/withdraw/bitcoin/')
            self.browser.fill('amount_integer', str(amount_integer))
            self.browser.fill('amount_decimal', str(amount_decimal))
            self.browser.fill('adress', str(adress))
            button = self.browser.find_by_id('modal-fire-button')
            button.click()
        except Exception as e:
            print e
            return False


    #needs login_with_your_account
    def get_send_url_bitcoin_value(self, adress):
        try:
            self.login_with_your_account()
            self.browser.click_link_by_href('/deposit/bitcoin/')
            index = 0
            while(True):
                if str(self.browser.find_by_tag('code')[index].value) == str(adress):
                    break
                else:
                    index = index + 1
            return self.browser.find_by_tag('td')[index+1].value
        except Exception as e:
            print e


