# ABC played tracks downloader

## Requirements

Requires requests (pip install requests) and Python 3.

## Usage
python get_abc_radio_tracks.py

This script searches the ABC Radio API for plays between two timestamps (q_from & q_to) and writen to a .csv file for each year. Columns: service_id (station name) , timestamp (GMT), song duration, track name, 1st-4th listed artists.

ABC API: https://music.abcradio.net.au/api/v1/plays/search.json. 

## Caveats:

* Song data isn't captured if the ABC studio in use doesn't send data to the playout stream (either because it is old, or the current track is being played off vinyl/CD instead of from the computer, etc). This mainly affects late night (after 9pm).
* I'm not aware of any massive gaps in data but I haven't checked thoroughly.