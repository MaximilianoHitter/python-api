Api creada con FastAPI, SQLAlchemy y Python.
Este es un proyecto pensado para utilizarse para consumir datos del proyecto https://github.com/MaximilianoHitter/laravel-react-api

Es necesario instalar primeramente python.
Es necesario contar con una base de datos mysql, con un servidor corriendo y en la línea 9
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://user:password@localhost/database", reemplazar user con el usuario, password con la contraseña y database con el nombre de la db.
Es necesario contar con las tablas trainers y specialists, las cuales deben contener al menos los siguientes campos:
-id (int, pk)
-name (varchar(255))
-last_name (varchar(255))
-profile_picture_url (varchar(255))

Para correr el server es necesario correr por consola fast_api\Scripts\activate
Luego levantar el servidor con uvicorn main:app (este server se levanta sobre el puerto 8000, en caso de querer cambiarlo luego de main:app añadir --port:xxxx reemplazando xxxx con el número de puerto)
Se puede acceder a la documentación por medio de localhost:PORT/docs
