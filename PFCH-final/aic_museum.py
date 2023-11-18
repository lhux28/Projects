# import requests
# import json
# import time


# url = 'https://api.artic.edu/api/v1/artwork-types'
# params = {
#     'limit': 44,
#     # 'page':'2',
#     # 'date_start':'1900',h
#     # 'department_title':'Architecture and Design'
#     # 'subject_titles'

# }
# headers = {
#     'AIC-user-agent': 'lhux28@pratt.edu'
# }

# req = requests.get(url, params=params, headers=headers)
# data = req.json()

# # print(json.dumps(data, indent=4))

# dict = 0

# while dict < params['limit']:
#     time.sleep(0.25)
#     loop_title = data['data'][dict]['title']
#     loop_id = data['data'][dict]['id']
    
#     print(loop_title, loop_id)

#     dict += 1

#querying for Design items

import time

page_num = 1
while page_num <= 5:
    time.sleep(0.25)
    url = f'https://api.artic.edu/api/v1/artworks/search?q=chair&query[term][artwork_type_id]=31&fields=id,api_link,medium_display,title,artist_display,date_display,date_start,main_reference_number,medium_display,provenance_text,image_id,artwork_type_title&page={page_num}'
    params = {
        'limit': 50,
        # 'current_page': 1,
    }
    headers = {
        'AIC-user-agent': 'lhux28@pratt.edu'
    }

    req_design = requests.get(url, params=params, headers=headers)
    aic_data = req_design.json()
    aic_json = json.dumps(aic_data, indent=4)
    
    print(aic_json)


    if page_num == 1:
        with open('/Users/liwen/Desktop/PFCH/Final/aic_chairs.json', 'w') as file:
            file.write(aic_json)
    else:
        with open('/Users/liwen/Desktop/PFCH/Final/aic_chairs.json', 'a') as file:
            file.write(aic_json)

    page_num += 1



#querying for furn items

page_number = 1
while page_number <= 3:
    url = f'https://api.artic.edu/api/v1/artworks/search?q=chair&query[term][artwork_type_id]=6&fields=id,api_link,medium_display,title,artist_display,date_display,date_start,main_reference_number,medium_display,provenance_text,image_id,artwork_type_title&page={page_number}'
    params = {
        'limit': 50
        # 'current_page': 1,
    }
    headers = {
        'AIC-user-agent': 'lhux28@pratt.edu'
    }

    req_furn = requests.get(url, params=params, headers=headers)
    aic_furn_data = req_furn.json()
    aic_furn_json = json.dumps(aic_furn_data, indent=4)

    print(aic_furn_json)
    
    with open('/Users/liwen/Desktop/PFCH/Final/aic_chairs.json', 'a') as file:
        file.write(aic_furn_json)

    page_number += 1

