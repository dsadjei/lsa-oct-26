# Mounting Drive with data folder
from google.colab import drive
drive.mount('/content/drive')
RAW = '/content/drive/MyDrive/LSA_Oct2026/raw'

from pyspark.sql import SparkSession, functions as F
spark = (SparkSession.builder.appName('lsa-oct-2026').master('local[*]')
         .config('spark.driver.memory', '4g')
         .config('spark.sql.shuffle.partitions', '8')
         .getOrCreate())
print(spark.version)

# Loading data into spark
appointments_df = spark.read.csv("/content/drive/MyDrive/Personal/Professional Development/LSA Internship/raw/appointments_regional.csv", header=True, inferSchema=True)
