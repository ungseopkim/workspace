# -*- coding: utf-8 -*-
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#ax = fig.add_subplot(1,1,1)
#ax1 = fig.add_subplot(2,2,1)
#ax2 = fig.add_subplot(2,2,2)
#ax3 = fig.add_subplot(2,2,3)
#ax4 = fig.add_subplot(2,2,4)

#plt.plot(np.random.randn(50).cumsum(),
#         'cp-')
#         
#_ = ax1.hist(np.random.randn(100),
#             bias = 20,
#             color = 'k',
#             alpha=0.3)
#             
#ax2.scatter(np.arange(30),
#            np.arange(30)+3*np.random.randn(30))        
#            
#
#fig, axes = plt.subplots(2,3)
#
#print axes
#
#fig, axes = plt.subplots(2,2, sharex=True)
#
#print axes
#
#
#fig, axes = plt.subplots(2,2, sharey=True)
#
#print axes
#
#
#fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
#
#print axes

#
#fig, axes = plt.subplots(2,2, sharex=True, sharey= True)
#
#for i in range(2):
#    for j in range(2):
#        axes [i,j].hist(np.random.randn(500),
#                        bins = 50,
#                        color = 'k')
#plt.subplots_adjust(wspace=0.5, hspace=0.5)
#
#data = np.random.randn(30).cumsum()
#
#plt.plot(data, 'k--', label='Default')
#
#plt.plot(data, 'k--', drawstyle='steps-post', Label = 'state-post )
#
#plt.legend(loc='best')
#
#fig = plt.figure()
#fig = plt.figure(); ax = fig.add_subplot(1,1,1)
#ax.plot(np.random.randn(1000).cumsum())
#
#tick = ax.set_xticks([0,250,500,750,1000])
#labels = ax.set_xticklabels(['one','two','three','four','five'],
#                            rotation=30,
#                            fontsize='small')
#ax.set_title('My float')
#
#ax.set_xlabel('Stages')
#ax.set_ylabel('Values')
#                            
#a = np.arange(1,10)
#
#print a
#
#print a.cumprod()                            
#
#-----------------------------------------------
#ax = fig.add_subplot(1,1,1)
#
#data = pd.read_csv('spx.csv', index_col=0, parse_dates=True)
#spx = data['SPX']
#
#spx.plot(ax=ax, style='k--')
#
#crisis_data = [
#    (datetime(2007,10,11), 'Peak of bull market'),
#    (datetime(2008,3,12), 'Bear Stearns Fails'),
#    (datetime(2008,9,15), 'Lehman Bankruptcy')
#]
#
#for date, label in crisis_data:
#    ax.annotate(label, 
#                xy=(date, spx.asof(date)+50),
#                xytext=(date, spx.asof(date)+200),
#                arrowprops=dict(facecolor='black'),
#                horizontalalignment='left',
#                verticalalignment='top')
#                
#ax.set_xlim(['1/1/2007','1/1/2011'])
#ax.set_ylim([600,1800])
#
#ax.set_title('Important dates in 2008-2009 financial crisis')
#
#-----------------------------------------
#import matplotlib.pylab as plt
#
#fig = plt.figure()
#
#ax = fig.add_subplot(1,1,1)
#
#
#rect=plt.Rectangle((0.2,0.75),
#                0.4,
#                0.15,
#                color='k',
#                alpha=0.3)
#circ = plt.Circle((0.7,0.2),
#                  0.15,
#                  color='r',
#                  alpha=0.3)
#pgon = plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],
#                   color='0',
#                   alpha=0.5)
#                   
#ax.add_patch(rect)
#ax.add_patch(circ)
#ax.add_patch(pgon)
#
#plt.savefig('shape.svg', dpi=600)

#---------------------------------
#
#s = pd.Series(np.random.randn(10).cumsum(),
#              index=np.arange(0,100,10))
#
#s.plot()

#-----------------------------------
#
#df = pd.DataFrame(np.random.randn(10,4).cumsum(0),
#                  columns=['A','B','C','D'],
#                    index=np.arange(0,100,10))
#                    
#df.plot()
##df.plot(logy=True) 로그값으로나타낼때
#
#df.plot(xlim=50, title='My')
#
#-------------------------------------
#fig, axes = plt.subplots(2,1)
#
#data= pd.Series(np.random.randn(16),
#                index=list('abcdefghijklmnop'))
#data.plot(kind='bar', ax=axes[0])
#data.plot(kind='barh',ax=axes[1])
#
#----------------------------------------
#df = pd.DataFrame(np.random.randn(6,4),
#                  index= ['one','two' , 'three', 'four', 'five', 'six'],
#                  columns=pd.Index(['A','B','C','D'], name='Genus'))
#
#df.plot(kind='bar')
#
#df.plot(kind='bar', stacked=True)
#-------------------------------------------
#
#tips = pd.read_csv('tips.csv')
#
#tips['tip_pct'] = tips['tip'] / tips['total_bill']
#tips['tip_pct'].hist(bins=50)
#tips['tip_pct'].plot(kind='kde')
#--------------------------------------------
#
#comp1 = np.random.normal(0,1,size=200)
#comp2 = np.random.normal(10,2,size=200)
#values = pd.Series(np.concatenate((comp1,comp2)))
#
#values.hist(bins=200, normed=True)
#values.plot(kind='kde')
#
#macro = pd.read_csv('macrodata.csv')
#
#data = macro[['cpi','m1','tbilrate','unemp']]
#
#trans_data = np.log(data).diff().dropna()
#
#plt.scatter(trans_data['m1'], trans_data['unemp'])
#
#pd.scatter_matrix(trans_data, diagonal='kde')