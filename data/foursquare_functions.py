{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0cb1b187-cce9-438f-a0b2-3197613e4243",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "city_name = \"Vancouver, Canada\"\n",
    "\n",
    "# '49.2827,-123.1207'\n",
    "def foursquare_bike_stations(city_name, latitude, longitude, api_key):\n",
    "    url = f\"https://api.foursquare.com/v3/places/search\"\n",
    "\n",
    "    params = {\n",
    "        'll': f\"{latitude},{longitude}\",  # Latitude and longitude of the bike station\n",
    "        'radius': 500,\n",
    "        'categories': \"13033\",   # foursquare category for bubble tea shops\n",
    "        'limit': 5\n",
    "    }\n",
    "\n",
    "    headers = {\"Accept\": \"application/json\"}\n",
    "    headers['Authorization'] = api_key\n",
    "\n",
    "    response = requests.get(url, params=params, headers=headers)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "        data = response.json()\n",
    "        bike_stations = data.get('results', [])\n",
    "\n",
    "        return bike_stations\n",
    "    else:\n",
    "        print(f\"Error: Unable to fetch Foursquare data. Status code: {response.status_code}\")\n",
    "        return []\n",
    "\n",
    "# Function to collect the details of the bubble tea shops for each bike station\n",
    "def bubble_tea_details(station_name, bubble_tea_shops):\n",
    "    details_list = []\n",
    "    for idx, shop in enumerate(bubble_tea_shops, start=1):\n",
    "        name = shop.get('name', 'N/A')\n",
    "        rating = shop.get('rating', 'N/A')\n",
    "        location = shop.get('location', {})\n",
    "        shop_latitude = location.get('lat', 'N/A')\n",
    "        shop_longitude = location.get('lng', 'N/A')\n",
    "\n",
    "        details_list.append({\n",
    "            'Station Name': station_name,\n",
    "            'Bubble Tea Shop Name': name,\n",
    "            'Rating': rating,\n",
    "            'Latitude': shop_latitude,\n",
    "            'Longitude': shop_longitude\n",
    "        })\n",
    "\n",
    "    return details_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a05f7ad6-228b-4a26-80b6-0c657e4d553d",
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
