# Proyecto Final Análisis
#
Pulso Politico por Ciudades
  Este tema tiene un solo origin de datos que son los tweets del Pulso politico en las diferetes ciudades de Ecuador. 
  Los datos se recopilarían mediante un scrpit "Tweets Ciudades.py" de tweets con las credenciales de la API de Twitter. Estso datos se guardaran en una database ciudades y en cada coleccion los datos de cada tweet.
  <br/>
  Al finalizar los datos se indexaran a Elastisearch, pero antes se debian mover a CouchDB por el inconveniente de que no existe plugin de input en Logstash,a se que con el archivo "Paso de Datos a Diferentes Bases.txt", y asi subirlos a Couch, una vez desde aqui se los indexara a Elastichsearch mediante Logstash con el archivo "couchdb.conf".
  Cuando se indexen los datos a elastic, se procede a unir con kibana y crear un index pattern que servira para tomar los datos desde elasticsearh y realizar las visualizaciones correspondientes.
  estas se pueden visualizar desde el archivo rar "Visualizaciones Kibana".
<br/>
Pulso Político por provincias
  Este tema tiene dos fuentes de datos la primera es un dataset proporcionado por una encuesta realizada por diario El Mercurio de Cuenca, en el cual se pregunta ¿Si las     elecciones fueran hoy por quién usted votaría? la cual cuenta con alrededor de 4000 votaciones.<br/>
  <br/>
  La segunda fuente es twitter se elaboro el script "pulsopolitico.py" para la recolección de datos tanto con filtro de geolocalización usando las coordenadas del archivo "Coordenadas por provincia" y de palabras. <br/>
  <br/>
  El archivo "dataset encuesta" tiene como campos "Date and Time, Time, Candidato, Country, Region, IP" de los cuales solo se utilizaron solo los 5 primeros.   <br/>
  <br/>
  Los tweets tiene una estructura amplia de la cual nos interesa los hashtags, menciones, el texto y el lugar (país, ciudad).  <br/>
  <br/>
  La carpeta comprimida "bases couchDB pulso politico por provincias.rar" contiene las bases de datos locales de CouchDB donde se almacenaron los tweets, estas bases representan a cada una de las provincias.<br/>
  <br/>
  Para usar elasticsearch primero, se procedió a crear cada indice y para cada indice se realizó la configuración de mapping detallada en el archivo "mapping indices elasticseach" donde se definen los formatos de fecha y geolocalización para los tweets.<br/>
  <br/>
  El traslado de datos de couchDB y el archivo CSV a elasticsearch se lo realizo con los archivos de configuración de la carpeta comprimida "Archivos conf de logstash".<br/>
  <br/>
  Finalmente en kibana se realizaron las visualizaciones, ya que kibana tiene el benfecio de conectarse con elasticsearch, es aquí donde se realizaron visualizaciones de tag cloud, mapas de calor, barras laterales y pastel. Las visualizaciones se encuentran en la carpeta comprimida "Visualizaciones pulso politico por provincias".<br/>
  <br/>
  En la carpeta <strong>Evento o noticial mundial</strong> se encuentra los datasets utilizados para la recopilación de la información. También se encuentra el archivo de PowerBI con todas las visualizaciones realizadas con la información obtenida.
  <br/>
  <br/>
  En la carpeta **Video Juegos** se encuentra el dataset que se utilizó para realizar el análisis. También se encuentra el archivo de PowerBI con el dashboaard respectivo.
  <br/>
  <br/>
  Se adjunta la dirección del cluster de MomgoDB donde se encuentra la Base de Datos general de todo el proyecto.
  <b>mongodb+srv://yolo13a:12345@cluster0.lhnsz.mongodb.net/test</b>
  <br/>
  <br/>
  Link del video de youtube: https://www.youtube.com/watch?v=ADnMoDp0TsQ&t=5s 
