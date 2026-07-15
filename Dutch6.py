# nl julie
#1.5 The fool and w/u
import random
running = True

def my_random_choice(a_list):
    random_index = random.randint(0, len(a_list) - 1)
    return a_list[random_index]

def puntjes() :
    for i in range(6):
      print("")

def custom_shuffle(a_list):
    # Implements a shuffle without random.shuffle()
    n = len(a_list)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)  # Pick a random index from 0 to i
        a_list[i], a_list[j] = a_list[j], a_list[i]  # Swap elements

Innocents = []
words = [
"hond", "kat", "paard", "koe", "schaap", "geit", "kip", "haan", 
"eend", "varken", "leeuw", "tijger", "olifant", "giraf", "zebra", "aap", 
"beer", "wolf", "vos", "hert", "kangoeroe", "pinguin", "dolfijn", "haai", 
"walvis", "octopus", "schildpad", "krokodil", "slang", "adelaar", "uil", "duif", 
"mus", "vlinder", "bij", "mier", "spin", "mug", "eekhoorn", "konijn", 
"hamster", "cavia", "papegaai", "kanarie", "zwaan", "zeehond", "oma", "opa", 
"oom", "tante", "broertje", "zusje", "zus", "broer", "bakker", "slager", 
"tandarts", "dokter", "verpleegkundige", "brandweerman", "politieagent", "leraar", "kapper", "kok", 
"ober", "piloot", "chauffeur", "boer", "architect", "programmeur", "journalist", "fotograaf", 
"schilder", "acteur", "zanger", "muzikant", "rechter", "advocaat", "monteur", "elektricien", 
"loodgieter", "kapitein", "postbode", "dierenarts", "astronaut", "bibliothecaris", "taxichauffeur", "uitvinder", 
"directeur", "manager", "wetenschapper", "detective", "tuinman", "kasteel", "paleis", "gevangenis", 
"ziekenhuis", "bibliotheek", "museum", "stadion", "theater", "pretpark", "dierentuin", "strand", 
"woestijn", "oerwoud", "eiland", "vulkaan", "waterval", "berg", "grot", "haven", 
"markt", "restaurant", "hotel", "camping", "zwembad", "supermarkt", "kerk", "moskee", 
"tempel", "school", "universiteit", "brug", "tunnel", "toren", "vuurtoren", "boerderij", 
"kantoor", "fabriek", "treinstation", "luchthaven", "parlement", "bruiloft", "begrafenis", "verjaardag", 
"kerstmis", "pasen", "carnaval", "festival", "wedstrijd", "tentamen", "sollicitatie", "vakantie", 
"verhuizing", "ongeluk", "aardbeving", "storm", "overstroming", "reunie", "afscheid", "opening", 
"premiere", "concert", "toneelstuk", "filmavond", "kampvuur", "picknick", "parade", "demonstratie", 
"vergadering", "schoolreis", "eindexamen", "paraplu", "koffer", "paspoort", "telefoon", "camera", 
"bril", "sleutel", "portemonnee", "rugzak", "helm", "fiets", "motor", "trein", 
"vliegtuig", "boot", "auto", "step", "skateboard", "rolschaatsen", "tractor", "kaars", 
"spiegel", "wekker", "kussen", "deken", "koelkast", "magnetron", "oven", "pan", 
"mes", "vork", "lepel", "bord", "glas", "fles", "tas", "jas", 
"sjaal", "handschoen", "pet", "pizza", "pannenkoek", "hamburger", "soep", "salade", 
"ijsje", "chocolade", "koekje", "taart", "appeltaart", "spaghetti", "rijst", "boterham", 
"kaas", "worst", "appel", "banaan", "aardbei", "watermeloen", "citroen", "druif", 
"ananas", "mango", "broccoli", "wortel", "patat", "lasagne", "omelet", "pudding", 
"popcorn", "sprookje", "superheld", "piraat", "ridder", "heks", "tovenaar", "spion", 
"robot", "monster", "draak", "prins", "koningin", "keizer", "cowboy", "ninja", 
"samurai", "viking", "clown", "goochelaar", "alien", "zombie", "spook", "tijdreiziger", 
"bodyguard", "kampioen", "scheidsrechter", "verkenner", "laptop", "tablet", "koptelefoon", "gameconsole", 
"afstandsbediening", "microfoon", "printer", "drone", "robotstofzuiger", "smartwatch", "fitnessband", "wifi", 
"podcast", "videogame", "controller", "toetsenbord", "muis", "monitor", "speaker", 
"maan", "zon", "planeet", "ster", "regenboog", "bliksem", "sneeuw", "mist", 
"ijsberg", "gletsjer", "kompas", "schatkist", "diamant", "goud", "zilver", "standbeeld", 
"fontein", "schilderij", "stripboek", "dagboek", "tent", "slaapzak", "zaklamp", "verrekijker", 
"hangmat", "kooi", "aquarium", "terrarium", "koets", "tandpasta", "haarborstel", "tandenstoker", 
"kiespijn", "zonlicht", "maanlicht", "sneeuwbal", "sneeuwvlok", "regendruppel", "regenval", "sneeuwval", 
"bosbrand", "zandstorm", "onweersbui", "brandweerauto", "politieauto", "raceauto", "ruimteschip", "spoorweg", 
"snelweg", "zeehaven", "onderzeeboot", "wolkenkrabber", "open haard", "speelplaats", "klaslokaal", "badkamer", 
"slaapkamer", "laboratorium", "boekenplank", "deurbel", "handtas", "regenjas", "schoenveter", "bedframe", 
"touchscreen", "wachtwoord", "gebruikersnaam", "software", "hardware", "lunchtrommel", "creditcard", "milkshake", 
"gehaktbal", "bosbes", "braam", "voetballer", "doelman", "brievenbus", "rockband", "popster", 
"verkeerslicht", "verkeersbord", "parkeerplaats", "fietspad", "skatepark", "zonnebloem", "libel", "lieveheersbeestje", 
"zeepaardje", "zeester", "kwal", "goudvis", "oorbel", "halsketting", "armband", "schoenendoos", 
"handdruk", "muismat", "bureaublad", "smartphone", "videospel", "bordspel", "zonnebrand", "sneeuwstorm", 
"rivieroever", "oever", "zeekust", "kustlijn", "strandbal", "zandkasteel", "zonsondergang", "zonsopgang", 
"avondschemering", "daglicht", "bedzijde", "boekhandelaar", "huisgenoot", "klasgenoot", "schoolplein", "schooltas", 
"werkplek", "notitieblok", "bladwijzer", "deurdrempel", "deurmat", "deurklink", "deurkozijn", "handafdruk", 
"voetafdruk", "kapsel", "haarband", "föhn", "kop", "sleutelgat", "achtertuin", "stoep", 
"oversteekplaats", "oprit", "fauteuil", "laken", "bedtijd", "brandhout", "vuurbal", "brandalarm", 
"snowboard", "sneeuwscooter", "sneeuwschoen", "regenbui", "regenwoud", "levenslang", "fulltime", "zonnehoed", 
"zonnebrandcrème", "moonwalk", "maansteen", "sterrenlicht", "regenworm", "opkomst van de aarde", "schuurpapier", "zandbak", 
"boekensteun", "boekhandel", "boekenwurm", "giraffe", "pinguïn", "arend", "gordeldier", "das", 
"vleermuis", "bizon", "kameel", "kariboe", "kraai", "fret", "flamingo", "gekko", 
"gorilla", "reiger", "hyena", "ibis", "leguaan", "jakhals", "jaguaar", "optocht", 
"schoolreisje", "duik", "dans", "wandeltocht", "marathon", "feest", "protest", "race", 
"workshop", "yoga", "zumba", "beurs", "toernooi", "ceremonie", "rechtszaak", "uitdaging", 
"logeerpartij", "kamperen", "rondleiding", "trektocht", "surfen", "zeilen", "motorfiets", "scooter", 
"spelcomputer", "fitness tracker", "luidspreker", "stoel", "kam", "computer", "ventilator", "lamp", 
"microscoop", "notitieboek", "potlood", "radio", "liniaal", "schaar", "schep", "bank", 
"televisie", "tandenborstel", "horloge", "rolstoel", "prullenbak", "pendel", "penseel", "palet", 
"telescoop", "viool", "kaart", "sleutelhanger", "kristal", "lantaarn", "satelliet", "trofee", 
"fluitje", "ijs", "broodje", "friet", "avocado", "bagel", "spek", "brood", 
"brownie", "kool", "snoep", "ontbijtgranen", "cheesecake", "chilipeper", "maïs", "croissant", 
"cupcake", "dumpling", "eieren", "falafel", "guacamole", "honing", "linzen", "aardappelpuree", 
"noedels", "havermout", "pasta", "pindakaas", "krakeling", "quiche", "sushi", "taco", 
"tofu", "wafel", "yoghurt", "buitenaards wezen", "geest", "lijfwacht", "ontdekkingsreiziger", "elf", 
"fee", "kabouter", "griffioen", "zeemeermin", "ork", "prinses", "magiër", "trol", 
"vampier", "weerwolf", "feniks", "reus", "demoon", "eenhoorn", "harp", "raket", 
"zeilboot", "windmolen", "jacht", "amfitheater"]

