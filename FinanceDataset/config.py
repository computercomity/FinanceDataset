#!/usr/bin/python
# -*- coding: <utf-8> -*-


class Config:
    pass


class YahooConfig(Config):
    LIVE_DATA_API = 'http://finance.yahoo.com/d/quotes.csv'
    HISTORY_DATA_API = 'http://ichart.yahoo.com/table.csv'


