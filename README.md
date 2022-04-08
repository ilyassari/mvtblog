# MVT-Blog
This repo is a django blog template. function based views and forms-form are used.

## Installation

* Firstly clone the project
```bash
git clone https://github.com/ilyassari/mvtblog
```

* After clone the project; open terminal in base directory (the folder which contains *'manage.py'* )

* Python3 must be installed. See official [python](https://www.python.org/) website to learn how installation be in your os.

* Create a virtual environment  
{environment_name} should change any name you choose.
```bash
python3 -m venv {environment_name}
```

* Activate virtual environment in linux (or any posix)
```bash
source {environment_name}/bin/activate
```
Activate virtual environment in windows
```
{environment_name}/bin/activate
```
* To install requirement files in linux
```bash
sudo apt update
sudo apt-get install python3.8.10
pip install -r requirements.txt
```
* Rename *'sample.env'* to *'.env'*

* Create a new *SECRET_KEY*: [this website](https://djecrety.ir/) is recomended. paste new *SECRET_KEY* in the file named *'.env'*

* Use other infos in '.env' if smtplib is using; otherwise you can delete other infos and delete *line 19* in *link/views/contact.py* to prevent errors


## Usage
* To start the virtual server
```bash
python manage.py runserver 8000
```
Then open the browser and go 'http://localhost:8000/' or 'http://127.0.0.1:8000'   
also this will create new database file named '*db.sqlite3*'

* Open a new terminal and create a superuser
```bash
python manage.py createsuperuser
```
This will ask username, email address and password. Fill them.

* You can use blog website.
