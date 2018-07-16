#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from main import get_all_model,get_perf,my_sort,write_csv


class TestMain(unittest.TestCase):

    def test_get_all_model(self):
        models = get_all_model()
        self.assertTrue(isinstance(models, list))
        self.assertEqual(len(models[0]), 2)

    def test_get_perf(self):
        models = [
            ['1320', 'M440'],
            ['3025', 'M200'],
            ['8811', 'T70']
        ]
        model_list = get_perf(models)
        self.assertEqual(len(model_list[1]), 8)
        self.assertEqual(model_list[3][2], '6.7 Gbps')

    def test_my_sort(self):
        models = [
            ['1320', 'M440', '6.7 Gbps', '3.2 Gbps'],
            ['3025', 'M200', '3.2 Gbps', '1.2 Gbps'],
            ['8811', 'T70', '4 Gbps', '740 Mbps']
        ]
        model_list = my_sort(models)
        self.assertEqual(model_list[2][2], '6.7 Gbps')

    def test_my_sort_neg(self):
        models = [
            ['1320', 'M440'],
            ['3025', 'M200'],
            ['8811', 'T70']
        ]
        with self.assertRaises(IndexError):
            my_sort(models)


if __name__ == '__main__':
    unittest.main()
