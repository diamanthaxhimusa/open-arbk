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
sudo a2ensite peaceobservatory-cgs.org.conf
```

Restarto serverin per te marr efekt ndryshimet:
```
sudo service apache2 restart
```
