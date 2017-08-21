# Open Businesses

>
## Project description

Open Businesses is a business registration search engine with data from over 170,000 businesses in Kosovo. The data was scraped from the Kosovo Business Registration Agency (ARBK). Opening business data allows economic analysis of sectors as well as various economic activities. It creates space for analyzing economic trends in different periods and regions. It creates space for market analysis by local and international investors. Opening these business data enables data linking with other sectors such as public procurement or property declaration, which would strengthen anti-corruption mechanisms.

## Technical Instructions
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
The data have been extracted from the [ARBK](http://arbk.rks-gov.net/) official site using our open source web scraper [ARBK Scraper](https://github.com/opendatakosovo/arbk-scraper/).

After ARBK scraper is done, each document will look like this for example:
```
{
    "_id" : ObjectId("58ceb46cffd93a027eae32ef"),
    "raw" : {
        "info" : [
            {
                "key" : "Emri",
                "value" : "\" Lirita\" Sh.p.k."
            },
            {
                "key" : "Lloji Biznesit",
                "value" : "Shoqëri me përgjegjësi të kufizuara"
            },
            {
                "key" : "Nr Regjistrimit",
                "value" : "70318754"
            },
            {
                "key" : "Nr Fiskal",
                "value" : ""
            },
            {
                "key" : "Nr Cerfitikues KTA",
                "value" : ""
            },
            {
                "key" : "Nr Punëtorëve",
                "value" : "5"
            },
            {
                "key" : "Data e konstituimit",
                "value" : "2006.02.10"
            },
            {
                "key" : "Data e Aplikimit",
                "value" : "2005.11.23"
            },
            {
                "key" : "Komuna",
                "value" : "Bibaj"
            },
            {
                "key" : "Adresa",
                "value" : ","
            },
            {
                "key" : "Telefoni",
                "value" : "044-343-875"
            },
            {
                "key" : "E-mail",
                "value" : ""
            },
            {
                "key" : "Kapitali",
                "value" : "2501.00"
            },
            {
                "key" : "Statusi në ATK",
                "value" : "//"
            },
            {
                "key" : "Emri",
                "value" : "\" Lirita\" Sh.p.k."
            },
            {
                "key" : "Lloji Biznesit",
                "value" : "Shoqëri me përgjegjësi të kufizuara"
            },
            {
                "key" : "Nr Regjistrimit",
                "value" : "70318754"
            },
            {
                "key" : "Nr Fiskal",
                "value" : ""
            },
            {
                "key" : "Nr Cerfitikues KTA",
                "value" : ""
            },
            {
                "key" : "Nr Punëtorëve",
                "value" : "5"
            },
            {
                "key" : "Data e konstituimit",
                "value" : "2006.02.10"
            },
            {
                "key" : "Data e Aplikimit",
                "value" : "2005.11.23"
            },
            {
                "key" : "Komuna",
                "value" : "Bibaj"
            },
            {
                "key" : "Adresa",
                "value" : ","
            },
            {
                "key" : "Telefoni",
                "value" : "044-343-875"
            },
            {
                "key" : "E-mail",
                "value" : ""
            },
            {
                "key" : "Kapitali",
                "value" : "2501.00"
            },
            {
                "key" : "Statusi në ATK",
                "value" : "//"
            }
        ],
        "authorized" : [
            {
                "key" : "Lyirim Zefi",
                "value" : "Drejtor."
            }
        ],
        "owners" : [
            {
                "key" : "1",
                "value" : "N.T.P. \"Zefi S\""
            },
            {
                "key" : "2",
                "value" : "\"Q.K.I. \" Sh.p.k."
            }
        ],
        "activities" : [
            {
                "key" : "4671",
                "value" : "Tregtia me shumicë e lëndëve djegëse të ngurta, të lëngëta ose të gazta dhe produkteve të lidhur me to"
            },
            {
                "key" : "4711",
                "value" : "Tregtia me pakicë në dyqane jo të specializuar, ku mbizotëron ushqimi, pijet dhe duhani"
            },
            {
                "key" : "5610",
                "value" : "Restorantet dhe aktivitetet shërbyese lëvizëse të ushqimit"
            },
            {
                "key" : "4752",
                "value" : "Tregtia me pakicë e artikujve elektronikë, ngjyrave dhe xhamit, në dyqane të specializuara"
            },
            {
                "key" : "4730",
                "value" : "Tregtia me pakicë e karburantit për automjete në dyqane të specializuar"
            }
        ]
    },
    "formatted" : {
        "owners" : [
            "N.T.P. \"Zefi S\"",
            "\"Q.K.I. \" Sh.p.k."
        ],
        "authorized" : [
            "Lyirim Zefi"
        ],
        "activities" : [
            4671,
            4711,
            5610,
            4752,
            4730
        ],
        "type" : "Shoqëri me përgjegjësi të kufizuara",
        "registrationNum" : 70318754,
        "employeeCount" : 5,
        "establishmentDate" : ISODate("2006-02-10T00:00:00.000Z"),
        "applicationDate" : ISODate("2005-11-23T00:00:00.000Z"),
        "municipality" : "Bibaj",
        "capital" : 2501.0,
        "atkStatus" : "//",
        "timestamp" : ISODate("2017-03-19T16:40:12.776Z"),
        "name" : "\" Lirita\" Sh.p.k.",
        "status" : "Aktiv",
        "arbkUrl" : "http://arbk.rks-gov.net/page.aspx?id=1,38,125018763"
    }
}
```

Then we need to run importers to format data.
```
bash activity-importer.sh
```
The activity importer creates a collection with codes and description of all 615 activities.
Example:
```
{
    "_id" : ObjectId("597b4612bacaea17c7e68618"),
    "code" : "111",
    "activity" : {
        "sq" : "Kultivimi i drithërave (përveç orizit), i bimëve bishtajore dhe i farërave vajore",
        "en" : "Growing of cereals (except rice), leguminous crops and oil seeds"
    }
}
```

The municipality importer creates a collection with municipalities and places that belongs to them. This is used to correct the data we got from ARBK where in some cases they showed places instead of actual municipalities. In this example is 'Bibaj' which belongs to 'Ferizaj'.
```
bash muni-importer.sh
```
A municipality in the municipality collection will look like this:
```
{
    "_id" : ObjectId("5996ae27bacaea119874a6fb"),
    "districts" : [
        "Bablak",
        "Babush",
        "Balaj",
        "Bibaj",
        "Burrnik",
        "Bajicë",
        "Baincë",
        "Cërnillë",
        "Doganaje",
        "Dremjak",
        "Babush",
        "Dardani",
        "Ferizaj",
        "Gaçkë",
        "Gurëz",
        "Jazhincë",
        "Biçec",
        "Greme",
        "Jezercë",
        "Komogllavë",
        "Nekodim",
        "Koshare",
        "Kosinë",
        "Lloshkobare",
        "Nikadin",
        "Nerodime e Epërme",
        "Nerodime e Ulët",
        "Mirash",
        "Muhovc",
        "Manastircë",
        "Mirosalë",
        "Papaz",
        "Pleshinë",
        "Pleshinë e Epërme",
        "Pleshinë e ulët",
        "Pojatë",
        "Prelez i Jerlive",
        "Prelez i Muhaxherëve",
        "Rahavicë",
        "Rakaj",
        "Sazli",
        "Slivove",
        "Softaj",
        "Sojevë",
        "Surqinë",
        "Fshati i Vjetër",
        "Talinovc i Jerlive",
        "Talinovc i Muhaxherëve",
        "Tërn",
        "Varosh",
        "Zaskoc"
    ],
    "municipality" : {
        "sq" : "Ferizaj",
        "en" : "Ferizaj"
    },
    "slug" : {
        "sq" : "ferizaj",
        "en" : "ferizaj"
    }
}
```
These two importers prepare municipalities and acitivities in two seperate collections.
After importing municipalities and activities we are ready to import the businesses collection, which will create a collection called "reg_businesses".
```
bash data-importer.sh
```
After running all importers a the document will look like this:
```
{
    "_id" : ObjectId("5996b0d4bacaea16286f107e"),
    "status" : {
        "sq" : "Aktiv",
        "en" : "Active"
    },
    "activities" : [
        4671,
        4711,
        5610,
        4752,
        4730
    ],
    "owners" : [
        {
            "gender" : "unknown",
            "name" : "N.T.P. \"Zefi S\""
        },
        {
            "gender" : "unknown",
            "name" : "\"Q.K.I. \" Sh.p.k."
        }
    ],
    "slugifiedMunicipality" : {
        "sq" : "ferizaj",
        "en" : "ferizaj"
    },
    "arbkUrl" : "http://arbk.rks-gov.net/page.aspx?id=1,38,125018763",
    "atkStatus" : "//",
    "fiscalNum" : "",
    "establishmentDate" : ISODate("2006-02-10T00:00:00.000Z"),
    "slugifiedOwners" : [
        "n-t-p-zefi-s",
        "q-k-i-sh-p-k"
    ],
    "municipality" : {
        "place" : "Bibaj",
        "municipality" : {
            "sq" : "Ferizaj",
            "en" : "Ferizaj"
        }
    },
    "applicationDate" : ISODate("2005-11-23T00:00:00.000Z"),
    "slugifiedAuthorized" : [
        "lyirim-zefi"
    ],
    "slugifiedBusiness" : "lirita-sh-p-k",
    "authorized" : [
        {
            "gender" : "male",
            "name" : "Lyirim Zefi"
        }
    ],
    "capital" : 2501,
    "employeeCount" : 5,
    "registrationNum" : 70318754,
    "type" : {
        "sq" : "Shoqëri me përgjegjësi të kufizuara",
        "en" : "Limited Liability Company"
    },
    "dataRetrieved" : ISODate("2017-03-19T16:40:12.776Z"),
    "name" : " Lirita Sh.p.k."
}
```

When all importers are done, run this to create CSV and JSON files for download, this will create a folder in app/static/ called 'downloads' and will create files in both formats seperatet by year range from 2000 to 2017 and complete files:
```
sudo bash document-prepare.sh
```
In order to reduce the complete data files (JSON/CSV), we run this script which compresses the files.
```
sudo bash zip-json-csv.sh
```
