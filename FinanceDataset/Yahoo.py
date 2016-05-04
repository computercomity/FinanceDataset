#!/usr/bin/python
# -*- coding: <utf-8> -*-
import requests

# import pandas as pd
# import numpy as np

from FinanceDataset.config import YahooConfig


__author__ = 'JasonGUTU'
__version__ = '0.0.1'
__license__ = 'The MIT License (MIT)'
__copyright__ = 'Copyright (c) 2016 CUHK(SZ) Computer @nd Comity'


class YahooFinance:
    """ A simple encapsulation of Yahoo Finance Data, easy to require, easy to analise """
    def __init__(self, stock_name):
        if isinstance(stock_name, (tuple, list)):
            for name in stock_name:
                if not isinstance(name, str):
                    raise TypeError('stock name must be a string, or a list or tuple of strings.')
            self.iterable = True
        elif isinstance(stock_name, str):
            self.iterable = False
        else:
            raise TypeError('stock name must be a string, or a list or tuple of strings.')
        self.stock_name = stock_name

    def get_live_price(self, data_frame=False, *data_field):
        """
        method to get live price, few params can be choose, the params must be strings,
        return a list(two dimensions list if not only one stock),
            or a DataFrame object if data_frame param is True(default to be False).
        the returns will follow the order you input the params.
        If the param `data_field` is empty, it will return the list of:
            [Stock name, Last Trade Date, Last Trade Price, Open, High]

        if can not find the data you want, the corresponding field will be 'N/A'.

        :param data_field:
            'a' - Ask, 'a2' - Average Daily Volume, 'a5' - Ask Size
            'b' - Bid, 'b2' - Ask (Real-time), 'b3' - Bid (Real-time), 'b4' - Book Value, 'b6' - Bid Size
            'c' - Change & Percent Change, 'c1' - Change, 'c3' - Commission,
                        'c6' - Change (Real-time), 'c8' - After Hours Change (Real-time)
            'd' - Dividend/Share, 'd1' - Last Trade Date, 'd2' - Trade Date
            'e' - Earnings/Share, 'e1' - Error Indication (returned for symbol changed / invalid), 'e7' - EPS Estimate Current Year
                        'e8' - EPS Estimate Next Year, 'e9' - EPS Estimate Next Quarter
            'f6' - Float Shares
            'g' - Day’s Low, 'g1' - Holdings Gain Percent, 'g3' - Annualized Gain, 'g4' - Holdings Gain,
                        'g5' - Holdings Gain Percent (Real-time), 'g6' - Holdings Gain (Real-time)
            'h' - Day’s High
            'i' - More Info, 'i5' - Order Book (Real-time)
            'j' - 52-week Low, 'j1' - Market Capitalization, 'j3' - Market Cap (Real-time), 'j4' - EBITDA,
                        'j5' - Change From 52-week Low, 'j6' - Percent Change From 52-week Low
            'k' - 52-week High, 'k1' - Last Trade (Real-time) With Time, 'k2' - Change Percent (Real-time), 'k3' - Last Trade Size,
            	        'k4' - Change From 52-week High, 'k5' - Percebt Change From 52-week High
            'l' - Last Trade (With Time), 'l1' - Last Trade (Price Only), 'l2' - High Limit, 'l3' - Low Limit
            'm	Day’s Range, 'm2' - Day’s Range (Real-time), 'm3' - 50-day Moving Average, 'm4' - 200-day Moving Average,
                        'm5' - Change From 200-day Moving Average, 'm6' - Percent Change From 200-day Moving Average,
                        'm7' - Change From 50-day Moving Average, 'm8' - Percent Change From 50-day Moving Average
            'n' - Name, 'n4' - Notes
            'o' - Open
            'p' - Previous Close, 'p1' - Price Paid, 'p2' - Change in Percent, 'p5' - Price/Sales, 'p6' - Price/Book
            'q' - Ex-Dividend Date
            'r' - P/E Ratio, 'r1' - Dividend Pay Date, 'r2' - P/E Ratio (Real-time), 'r5' - PEG Ratio
                        'r6' - Price/EPS Estimate Current Year, 'r7' - Price/EPS Estimate Next Year
            's' - Symbol, 's1' - Shares Owned, 's7' - Short Ratio
            't1' - Last Trade Time, 't6' - Trade Links, 't7' - Ticker Trend, 't8' - 1 yr Target Price
            'v' - Volume, 'v1' - Holdings Value, 'v7' - Holdings Value (Real-time)
            'w' - 52-week Range, 'w1' - Day’s Value Change, 'w4' - Day’s Value Change (Real-time)
            'x' - Stock Exchange
            'y' - Dividend Yield
        :return:
            a list of each field, order by your input
            'N/A' if the data can't be found
        """
        if data_field is None:
            field_param = 'sd1l1oh'
            tags = ['s', 'd1', 'l1', 'o', 'h']
        else:
            field_param = ''
            tags = list()
            for para in data_field:
                field_param += para
                tags.append(para)
        if self.iterable:
            stocks = ''
            '+'.join(self.stock_name)
        else:
            stocks = self.stock_name
        data = {
            's': stocks,
            'f': field_param
        }
        response = requests.get(YahooConfig.LIVE_DATA_API, params=data)
        result = response.text.split('\n')
        for item in result:
            item = item.split(',')
        # if data_frame:
        #     result = pd.DataFrame(result, columns=tags)
        #     return result
        # else:
        #     return result
        return result

    def get_history(self, start_day, end_day=None, time_interval='d', data_frame=False):
        """
        method to get history stock prices, start day and end day can be choose,
        the last argv is time interval:
            d -> day, w -> week，m -> mouth，v -> dividends only
        return a list(two dimensions list if not only one stock),
            or a DataFrame object if data_frame param is True(default to be False).

        if can not find the data you want, the corresponding field will be 'N/A'.
        """
        