undercover_mapping = {
"hond": "wolf", "kat": "leeuw", "paard": "zebra", "koe": "bizon", 
"schaap": "geit", "geit": "schaap", "kip": "haan", "haan": "kip", 
"eend": "zwaan", "varken": "koe", "leeuw": "tijger", "tijger": "leeuw", 
"olifant": "giraf", "giraf": "olifant", "zebra": "paard", "aap": "gorilla", 
"beer": "wolf", "wolf": "vos", "vos": "wolf", "hert": "kariboe", 
"kangoeroe": "koala", "pinguin": "zeehond", "dolfijn": "walvis", "haai": "krokodil", 
"walvis": "dolfijn", "octopus": "kwal", "schildpad": "krokodil", "krokodil": "schildpad", 
"slang": "leguaan", "adelaar": "arend", "uil": "kraai", "duif": "mus", 
"mus": "duif", "vlinder": "libel", "bij": "mier", "mier": "bij", 
"spin": "kwal", "mug": "bij", "eekhoorn": "hamster", "konijn": "cavia", 
"hamster": "cavia", "cavia": "hamster", "papegaai": "kanarie", "kanarie": "papegaai", 
"zwaan": "eend", "zeehond": "walvis", "oma": "opa", "opa": "oma", 
"oom": "tante", "tante": "oom", "broertje": "zusje", "zusje": "broertje", 
"broer": "zus", "zus": "broer", "bakker": "kok", "slager": "bakker", 
"tandarts": "dokter", "dokter": "verpleegkundige", "verpleegkundige": "dokter", "brandweerman": "politieagent", 
"politieagent": "brandweerman", "leraar": "bibliothecaris", "kapper": "schilder", "kok": "bakker", 
"ober": "kok", "piloot": "astronaut", "chauffeur": "taxichauffeur", "boer": "tuinman", 
"architect": "programmeur", "programmeur": "wetenschapper", "journalist": "fotograaf", "fotograaf": "journalist", 
"schilder": "fotograaf", "acteur": "zanger", "zanger": "muzikant", "muzikant": "zanger", 
"rechter": "advocaat", "advocaat": "rechter", "monteur": "loodgieter", "elektricien": "loodgieter", 
"loodgieter": "elektricien", "kapitein": "piloot", "postbode": "taxichauffeur", "dierenarts": "dokter", 
"astronaut": "piloot", "bibliothecaris": "leraar", "taxichauffeur": "chauffeur", "uitvinder": "wetenschapper", 
"directeur": "manager", "manager": "directeur", "wetenschapper": "programmeur", "detective": "politieagent", 
"tuinman": "boer", "kasteel": "paleis", "paleis": "kasteel", "gevangenis": "ziekenhuis", 
"ziekenhuis": "laboratorium", "bibliotheek": "museum", "museum": "bibliotheek", "stadion": "theater", 
"theater": "concert", "pretpark": "dierentuin", "dierentuin": "aquarium", "strand": "eiland", 
"woestijn": "oerwoud", "oerwoud": "jungle", "eiland": "strand", "vulkaan": "berg", 
"waterval": "rivieroever", "berg": "grot", "grot": "tunnel", "haven": "zeehaven", 
"markt": "supermarkt", "restaurant": "hotel", "hotel": "camping", "camping": "tent", 
"zwembad": "strand", "supermarkt": "markt", "kerk": "moskee", "moskee": "tempel", 
"tempel": "kerk", "school": "universiteit", "universiteit": "school", "brug": "tunnel", 
"tunnel": "brug", "toren": "vuurtoren", "vuurtoren": "toren", "boerderij": "fabriek", 
"kantoor": "fabriek", "fabriek": "kantoor", "treinstation": "luchthaven", "luchthaven": "treinstation", 
"parlement": "rechtszaak", "bruiloft": "verjaardag", "begrafenis": "afscheid", "verjaardag": "feest", 
"kerstmis": "pasen", "pasen": "kerstmis", "carnaval": "festival", "festival": "carnaval", 
"wedstrijd": "toernooi", "tentamen": "eindexamen", "sollicitatie": "vergadering", "vakantie": "kamperen", 
"verhuizing": "opening", "ongeluk": "storm", "aardbeving": "overstroming", "storm": "onweersbui", 
"overstroming": "aardbeving", "reunie": "vergadering", "afscheid": "begrafenis", "opening": "premiere", 
"premiere": "opening", "concert": "toneelstuk", "toneelstuk": "concert", "filmavond": "bordspel", 
"kampvuur": "picknick", "picknick": "kampvuur", "parade": "demonstratie", "demonstratie": "parade", 
"vergadering": "reunie", "schoolreis": "rondleiding", "eindexamen": "tentamen", "paraplu": "regenjas", 
"koffer": "rugzak", "paspoort": "creditcard", "telefoon": "smartphone", "camera": "drone", 
"bril": "verrekijker", "sleutel": "sleutelgat", "portemonnee": "handtas", "rugzak": "koffer", 
"helm": "pet", "fiets": "step", "motor": "auto", "trein": "vliegtuig", 
"vliegtuig": "piloot", "boot": "zeilboot", "auto": "raceauto", "step": "fiets", 
"skateboard": "rolschaatsen", "rolschaatsen": "skateboard", "tractor": "boerderij", "kaars": "zaklamp", 
"spiegel": "schilderij", "wekker": "horloge", "kussen": "deken", "deken": "kussen", 
"koelkast": "magnetron", "magnetron": "oven", "oven": "pan", "pan": "mes", 
"mes": "vork", "vork": "lepel", "lepel": "bord", "bord": "glas", 
"glas": "fles", "fles": "glas", "tas": "rugzak", "jas": "regenjas", 
"sjaal": "handschoen", "handschoen": "sjaal", "pet": "helm", "pizza": "lasagne", 
"pannenkoek": "wafel", "hamburger": "gehaktbal", "soep": "salade", "salade": "broccoli", 
"ijsje": "milkshake", "chocolade": "koekje", "koekje": "brownie", "taart": "appeltaart", 
"appeltaart": "taart", "spaghetti": "lasagne", "rijst": "noedels", "boterham": "brood", 
"kaas": "yoghurt", "worst": "gehaktbal", "appel": "banaan", "banaan": "appel", 
"aardbei": "bosbes", "watermeloen": "mango", "citroen": "ananas", "druif": "bosbes", 
"ananas": "mango", "mango": "ananas", "broccoli": "wortel", "wortel": "broccoli", 
"patat": "friet", "lasagne": "spaghetti", "omelet": "eieren", "pudding": "yoghurt", 
"popcorn": "chips", "milkshake": "ijsje", "gehaktbal": "hamburger", "bosbes": "braam", 
"braam": "bosbes", "avocado": "guacamole", "bagel": "croissant", "spek": "worst", 
"brood": "boterham", "brownie": "koekje", "kool": "broccoli", "snoep": "chocolade", 
"ontbijtgranen": "havermout", "cheesecake": "taart", "chilipeper": "soep", "maïs": "broccoli", 
"croissant": "bagel", "cupcake": "taart", "dumpling": "noedels", "eieren": "omelet", 
"falafel": "tofu", "guacamole": "avocado", "honing": "pindakaas", "linzen": "rijst", 
"aardappelpuree": "patat", "noedels": "spaghetti", "havermout": "ontbijtgranen", "pasta": "spaghetti", 
"pindakaas": "honing", "krakeling": "broodje", "quiche": "omelet", "sushi": "vis", 
"taco": "hamburger", "tofu": "kaas", "wafel": "pannenkoek", "yoghurt": "kaas", 
"sprookje": "stripboek", "superheld": "spion", "piraat": "viking", "ridder": "samurai", 
"heks": "tovenaar", "tovenaar": "heks", "spion": "detective", "robot": "alien", 
"monster": "draak", "draak": "monster", "prins": "koningin", "koningin": "prinses", 
"keizer": "koning", "cowboy": "viking", "ninja": "samurai", "samurai": "ninja", 
"viking": "piraat", "clown": "goochelaar", "goochelaar": "clown", "alien": "ruimteschip", 
"zombie": "vampier", "spook": "zombie", "tijdreiziger": "astronaut", "bodyguard": "detective", 
"kampioen": "scheidsrechter", "scheidsrechter": "kampioen", "verkenner": "ontdekkingsreiziger", "elf": "fee", 
"fee": "elf", "kabouter": "trol", "zeemeermin": "zeehond", "ork": "trol", 
"prinses": "koningin", "trol": "ork", "vampier": "weerwolf", "weerwolf": "vampier", 
"feniks": "draak", "reus": "olifant", "demoon": "monster", "eenhoorn": "paard", 
"laptop": "tablet", "tablet": "laptop", "koptelefoon": "speaker", "gameconsole": "controller", 
"afstandsbediening": "televisie", "microfoon": "speaker", "printer": "computer", "drone": "camera", 
"robotstofzuiger": "robot", "smartwatch": "horloge", "fitnessband": "smartwatch", "videogame": "bordspel", 
"controller": "gameconsole", "toetsenbord": "muis", "muis": "toetsenbord", "monitor": "televisie", 
"speaker": "microfoon", "smartphone": "telefoon", "videospel": "bordspel", "maan": "zon", 
"zon": "maan", "planeet": "ster", "ster": "planeet", "regenboog": "bliksem", 
"bliksem": "onweersbui", "sneeuw": "ijs", "mist": "regen", "ijsberg": "gletsjer", 
"gletsjer": "ijsberg", "kompas": "kaart", "schatkist": "goud", "diamant": "goud", 
"goud": "zilver", "zilver": "goud", "standbeeld": "fontein", "fontein": "standbeeld", 
"schilderij": "standbeeld", "stripboek": "dagboek", "dagboek": "notitieboek", "tent": "slaapzak", 
"slaapzak": "tent", "zaklamp": "kaars", "verrekijker": "bril", "hangmat": "slaapzak", 
"kooi": "aquarium", "aquarium": "terrarium", "terrarium": "aquarium", "koets": "boot", 
"tandpasta": "tandenborstel", "haarborstel": "kam", "tandenstoker": "vork", "kiespijn": "tandarts", 
"zonlicht": "zon", "maanlicht": "maan", "sneeuwbal": "sneeuw", "sneeuwvlok": "sneeuw", 
"regendruppel": "sneeuwvlok", "regenval": "overstroming", "sneeuwval": "sneeuw", "bosbrand": "vulkaan", 
"zandstorm": "storm", "onweersbui": "bliksem", "brandweerauto": "brandweerman", "politieauto": "politieagent", 
"raceauto": "auto", "ruimteschip": "raket", "spoorweg": "trein", "snelweg": "weg", 
"zeehaven": "haven", "onderzeeboot": "boot", "wolkenkrabber": "toren", "open haard": "kampvuur", 
"speelplaats": "schoolplein", "klaslokaal": "school", "badkamer": "slaapkamer", "slaapkamer": "bed", 
"laboratorium": "wetenschapper", "boekenplank": "bibliotheek", "deurbel": "wekker", "handtas": "tas", 
"regenjas": "jas", "schoenveter": "schoenendoos", "bedframe": "bed", "touchscreen": "tablet", 
"wachtwoord": "sleutel", "gebruikersnaam": "wachtwoord", "software": "hardware", "hardware": "computer", 
"lunchtrommel": "tas", "creditcard": "portemonnee", "voetballer": "kampioen", "doelman": "voetballer", 
"brievenbus": "postbode", "rockband": "muzikant", "popster": "zanger", "verkeerslicht": "verkeersbord", 
"verkeersbord": "verkeerslicht", "parkeerplaats": "garage", "fietspad": "fiets", "skatepark": "skateboard", 
"zonnebloem": "vlinder", "libel": "vlinder", "lieveheersbeestje": "bij", "zeepaardje": "goudvis", 
"zeester": "zeehond", "kwal": "octopus", "goudvis": "vis", "oorbel": "halsketting", 
"halsketting": "armband", "armband": "halsketting", "schoenendoos": "doos", "handdruk": "afscheid", 
"muismat": "muis", "bureaublad": "computer", "bordspel": "videogame", "zonnebrand": "zonnebrandcrème", 
"sneeuwstorm": "storm", "rivieroever": "rivier", "oever": "strand", "zeekust": "strand", 
"kustlijn": "strand", "strandbal": "strand", "zandkasteel": "kasteel", "zonsondergang": "zonsopgang", 
"zonsopgang": "zonsondergang", "avondschemering": "nacht", "daglicht": "zonlicht", "bedzijde": "bed", 
"boekhandelaar": "bibliothecaris", "huisgenoot": "familie", "klasgenoot": "leerling", "schoolplein": "speelplaats", 
"schooltas": "rugzak", "werkplek": "kantoor", "notitieblok": "dagboek", "bladwijzer": "boek", 
"deurdrempel": "deur", "deurmat": "tapijt", "deurklink": "deur", "deurkozijn": "deur", 
"handafdruk": "voetafdruk", "voetafdruk": "handafdruk", "kapsel": "haarband", "haarband": "haarborstel", 
"föhn": "haarborstel", "kop": "hoofd", "sleutelgat": "sleutel", "achtertuin": "tuinman", 
"stoep": "straat", "oversteekplaats": "verkeerslicht", "oprit": "parkeerplaats", "fauteuil": "stoel", 
"laken": "deken", "bedtijd": "slaapzak", "brandhout": "kampvuur", "vuurbal": "vulkaan", 
"brandalarm": "brandweerman", "snowboard": "skateboard", "sneeuwscooter": "scooter", "sneeuwschoen": "schoen", 
"regenbui": "storm", "regenwoud": "oerwoud", "levenslang": "tijdreiziger", "fulltime": "werkplek", 
"zonnehoed": "pet", "zonnebrandcrème": "zonnebrand", "moonwalk": "dans", "maansteen": "kristal", 
"sterrenlicht": "ster", "regenworm": "worm", "opkomst van de aarde": "zonsopgang", "schuurpapier": "papier", 
"zandbak": "speelplaats", "boekensteun": "boekenplank", "boekhandel": "bibliotheek", "boekenwurm": "bibliothecaris", 
"giraffe": "giraf", "pinguïn": "pinguin", "arend": "adelaar", "gordeldier": "schildpad", 
"das": "vos", "vleermuis": "uil", "bizon": "koe", "kameel": "dromedaris", 
"kariboe": "hert", "kraai": "duif", "fret": "hamster", "flamingo": "zwaan", 
"gekko": "slang", "gorilla": "aap", "reiger": "zwaan", "hyena": "wolf", 
"ibis": "vogel", "leguaan": "slang", "jakhals": "wolf", "jaguaar": "tijger", 
"optocht": "parade", "schoolreisje": "schoolreis", "duik": "zwemmen", "dans": "zumba", 
"wandeltocht": "trektocht", "marathon": "race", "feest": "verjaardag", "protest": "demonstratie", 
"race": "wedstrijd", "workshop": "vergadering", "yoga": "zumba", "zumba": "dans", 
"beurs": "markt", "toernooi": "wedstrijd", "ceremonie": "bruiloft", "rechtszaak": "rechter", 
"uitdaging": "wedstrijd", "logeerpartij": "kamperen", "kamperen": "camping", "rondleiding": "museum", 
"trektocht": "wandeltocht", "surfen": "zwemmen", "zeilen": "boot", "motorfiets": "motor", 
"scooter": "step", "spelcomputer": "gameconsole", "fitness tracker": "fitnessband", "luidspreker": "speaker", 
"stoel": "fauteuil", "kam": "haarborstel", "computer": "laptop", "ventilator": "airco", 
"lamp": "kaars", "microscoop": "telescoop", "notitieboek": "notitieblok", "potlood": "pen", 
"radio": "podcast", "liniaal": "meetlat", "schaar": "mes", "schep": "schop", 
"bank": "stoel", "televisie": "monitor", "tandenborstel": "tandpasta", "horloge": "wekker", 
"rolstoel": "stoel", "prullenbak": "afvalbak", "pendel": "klok", "penseel": "schilder", 
"palet": "penseel", "telescoop": "microscoop", "viool": "muzikant", "kaart": "kompas", 
"sleutelhanger": "sleutel", "kristal": "diamant", "lantaarn": "zaklamp", "satelliet": "raket", 
"trofee": "kampioen", "fluitje": "scheidsrechter", "ijs": "sneeuw", "broodje": "boterham", 
"friet": "patat", "buitenaards wezen": "alien", "geest": "spook", "lijfwacht": "bodyguard", 
"ontdekkingsreiziger": "verkenner", "griffioen": "draak", "magiër": "tovenaar", "harp": "viool", 
"raket": "ruimteschip", "zeilboot": "boot", "windmolen": "molen", "jacht": "boot", 
"amfitheater": "theater", "wifi": "computer", "podcast": "radio"}

