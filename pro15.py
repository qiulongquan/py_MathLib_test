#coding=utf:8
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim([1,7])
ax.set_ylim([1,5])
ax.text(2,4.5,'this is comment test',color='r')
ax.text(2,4.7,r'http://matplotlib.org/users/mathtext.html',color='g')
print('字母输入参考文献http://matplotlib.org/users/mathtext.html')
ax.text(1,4,r'$\alpha_i\beta_j\pi\lambda\omega$',size=20)
ax.text(3,4,r'$\sin(0)=cos(\frac{\pi}{2})$',size=20)
ax.text(1,2,r'$\lim_{x \rightarrow y}\frac{1}{x^3}$',size=20)
ax.text(3,2,r'$\sqrt[4]{x}=\sqrt{y}$',size=20)
plt.show()