#Initial checks of data set
#display first five rows and total row count of appointments.regional.csv file
appointments_df.show(5)
appointments_df.count()

#display dataset schema
appointments_df.printSchema()

#checking for duplicate values
total_rows = appointments_df.count()
unique_rows = appointments_df.distinct().count()

print(f"Total Rows: {total_rows}")
print(f"Unique Rows: {unique_rows}")
print(f"Duplicate Rows: {total_rows - unique_rows}")


# Get separate distinct counts for multiple columns
from pyspark.sql.functions import countDistinct

appointments_df.select(
    countDistinct("icb_ons_code").alias("unique_icb"),
    countDistinct("appointment_status").alias("unique_status"),
    countDistinct("hcp_type").alias("unique_hcpType"),
    countDistinct("appointment_month").alias("unique_month"),
    countDistinct("time_between_book_and_appointment").alias("unique_bktime"),
    countDistinct("appointment_mode").alias("unique_mode"),
    countDistinct("count_of_appointments").alias("unique_counts")
).show()

#display the distinct values of the selected columns for first 20 rows
appointments_df.select('appointment_status', 'hcp_type', 'appointment_mode').distinct().show()


#display the minimum and maximum value of the date column
from pyspark.sql.functions import min, max
date_bounds = appointments_df.select(
    min("appointment_month").alias("earliest_date"), 
    max("appointment_month").alias("latest_date")
)
# Display the result 
date_bounds.show()

#checking data schema
nationalcat_df.printSchema()

#checking for dulicates
total_rows = df.count()
unique_rows = df.distinct().count()

print(f"Total Rows: {total_rows}")
print(f"Unique Rows: {unique_rows}")
print(f"Duplicate Rows: {total_rows - unique_rows}")

#checking unique values in national categories
nationalcat_df.select(
    countDistinct("appointment_date").alias("unique_date"),
    countDistinct("icb_ons_code").alias("unique_icb"),
    countDistinct("sub_icb_location_name").alias("unique_subicb"),
    countDistinct("service_setting").alias("unique_servsetting"),
    countDistinct("context_type").alias("unique_context"),
    countDistinct("national_category").alias("unique_cat"),
    countDistinct("appointment_month").alias("unique_month"),
    countDistinct("count_of_appointments").alias("unique_apps")
    
  ).show()

#checking earliest and latest appointment_month dates
natappoint_date_bounds = nationalcat_df.select(
    min("appointment_month").alias("earliest_date"), 
    max("appointment_month").alias("latest_date")
)
# Display the result 
natappoint_date_bounds.show()
