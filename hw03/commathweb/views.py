from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

#แปลงเลขทศนิยมเป็น IEEE floating point single precision (32-bit)
def dec_32(req):
	if req.method == 'POST':
		d = float(req.POST.get('x'))
		nb = bin(int(d))
		lung = d - int(d)
		bilung=''
		count = 0
		while(lung!=0):
			lung*=2
			bilung = bilung+str(int(lung))
			lung -= int(lung)
			count += 1
			if count == 17 : break
		nb = nb[2:]
		e = len(nb)-1
		s = '0' if d >= 0 else '1'
		e += 127
		bie = bin(e)
		nbbilung = nb+bilung
		bie = bie[2:]
		nbbilung = nbbilung[1:]
		bx = s+bie+nbbilung
		b = bx + '0'*(32-len(bx))
		# result = Convertback32(b)
		s = b[0]
		e = b[1:9]
		f = b[9:33]
		return render(req,'dec_32.html',{'s':s,'e':e,'f':f,'b':b,'d':d})
	else :
		return render(req,'dec_32.html')

#แปลงเลขทศนิยมเป็น IEEE floating point double precision (64-bit)
def dec_64(req):
	if req.method == 'POST':
		d = float(req.POST.get('x'))
		nb = bin(int(d))
		lung = d - int(d)

		bilung=''

		count = 0
		while(lung!=0):
			lung*=2
			bilung = bilung+str(int(lung))
			lung -= int(lung)
			count += 1
			if count == 44 : break

		nb = nb[2:]
		e = len(nb)-1

		s = '0' if d >= 0 else '1'
		e += 1023
		bie = bin(e)

		nbbilung = nb+bilung
		bie = bie[2:]
		nbbilung = nbbilung[1:]
		bx = s+bie+nbbilung
		b = bx + '0'*(64-len(bx))
		# conb = Convertback64(b)

		s = b[0]
		e = b[1:12]
		f = b[12:65]

		return render(req,'dec_64.html',{'s':s,'e':e,'f':f,'d':d,'b':b})
	else:
		return render(req,'dec_64.html')
	#pass

def solve(A, b):
    import numpy as np
    a,b = np.array(A), np.array(b)
    n= len(A[0])
    x = np.array([0]*n)

    for k in range(0, n-1):
#1
        for j in range(k+1, n):
            if a[j,k] != 0.0:
                lam = a[j][k]/a[k][k]
                a[j,k:n] = a[j, k:n] - lam*a[k,k:n]
                b[j] = b[j] - lam*b[k]
#2
    for k in range(n-1,-1,-1):
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x.flatten()
#แก้ระบบสมการเชิงเส้น $Ax = b$
	#pass
def datasolve(req):
	if req.method == 'POST':
		matrix_y=[]
		matrix_x=[]
		data= req.POST.get('data')
		#x = data.split(',')
		data2 = data.split('\n')
		for i in data2:
			y=[float( i.split('=')[-1] )]
			matrix_y.append(y)
			x = (i.split('=')[0]).split(',')
			matrix_x.append(list(map(float, x)))

		results=solve(matrix_x,matrix_y)
		mylist = zip(matrix_x,matrix_y)
	try:
		return render(req,'solve.html',{'mylist':mylist,'results':results})
	except:
		return render(req,'solve.html')
