# Bizneset e Hapura

#
# Pershkrimi i projektit
>

# Instruksionet Teknike
### 1. Instalimi ne Server
#### Hapsira Punuese
- Ubuntu 16.04 LTS 64 bit
- MongoDB 3.2.x
- Apache Virtual Hosts (httpd)
- Python 2.2.7

#### Hapi i pare
Apache Virtual Host:
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```

Hap nje fajl te ri ne terminal si super admin:
```
sudo nano app.wsgi
```

Dhe konfiguro vendin e projektit:
```
app_dir_path = '/var/www/open-arbk'
```

Krijo dhe edito fajlin e konfigurimit te projektit:
```
sudo cp config-template.cfg config.cfg
sudo nano config.cfg
```


#### Krijo nje Hapsire Virtuale
Kopjo konfigurimin default te hapsires virtuale tek nje fajl i ri enkas per projektin:
```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/open-arbk.conf
```

Hap fajlin e ri ne terminal si super admin:
```
sudo nano /etc/apache2/sites-available/open-arbk.conf
```

Dhe konfiguroje ate te shkoj te app.wsgi fajli i projektit:
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

#### Aktivizo hapsiren e re virtuale
Se pari deaktivizo default:
```
sudo a2dissite 000-default.conf
```

Pastaj aktivizo ate qe sapo krijuam:
```
sudo a2ensite open-arbk.conf
```

Restarto serverin per te marr efekt ndryshimet:
```
sudo service apache2 restart
```

### 2. Instalimi Lokal (UBUNTU)


Se pari, krijo nje folder ne desktopin tuaj:
```
cd ~
mkdir dev
cd dev
```

Merrni projektin lokalisht:
```
git clone https://github.com/opendatakosovo/open-arbk.git
cd bpo
```

Instalo the fillo projektin:
```
bash install.sh
bash run-debug.sh
```

### 3. Pergaditja e dokumenteve dhe databases
Se pari pasi qe te importoni databasen ne mongo duhet startuar skripta qe rregullon dokumentet:
```
ruby fix_activities.rb
```

```
bash activity-importer.sh
bash muni-importer.sh
```

Pastaj startoni skripten e cila formaton databasen e vjeter ne nje te re te formatuar:
```
bash data-importer.sh
```

Pasi te perfundoj krijimi i koleksionit te ri, duhet pergatitur dokumentet per shkarkim:
```
bash document-prepare.sh
bash zip-json-csv.sh
```
