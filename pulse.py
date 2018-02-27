import cv2
import numpy as np
import statistics
from collections import Counter
from scipy import signal
from sklearn.decomposition import PCA
from scipy.signal import butter, lfilter, freqz
from scipy.signal import find_peaks_cwt
from scipy.interpolate import interp1d

def getavg(indexes,tr):
	dif = []
	if len(indexes)>2:
		for i in range(1,len(indexes)):
			sub = indexes[i]-indexes[i-1]
			if tr<= sub:
				dif.append(indexes[i]-indexes[i-1])
		return np.average(dif[:20])
	else:
		return np.average(indexes)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def combinelists(l1,l2):
	l = [None]*(len(l1)+len(l2))
	l[0:len(l1)] = l1
	l[len(l1):len(l1)+len(l2)] = l2
	return l
def get2dList(N):
	l=[]
	for i in xrange(N):
		l.append([])
	return l

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True

face_cascade = cv2.CascadeClassifier('/home/ajwahir/imagine_cup/cfd/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/ajwahir/imagine_cup/cfd/haarcascade/haarcascade_eye.xml')

vidcap = cv2.VideoCapture(0)
# vidcap = cv2.VideoCapture('/home/ajwahir/acads/pd3/face2.mp4')
vidcap.set(4,1280)
vidcap.set(5,720)
# vidcap.set(4,520)
# vidcap.set(5,718)
success,image = vidcap.read()

lowcut = 0.75
highcut = 5.0
fs=250.
fc=30.


count = 0
success = True
while success:
	count= count+1
	success,image = vidcap.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 2)
	if not len(faces):
		count=count-1
		continue
	(x,y,w,h)=faces[0]
	# print 'here'


	# roi =gray[x+w*0.25:w*0.5, y:h*0.9]
	roi1 =image[y:y+int(h*0.9*0.2),int(x+w*0.25):int(w*0.5)+int(x+w*0.25)]
	roi2 =image[int(y+h*0.9*0.55):int(h*0.9*0.45)+int(y+h*0.9*0.55),int(x+w*0.25):int(w*0.5)+int(x+w*0.25)]
	lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
	if count==1:

		fast = cv2.FastFeatureDetector_create(threshold=8)
		_kp1 = fast.detect(roi1,None)
		_kp2 = fast.detect(roi2,None)

		kp1=[]
		# kp2=[]
		for kp in _kp1[::-1]:
			kp1.append(cv2.KeyPoint(kp.pt[1]+int(x+w*0.25), kp.pt[0]+y, 0))
		for kp in _kp2[::-1]:
			kp1.append(cv2.KeyPoint(kp.pt[1]+int(x+w*0.25),kp.pt[0]+int(y+h*0.9*0.55),0))
		prev=gray
		knp=[]
		for kp in kp1:
			knp.append([kp.pt[1],kp.pt[0]])

		N=len(knp)
		yL=get2dList(len(knp))
		knp=np.asarray(knp,dtype=np.float32)
	else:
		p1, st, err = cv2.calcOpticalFlowPyrLK(prev, gray, knp, None, **lk_params)

		kl=list(knp)
		pl=[]
		md=[]

		for g in range(0,len(p1)):
			pl.append(list(p1[g]))
		for i in range(0,len(p1)):
			if(len(yL[i])==250):
				del yL[i][0]
			md.append(int(pl[i][0]-kl[i][0]))


		# print yL[0]
		# for i in range(0,len(yL[0])):
		for i in range(0,len(p1)):
			yL[i].append(pl[i][0]-kl[i][0])
			x_resample = np.linspace(0, len(yL[i])/fc, num=(len(yL[i])*fs)/(fc), endpoint=False)

		# Get mode and remove if the amplitude is more than the mode

		mod = max(set(md),key=md.count)
		# mod = md.most_common(1 	)
		for i in range(0,len(p1)):
			if md[i]<=mod:
				yL[i].append(pl[i][0]-kl[i][0])
			else:
				yL[i].append(0)

		xL=[]
		for i in range(0,len(pl)):
			xL.append(butter_bandpass_filter(yL[i],lowcut,highcut,fs,5))
		xLT=np.transpose(xL)

		if(count%50==0):
			cv2.imwrite('image.jpg',image)

		# print xLT
		tr=0

		if len(xLT)>5:
			pca = PCA(n_components=5)
		# # pca.fit(np.asarray(xL))
			x_p=pca.fit_transform(np.asarray(xLT), y=None)

			x_pf=np.transpose(x_p)
			indexes=[]
			getfreq=[]
			for i in range(0,5):
				indexes.append(find_peaks_cwt(x_pf[i][:250], np.arange(1, 250)))
				getfreq.append(getavg(indexes[i],tr))

			fin = np.max(getfreq)
			finp=fin/fs
			finp=finp*120

			print finp

			f=open('static/heartrate.txt','w')
			f.write('Your Pulse Rate is '+ str(round(finp,2)))
			f.close()
		
