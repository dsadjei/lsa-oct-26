#Check java version else install java

!java -version          # need 17, 21 or 25
# If no Java, or the version is too old:
# !apt-get -qq install -y openjdk-21-jre-headless

!pip install -q pyspark "pandas<3" pyarrow duckdb openpyxl pytest

#run Spark_Setup_Check
#start spark session 

import time
from pyspark.sql import SparkSession, functions as F

t0 = time.time()
spark = (
    SparkSession.builder
    .appName("setup-check")
    .master("local[*]")
    .config("spark.driver.memory", "4g")        # lower to 2g on an 8 GB laptop
    .config("spark.sql.shuffle.partitions", "8")  # default is 200 - far too many for one machine
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

print(f"OK - Spark {spark.version} started in {time.time() - t0:.1f}s")
print("cores available to Spark:", spark.sparkContext.defaultParallelism)
print("Spark UI:", spark.sparkContext.uiWebUrl)

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

#loading national categories file into spark
nationalcat_df = spark.read.csv("/content/drive/MyDrive/Personal/Professional Development/LSA Internship/raw/national_categories.csv", header=True, inferSchema=True)


#actual duration file needs to be converted into csv before loading into Spark
import pandas as pd
# 1. Convert the Excel file to a CSV using pandas
excel_df = pd.read_excel('/content/drive/MyDrive/Personal/Professional Development/LSA Internship/raw/actual_duration.csv.xlsx')
excel_df.to_csv('actual_duration.csv', index=False)

# 2. Load the CSV into Spark
actual_duration_df = spark.read.csv('actual_duration.csv', header=True, inferSchema=True)
df.show(5)
