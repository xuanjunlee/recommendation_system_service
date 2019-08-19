#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 19:12
from flask import Flask

app = Flask('recommendation_system')
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
