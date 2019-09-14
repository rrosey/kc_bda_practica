# Big Data Architecture - Práctica Airbnb
Este repositorio describe cada una de las partes desarralladas en la practica de Big Data Architecture del _Bootcamp Big Data & Machine Learning_ de [KeepCoding](https://keepcoding.io/es/)
## 1. Architectura y Flujo de datos
### Diseño del data lake
A continuación se muestra un diagrama de las herramientas utilizadas para desarrollar el proyecto planteado:
[IMG]

## 2. Datasets y scraping
El proyecto hará uso de varias fuentes de datos con diferente formato, y que se extraeran mediante distintas tácnicas. A modo de ejemplo se ha desarrollado un pequeño crawler utilizando la libreria scrapy para 

## 3. Despliegue de cluster Hadoop
### Cluster en Google Cloud Platform

### Crear segmento (Google Storage)
### Comprobar los recusrsos YARN
### Visualizar datos en HDFS
## 4. Subir datasets al cluster
Para el procesamiento de los datos necesitamos subir alguno de los datasets que hemos extraido de forma local. Para ello haremos usod de Google Cloud Storage, ya que este almacenamiento se integra dentro de la platafoma Hadoop de Google Cloud, y podemos facilmente consultarlo y cargarlos haciendo uso de HIVE.

### Subida de datos desde python
Para subir los datos extraidos mediante scraping o cualquier otro dataset adicinal como un csv, json,... utilizaremos la API de python que google proporciona para comunicarse con Google Storage. A diferencia de las pruebas que hemos hecho desde un Collaboratory, cuando lo utilizamos desde un cliente local necesitaremos autentificarnos para poder llevar a cabo la subido de los ficheros.

Los pasos a seguir son:
1. afda
2. asdasf

## 5. Ingestion y Procesado de datos
### Procesado en streaming

### Procesado en batch
#### HIVE
Transformacion y agregacion de los datos
### Procesado de los datos


## 6. Visualizacion y analisis
Con el objetivo de poder cosultar los datos y hacer nuestros propios analiasis
DBeaver
Tableau, Power BI Desktoop, Superset
