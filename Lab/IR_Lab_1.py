#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen


# In[8]:


url = "http://shakespeare.mit.edu/romeo_juliet/romeo_juliet.1.1.html"


# In[9]:


page = urlopen(url)


# In[10]:


page
<http.client.HTTPResponse object at 0x105fef820>


# In[11]:


html_bytes = page.read()


# In[12]:


html = html_bytes.decode("utf-8")


# In[13]:


print(html)


# In[ ]:




