#!/usr/bin/env python
# coding: utf-8

# # Python ja tekoäly, koodauksen perusteet
# 
# # Koulutus: 28.11.2019
# 
# # Aihe: Lineaarinen regressio

# # Harjoitusesimerkki lineaarisesta regressiosta

# Tässä harjoituksessa rakennamme kokonaisen analyysiketjun, jossa ladataan data jollain opitulla tavalla.
# Datasta valitaan halutut muuttujat, ja tehdään ennustin. Ennustimen tarkkuus mitataan huolellisesti ristiinvalidoimalla.

# Ensin tarvitaan kuitenkin tavalliset kirjastot, josta saamme tietorakenteita ja funktiota käyttöön:

# In[43]:


import numpy as np
import pandas as pd


from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# # Mieti millaisen ennustusongelman haluat ratkaista ja lataa siihen liittyvä data
# 
# Voit tutustua halutessasi Scikit-learn -kirastossa oleviin datajoukkoihin: https://scikit-learn.org/stable/datasets/index.html#
# Voit korvata seuraavan haluamallasi datalla:

matkat = pd.read_csv("ajetut_matkat.csv")


# Katsotaan datan ominaisuuksia:
matkat
matkat.head()
matkat.info()
matkat.describe()
matkat.columns


# # Poimi x ja y muuttujat:
# Poimitaan Datasta etaisyys ja kulutus omiksi muuttujikseen
x = matkat['etaisyys']
y = matkat['kulutus']


# Joskus datan tyyppiä täytyy muokata, jos se on esim. kokonaislukuina
x_f = x.astype(float)
y_f = y.astype(float)


# Käytetään Matplotlib-kirjastoa kuvien piirtämiseen
import matplotlib.pyplot as plt


# Piirretään opetusdata x-y -koordinaatistoon
plt.scatter(x,y)
plt.suptitle('Opetusdata', fontsize=16)


# Käytetään kirjastoa scikit-learn:
from sklearn.linear_model import LinearRegression


# # Opeta lineaarinen malli datasta

# In[58]:


lm = LinearRegression(fit_intercept=True)


# In[59]:


x


# In[60]:


x_f


# In[61]:


y


# In[62]:


y.values


# In[63]:


y_f


# In[64]:


data_x = pd.DataFrame(x_f)


# In[65]:


data_y = pd.DataFrame(y_f)


# # Jaa data opetusjoukkoon ja validointijoukkoon:

# Opetetaan malli opetusdatasta, jätä toistaiseksi validointidata käyttämättä:

# In[66]:


data_x_opetus, data_x_validointi, data_y_opetus, data_y_validointi = train_test_split(
    data_x, data_y, test_size=0.2, random_state=0)


# In[67]:


# Lineaarinen malli sovitetaan opetusdataan:

lm.fit(data_x_opetus,data_y_opetus)


# In[68]:


lm


# # Laske mallin opetusvirhe ja validointivirhe
# 
# Käytetään mallia ennustamaan kulutusta ajettujen kilometrien perusteella:

# In[69]:


# Lasketaan lineaarisella mallilla ennustukset arvoille 0, 10, 20, ..
predictions = lm.predict(np.arange(0,250,10).reshape(-1,1))


# In[70]:


# Lasketaan ennustusten opetusvirhe (MSE = mean squared error eli keskimääräinen neliövirhe)
ennustukset_opetus = lm.predict(data_x_opetus)
opetus_mse = mean_squared_error(data_y_opetus, ennustukset_opetus)
opetus_mse


# In[71]:


# Lasketaan ennustusten validointivirhe
ennustukset_validointi = lm.predict(data_x_validointi)
validointi_mse = mean_squared_error(data_y_validointi, ennustukset_validointi)
validointi_mse


# In[72]:


plt.plot(np.arange(0,250,10),predictions,'-')
plt.scatter(data_x,data_y)


