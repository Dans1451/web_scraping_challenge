{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "87762de5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import os\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "73e911f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "INFO:WDM:====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 102.0.5005\n",
      "INFO:WDM:Current google-chrome version is 102.0.5005\n",
      "[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "INFO:WDM:Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "[WDM] - Driver [C:\\Users\\dans1\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n",
      "INFO:WDM:Driver [C:\\Users\\dans1\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "d7d1a1a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "754f6cbf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "From JPL's Mailroom to Mars and Beyond\n",
      "Bill Allen has thrived as the mechanical systems design lead for three Mars rover missions, but he got his start as a teenager sorting letters for the NASA center.\n"
     ]
    }
   ],
   "source": [
    "for x in range(50):\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    results = soup.find('div', class_ = 'list_text')\n",
    "    \n",
    "title1 = results.find('div', class_ = \"content_title\").text\n",
    "par = results.find('div', class_ = 'article_teaser_body').text\n",
    "print(title1)\n",
    "print(par)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "3764dfbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "62c21786",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "INFO:WDM:====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 102.0.5005\n",
      "INFO:WDM:Current google-chrome version is 102.0.5005\n",
      "[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "INFO:WDM:Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "[WDM] - Driver [C:\\Users\\dans1\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n",
      "INFO:WDM:Driver [C:\\Users\\dans1\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "f358ad09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/featured/mars1.jpg\n"
     ]
    }
   ],
   "source": [
    "for x in range(50):\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    results = soup.find('img', class_ = 'headerimage')\n",
    "featured_image_url = results['src'] \n",
    "featured_image_url = (f'{url}/{featured_image_url}')\n",
    "print (featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "b1bac4dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "e3581f7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "url= 'https://galaxyfacts-mars.com'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "469541b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result1 = pd.read_html(url)\n",
    "result1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "261e01fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Category             Mars            Earth\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5          Length of Year:   687 Earth days      365.24 days\n",
       "6             Temperature:     -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=result1[0]\n",
    "df.columns = ['Category','Mars','Earth']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "e5067fa3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://marshemispheres.com/cerberus.html', 'https://marshemispheres.com/schiaparelli.html', 'https://marshemispheres.com/syrtis.html', 'https://marshemispheres.com/valles.html']\n"
     ]
    }
   ],
   "source": [
    "titles=[]\n",
    "img_urls=[]\n",
    "new_urls=[]\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "results = soup.find_all('div', class_ = 'item')\n",
    "browser.quit()\n",
    "#print(results[0].div.a['href'])\n",
    "#print(len(results))\n",
    "for x in range(len(results)):\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    url = 'https://marshemispheres.com/'\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    results = soup.find_all('div', class_ = 'item')\n",
    "    link = results[x].div.a['href']\n",
    "    new_url = (f'{url}{link}')\n",
    "    new_urls.append(new_url)\n",
    "    browser.quit()\n",
    "#     browser.visit(new_url)\n",
    "    \n",
    "print(new_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "3f5786b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://marshemispheres.com/cerberus.htmlimages/full.jpg', 'https://marshemispheres.com/schiaparelli.htmlimages/schiaparelli_enhanced-full.jpg', 'https://marshemispheres.com/syrtis.htmlimages/syrtis_major_enhanced-full.jpg', 'https://marshemispheres.com/valles.htmlimages/valles_marineris_enhanced-full.jpg']\n",
      "['Cerberus Hemisphere', 'Schiaparelli Hemisphere', 'Syrtis Major Hemisphere', 'Valles Marineris Hemisphere']\n"
     ]
    }
   ],
   "source": [
    "results=[]\n",
    "for x in range(len(new_urls)):\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    url = 'https://marshemispheres.com/'\n",
    "    browser.visit(url)\n",
    "    browser.visit(new_urls[x])\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    result = soup.find('div', class_ = 'downloads')\n",
    "    img_url=result.a['href']\n",
    "    i_url=(f'{new_urls[x]}{img_url}')\n",
    "    img_urls.append(i_url)\n",
    "    result = soup.find('h2', class_ = 'title').text\n",
    "    title=result.replace(' Enhanced', '')\n",
    "    titles.append(title)\n",
    "    browser.quit()\n",
    "    \n",
    "print(img_urls)\n",
    "print(titles)    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "df99b718",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/cerberus.htmlimages/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/schiaparelli.htmlimages/schiaparelli_enhanced-full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/syrtis.htmlimages/syrtis_major_enhanced-full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/valles.htmlimages/valles_marineris_enhanced-full.jpg'}]"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls=[]\n",
    "for x in range(len(titles)):\n",
    "    diction={'title':titles[x],'img_url' : img_urls[x]}\n",
    "    hemisphere_image_urls.append(diction)\n",
    "    \n",
    "hemisphere_image_urls"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
