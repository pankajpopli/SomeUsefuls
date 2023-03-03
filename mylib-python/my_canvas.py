#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
import numpy as np
#%%
def canvas_1by1(size=[10,10],labelx=r'$x$',labely=r'$y$',TextSize=20,ticksize=18):
   """Create a canvas of 1by1
      add xlabel or ylabel, TextSize, ticksize.
      add additional subplt_kwargs for fig.add_subplot().
   """
   fig = plt.figure(figsize=size)
   ax = plt.axes()
   ax.set_xlabel(labelx,fontsize=TextSize)
   ax.set_ylabel(labely,fontsize=TextSize)
   ax.tick_params(axis='both', which='major', labelsize=ticksize)
   return ax,fig


def canvas_1by2(size=[18,4],xlabel=[r'x']*2,ylabel=[r'x']*2,TextSize=20,ticksize=18, **subplt_kwargs):
   """Create a canvas of 1by2
      add xlabel or ylabel, TextSize, ticksize.
      add additional subplt_kwargs for fig.add_subplot().
   """
   nrow=1
   ncol=2
   fig = plt.figure(figsize=size,constrained_layout=True)
   gs = plt.GridSpec(nrows=nrow, ncols=ncol, wspace=0.04,hspace=0.5, figure=fig)
   ax=list()
   for i in range(nrow*ncol):
      ax.append(fig.add_subplot(gs[i],**subplt_kwargs))
      ax[i].set_xlabel(xlabel[i],fontsize=TextSize)
      ax[i].set_ylabel(ylabel[i],fontsize=TextSize)
      ax[i].tick_params(axis='both', which='major', labelsize=ticksize)
   return ax,fig

def canvas_2by2(size=[15,7],xlabel=[r'x']*4,ylabel=[r'y']*4,TextSize=20,ticksize=18, **subplt_kwargs):
   """Create a canvas of 2by2
      add xlabel or ylabel, TextSize, ticksize.
      add additional subplt_kwargs for fig.add_subplot().
   """
   nrow=2
   ncol=2
   fig = plt.figure(figsize=size,constrained_layout=True)
   gs = plt.GridSpec(nrows=nrow, ncols=ncol, wspace=0.04,hspace=0.01, figure=fig)
   ax=list()
   for i in range(nrow*ncol):
      ax.append(fig.add_subplot(gs[i],**subplt_kwargs))
      ax[i].set_xlabel(xlabel[i],fontsize=TextSize)
      ax[i].set_ylabel(ylabel[i],fontsize=TextSize)
      ax[i].tick_params(axis='both', which='major', labelsize=ticksize)
   return ax,fig

def canvas_NbyM(nrow,ncol,size=[15,7],xlabel=[r'x'],ylabel=[r'y'],TextSize=20,ticksize=18, **subplt_kwargs):
   """Create a canvas of NbyM, default 4by3.
      add xlabel or ylabel, TextSize, ticksize.
      add additional subplt_kwargs for fig.add_subplot().
   """
   xlabel=[r'x']*nrow*ncol;
   ylabel=[r'y']*nrow*ncol;
   fig = plt.figure(figsize=size,constrained_layout=True)
   gs = plt.GridSpec(nrows=nrow, ncols=ncol, wspace=0.04,hspace=0.01, figure=fig)
   ax=list()
   for i in range(nrow*ncol):
      ax.append(fig.add_subplot(gs[i],**subplt_kwargs))
      ax[i].set_xlabel(xlabel[i],fontsize=TextSize)
      ax[i].set_ylabel(ylabel[i],fontsize=TextSize)
      ax[i].tick_params(axis='both', which='major', labelsize=ticksize)
   return ax,fig

def canvas_NbyM_colorbar(nrow=1,ncol=2,size=[10,10],xlabel=[r'x'],ylabel=[r'y'],title=r'latex title here',clabel=r'Clabel',TextSize=20,ticksize=18, **subplt_kwargs):
   """Create a canvas of NbyM with colorbar, default 1by2.
      add xlabel or ylabel, TextSize, ticksize, title, clabel and more. Option disbaled for now.
      add additional subplt_kwargs for fig.add_subplot().
   """
   fig = plt.figure(figsize=size,constrained_layout=True)
   ncolPlusCbar = ncol*2
   xlabel=[r'x']*nrow*ncolPlusCbar;
   ylabel=[r'y']*nrow*ncolPlusCbar;
   gs = plt.GridSpec(nrows=nrow, ncols=ncolPlusCbar,figure=fig,width_ratios=(1,0.05)*ncol)
   ax=list()
   for i in range(nrow):
      for j in range(ncolPlusCbar):
         if j%2!=0:
            ratio=20
         else:
            ratio=1
         ax.append(fig.add_subplot(gs[i,j],box_aspect=ratio,**subplt_kwargs))
   
   # for i in range(np.size(ax)):
   #    ax[i].tick_params(axis='both', which='major', labelsize=ticksize)
   #    npArray = np.array([[[200, 200, 200, 255]]], dtype='uint8')
   #    ax[i].set_xlabel(xlabel[i])
   #    ax[i].set_ylabel(ylabel[i])
   #    if i%2==0:
   #       sc1=ax[i].imshow(npArray, interpolation='nearest')
   #       print(sc1)
   #       ax[i].set_title(title,fontsize=TextSize)
   #    elif i%2 != 0:
   #       plt.colorbar(sc1,cax=ax[i],format='%0.01f').set_label(label=clabel,size=TextSize)
         
   axz=[*zip(ax[::2], ax[1::2])]
   return axz, fig
# %%
