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

Otros posibles datasets que habria que evaluar serian:
- Twitter analisis de sentimientos y geolocalizacion, con la finalidad de evaluar la carencia de ciertos servicios en las ciudades.
- Distancias google matrix
- Predicciones aemet
- Policía Municipal. Datos estadísticos actuaciones Policía Municipal



## 3. Despliegue de cluster Hadoop
### Cluster en Google Cloud Platform
Los pasos a seguir son:
1. Ir a la consola de GCP
2. Selecionar o crear un proyecto
3. Crear un cluster mediante el servicio Dataproc que nos permite crear de una forma sencilla un clusteres con Apache Hadoop (HDFS, Pig, Hive,...) y Apache Spark.
4. En opciones avanzadas seleccionar el bucket que hemos creado.
5. Añadir las reglas en el firewall que nos dan acceso a las webs de administracion de HDFS y YARN (en GCP funcionan a traves de los puertos 8088 y 8970). Tambien abrimos el puerto 10000 para las conexiones a Hive server.





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

```sql
CREATE TABLE airbnb (ID INT, Listing_Url STRING, Scrape_ID STRING, Last_Scraped STRING, Name STRING, Summary STRING, Space STRING, Description STRING, Experiences_Offered STRING, Neighborhood_Overview STRING, Notes STRING, Transit STRING, Access STRING, Interaction STRING, House_Rules STRING, Thumbnail_Url STRING, Medium_Url STRING, Picture_Url STRING, XL_Picture_Url STRING, Host_ID STRING, Host_URL STRING, Host_Name STRING, Host_Since STRING, Host_Location STRING, Host_About STRING, Host_Response_Time STRING, Host_Response_Rate STRING, Host_Acceptance_Rate STRING, Host_Thumbnail_Url STRING, Host_Picture_Url STRING, Host_Neighbourhood STRING, Host_Listings_Count STRING, Host_Total_Listings_Count STRING, Host_Verifications STRING, Street STRING, Neighbourhood STRING, Neighbourhood_Cleansed STRING, Neighbourhood_Group_Cleansed STRING, City STRING, State STRING, Zipcode STRING, Market STRING, Smart_Location STRING, Country_Code STRING, Country STRING, Latitude STRING, Longitude STRING, Property_Type STRING, Room_Type STRING, Accommodates STRING, Bathrooms STRING, Bedrooms STRING, Beds STRING, Bed_Type STRING, Amenities STRING, Square_Feet STRING, Price STRING, Weekly_Price STRING, Monthly_Price STRING, Security_Deposit STRING, Cleaning_Fee STRING, Guests_Included STRING, Extra_People STRING, Minimum_Nights STRING, Maximum_Nights STRING, Calendar_Updated STRING, Has_Availability STRING, Availability_30 STRING, Availability_60 STRING, Availability_90 STRING, Availability_365 STRING, Calendar_last_Scraped STRING, Number_of_Reviews STRING, First_Review STRING, Last_Review STRING, Review_Scores_Rating STRING, Review_Scores_Accuracy STRING, Review_Scores_Cleanliness STRING, Review_Scores_Checkin STRING, Review_Scores_Communication STRING, Review_Scores_Location STRING, Review_Scores_Value STRING, License STRING, Jurisdiction_Names STRING, Cancellation_Policy STRING, Calculated_host_listings_count STRING, Reviews_per_Month STRING, Geolocation STRING, Features STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';';
```

Como tenemos los datos en el Cloud Storage podemos cargar directamente los datos indicando el path a gs:
```
LOAD DATA INPATH 'gs://gs-kc-airbnb/datasets/airbnb/airbnb-listings-lite.csv' INTO TABLE airbnb;
```
Para la carga del dataset de prueba que hemos scrapeado de la web [idelista.com](https://www.idealista.com)

```
CREATE TABLE locales (Title STRING, Price STRING, m2 INT, Telf STRING, Desc STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';';
```

```
LOAD DATA INPATH 'gs://gs-kc-airbnb/datasets/idealista/idealista-locales_20190912.csv' INTO TABLE locales;
```



### Procesado de los datos
Ejemplo utilizando wordcount. De forma manual nos conectamos mediante SSH a una de las maquinas del cluster para lanzar la tarea MapReduce:

```bash
yarn jar hadoop-mapreduce-examples.jar wordcount 'gs://gs-kc-airbnb/datasets/airbnb/airbnb-listings-lite.csv' 'wordcount'
```

Tambien se podría realizar mediante la utilidad de lanzar tareas del GCP Dataproc

## 6. Visualizacion y analisis
Con el objetivo de poder cosultar los datos y hacer nuestros propios analiasis
DBeaver
Tableau, Power BI Desktoop, Superset