# Nyt harjoitellaan ristiinvaidointia, jossa data jaetaan opetusjoukkoon ja validointijoukkoon monta kertaa. Kullekin jaolle opetetaan malli opetusdatalla ja mallille lasketaan sekä opetusvirhe että validointivirhe.

# In[73]:


# Opetusvirheet tallennetaan taulukkoon:
opetus_mse = np.zeros(10)
opetus_r2 = np.zeros(10)

# Validointivirheet tallenetaan taulukkoon:
validointi_mse = np.zeros(10)
validointi_r2 = np.zeros(10)

# Toista jako opetus- ja validointidataan 10 kertaa, opeta
# joka kerta uusi malli, jolle lasket opetusvirheen (opetusdatan
# avulla) ja validointivirheen(validointidatan avulla)

for i in np.arange(0,10):
  data_x_opetus, data_x_validointi, data_y_opetus, data_y_validointi = train_test_split(data_x, data_y, test_size=0.2, random_state=689*i)

  # Opetetaan malli tällä nimenomaisella jaolla!
  lm.fit(data_x_opetus,data_y_opetus)

  # Lasketaan ennustusten opetusvirhe (MSE ja R2):
  ennustukset_opetus = lm.predict(data_x_opetus)
  opetus_mse[i] = mean_squared_error(data_y_opetus, ennustukset_opetus)
  opetus_r2[i] = r2_score(data_y_opetus, ennustukset_opetus)

  # Lasketaan ennustusten validointivirhe (MSE ja R2):
  ennustukset_validointi = lm.predict(data_x_validointi)
  validointi_mse[i] = mean_squared_error(data_y_validointi, ennustukset_validointi)
  validointi_r2[i] = r2_score(data_y_validointi, ennustukset_validointi)


# In[74]:


# 10 toistoa, 10 virhettä (MSE):
print(opetus_mse)


# In[75]:


# Yleensä raportoidaan toistettujen mallinnusten keskimääräinen virhe:
print(np.mean(opetus_mse))


# In[76]:


# Kymmenen toistoa, 10 virhettä (MSE)
print(validointi_mse)


# In[77]:


# Yleensä raportoidaan toistettujen mallinnusten keskimääräinen virhe:
print(np.mean(validointi_mse))


# In[78]:


# Tee tuloskuva, jossa opetusvirheet ja validointivirheet
# on visualisoitu:
plt.plot(np.ones((10,1)), opetus_mse, '.')
plt.plot(2*np.ones((10,1)), validointi_mse, '.')
plt.title('Lineaarisen mallin opetus- ja validointivirhe (MSE)')
plt.xticks([1,2], ['opetus', 'validointi'])
plt.ylabel('Keskimääräinen neliövirhe')
plt.show()


# In[79]:


# 10 toistoa, 10 selitysastetta:
print(opetus_r2)


# In[80]:


# Yleensä raportoidaan toistettujen mallinnusten keskimääräinen selitysaste:
print(np.mean(opetus_r2))


# In[81]:


# 10 toistoa, 10 selitysastetta:
print(validointi_r2)


# In[82]:


# Yleensä raportoidaan toistettujen mallinnusten keskimääräinen selitysaste:
print(np.mean(validointi_r2))


# In[83]:


# Tee tuloskuva, jossa opetusvirheet ja validointivirheet
# on visualisoitu:
plt.plot(np.ones((10,1)), opetus_r2, '.')
plt.plot(2*np.ones((10,1)), validointi_r2, '.')
plt.title('Lineaarisen mallin opetus- ja validointivirheet (selitysaste)')
plt.xticks([1,2], ['opetus', 'validointi'])
plt.ylabel('Selitysaste, R^2')
plt.show()


# Tehtävä 1. Kokeile samaa analyysiketjua jollakin muulla datalla, jossa on yksi syötemuuttuja ja yksi vastemuuttuja. Voit valita datan vaikka kirjastosta sklearn.datasets ja poimia datasta haluamasi syötemuuttujan x ja vastemuuttujan y. Mieti tarvitaanko malliin molemmat paramterit a ja b, tai vain a?

# In[ ]:




