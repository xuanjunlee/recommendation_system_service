#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 19:58
import os
from surprise import SVD
from surprise import Dataset
from surprise import Reader, GridSearch

file_path = os.path.expanduser('~/.surprise_data/ml-100k/ml-100k/u.data')

reader = Reader(line_format='user item rating timestamp', sep='\t')

data = Dataset.load_from_file(file_path, reader=reader)

data.split(n_folds=5)

param_grid = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005],
              'reg_all': [0.4, 0.6]}

grid_search = GridSearch(SVD, param_grid, measures=['RMSE', 'FCP'])

data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)
grid_search.evaluate(data)

print(grid_search.best_score['RMSE'])

print(grid_search.best_params['RMSE'])

print(grid_search.best_score['FCP'])

print(grid_search.best_params['FCP'])
