Setup on windows

cd ./server

A. Server setup

1. Install Python 3.9
  * https://www.python.org/downloads/windows/

2. Install/Setup Python VirtualEnv
  * py -m pip install --user virtualenv
  * py -m venv env
  * _If getting warning on cache : https://github.com/pypa/pip/issues/5250_
  * source .\env\Scripts\activate

3. Install Django and DRF
  * pip3 install -r requirements.txt

4. MYSQL(version 5.7) on windows:
  * Install using windows installer. https://dev.mysql.com/downloads/mysql/5.7.html#downloads
  * pip install mysqlclient (if required)

5. Mysql User setup:
  * CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
  * create database ordermanager;
  * GRANT ALL PRIVILEGES ON ordermanager. * TO 'root'@'localhost';
  * Flush privileges;

6. Complete mysql setup(below) before this:
  * py manage.py migrate
  * py manage.py createsuperuser

7. Running the server
  * py manage.py runserver 
  * Server will run on port 8000

B. Client setup

cd ./client
1. Install NodeJs
 * https://nodejs.org/en/download/

2. Install dependencies
  * npm install

3. Run
  * npm start