{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c68afcd-2477-424b-9dea-2560685d66fb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "city_name = \"Vancouver, Canada\"\n",
    "\n",
    "def yelp_bike_stations(city_name, latitude, longitude, yelp_api_key):\n",
    "    url = f\"https://api.yelp.com/v3/businesses/search\"\n",
    "\n",
    "    params = {\n",
    "        'latitude': latitude,\n",
    "        'longitude': longitude,\n",
    "        'radius': 500,              # 500 meters radius for Yelp API request - reduced to return less results, run faster cod\n",
    "        'categories': \"bubbletea\",\n",
    "        'limit': 5\n",
    "    }\n",
    "\n",
    "    headers = {\"Authorization\": f\"Bearer {yelp_api_key}\"}\n",
    "\n",
    "    response = requests.get(url, params=params, headers=headers)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "        data = response.json()\n",
    "        bike_stations = data.get('businesses', [])\n",
    "\n",
    "        return bike_stations\n",
    "    else:\n",
    "        print(f\"Error: Unable to fetch Yelp data. Status code: {response.status_code}\")\n",
    "        return []\n",
    "\n",
    "# collect details of Yelp businesses for each bike station\n",
    "def collect_yelp_details(station_name, bike_stations):\n",
    "    details_list = []\n",
    "    for idx, station in enumerate(bike_stations, start=1):\n",
    "        station_latitude = station.get('coordinates', {}).get('latitude', 'N/A')\n",
    "        station_longitude = station.get('coordinates', {}).get('longitude', 'N/A')\n",
    "\n",
    "        # Fetch Yelp business details for the current bike station\n",
    "        yelp_businesses = yelp_bike_stations(city_name, station_latitude, station_longitude, yelp_api_key)\n",
    "\n",
    "        if yelp_businesses:\n",
    "            for idx, business in enumerate(yelp_businesses, start=1):\n",
    "                name = business.get('name', 'N/A')\n",
    "                rating = business.get('rating', 'N/A')\n",
    "                business_latitude = business.get('coordinates', {}).get('latitude', 'N/A')\n",
    "                business_longitude = business.get('coordinates', {}).get('longitude', 'N/A')\n",
    "\n",
    "                details_list.append({\n",
    "                    'Station Name': station_name,\n",
    "                    'Station Latitude': station_latitude,\n",
    "                    'Station Longitude': station_longitude,\n",
    "                    'Bubble Tea Shop Name': name,                    # Yelp Business Name\n",
    "                    'Rating': rating,\n",
    "                    'Business Latitude': business_latitude,\n",
    "                    'Business Longitude': business_longitude\n",
    "                })\n",
    "\n",
    "    return details_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0a9471fd-4a80-4211-8eeb-290b8fe1a1f6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
