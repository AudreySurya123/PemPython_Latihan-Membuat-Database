#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'root',
    host = 'localhost',
    database = 'test')

print(conn)

#Disconnecting from the server
conn.close()


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[16]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user = "root",
  passwd ="",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MAHASISWA (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30) NOT NULL,
                    Alamat VARCHAR(255) NOT NULL,
                    Mata_kuliah_yang_diikuti VARCHAR(10),
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[22]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd = "",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MAHASISWA (NIM, Nama, Alamat, Mata_kuliah_yang_diikuti, Umur, Jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s)"
val = [("T0501", "Afif", "Madiun", "Basis Data", "20", "L"),
       ("T0502", "Surya", "Madiun", "Prak PBO", "19", "L"),
       ("T0503", "Susan", "Madiun", "Python", "20", "P"),
       ("T0504", "Tian", "Madiun", "KWU", "19", "L"),
       ("T0505", "Zahra", "Madiun", "Statistika", "19", "P")
      
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[23]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user = "root",
  passwd ="",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama VARCHAR(50) NOT NULL,
                    Mata_kuliah_yang_diajar VARCHAR(50),
                    Alamat VARCHAR(255) NOT NULL,
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[24]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd = "",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, Nama, Mata_kuliah_yang_diajar, Alamat, Umur, Jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s)"
val = [("L055025521", "Masbahah", "Basis Data", "Madiun", "30", "P"),
       ("L055025522", "Akhmad Syarif", "Prak PBO", "Banjarmasin", "29", "L"),
       ("L055025523", "Yusuf Fadlila", "Python", "Madiun", "29", "L"),
       ("L055025524", "Darmawan Lahru", "KWU", "Madiun", "31", "L"),
       ("L055025525", "Trisna Ari", "Statistika", "Ponorogo", "30", "P")
      
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[26]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user = "root",
  passwd ="",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MATA_KULIAH (
                    Kode_MK VARCHAR(10) NOT NULL,
                    Nama_MK VARCHAR(50) NOT NULL,
                    Waktu DATE,
                    Ruangan VARCHAR(10),
                    Tempat VARCHAR(20)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[33]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd = "",
  database = "d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (Kode_MK, Nama_MK, Waktu, Ruangan, Tempat)VALUES (%s, %s, %s, %s, %s)"
val = [("MK171", "Basis Data", "2023-04-3", "L4R2", "G.Biru"),
       ("MK172", "Prak PBO", "2023-04-5", "L2R5", "G.Hijau"),
       ("MK173", "Python", "2023-04-6", "L2R3", "G.Hijau"),
       ("MK174", "KWU", "2023-04-7", "L1R2", "G.Biru"),
       ("MK175", "Statistika", "2023-04-8", "L3R7", "G.Biru")
       
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[35]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()


sql = "SELECT   matkul.Nama_MK, mahasiswa.Nama, dosen.Nama FROM MATA_KULIAH matkul    INNER JOIN MAHASISWA mahasiswa ON mahasiswa.Mata_kuliah_yang_diikuti = matkul.Nama_MK    INNER JOIN DOSEN dosen ON dosen.Mata_kuliah_yang_diajar = matkul.Nama_MK"

cursorObject.execute(sql)

result = cursorObject.fetchall()

for row in result:
    print(row)

dataBase.close()


# In[ ]:




