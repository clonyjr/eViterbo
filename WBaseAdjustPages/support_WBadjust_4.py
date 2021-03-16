S = requests.Session()

URL = "http://ieeta-eviterbo.web.ua.pt/api.php"
URL_IEETA = "ieeta-eviterbo.web.ua.pt"
URL_GET_PAGE = "http://ieeta-eviterbo.web.ua.pt/api.php?action=parse&page=Academia_Politécnica_do_Porto&prop=text&formatversion=2"
URL_GET_PAGE_END_STRING = "&prop=text&formatversion=2"
PATH_EXCEL_PROPERTIES = "/Users/clonyjr/Library/Mobile Documents/com~apple~CloudDocs/Aveiro/UA/CLONY/TechnetEmpire/WBaseAdjustPages/Propriedades.xlsx"
# get page content
site = Site(URL_IEETA, scheme='http', path='/')
#site = Site(URL_IEETA, scheme='http', path='/')
site.login("operador","eviterbo01")
page = site.pages['Academia Politécnica do Porto']
#print(page.can('edit'))
text = page.text()

#URL_GET_PAGE + "Academia_Politécnica_do_Porto" + URL_GET_PAGE_END_STRING
#request_page = S.get(URL_GET_PAGE)
#print(text)

excelfile = openpyxl.load_workbook(PATH_EXCEL_PROPERTIES)

ws = excelfile.active
maxRows = ws.max_row
maxCol = ws.max_column
print(excelfile.sheetnames)

colunas_planilha = ['A','B','C','D','E','F','G']
for i in colunas_planilha:
    column_religiao = ws[i]
    for x in range(len(column_religiao)):
        if(column_religiao[x].value is not None):
            column_religiao[x].value
        else: continue

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()
#print(DATA)

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

#print(LOGIN_TOKEN)

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action':"login",
    'lgname':"Operador@evitWikiBase",
    'lgpassword':"kf2eei97qac85brujd5hii0fae0ok3vk",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

#print(DATA)

# Step 3: GET request to fetch CSRF token
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to ge properties of a page
PARAMS_3 = {
    "action": "wbeditentity",
    "id": 'Q48',#"José Sande Vasconcelos Wikibase",#"Academia Politécnica do Porto",
    #"new":'item',
    #"site":'http://ieeta-eviterbo.web.ua.pt/index.php/Academia_Politécnica_do_Porto',
    "data": '{"claims":{"mainsnak":{"snaktype":"value","property":"P29"}}}',
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)

PARAMS_4 = {
    "action": "wbgetclaims",
    "id": 'Q48',
    #"site":'http://ieeta-eviterbo.web.ua.pt/index.php/Academia_Politécnica_do_Porto',
    "data": '{"claims":{"mainsnak":{"snaktype":"value","property":"P29"}}}',
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_4)
DATA = R.json()

print(DATA)