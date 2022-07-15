#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install psycopg2')


# In[2]:


import psycopg2


# In[3]:


try:
    conn = psycopg2.connect("host = localhost dbname = postgres user= postgres password = admin22")
except psycopg2.Error as e:
    print("error: could not make connection")
    print(e)


# In[4]:


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error could not get cursor")
    print(e)


# In[5]:


conn.set_session(autocommit = True)


# In[6]:


try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)


# In[7]:


try:
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try:
    conn = psycopg2.connect("host = localhost dbname = myfirstdb user= postgres password = admin22")
except psycopg2.Error as e:
    print("error: could not make connection")
    print(e)
    
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error could not get cursor")
    print(e)    
conn.set_session(autocommit = True)   


# In[8]:


try:
    cur.execute("CREATE TABLE IF NOT EXISTS students(student_id int, name varchar, age int, gender varchar,     subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: crating table")
    print(e)


# In[9]:


try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks)    VALUES(%s, %s, %s, %s, %s, %s)",                (1, "Suyash", 22, "Male", "Java", 85))
except psycopg2.Error as e:
    print("Error entering records")
    print(e)
try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks)    VALUES(%s, %s, %s, %s, %s, %s)",                (2, "Chaz", 23, "Male", "Python", 70))
except psycopg2.Error as e:
    print("Error entering records")
    print(e)       
try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks)    VALUES(%s, %s, %s, %s, %s, %s)",                (3, "Ram", 21, "Male", "PHP", 80))
except psycopg2.Error as e:
    print("Error entering records")
    print(e)    
try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks)    VALUES(%s, %s, %s, %s, %s, %s)",                (4, "Seema", 24, "Male", "Java", 95))
except psycopg2.Error as e:
    print("Error entering records")
    print(e)


# In[11]:


try:
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e:
    print('Error finding records')
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()


# In[12]:


cur.close()
conn.close()


# In[ ]:




