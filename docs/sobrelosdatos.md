---
title: Sobre los datos
subtitle: Origen y tratamiento de los datos de este proyecto
layout: page
hero_image: https://github.com/Maleniski/ing-caracteristicas-migrantes-sonora-arizona/raw/main/docs/imagenes/ARIVACA_CROSSES-800x500-1.jpg
hero_darken: true
show_sidebar: false
---

Se utilizaron dos fuentes principales para este proyecto. El apartado de la SEGOB del registo de eventos de devolución de mexicanas y mexicanos desde Estados Unidos (disponible en esta [liga](http://portales.segob.gob.mx/es/PoliticaMigratoria/EvDevMexEUU)) y el Arizona OpenGIS Initiative for Deceased Migrants (disponible en esta [liga](https://humaneborders.info/)).

Los datos de la SEGOB nos presenta información de repatriados desde Estados Unidos a México del 2016 al 2021, por lo cual se restringieron los datos a repatriados localizados en la frontera de Sonora con Arizona. El Arizona OpenGIS Initiative for Deceased Migrants nos presenta los datos desde 2000 al 2021 de inmigrantes localizados sin vida en Arizona. 

Para hacer una comparación lo más justa posible, se limitaron los datos a los registros de ambas tablas del 2016 al 2021 y posteriormente se hizo una armonización de las tablas para trabajar con solamente una. Los datos armonizados con los datos de las fuentes a noviembre del 2022 estan disponibles en [esta](https://github.com/Maleniski/ing-caracteristicas-migrantes-sonora-arizona/blob/main/migrantsdata.parquet.gzip) liga para su uso.

Se deja también a disposición el script de python que realiza la extracción desde la fuente, limpieza y armonización en la siguiente liga.

El análisis exploratorio de datos puede ser localizado en [este](https://colab.research.google.com/drive/1Fsi7c6mfygu9j_oj2BnoG1lCVmaGWYY8?usp=sharing) Jupyter Notebook en Colab así como un tratamiento completo de los datos en este [otro](https://colab.research.google.com/drive/1F4Tm9_K_bTLebk-QxemxPJVVjkkHA7Up?usp=sharing) Jupyter Notebook de Colab.

Para ver los parámetros que dieron origen a este trabajo, estan disponibles las instrucciones del proyecto en [esta](https://mcd-unison.github.io/ing-caract/proyecto4/) liga, así como la [página del curso](https://mcd-unison.github.io/ing-caract/) de Ingeniería de Características.
