import sys

from pyspark import SparkContext, SparkConf


# create Spark context with Spark configuration
conf = SparkConf().setAppName("Word Count - Python").set("spark.hadoop.yarn.resourcemanager.address","192.168.1.249:9099")
sc = SparkContext(conf=conf)

# read in text file and split each document into words
words = sc.textFile("/user/input/Shakespeare_in.txt").flatMap(lambda line: line.split(" "))

# count the occurrence of each word
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

wordCounts.saveAsTextFile("/user/input/Shakespeare_out.txt")
