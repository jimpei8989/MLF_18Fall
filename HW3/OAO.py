import numpy as np
import matplotlib.pyplot as plt

def read_data(url):
	# train = urllib3.urlopen(url)
	data = np.loadtxt(url, dtype=np.float)
	row, col = data.shape
	X = np.concatenate((np.ones((row, 1), dtype=np.float), data[:, 0:col-1]), axis=1)
	Y = data[:, -1:]
	# X = np.c_[np.ones((row, 1)), data[:, 0:col-1]]
	# Y = np.c_[data[:, -1]]
	return X, Y

def theta_function(c):
	return 1 / (1+np.exp(-1*c))

def log_reg(x, y, yeeeeta, times, testX, testY):
	row, col = x.shape
	W = np.zeros((col, 1), dtype=np.float)
	ein = np.zeros(times, dtype=np.float)
	eout = np.zeros(times, dtype=np.float)
	# print (y.shape)
	# print(x.shape)
	# print (W.shape)
	# exit()
	for t in range(times):
		Theta = theta_function(-1*y*x.dot(W))
		# print (Theta.shape)
		# exit()
		gradient_E = -(y*x).T.dot(Theta)/float(row)
		ein[t] = error_measure(x, y, W)
		eout[t] = error_measure(testX, testY, W)
		W -= yeeeeta*gradient_E
	return ein, eout

def SGD(x, y, yeeeeta, times, testX, testY):
	row, col = x.shape
	Ein = np.zeros(times, dtype=np.float)
	Eout = np.zeros(times, dtype=np.float)
	W = np.zeros((col, 1), dtype=np.float)
	cur = 0
	for t in range(times):
		# print (x.shape)
		# print (x[t%row].dot(W).shape)
		# exit()
		Theta = theta_function(-1*y[t%row]*x[t%row].dot(W))
		gradient_E = -y[t%row]*x[t%row].T*Theta
		gradient_E.shape = (col, 1)
		Ein[t] = error_measure(x, y, W)
		Eout[t] = error_measure(testX, testY, W)
		W -= yeeeeta*gradient_E
	return Ein, Eout

def error_measure(testdata, y, ww):
	row, col = testdata.shape
	y_predict = np.sign(np.dot(testdata, ww))
	y_predict[y_predict==0] = -1
	err = np.sum(y_predict != y) / float(row)
	return err
	
if __name__ == '__main__':
	# read training and testing data
	x, y = read_data('hw3_train.dat')
	testX, testY = read_data('hw3_test.dat')
	# eta = 0.01
	err_in_0, err_out_0 = log_reg(x, y, 0.01, 2000, testX, testY)
	SGD_ein_0, SGD_eout_0 = SGD(x, y, 0.001, 2000, testX, testY)
	# # Ein
	plt.figure(figsize=(10,7))
	plt.xlabel("t (times)")
	plt.ylabel("E_in")
	plt.xlim(0, 2000)
	plt.ylim(0, 0.6)
	# plt.ylim(0.1, 0.5)
	plt.plot(err_in_0, '-', label="GD")
	plt.plot(SGD_ein_0, '-', label="SGD")
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
	plt.show()
	# Eout
	plt.figure(figsize=(10,7))
	plt.xlabel("t (times)")
	plt.ylabel("E_out")
	plt.xlim(0, 2000)
	plt.ylim(0, 0.6)
	# plt.ylim(0, 0.5)
	plt.plot(err_out_0, '-', label="GD")
	plt.plot(SGD_eout_0, '-', label="SGD")
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
	plt.show()	
	# # eta = 0.001
	err_in_1, err_out_1 = log_reg(x, y, 0.001, 2000, testX, testY)
	SGD_ein_1, SGD_eout_1 = SGD(x, y, 0.001, 2000, testX, testY)
	# # # Ein
	plt.figure(figsize=(10,7))
	plt.xlabel("t (times)")
	plt.ylabel("E_in")
	plt.xlim(0, 2000)
	plt.ylim(0, 0.6)
	# plt.ylim(0.4, 0.5)
	plt.plot(err_in_1, '-', label="GD")
	plt.plot(SGD_ein_1, '-', label="SGD")
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
	plt.show()
	# # # Eout
	plt.figure(figsize=(10,7))
	plt.xlabel("t (times)")
	plt.ylabel("E_out")
	plt.xlim(0, 2000)
	plt.ylim(0, 0.6)
	# plt.ylim(0.4, 0.5)
	plt.plot(err_out_1, '-', label="GD")
	plt.plot(SGD_eout_1, '-', label="SGD")
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
	plt.show()
