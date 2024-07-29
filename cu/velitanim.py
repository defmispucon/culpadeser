import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot([1, 2, 3])
ax[1, 1].plot([4, 5, 6])

plt.tight_layout()
plt.show()
