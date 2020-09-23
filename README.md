# ProyectoFinalAnalisis
#
Pulso Político por provincias
  Este tema tiene dos fuentes de datos la primera es un dataset proporcionado por una encuesta realizada por diario El Mercurio de Cuenca, en el cual se pregunta ¿Si las     elecciones fueran hoy por quién usted votaría? la cual cuenta con alrededor de 4000 votaciones.<br/>
  La segunda fuente es twitter se elaboro el script "pulsopolitico.py" para la recolección de datos tanto con filtro de geolocalización usando las coordenadas del archivo "Coordenadas por provincia" y de palabras. <br/>
  El archivo "dataset encuesta" tiene como campos "Date and Time, Time, Candidato, Country, Region, IP" de los cuales solo se utilizaron solo los 5 primeros.   <br/>
  Los tweets tiene una estructura amplia de la cual nos interesa los hashtags, menciones, el texto y el lugar (país, ciudad).  <br/>
  La carpeta comprimida "bases couchDB pulso politico por provincias.rar" contiene las bases de datos locales de CouchDB donde se almacenaron los tweets, estas bases representan a cada una de las provincias.<br/>
  Para usar elasticsearch primero, se procedió a crear cada indice y para cada indice se realizó la configuración de mapping detallada en el archivo "mapping indices elasticseach" donde se definen los formatos de fecha y geolocalización para los tweets.<br/>
  El traslado de datos de couchDB y el archivo CSV a elasticsearch se lo realizo con los archivos de configuración de la carpeta comprimida "Archivos conf de logstash".<br/>
  Finalmente en kibana se realizaron las visualizaciones, ya que kibana tiene el benfecio de conectarse con elasticsearch, es aquí donde se realizaron visualizaciones de tag cloud, mapas de calor, barras laterales y pastel. Las visualizaciones se encuentran en la carpeta comprimida "Visualizaciones pulso politico por provincias".<br/>
  
