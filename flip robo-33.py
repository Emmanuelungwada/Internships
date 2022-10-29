#!/usr/bin/env python
# coding: utf-8

# QUESTION 1:
#     Write a python program to display all the header tags from wikipedia.org

# In[ ]:





# ANSWER

# In[ ]:





# In[171]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


wiki_url = 'https://en.wikipedia.org/wiki/Main_Page'


# In[172]:


class_id = 'client-js ve-available'


# In[173]:


response = requests.get(wiki_url)


# In[174]:


soup = BeautifulSoup(response.text,'html.parser')


# In[175]:


print(soup)


# In[177]:


wikipedia_table = soup.find('table', attrs={'id'})


# In[ ]:


df=pd.read_html(str(wikipedia_table))


# In[ ]:


print(df)


# In[ ]:





# In[ ]:





# QUESTION 2 AND 3
# 
# Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[ ]:





# In[ ]:





# In[240]:


from pandas import DataFrame, Series
from tqdm import tqdm
import re
from bs4 import BeautifulSoup


# In[241]:


import requests


# In[260]:


r=requests.get("https://www.imdb.com//india/top-rated-indian-movies/?sort=rk,asc&mode=simple&page=1")


# In[ ]:





# In[261]:


r.text[:]


# In[ ]:





# In[262]:


from bs4 import BeautifulSoup


# In[245]:


soup=BeautifulSoup(r.text,"html.parser")


# In[263]:


results=soup.find_all("td")


# In[259]:


results[0].text.strip().split(".")[-1].strip().split("\n")[1]


# In[264]:


results[1].text.strip().split(".")[-1].strip().split("\n")[-1][1:-1]#year


# In[265]:


results[2].text.strip()#Ranting


# In[266]:


results[1]


# In[195]:


results[1].text.strip().split("\n")


# In[ ]:





# In[267]:


import pandas as pd


# In[ ]:





# In[268]:


l=[]
for i in range(1, len(results),6):
    if i == len(results)-1:
        break
        
    else:
        name=results[i].text.strip().split(".")[-1].strip().split("\n")[0]
        year=results[i].text.strip().split(".")[-1].strip().split("\n")[-1][1:-1]
        ranting=results[i+1].text.strip()
    
    l.append([name,year,ranting])


# In[269]:


l


# In[ ]:





# In[270]:


df=pd.DataFrame(l,columns=["Name","Year of Release", "Ranting"])


# In[271]:


df


# In[ ]:





# In[ ]:





# QUESTION 4 :
#     
#     Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm
# 

# AANSWER

# In[ ]:





# In[155]:


from pandas import DataFrame, Series
from tqdm import tqdm
import re
from bs4 import BeautifulSoup


# In[156]:


import requests


# In[ ]:





# In[ ]:





# In[ ]:





# In[157]:


r=requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[158]:


r.text[:]


# In[159]:


url= "https://presidentofindia.nic.in/former-presidents.htm"


# In[278]:


table_id ="listing cf"


# In[279]:


print(table_id)


# In[161]:


response = requests.get(url)


# In[281]:


soup = BeautifulSoup(response.text,'html.parser')


# In[163]:


print(soup)


# In[273]:


presidents_table = soup.find('table', attrs={'id': table_id})


# In[ ]:


df=pd.read_html(str(presidents_table))


# In[ ]:


print(df)


# In[ ]:





# QUESTION 5 and 6:
#     Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.

# 

# ANSWER

# In[ ]:





# In[284]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[289]:


page  = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")


# In[290]:


page


# In[291]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:



url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
r = requests.get(url)
r.content
soup = BeautifulSoup(r.content, "html.parser")

specific_div = soup.find_all("div", {"id": "batsmen-tests"})
maindiv = specific_div[10].find_all("div", {"class": "text-center"})
for div in maindiv:
    print(div.text) 


# In[ ]:





# QUESTION 7
# 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# 
# i) Headline
# ii) Time
# iii) News Link

# In[ ]:





# ANSWERS

# In[ ]:


# importing the necessary packages
import requests
from bs4 import BeautifulSoup


# In[ ]:


url= "https://www.cnbc.com/world/?region=world"


# In[ ]:


r1 = requests.get(url)
coverpage = r1.content


# In[ ]:


soup1 = BeautifulSoup(coverpage, 'html5lib')


# In[ ]:


coverpage_news = soup1.find_all('h2', class_='CNBCGlobalNav-container')


# In[ ]:


coverpage_news


# In[ ]:


coverpage_news[4].get_text()


# In[ ]:


# Scraping the first 5 articles
number_of_articles = 5
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):
    
    # only news articles (there are also albums and other things)
    if "inenglish" not in coverpage_news[n].find('a')['href']:  
        continue
    
    # Getting the link of the article
    link = coverpage_news[n].find('a')['href']
    list_links.append(link)
    
    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)
    
    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='articulo-cuerpo')
    x = body[0].find_all('p')
    
    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
        
    news_contents.append(final_article)


# 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL 

# ANSWER
# 
# The link to this question is not correct or not found.

# In[ ]:





# 
# QUESTION 10.
# Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en
# i) Rank
# ii) Publication
# iii) h5-index
#  iv) h5-median

# In[ ]:





# ANSWER

# In[ ]:





# In[303]:


get_ipython().system('pip install requests --upgrade')


# In[304]:


import requests


# In[315]:


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}


# In[316]:


url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=object+detection+in+aerial+image+&btnG=&oq=ob'


# In[317]:


response=requests.get(url,headers=headers)


# In[318]:


response.status_code


# In[319]:


page_contents = response.text


# In[320]:


len(page_contents)


# In[ ]:





# In[321]:


from bs4 import BeautifulSoup


# In[322]:


doc = BeautifulSoup(page_contents,'html.parser')


# In[323]:


type(doc)


# In[324]:


paper_names_tag = doc.select('[data-lid]')


# In[325]:


paper_names = []
for tag in paper_names_tag:
  paper_names.append(tag.select('h3')[0].get_text())


# In[326]:


paper_names


# In[327]:


citations = doc.select('[title=Cite] + a')


# In[ ]:


citations[1].text


# In[ ]:


#for taking only integer from text 
import re
int(re.search(r'\d+', string1).group())


# In[ ]:





# In[ ]:


cite_count = []
for i in citations:
    if i is None :
        cite_count.append(0)
    else:
        cite = i.text
        cite_count.append(int(re.search(r'\d+', cite).group()))


# In[ ]:





# In[ ]:


cite_count


# In[ ]:


links = paper_names_tag[0].find('h3')


# In[ ]:


link_tag = doc.find_all('h3',{"class" : "gs_rt"})


# In[ ]:


link_tag[0]


# In[ ]:


link_tag[0].a['href']


# In[ ]:


links = []

for i in range(len(link_tag)) :
    links.append(link_tag[i].a['href'])


# In[ ]:


import pandas as pd


# In[ ]:


paper_dict = {
    'paper title ' : paper_names,
    'authors' : authors_list,
    'citation' : cite_count,
    'url of paper' : links
}


# In[ ]:


papers_df = pd.DataFrame(paper_dict)


# In[ ]:


papers_df

