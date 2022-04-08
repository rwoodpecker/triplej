import requests
import json
import csv
import os


def parse_response(r):
    data = r.json()
    for item in data["items"]:
        play = {}
        artists = []
        artist_count = 0
        for artist in item["recording"]["artists"]:
            play["artist_" + str(artist_count)] = artist["name"]
            artist_count = artist_count + 1
            artists.append(artist["name"])
        # play['played_time'] = item['played_time']
        # play['title'] = item['recording']['title']
        output_string = [
            item["service_id"],
            item["played_time"],
            item["recording"]["duration"],
            item["recording"]["title"],
            play.get("artist_0", ""),
            play.get("artist_1", ""),
            play.get("artist_2", ""),
            play.get("artist_3", ""),
            artist_count,
        ]
        # print output_string
        year = item["played_time"][:4]
        output_file_name = year + "_abc_radio_plays" + ".csv"
        if not os.path.exists(output_file_name):
            with open(output_file_name, "w") as f:
                f.write(
                    "service_id,timestamp,duration,song,artist1,artist2,artist3,artist4,artistcount\n"
                )
        output_file = open(output_file_name, "a", newline="", encoding="utf-8")
        with output_file:
            writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
            writer.writerow(output_string)


# basic parameters
base_url = "http://music.abcradio.net.au/api/v1/plays/search.json"
q_limit = "100"
q_page = "0"
#q_station = "triplej"
q_from = "2014-12-31T00:00:00.000Z"
q_to = "2015-01-01T23:59:59.000Z"

# find how many total items we're getting
query = base_url + "?from=%s&limit=%s&offset=%s&page=0&to=%s" % (
    q_from,
    q_limit,
    0,
    q_to,
)
r = requests.get(query)
total = r.json()["total"]
print(f"{total} items to get between {q_from} and {q_to}. ")

# retrieve that many items
x = 0
while x < total:
    q_offset = x
    q_limit = 100  # max 100 items per page
    print(f"Completed: {q_offset}.")
    query = base_url + "?from=%s&limit=%s&offset=%s&page=0&&to=%s" % (
        q_from,
        q_limit,
        q_offset,
        q_to,
    )
    r = requests.get(query)
    parse_response(r)
    x = x + q_limit
