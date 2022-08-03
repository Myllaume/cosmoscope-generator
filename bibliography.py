import json
import requests

zotero_api_url = "https://api.zotero.org/groups/4724580/items?format=csljson"

def gen_id(zotero_item):
    first_author_family = zotero_item['author'][0]['family']
    year = str(zotero_item['issued']['date-parts'][0][0])
    return first_author_family + year

with requests.Session() as s:
    download = s.get(zotero_api_url)
    decoded_content = download.content.decode('utf-8')

    zotero_data = json.loads(decoded_content)
    zotero_items = zotero_data['items']
    for i, zotero_item in enumerate(zotero_items):
        zotero_items[i]['id'] = gen_id(zotero_item)

    json_bib = json.dumps(zotero_items, indent=4, ensure_ascii=False)
    with open('./assets/bib.json', "w") as f:
        f.write(json_bib)