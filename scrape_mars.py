def scrape():
    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:


    #Dependencies
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import requests
    import os
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd


    # In[2]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = 'https://redplanetscience.com'
    browser.visit(url)


    # In[4]:


    for x in range(50):
        html = browser.html
        soup = bs(html, 'html.parser')
        results = soup.find('div', class_ = 'list_text')
        
    title1 = results.find('div', class_ = "content_title").text
    par = results.find('div', class_ = 'article_teaser_body').text
    print(title1)
    print(par)

        


    # In[5]:


    browser.quit()


    # In[6]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # In[7]:


    for x in range(50):
        html = browser.html
        soup = bs(html, 'html.parser')
        results = soup.find('img', class_ = 'headerimage')
    featured_image_url = results['src'] 
    featured_image_url = (f'{url}/{featured_image_url}')
    print (featured_image_url)


    # In[8]:


    browser.quit()


    # In[9]:


    url= 'https://galaxyfacts-mars.com'


    # In[10]:


    result = pd.read_html(url)
    result


    # In[18]:


    df=result[0]
    df.columns = ['','Mars','Earth']
    df.set_index('', inplace = True)
    df
    result1 = df.to_html()


    # In[13]:


    titles=[]
    img_urls=[]
    new_urls=[]
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('div', class_ = 'item')
    for x in range(len(results)):
        link = results[x].div.a['href']
        new_url = (f'{url}{link}')
        new_urls.append(new_url)

        
    print(new_urls)


    # In[14]:


    results=[]
    for x in range(len(new_urls)):
        browser.visit(new_urls[x])
        html = browser.html
        soup = bs(html, 'html.parser')
        result = soup.find('img', class_ = 'wide-image')
        img_url=result['src']
        i_url=(f'{url}{img_url}')
        img_urls.append(i_url)
        result = soup.find('h2', class_ = 'title').text
        title=result.replace(' Enhanced', '')
        titles.append(title)
        
    print(img_urls)
    print(titles) 
    browser.quit()
        


    # In[15]:


    hemisphere_image_urls=[]
    for x in range(len(titles)):
        diction={'title':titles[x],'img_url' : img_urls[x]}
        hemisphere_image_urls.append(diction)
        
    hemisphere_image_urls


    # In[16]:


    end_results={}
    end_results['news']=[title1, par]
    end_results['image']=[featured_image_url]
    end_results['facts']=[result1]
    end_results['hemispheres']=[hemisphere_image_urls]
    return end_results
