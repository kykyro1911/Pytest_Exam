#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest
import requests
import os, configparser

host = 'https://swapi.dev/api/'
# rdINI
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, 'StarWars_Params.ini')
conf = configparser.ConfigParser()
conf.read(cfgpath, encoding='utf-8')
cfg_ = conf['params']

class Test_StarWars_Ex:
    def GET_method_API(self, host):
        return requests.get(host)

    def Trans_json(self, HTMLtext):
        return json.loads(HTMLtext)

    def GET_api1_json(self):
        api1_resp = self.GET_method_API(host + 'people/' + cfg_['var_people_id'] +
                                   '/')
        api1_json = self.Trans_json(api1_resp.text)

        return api1_resp, api1_json

    def GET_api2_json(self):
        api2_resp = self.GET_method_API(host + 'films/' + cfg_['var_flims_id'] +
                                   '/')
        api2_json = self.Trans_json(api2_resp.text)

        return api2_resp, api2_json

    def test_People_api_1(self):
        API1_response, API1_json = self.GET_api1_json()

        # 1_1. check http code 200
        assert API1_response.status_code == 200, "HTTP response isn't OK. (" + API1_response.status_code + ")"
        # 1_2. height應該超過 var_height
        assert int(API1_json['height']) > int(cfg_['var_height']), API1_json['name'] + "'s height is not higher var_height."
        # 1_3. Vehicles數量應該等於 var_vehicles_count
        assert len(API1_json['vehicles']) == int(cfg_['var_vehicles_count']), API1_json['name'] + "'s vehicles amount is not equal to var_vehicles_count"

    def test_Films_api_2(self):
        API1_response, API1_json = self.GET_api1_json()
        API2_response, API2_json = self.GET_api2_json()

        # 2_1. check http code 200
        assert API2_response.status_code == 200, "HTTP response isn't OK. (" + API2_response.status_code + ")"
        # 2_2. API 2的⾶船數⽬應該要⼤於API 1的⾶船數量
        assert len(API2_json['starships']) > len(API1_json['starships']), API2_json['name'] + "'s starships amount is not more than " + API1_json['name'] + "'s starships amount"
