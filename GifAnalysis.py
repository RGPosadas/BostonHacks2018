
# coding: utf-8

# In[1]:


from PIL import Image


# In[2]:


from PIL import GifImagePlugin


# In[5]:


imageObject = Image.open("Desktop/gifSample.gif")


# In[7]:


#Display individual frames from the loaded animated GIF file
for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    imageObject.show()

