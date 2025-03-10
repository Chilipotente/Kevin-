# -*- coding: utf-8 -*-
"""xio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GJBkJfdf4O_WQQUKjEXjbTwWdoNwhDzq
"""

from pyspark import SparkContext

sc = SparkContext("local", "Distinct and Reduce Example")

rdd = sc.parallelize([1, 2, 2, 3, 4, 4, 4, 5])

distinct_rdd = rdd.distinct()

sum_result = distinct_rdd.reduce(lambda x, y: x + y)

print(sum_result)  # Salida: 15 (1 + 2 + 3 + 4 + 5)

