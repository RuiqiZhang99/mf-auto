import numpy as np
import matplotlib.pyplot as plt

path_list = ['./drivable_area.npy',
            './norm_distance_from_start.npy',
            './norm_distance_to.npy',
            './norm_distance_to_obstacle.npy',
            # './properties.npy'
]
for path in path_list:
    data = np.load(path)
    plt.imshow(data, cmap="gray")
    plt.show()