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
The data have been extracted from the KBRA’s official site using our open source web scraper [ARBK Scraper](https://github.com/opendatakosovo/arbk-scraper/).

After ARBK scraper is done, each document will look like this for example:
```
{
    "_id" : ObjectId("58cc8dbc70ff0e9ff2de8807"),
    "raw" : {
        "info" : [
            {
                "key" : "Emri",
                "value" : "N.T.SH. \"Kosova - Tex\""
            },
            {
                "key" : "Lloji Biznesit",
                "value" : "Biznes individual"
            },
            {
                "key" : "Nr Regjistrimit",
                "value" : "70000015"
            },
            {
                "key" : "Nr Fiskal",
                "value" : "600538063"
            },
            {
                "key" : "Nr Cerfitikues KTA",
                "value" : ""
            },
            {
                "key" : "Nr Punëtorëve",
                "value" : "2"
            },
            {
                "key" : "Data e konstituimit",
                "value" : "2011.08.16"
            },
            {
                "key" : "Data e Aplikimit",
                "value" : "2003.03.13"
            },
            {
                "key" : "Komuna",
                "value" : "Ferizaj"
            },
            {
                "key" : "Adresa",
                "value" : "Ismet Ramadani"
            },
            {
                "key" : "Telefoni",
                "value" : ""
            },
            {
                "key" : "E-mail",
                "value" : ""
            },
            {
                "key" : "Kapitali",
                "value" : "0.00"
            },
            {
                "key" : "Statusi në ATK",
                "value" : "//"
            },
            {
                "key" : "Emri",
                "value" : "N.T.SH. \"Kosova - Tex\""
            },
            {
                "key" : "Lloji Biznesit",
                "value" : "Biznes individual"
            },
            {
                "key" : "Nr Regjistrimit",
                "value" : "70000015"
            },
            {
                "key" : "Nr Fiskal",
                "value" : "600538063"
            },
            {
                "key" : "Nr Cerfitikues KTA",
                "value" : ""
            },
            {
                "key" : "Nr Punëtorëve",
                "value" : "2"
            },
            {
                "key" : "Data e konstituimit",
                "value" : "2011.08.16"
            },
            {
                "key" : "Data e Aplikimit",
                "value" : "2003.03.13"
            },
            {
                "key" : "Komuna",
                "value" : "Ferizaj"
            },
            {
                "key" : "Adresa",
                "value" : "Ismet Ramadani"
            },
            {
                "key" : "Telefoni",
                "value" : ""
            },
            {
                "key" : "E-mail",
                "value" : ""
            },
            {
                "key" : "Kapitali",
                "value" : "0.00"
            },
            {
                "key" : "Statusi në ATK",
                "value" : "//"
            }
        ],
        "authorized" : [
            {
                "key" : "Mezafer Aliu",
                "value" : "Agjent i regjistruar"
            }
        ],
        "owners" : [
            {
                "key" : "1",
                "value" : "Mezafer Aliu"
            }
        ],
        "activities" : [
            {
                "key" : "4645",
                "value" : "Tregtia me shumicë e artikujve të parfumerisë dhe kozmetikës"
            },
            {
                "key" : "4621",
                "value" : "Tregtia me shumicë e drithërave, duhanit të papërpunuar, farërave dhe ushqimit të kafshëve"
            },
            {
                "key" : "5020",
                "value" : "Transporti detar dhe bregdetar i mallrave"
            },
            {
                "key" : "9609",
                "value" : "Aktivitetet e tjera p.k.t."
            },
            {
                "key" : "4636",
                "value" : "Tregtia me shumicë e sheqerit, e çokollatës dhe e ëmbëlsirave"
            },
            {
                "key" : "4638",
                "value" : "Tregtia me shumicë e artikujve të tjerë ushqimorë, përfshirë peshkun, krustacet dhe molusqet (frutat e detit)"
            },
            {
                "key" : "4690",
                "value" : "Tregtia me shumicë jo e specializuar"
            },
            {
                "key" : "4637",
                "value" : "Tregtia me shumicë e kafes, çajit, kakaos dhe erëzave"
            },
            {
                "key" : "9329",
                "value" : "Aktivitetet e tjera të argëtimit dhe rekreacionit"
            },
            {
                "key" : "4642",
                "value" : "Tregtia me shumicë e veshjeve dhe këpucëve"
            },
            {
                "key" : "4799",
                "value" : "Tregtia tjetër me pakicë, jo në dyqane, tezga ose tregje"
            },
            {
                "key" : "4941",
                "value" : "Transporti rrugor i mallrave"
            }
        ]
    },
    "formatted" : {
        "owners" : [
            "Mezafer Aliu"
        ],
        "authorized" : [
            "Mezafer Aliu"
        ],
        "activities" : [
            4645,
            4621,
            5020,
            9609,
            4636,
            4638,
            4690,
            4637,
            9329,
            4642,
            4799,
            4941
        ],
        "type" : "Biznes individual",
        "registrationNum" : 70000015,
        "fiscalNum" : 600538063,
        "employeeCount" : 2,
        "establishmentDate" : ISODate("2011-08-16T00:00:00.000Z"),
        "applicationDate" : ISODate("2003-03-13T00:00:00.000Z"),
        "municipality" : "Ferizaj",
        "capital" : 0.0,
        "atkStatus" : "//",
        "timestamp" : ISODate("2017-03-18T01:30:36.316Z"),
        "name" : "N.T.SH. \"Kosova - Tex\"",
        "status" : "Aktiv",
        "arbkUrl" : "http://arbk.rks-gov.net/page.aspx?id=1,38,125000011"
    }
}
```

Then we need to run importers to format data:
```
bash activity-importer.sh
bash muni-importer.sh
```
These two importers prepare municipalities and acitivities in two seperate collections.
After importing municipalities and activities we are ready to import the businesses collection, which will create a collection called "reg_businesses".
```
bash data-importer.sh
```
After this importer is done a document will lok like this for example:
```
{
    "_id" : ObjectId("5996b0b3bacaea16286ef2be"),
    "status" : {
        "sq" : "Aktiv",
        "en" : "Active"
    },
    "activities" : [
        4645,
        4621,
        5020,
        9609,
        4636,
        4638,
        4690,
        4637,
        9329,
        4642,
        4799,
        4941
    ],
    "owners" : [
        {
            "gender" : "male",
            "name" : "Mezafer Aliu"
        }
    ],
    "slugifiedMunicipality" : {
        "sq" : "ferizaj",
        "en" : "ferizaj"
    },
    "arbkUrl" : "http://arbk.rks-gov.net/page.aspx?id=1,38,125000011",
    "atkStatus" : "//",
    "fiscalNum" : 600538063,
    "establishmentDate" : ISODate("2011-08-16T00:00:00.000Z"),
    "slugifiedOwners" : [
        "mezafer-aliu"
    ],
    "municipality" : {
        "place" : "Ferizaj",
        "municipality" : {
            "sq" : "Ferizaj",
            "en" : "Ferizaj"
        }
    },
    "applicationDate" : ISODate("2003-03-13T00:00:00.000Z"),
    "slugifiedAuthorized" : [
        "mezafer-aliu"
    ],
    "slugifiedBusiness" : "n-t-sh-kosova-tex",
    "authorized" : [
        {
            "gender" : "male",
            "name" : "Mezafer Aliu"
        }
    ],
    "capital" : 0,
    "employeeCount" : 2,
    "registrationNum" : 70000015,
    "type" : {
        "sq" : "Biznes individual",
        "en" : "Individual Business"
    },
    "dataRetrieved" : ISODate("2017-03-18T01:30:36.316Z"),
    "name" : "N.T.SH. Kosova - Tex"
}
```

When creating the new collection is finished, run scripts to prepare data for download:
```
sudo bash document-prepare.sh
sudo bash zip-json-csv.sh
```
