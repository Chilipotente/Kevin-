# -*- coding: utf-8 -*-
"""Kevin_Filter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RYts1DVySyMlpZyx9p_mJ8J5wu9AGD6p
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FilterExample") \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.parallelize([1, 2, 3, 4, 5])

even_numbers_rdd = rdd.filter(lambda x: x % 2 == 0)

result = even_numbers_rdd.collect()
print(result)

maximo = rdd.max()
minimo = rdd.min()

print("Máximo:", maximo)
print("Mínimo:", minimo)