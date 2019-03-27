import numpy as np
import matplotlib.pyplot as plt
import cv2

a = np.load('out/disparities.npy')

f = open("utils/filenames/stereo360_test.txt", "r")
ps = []
for p in f:
    ps.append('data\\' + p.split(' ')[0])

for i in range(100):
    im = cv2.imread(ps[i])
    im = cv2.resize(im, (a[i].shape[1], a[i].shape[0]))
    cv2.imwrite('out/vis/%i_rgb.jpg' % i, im)
    np.save('out/vis/%i_d' % i, a[i])
    cv2.imwrite('out/vis/%i_d.jpg' % i, 2 * a[i] / np.max(a[i]) * 255)
