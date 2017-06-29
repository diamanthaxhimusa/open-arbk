# Open Businesses

#
# Project description
>

# Technical Instructions
### 1. Server Installation
#### Environment
- Ubuntu 16.04 LTS 64 bit
- MongoDB 3.2.x
- Apache Virtual Hosts (httpd)
- Python 2.2.7

#### Initial Setup
Apache Virtual Host:
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```

Open the new file in your editor with root privileges:
```
sudo nano app.wsgi
```

And configure the project's path:
```
app_dir_path = '/var/www/open-arbk'
```

Create and edit project config file:
```
sudo cp config-template.cfg config.cfg
sudo nano config.cfg
```


#### Create New Virtual Host
Copy default virtual host config file to create new file specific to the project:
```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/open-arbk.conf
```

Open the new file in your editor with root privileges:
```
sudo nano /etc/apache2/sites-available/open-arbk.conf
```

And configure it to point to the project's app.wsgi file:
```
<VirtualHost *:80>
  ServerAdmin admin@localhost

  WSGIScriptAlias / /var/www/open-arbk/app.wsgi
  <Directory /var/www/open-arbk>
    Order allow,deny
    Allow from all
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

#### Enable New Virtual Host
First disable the defaul one:
```
sudo a2dissite 000-default.conf
```

Then enable the new one we just created:
```
sudo a2ensite open-arbk.conf
```

Restart the server for these changes to take effect:
```
sudo service apache2 restart
```

### 2. Local Installation (UBUNTU)


First create a folder in your desktop called dev:
```
cd ~
mkdir dev
cd dev
```

Getting the project in your local machine:
```
git clone https://github.com/opendatakosovo/open-arbk.git
cd open-arbk
```

Install and run the app:
```
bash install.sh
bash run-debug.sh
```

### 3. Database and Documents Preparation
First after importing the database in mongo you need to start the scripts that fix the database:
```
ruby fix_activities.rb
```

```
bash activity-importer.sh
bash muni-importer.sh
```

Then start the script that formattes the old collection of the database to a new improved one:
```
bash data-importer.sh
```

When creating the new collection is finished , run scripts to prepare data for download:
```
sudo bash document-prepare.sh
sudo bash zip-json-csv.sh
```
