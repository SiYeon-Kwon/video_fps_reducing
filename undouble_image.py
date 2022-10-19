import cv2
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
from imagesc import imagesc
from undouble import Undouble

methods = ['ahash', 'dhash', 'whash-haar']

for method in methods:
    # Average Hash
    model = Undouble(method=method, hash_size=8)
    # Import example data
    targetdir = r'/home/kwon/compression/image'
    # Grayscaling and scaling
    model.import_data(targetdir)
    # Compute image for only the first image.
    hashs = model.compute_imghash(model.results['img'][0], to_array=False)
    # Compute the image-hash
    print(method + ' Hash:')
    image_hash = ''.join(hashs[0].astype(int).astype(str).ravel())
    print("Binary image hash: %s" %(image_hash))
    print("Hex image hash: %s" %(hex(int(image_hash, 2))))

    # Import image for plotting purposes
    img_g = cv2.imread(model.results['pathnames'][0], cv2.IMREAD_GRAYSCALE)
    img_r = cv2.resize(img_g, (8, 8), interpolation=cv2.INTER_AREA)

    # Make the figure
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    ax[0][0].imshow(model.results['img'][0][..., ::-1])
    ax[0][0].axis('off')
    ax[0][0].set_title('Source image')
    ax[0][1].imshow(img_g, cmap='gray')
    ax[0][1].axis('off')
    ax[0][1].set_title('grayscale image')
    ax[1][0].imshow(img_r, cmap='gray')
    ax[1][0].axis('off')
    ax[1][0].set_title('grayscale image, size %.0dx%.0d' %(8, 8))
    ax[1][1].imshow(hashs[0], cmap='gray')
    ax[1][1].axis('off')
    ax[1][1].set_title(method + ' function')

# Initialize model
model = Undouble(method='phash', hash_size=8)

# Import example data
targetdir = r'/home/kwon/compression/image'

model.import_data(targetdir)
model.compute_hash()
model.group(threshold=0.9)
model.plot()
model.move(r'/home/kwon/compression')

'''
# Import library
from clustimage import Clustimage

# init
cl = Clustimage(method='pca')

# Note that you manually need to download the data from the caltech website and simply provide the directory where the images are stored.
# Download dataset

# Cluster  images in path location.
results = cl.fit_transform(r'/home/kwon/compression/image', min_clust=60, max_clust=110)

# If you want to experiment with a different clustering and/or evaluation approach, use the cluster functionality.
# This will avoid pre-processing, and performing the feature extraction of all images again.
# You can also cluster on the 2-D embedded space by setting the cluster_space parameter 'low'
#
# cluster(cluster='agglomerative', evaluate='dbindex', metric='euclidean', linkage='ward', min_clust=15, max_clust=200, cluster_space='high')

# Cluster evaluation plots such as the Silhouette plot
cl.clusteval.plot()
cl.clusteval.scatter(cl.results['xycoord'])

# PCA explained variance plot
cl.pca.plot()

# Dendrogram
cl.dendrogram()

# Plot unique image per cluster
cl.plot_unique(img_mean=False)

# Scatterplot
cl.scatter(dotsize=8, zoom=0.2, img_mean=False)

# Plot images per cluster or all clusters
cl.plot(labels=8)

cl.save(r'/home/kwon/compression/clustimage_model', overwrite=True)'''