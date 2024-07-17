# Databricks notebook source
def _create_demo_tmp_vw():
    print("Creating the temp view demo_tmp_vw")

    spark.sql("""
        CREATE OR REPLACE TEMP VIEW demo_tmp_vw(name, value) AS VALUES
        ("Yi", 1),
        ("Ali", 2),
        ("Selina", 3)
        """)
    



# COMMAND ----------

_create_demo_tmp_vw()
