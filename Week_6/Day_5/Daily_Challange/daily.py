#potgres

 HOSTNAME = 'localhost'
 USERNAME = 'postgres'
 PASSWORD = 'postgres'
 DATABASE = 'country_api'
 def db_update():
     request =requests.get('https://restcountries.eu/rest/v2/all')
     request=request.json()
     return request

 data=db_update()


 for i in range (10):
     db_update()
     connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
     cursor=connection.cursor()
     country=data[randint(0,30)]
     query=f"INSERT INTO countries(names,subregion,flag,population)VALUES ('{country['name']}','{country['flag']}','{country['subregion']}',{country['population']})"
     cursor.execute(query)
     connection.commit()
     connection.close()