#!/usr/bin/env python
# -*- coding: utf-8 -
import os, json

people = {
    "owners": [
    "Ramiz Qerimi",
    "Naser Abdullahu",
    "Ermal",
    "Kaltrin",
    "Mimoza",
    "Batishahe",
    "Bajrumshah",
    "Adelina Veseli",
    "Besnik Rexha",
    "Adnan Krasniqi",
    "Faton Krasniqi",
    "Hysen Krasniqi",
    "Todia Gvozden",
    "Muhamed Gërxhaliu",
    "Liridona Ejupi",
    "Florije Pavata",
    "Shpresa Saraçi",
    "Nezir Xhoxhaj",
    "Dragan Adancic",
    "Florent Bakija",
    "Adnon Lipovica",
    "Stanoje Lazarevia",
    "Ruždija Kojia",
    "Shaha Zylfiu",
    "Gëzim Xhevukaj",
    "Edmond Zeka",
    "Sabit Bajraktari",
    "Avdi Abazi"
    ]
}


# The Algorithm
total_male = 0
total_female = 0
for category in people:
    for person in people[category]:
        gender = ""
        splited = person.split(" ")
        each_char = list(splited[0])
        last_char = each_char[-1]
        if "a" == last_char:
            gender = "Femer"
            total_female += 1
        else:
            gender = "Mashkull"
            total_male += 1
        print {person: gender}
print {"Femra": total_female, "Mashkuj": total_male}