custom_shuffle(words)

while running :
  puntjes()
  while True:
      print('How many players?')
      user_input_players = input()
      try:
          num_players = int(user_input_players)
          if num_players > 2:
              Amountofplayers = num_players
              break
          else:
              print("Minimum 3 players.")
      except ValueError:
          print("Invalid input.")

  while True:
      print('How many imposters?')
      user_input_imposters = input()
      try:
          num_imposters = int(user_input_imposters)
          if num_imposters > -1 and num_imposters <= num_players :
              Visual_Amountofimposters = num_imposters
              Amountofimposters = num_imposters
              break
          else:
              print("Atleast 0 imposters.")
      except ValueError:
          print("Invalid input.")
  while True :
      print('How many undercovers?')
      user_input_undercovers = input()
      try:
          num_undercovers = int(user_input_undercovers)
          if num_undercovers >= 0 and num_undercovers <= num_players - Amountofimposters :
              Visual_Amountofundercovers = num_undercovers
              Amountofundercovers = num_undercovers
              break
          else:
            print('Excess undercovers.')
      except ValueError:
        print("Invalid input.")
  while True :
      print('How many fools?')
      user_input_fools = input()
      try:
          num_fools = int(user_input_fools)
          if num_fools >= 0 and num_fools <= num_players - Amountofimposters - Amountofundercovers :
              Amountoffools = num_fools
              break
          else:
            print('Excess fools.')
      except ValueError:
        print("Invalid input.")

  while True :
    print('How many Wht/Undrcvr?')
    user_input_random = input()
    try:
        num_random = int(user_input_random)
        if num_random >= 0 and num_random <= num_players - Amountofimposters - Amountofundercovers - Amountoffools :
            for i in range(num_random):
              if random.randint(1,2) == 1:
                Amountofimposters = Amountofimposters + 1
              else:
                Amountofundercovers = Amountofundercovers + 1
            Amountofrandoms = num_random
            break
        else:
          print('Excess Wht/Undrcvr.')
    except ValueError:
      print("Invalid input.")

  running_2 = True
  while running_2 :

    Innocents = []
    Innocent_counter = 1
    Imposters = []
    undercovers = []
    fools = []
    for i in range(Amountofplayers) :
      Innocents.append(Innocent_counter)
      Innocent_counter = Innocent_counter + 1

    puntjes()
    print(str(Amountofplayers) + ' players.')
    print(str(Visual_Amountofimposters) + ' imposters.')
    print(str(Visual_Amountofundercovers) + ' undercovers.')
    print(str(Amountoffools) + ' fools.')
    print(str(Amountofrandoms) + ' Wht/Undrcvrs.')
    print("- to end game.")
    Off = input("EXE to Start.")

    if Off == '-' :
        running_2 = False
        puntjes()
        print("Game ended.")
        print("New game?    - 1")
        print("Stop game?   - 2")

        while True:
            user_choice_final = input()

            if user_choice_final == '1':
                print("Starting new game...")
                break

            elif user_choice_final == '2':
                print("Goodbye!")
                running = False
                break

            else:
                print("Invalid input.")
        break

    puntjes()

    for i in range(Amountofimposters) :
      random_index = random.randint(0, len(Innocents)-1)
      imposter_player = Innocents.pop(random_index)
      Imposters.append(imposter_player)

    for i in range(Amountofundercovers) :
      random_index = random.randint(0, len(Innocents)-1)
      undercover_player = Innocents.pop(random_index)
      undercovers.append(undercover_player)

    for i in range(Amountoffools) :
      random_index = random.randint(0, len(Innocents)-1)
      fool_player = Innocents.pop(random_index)
      fools.append(fool_player)

    Word = my_random_choice(words)
    Undercover_word = undercover_mapping.get(Word, Word)
    Currentplayer = 1
    puntjes()
    running_3 = True
    round_ended_early = False

    while running_3 and Currentplayer <= Amountofplayers:

      print("- to end game.")
      print('Number ' + str(Currentplayer) + ".")
      if Currentplayer in Innocents :
        print("Word: " + str(Word) + ".")
      elif Currentplayer in Imposters :
        print("You are the imposter.")
      elif Currentplayer in undercovers :
        print("Word: " + str(Undercover_word) + ".")
      elif Currentplayer in fools :
        fool_word = Word
        while fool_word == Word:
          fool_word = my_random_choice(words)
        print("Word: " + fool_word + '.')

      Off = input("EXE to continue.")

      if Off == '-' :
        puntjes()
        print("Game ended.")
        print("Again?       - 1")
        print("New game?    - 2")
        print("Stop game?   - 3")

        while True:
            user_choice_final = input()

            if user_choice_final == '1':
                print("Starting new round...")
                round_ended_early = True
                break

            elif user_choice_final == '2':
                print("Starting new game...")
                running_2 = False
                break

            elif user_choice_final == '3':
                print("Goodbye!")
                running = False
                running_2 = False
                break

            else:
                print("Invalid input.")

        break

      if Currentplayer != Amountofplayers :
        puntjes()
        print('Number ' + str(Currentplayer + 1) + ".")
        input("EXE to continue.")
        puntjes()

      Currentplayer = Currentplayer + 1

    if not running_2:
        break

    if round_ended_early:
        continue

    Imposter_guess = 0
    puntjes()

    guess_counter = 0
    guessed_players = []
    print(str(random.randint(1,Amountofplayers))+ " is first." )
    while len(Imposters) + len(undercovers) + len(fools) != 0 :
      start_new_round = False
      start_new_game = False
      stop_game = False

      print("- to end game.")
      print("Who isn't innocent?")
      Imposter_guess_str = input()

      if Imposter_guess_str == '-':
          puntjes()
          print("Game ended.")
          print("Again?       - 1")
          print("New game?    - 2")
          print("Stop game?   - 3")

          while True:
              user_choice_final = input()

              if user_choice_final == '1':
                  print("Starting new round...")
                  start_new_round = True
                  break

              elif user_choice_final == '2':
                  print("Starting new game...")
                  start_new_game = True
                  break

              elif user_choice_final == '3':
                  print("Goodbye!")
                  stop_game = True
                  break

              else:
                  print("Invalid input.")

          break

      try:
        Imposter_guess = int(Imposter_guess_str)
        puntjes()
        if Imposter_guess < 1 or Imposter_guess > Amountofplayers:
          print("Player doesn't exist.")
          continue

        if Imposter_guess in guessed_players:
          print("Already guessed.")
          continue

        guessed_players.append(Imposter_guess)

        if Imposter_guess in Imposters or Imposter_guess in undercovers or Imposter_guess in fools:
          print("You are right!")
          guess_counter += 1
          if Imposter_guess in Imposters:
              Imposters.remove(Imposter_guess)
          if Imposter_guess in undercovers:
              undercovers.remove(Imposter_guess)
          if Imposter_guess in fools:
              fools.remove(Imposter_guess)
        else:
          print("Wrong.")
          guess_counter = guess_counter + 1

      except ValueError:
        print("Invalid input.")

    if stop_game:
      running = False
      break

    if start_new_game:
      running_2 = False
      break

    if start_new_round:
      continue

    puntjes()
    if guess_counter == Amountofimposters + Amountofundercovers + Amountoffools:
      print("Innocents won!")
    else :
      print("Innocents lost!")

    print("Again?       - 1")
    print("New game?    - 2")
    print("Stop game?   - 3")

    while True:
        user_choice_final = input()

        if user_choice_final == '1':
           if guess_counter % 2 == 0:
               custom_shuffle(words)
           print("Starting new round...")
           break

        elif user_choice_final == '2':
           print("Starting new game...")
           break

        elif user_choice_final == '3':
           print("Goodbye!")
           running = False
           break

        else:
          print("Invalid input.")

    if user_choice_final == '1':
        continue
    elif user_choice_final == '2':
        break
    elif user_choice_final == '3':
        break
