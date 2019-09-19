#!/usr/bin/env python
# coding: utf-8

# In[2]:


from astropy.io import fits
import glob
import numpy as np
#np.version.version
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


image = fits.open('saturnrotate.fits')
image0 = image[0].data*1.
plt.imshow(image0)
X= [250, 1000]
plt.colorbar()


# In[49]:


upperFlat = image0[0:500, 0:3250]
plt.imshow(upperFlat)
plt.colorbar(plt.clim(250, 1000))
x = upperFlat.shape[1]
upperMean= [None]*x

for i in range (x):
    upperMean[i] = np.mean(upperFlat[:, i])
print('The mean of the background below the spectrum is', upperMean)


# In[50]:


lowerFlat = image0[2000: 2500, 0:3250]
plt.imshow(lowerFlat)
plt.colorbar(plt.clim(250, 1000))
x = lowerFlat.shape[1]
lowerMean= [None]*x

for i in range (x):
    lowerMean[i] = np.mean(lowerFlat[:, i])
print('The mean of the background below the spectrum is', lowerMean)


# In[51]:


for i in range (x):
    backgroundMean[i] = np.divide((upperMean[i] + lowerMean[i]), 2)
plt.title('location of 1st order LHS')
LHS1st= image0[300:1000, 0:1000]
plt.imshow(LHS1st)
plt.colorbar(plt.clim(0, 35000))
print ('The total background mean is', backgroundMean)


# In[52]:


print(backgroundMean)
plt.plot(backgroundMean)


# In[24]:


# LHSnoB=np.subtract(LHS1st, backgroundMean)
# plt.imshow(LHSnoB)
# plt.title('LHS Spectrum without background spectrum')
# plt.colorbar(plt.clim(0, 35000))


# In[15]:


RHS1st= image0[1000:1500, 2000:3250]
plt.imshow(RHS1st)
plt.colorbar(plt.clim(0, 20000))


# In[23]:


# RHSnoB=np.subtract(RHS1st, backgroundMean)
# plt.imshow(RHSnoB)
# plt.title('RHS Spectrum without background spectrum')
# plt.colorbar(plt.clim(0, 20000))


# In[ ]:




