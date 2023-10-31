import requests
from bs4 import BeautifulSoup
from os.path import basename

links = ["https://www.booking.com/searchresults.html?label=gen173nr-1FCAQoggJCC3JlZ2lvbl80MTI3SDFYBGipAogBAZgBMbgBF8gBDNgBAegBAfgBA4gCAagCA7gCo-f_qQbAAgHSAiQ4ZDYzNjQ3YS1mNmUxLTQ3MDUtYTUzOS1lZGQ2MTk0ODcxYjjYAgXgAgE&aid=304142&ss=las+vegas&ssne=Orlando&ssne_untouched=Orlando&lang=en-us&src=searchresults&dest_id=20079110&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=db050363e045010f&ac_meta=GhBkYjA1MDM2M2UwNDUwMTBmIAAoATICZW46CWxhcyB2ZWdhc0AASgBQAA%3D%3D&checkin=2023-11-06&checkout=2023-11-11&ltfd=1%3A5%3A10-2023_11-2023_12-2023%3A1%3A&group_adults=2&no_rooms=1&group_children=0&flex_window=7&nflt=ht_id%3D204",
         "https://www.booking.com/searchresults.html?label=gen173nr-1FCAQoggJCC3JlZ2lvbl80MTI3SDFYBGipAogBAZgBMbgBF8gBDNgBAegBAfgBA4gCAagCA7gCo-f_qQbAAgHSAiQ4ZDYzNjQ3YS1mNmUxLTQ3MDUtYTUzOS1lZGQ2MTk0ODcxYjjYAgXgAgE&aid=304142&ss=Orlando%2C+Florida%2C+United+States&ssne=Goa&ssne_untouched=Goa&efdco=1&lang=en-us&src=searchresults&dest_id=20023488&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b79a80d17ed80281&ac_meta=GhBiNzlhODBkMTdlZDgwMjgxIAAoATICZW46A29ybEAASgBQAA%3D%3D&ltfd=1%3A5%3A10-2023_11-2023_12-2023%3A1%3A&group_adults=2&no_rooms=1&group_children=0&flex_window=7&nflt=ht_id%3D204",
         "https://www.booking.com/searchresults.html?ss=Branson%2C+United+States+of+America&ssne=Las+Vegas&ssne_untouched=Las+Vegas&label=gen173nr-1FCAQoggJCC3JlZ2lvbl80MTI3SDFYBGipAogBAZgBMbgBF8gBDNgBAegBAfgBA4gCAagCA7gCo-f_qQbAAgHSAiQ4ZDYzNjQ3YS1mNmUxLTQ3MDUtYTUzOS1lZGQ2MTk0ODcxYjjYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20071942&dest_type=city&checkin=2023-11-06&checkout=2023-11-11&ltfd=1%3A5%3A10-2023_11-2023_12-2023%3A1%3A&group_adults=2&no_rooms=1&group_children=0&flex_window=7",
         "https://www.booking.com/searchresults.html?ss=Dallas%2C+United+States+of+America&ssne=Branson&ssne_untouched=Branson&label=gen173nr-1FCAQoggJCC3JlZ2lvbl80MTI3SDFYBGipAogBAZgBMbgBF8gBDNgBAegBAfgBA4gCAagCA7gCo-f_qQbAAgHSAiQ4ZDYzNjQ3YS1mNmUxLTQ3MDUtYTUzOS1lZGQ2MTk0ODcxYjjYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20127504&dest_type=city&checkin=2023-11-06&checkout=2023-11-11&ltfd=1%3A5%3A10-2023_11-2023_12-2023%3A1%3A&group_adults=2&no_rooms=1&group_children=0&flex_window=7"
         ]
 
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5042.108 Safari/537.36"}
for curr in links:
    response = requests.get(curr, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
 
    print(response.status_code)
 
    hotel_results = []
 
    for link in soup.select("img[src^=https]"):
        lnk = link["src"]
        print(lnk)
        with open(basename(lnk.split("?")[0]),"wb") as f:
            #print(f)
            f.write(requests.get(lnk).content)
