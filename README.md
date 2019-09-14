# Big Data Architecture - Práctica Airbnb
Este repositorio describe cada una de las partes desarralladas en la practica de Big Data Architecture del _Bootcamp Big Data & Machine Learning_ de [KeepCoding](https://keepcoding.io/es/)
## Estrategia
Desarrallar una herramienta que nos permita detectar carencias de servicios en determinadas zonas de las ciudades. Oportunidades de negocio

Tendriamos un datalake con todo el conjunto de datos que se van recogiendo tanto en streaming con procesos programados en batch, permitiendo que nuestro algoritmo pueda consultar los datos necesarios y genera resultados que se puedan visualizar... ademas de para posibles analisis a traves de notebooks como Jupyter/Zepelin


## 1. Architectura y Flujo de datos
### Diseño del data lake
A continuación se muestra un diagrama de las herramientas utilizadas para desarrollar el proyecto planteado:
[IMG]

## 2. Datasets y scraping
El proyecto hará uso de varias fuentes de datos con diferente formato, y que se extraeran mediante distintas tácnicas. A modo de ejemplo se ha desarrollado un pequeño crawler utilizando la libreria scrapy para

Twitter analisis de sentimientos y geolocalizacion, con la finalidad de evaluar la carencia de ciertos servicios en las ciudades.

Distancias google matrix
Predicciones aemet
Policía Municipal. Datos estadísticos actuaciones Policía Municipal



## 3. Despliegue de cluster Hadoop
### Cluster en Google Cloud Platform

### Crear bucket (Google Storage)
Google Cloud ofrece almacenamiento de objetos en la nube que se integra con la plataforma de Hadoop de Google Cloud, permitiendo ejecutar trabajos de MapREduce directamente en los datos de Cloud Storage o importar/exportar datos con HIVE al igual que se puede realizar mediant HDFS.

Nos hemos creado un bucket adicional para identificarlo con un nombre que nos sea mas facil recordar. Ademas tambien se han creado varias carpetas dentro del bucket con las finaliadad de tener una mejor organizacion de los datasets recogidos y enviados a nuestro datalake.

![Directories Cloud Storge](img/gs-directories-airbnb.png)



### Comprobar los recusrsos YARN
### Visualizar datos en HDFS
## 4. Subir datasets al cluster
Para el procesamiento de los datos necesitamos subir alguno de los datasets que hemos extraido de forma local. Para ello haremos usod de Google Cloud Storage, ya que este almacenamiento se integra dentro de la platafoma Hadoop de Google Cloud, y podemos facilmente consultarlo y cargarlos haciendo uso de HIVE.

### Subida de datos desde python
Para subir los datos extraidos mediante scraping o cualquier otro dataset adicinal como un csv, json,... utilizaremos la API de python que google proporciona para comunicarse con Google Storage. A diferencia de las pruebas que hemos hecho desde un Collaboratory, cuando lo utilizamos desde un cliente local necesitaremos autentificarnos para poder llevar a cabo la subido de los ficheros.

Los pasos a seguir son:
1. Crear un cuenta de servicio
2. Rellenar los campos que nos pide y seleccionar crear clave de tipo json.
3. Se descagará un fichero json con nuestra clave privada y que utilizaremos desde python para autentificarnos.

Nuestro programa necesitará las librerias cliente para conectarse al Cloud Storage

```
pip install --upgrade google-cloud-storage
```



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
