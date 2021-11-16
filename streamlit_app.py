import s3fs
import os
import streamlit as st

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents. 
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("hellofreshexample/HelloFreshExample.csv")

# # Print results.
# for line in content.strip().split("\n"):
#     name, pet = line.split(",")
#     st.write(f"{name} has a :{pet}:")





# streamlit_app.py

# import streamlit as st
# # import s3fs
# import os
# import boto3

# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-east-2',
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
# )

# for bucket in s3.buckets.all():
#     print(bucket.name)




# # Create connection object.
# # `anon=False` means not anonymous, i.e. it uses access keys to pull data.
# fs = s3fs.S3FileSystem(anon=False)

# # Retrieve file contents.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def read_file(filename):
#     with fs.open(filename) as f:
#         return f.read().decode("utf-8")

# content = read_file("hellofreshexample/HelloFreshExample.csv")

# # # Print results.
# # for line in content.strip().split("\n"):
# #     name, pet = line.split(",")
# #     st.write(f"{name} has a :{pet}:")
