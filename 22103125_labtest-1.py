#!/usr/bin/env python
# coding: utf-8

# In[94]:


import numpy as np
import matplotlib.pyplot as plt


# In[95]:


city_x = np.array([100,120,85,90,110,95])
city_y = np.array([80,75,60,95,85,90])
city_z = np.array([150,140,135,160,155,170])


# In[102]:


total_rainfall_x = np.sum(city_x)
total_rainfall_y = np.sum(city_y)
total_rainfall_z = np.sum(city_z)


# In[103]:


avg_total_x = np.mean(city_x)
avg_total_y = np.mean(city_y)
avg_total_z = np.mean(city_z)


# In[104]:


def avg_for_each_month(city_x,city_y,city_z):
    all_avg_acc_to_months =[0,0,0,0,0,0]
    avg_six_months = 0
    for i in range(0,6):
        all_avg_acc_to_months[i] = city_x[i] + city_y[i] + city_z[i]
    for i in range(0,6):
        avg_six_months = np.mean(all_avg_acc_to_months)
    return avg_six_months


# In[105]:


print(avg_for_each_month(city_x,city_y,city_z))


# In[106]:


months = np.arange(1,7)
plt.figure(figsize=(10, 6))


# In[107]:


plt.subplot(2, 1, 1)
plt.bar(months - 0.2, city_x, width=0.2, label='City X')
plt.bar(months, city_y, width=0.2, label='City Y')
plt.bar(months + 0.2, city_z, width=0.2, label='City Z')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall for Each City')
plt.legend()


# In[ ]:


plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




