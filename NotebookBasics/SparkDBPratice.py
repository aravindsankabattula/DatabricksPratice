# Databricks notebook source
print("starting now")

# COMMAND ----------

dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# COMMAND ----------

# MAGIC %run ./example1-setup

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from demo_tmp_vw

# COMMAND ----------

spark.table("demo_tmp_vw").show()

# COMMAND ----------

dbutils.fs.cp("file:///Users/user1-42477660@lodsprodmca.onmicrosoft.com/DatabricksPratice/resources/employees.json","dbfs:/Volumes/")

# COMMAND ----------

peopleDF = spark.read.json("file:/Users/user1-42477660@lodsprodmca.onmicrosoft.com/DatabricksPratice/resources/employees.json")
