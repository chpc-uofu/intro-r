import matplotlib.pyplot as plt

# Case I: z <=1.0
fig, ax = plt.subplots()
plt.fill((0.0,0.0,0.80,0.0),(0., 0.80,0.0,0.0),color="b")
plt.plot((0.0,0.0,0.80,0.0),(0., 0.80,0.0,0.0), color="r")
plt.plot((0.0,0.0,1.0,1.0,0  ),(0.,1.,1.,0,0.),color="orange")
plt.xlim(0.0,1.10)
plt.ylim(0.0,1.10)
plt.xticks([0.0,1.0])
plt.yticks([0.0,1.0])
plt.xlabel(r"$X$")
plt.ylabel(r"$Y$")
plt.text(0.6, 0.25, r"$Y=z-X$")
ax.spines[['right', 'top']].set_visible(False)
plt.text(0.7850, -0.05, r"$z$")
plt.text(-0.035,0.80,r"$z$")
#plt.show()
plt.savefig('case1.pdf',dpi=600)
