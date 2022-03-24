import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib import cm

# caltech l1 l2
# result = [['0.2408', '0.2330', '0.2345', '0.2297', '0.2351', '0.2411'],
#           ['0.2456', '0.2390', '0.2423', '0.2368', '0.2427', '0.2392'],
#           ['0.2253', '0.2276', '0.2163', '0.2269', '0.2344', '0.2277'],
#           ['0.2133', '0.2205', '0.2188', '0.2241', '0.2260', '0.2294'],
#           ['0.2147', '0.2208', '0.2166', '0.2214', '0.2219', '0.2076'],
#           ['0.2166', '0.2201', '0.1884', '0.2166', '0.2162', '0.2239']]

# amazon l1 l2
# result = [['0.4432', '0.4491', '0.4402', '0.4503', '0.4545', '0.4322'],
#           ['0.4285', '0.4293', '0.4355', '0.4264', '0.4276', '0.4235'],
#           ['0.4176', '0.4184', '0.4183', '0.4275', '0.4103', '0.4252'],
#           ['0.4098', '0.4048', '0.4098', '0.3995', '0.4067', '0.4025'],
#           ['0.4011', '0.3798', '0.4074', '0.3883', '0.3964', '0.4069'],
#           ['0.4136', '0.4019', '0.4110', '0.4060', '0.4071', '0.4167']]

# webcam l1 l2
# result = [['0.4328', '0.4249', '0.4375', '0.4213', '0.4397', '0.4313'],
#           ['0.4176', '0.4142', '0.4000', '0.3914', '0.4158', '0.4355'],
#           ['0.3939', '0.3718', '0.4170', '0.4021', '0.4062', '0.3956'],
#           ['0.3791', '0.3755', '0.3909', '0.3659', '0.3900', '0.3821'],
#           ['0.3877', '0.4001', '0.4112', '0.3938', '0.3932', '0.4213'],
#           ['0.3922', '0.3659', '0.4112', '0.4010', '0.3905', '0.3845']]

# dslr l1 l2
# result = [['0.4750', '0.4703', '0.4716', '0.4680', '0.4690', '0.4701'],
#           ['0.4692', '0.4735', '0.4565', '0.4658', '0.4681', '0.4646'],
#           ['0.4411', '0.4312', '0.4388', '0.4487', '0.4517', '0.4449'],
#           ['0.4479', '0.4409', '0.4380', '0.4444', '0.4617', '0.4453'],
#           ['0.4363', '0.4470', '0.4510', '0.4512', '0.4491', '0.4329'],
#           ['0.4444', '0.4433', '0.4455', '0.4580', '0.4409', '0.4404']]

# Product-sub1 l1 l2
# result = [['0.3517', '0.3536', '0.3500', '0.3548', '0.3495', '0.3456'],
#           ['0.3395', '0.3594', '0.3509', '0.3485', '0.3408', '0.3404'],
#           ['0.3191', '0.3180', '0.3249', '0.3181', '0.3207', '0.3204'],
#           ['0.3262', '0.3205', '0.3166', '0.3369', '0.3210', '0.3189'],
#           ['0.3218', '0.3210', '0.3167', '0.3324', '0.3308', '0.3384'],
#           ['0.3101', '0.3118', '0.3177', '0.3245', '0.3046', '0.3138']]

# Product-sub2 l1 l2
# result = [['0.3242', '0.3383', '0.3226', '0.3383', '0.3027', '0.3375'],
#           ['0.2887', '0.3114', '0.2977', '0.3142', '0.2786', '0.3130'],
#           ['0.2967', '0.2868', '0.2978', '0.2873', '0.2980', '0.2877'],
#           ['0.2793', '0.2804', '0.2781', '0.2659', '0.2559', '0.2703'],
#           ['0.2735', '0.2761', '0.2761', '0.2743', '0.2910', '0.2766'],
#           ['0.2813', '0.2747', '0.2694', '0.2855', '0.2599', '0.2729']]

# Product-sub3 l1 l2
result = [['0.2603', '0.2532', '0.2544', '0.2633', '0.2449', '0.2537'],
          ['0.2479', '0.2485', '0.2473', '0.2447', '0.2501', '0.2364'],
          ['0.2320', '0.2309', '0.2298', '0.2234', '0.2295', '0.2325'],
          ['0.2218', '0.2302', '0.2157', '0.2389', '0.2206', '0.2266'],
          ['0.2347', '0.2273', '0.2259', '0.2190', '0.2269', '0.2350'],
          ['0.2145', '0.2199', '0.2260', '0.2172', '0.2328', '0.2151']]

result = np.array(result, dtype=np.float)
font = {'size': 12, 'weight': 'bold'}

fig = plt.figure(figsize=(5, 5), dpi=200)
ax1 = fig.add_subplot(111, projection='3d')
plt.tick_params(labelsize=12, pad=0)
xlabels = np.array(['1e-2', '1e-1', '1', '10', '$\mathregular{10^2}$', '$\mathregular{10^3}$'])
xpos = np.arange(xlabels.shape[0])
ylabels = np.array(['1e-2', '1e-1', '1', '10', '$\mathregular{10^2}$', '$\mathregular{10^3}$'])
ypos = np.arange(ylabels.shape[0])
labels = ax1.get_xticklabels() + ax1.get_yticklabels() + ax1.get_zticklabels()
# print labels
[label.set_fontweight('bold') for label in labels]

xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

dx = 0.8
dy = 0.8
dz = result.ravel()


ax1.w_xaxis.set_ticks(xpos + dx / 2., )
ax1.w_xaxis.set_ticklabels(xlabels)

ax1.w_yaxis.set_ticks(ypos + dy / 2.)
ax1.w_yaxis.set_ticklabels(ylabels)
ax1.zaxis.set_major_locator(MultipleLocator(0.2))
ax1.get_proj = lambda: np.dot(Axes3D.get_proj(ax1), np.diag([1, 1, 0.5, 1]))

ax1.set_xlabel(r"$\mathregular{λ_1}$", fontdict=font)
ax1.set_ylabel(r"$\mathregular{λ_2}$", fontdict=font)
ax1.set_zlabel("  NMI", fontdict=font)

values = np.linspace(0.2, 1., xposM.ravel().shape[0])
# colors = cm.rainbow(values)
colors = ['blue'] * 6 + ['cyan'] * 6 + ['limegreen'] * 6 + \
    ['yellow'] * 6 + ['orange'] * 6 + ['red'] * 6
print(colors)
ax1.bar3d(
    xposM.ravel(),
    yposM.ravel(),
    0,
    dx,
    dy,
    dz,
    color=colors,
    edgecolor='black')
plt.savefig('caltech')
plt.show()
