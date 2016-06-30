from skimage.morphology import medial_axis
import scipy.io as sio

import matplotlib.pyplot as plt

image = sio.loadmat('binaryImage.mat')['binaryImage']

skeleton, distance = medial_axis(image, return_distance=True)
dist_on_skel = distance * skeleton

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True,
                               subplot_kw={'adjustable': 'box-forced'})
ax1.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
ax2.contour(image, [0.5], colors='k')
ax2.axis('off')

plt.savefig('distance.png', dpi=1200)
# plt.show()