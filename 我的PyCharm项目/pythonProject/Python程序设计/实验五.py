import math
def fenduanfunction(x):
	input('请输入x的值')
	if x < 4:
		print(1+2*x)
		return
	elif x == 4:
		print(str(1+2*x)+'或'+ str(2+math.log(x)))
		return
	else:
		print(2+math.log(x))
		return
