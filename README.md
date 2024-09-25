# Steps to recreate the project
## Requirements
- Python 3.12
- Node v18.17.1
- Grunt

### Install Sao
1. Run in whether directory `npm install -g grunt`
2. Go to `cd sao`
3. Run `npm install --production --legacy-peer-deps`
4. Run `grunt`

### Setup trytond
1. Inside the virtual environment, run `pip install -r requirements.txt`
2. Create a new database `learning` with the user `tryton` and password `admin` it should be a superuser
3. Create a tryton-admin edit configuration in Pycharm with these parameters `-c trytond.conf -d learning --all`
4. Complete the information for the user and password
5. After that the database tables should be created
6. Create a trytond edit configuration in Pycharm with these parameters `-c trytond.conf -d learning -v`
7. Run the configuration and the server should be running