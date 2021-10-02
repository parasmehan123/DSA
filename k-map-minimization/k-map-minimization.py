	# CSE 101 - IP HW2
	# K-Map Minimization 
	# Name: HIMANSHU GARG
	# Roll Number: 2018337
	# Section: B
	# Group: 2
	# Date: 16th October 2018

def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.

        and will only work for two or more minterms when input 
	        
	Do not include any print statements in the function.
	"""
	import copy											#to use deep copy function


	num_var=numVar
	string=stringIn
	abc=string											#string consists of the function
	string=list(map(str,string.split("d")))				#used to split string in two
	a=str(string[0])
	a=a[1:-1]											#remove first and last braces of string[0]
	
	if a=="":											#when there is no necessary variable
		return "0"

	necessary=list(map(int,a.split(",")))				#stores main variables
	necessary.sort()


	a=str(string[1])
	if "-" in a:										#means there is no dont care
		dontcare=["empty"]								#bec dontcare will be empty string
	else:
		a=a[1:-1]										#remove first and last braces of string[0]
		dontcare=list(map(int,a.split(",")))			#stores don't care variables
		dontcare.sort()

	if "empty" in dontcare:
		totalminterms=necessary
	else:
		totalminterms=dontcare + necessary				#totalminterms is used to store all the minterms given in the function including dont cares also
		totalmintermsunsorted=copy.deepcopy(totalminterms)
		totalminterms.sort()




	#for the one when the whole kmap is filled with 1 or d
	if num_var==2 and len(totalminterms)==4:
		return "1"
	elif num_var==3 and len(totalminterms)==8:
		return "1"
	elif num_var==4 and len(totalminterms)==16:
		return "1"
		



	binary=[]											#binary is used to store BCD form of each input 

	"""
	convert decimal to binary and put it into binary[]
	"""
	if num_var==2:
		for i in totalminterms:
			if i==0:
				binary.append("00")
			elif i==1:
				binary.append("01")
			elif i==2:
				binary.append("10")
			elif i==3:
				binary.append("11")
	elif num_var==3:
		for i in totalminterms:
			if i==0:
				binary.append("000")
			elif i==1:
				binary.append("001")
			elif i==2:
				binary.append("010")
			elif i==3:
				binary.append("011")
			elif i==4:
				binary.append("100")
			elif i==5:
				binary.append("101")
			elif i==6:
				binary.append("110")
			elif i==7:
				binary.append("111")
	elif num_var==4:
		for i in totalminterms:
			if i==0:
				binary.append("0000")
			elif i==1:
				binary.append("0001")
			elif i==2:
				binary.append("0010")
			elif i==3:
				binary.append("0011")
			elif i==4:
				binary.append("0100")
			elif i==5:
				binary.append("0101")
			elif i==6:
				binary.append("0110")
			elif i==7:
				binary.append("0111")
			elif i==8:
				binary.append("1000")
			elif i==9:
				binary.append("1001")
			elif i==10:
				binary.append("1010")
			elif i==11:
				binary.append("1011")
			elif i==12:
				binary.append("1100")
			elif i==13:
				binary.append("1101")
			elif i==14:
				binary.append("1110")
			elif i==15:
				binary.append("1111")



	numberis=[[],[],[],[],[]]

	for i in binary:									#loop is used to add no of 1 = i in suitable list
		if i.count("1")==0:
			numberis[0].append(i)	
		elif i.count("1")==1:
			numberis[1].append(i)	
		elif i.count("1")==2:
			numberis[2].append(i)
		elif i.count("1")==3:
			numberis[3].append(i)
		elif i.count("1")==4:
			numberis[4].append(i)



	"""
	now following is used to store different size of implicants
	"""

	size2=[[],[],[],[]]
	size2decimal=[[],[],[],[]]									#sizeidecimal is used to store decimal value of implicants
	size4=[[],[],[]]											#sizei used to store size i implicants in binary form
	size4decimal=[[],[],[]]
	size8=[[],[]]
	size8decimal=[[],[]]

	vary=0														#vary variable is used to store no of fifferent digits in two binary nos taken


	for i in range(num_var):									#used to store in size2
		for j in range(len(numberis[i])):
			for k in range(len(numberis[i+1])):
				vary=0
				comp1=str(numberis[i][j])						#comp1 is used to store 1st variable that has to be compare 
				comp2=str(numberis[i+1][k])						#comp2 is used to store 2nd variable that has to be compare

				for c in range(num_var):
					if comp1[c]!=comp2[c]:
						vary=vary+1
						changed=c 								#changed is used to store the location no that is not same in both

				if vary==1:										#this means it has to be size 2 implicants
					no=str(numberis[i][j])
					size2decimal[i].append([int(comp1,2),int(comp2,2)])
					size2[i].append(no[:changed]+"-"+no[changed+1:])
	size2copy=copy.deepcopy(size2)
	EPI=[]														#used to store final ans
	empty='n'	
	whatinsize2decimal=[]

	for i in range(len(size2decimal)):							#used to store elements what all are there in size2decimal
		for j in range(len(size2decimal[i])):
			for k in range(len(size2decimal[i][j])):
				if size2decimal[i][j] not in whatinsize2decimal:
					whatinsize2decimal.append(size2decimal[i][j][k])
					


	if size2copy==[[],[],[],[]]:
		empty='y'
		for i in range(1,len(necessary)+1):
			EPI.append(binary[-i])
	
	for i in range(len(necessary)):
			if necessary[i] not in whatinsize2decimal:
				for j in range(len(totalminterms)):
					if necessary[i]==totalminterms[j]:
						EPI.append(binary[j])
	


	for i in range(len(size2)-1):								#used to store in size4
		for j in range(len(size2[i])):
			for k in range(len(size2[i+1])):
				vary=0
				comp1=str(size2[i][j])							#comp1 is used to store 1st variable that has to be compare 
				comp2=str(size2[i+1][k])						#comp2 is used to store 2nd variable that has to be compare

				for c in range(num_var):
					if comp1[c]!=comp2[c]:
						vary=vary+1
						changed=c 								#changed is used to store the location no that is not same in both

				if vary==1:										#this means it has to be size 4 implicants
					no=str(size2[i][j])
					size4decimal[i].append(size2decimal[i][j]+size2decimal[i+1][k])
					size4[i].append(no[:changed]+"-"+no[changed+1:])
					size2copy[i][j]=str(size2copy[i][j])+"*"					# * means it has already being taken i.e not essential prime implicant
					size2copy[i+1][k]=str(size2copy[i+1][k])+"*"



	#used to remove repeating implicants in size4
	for i in range(len(size4)):
		for j in range(len(size4[i])-1,-1,-1):
			if j%2==1:
				size4[i].pop(j)




	size4copy=copy.deepcopy(size4)



	u=[[],[],[],[]]										#a temp list to store unique values of size 4
	#used to remove repeating implicants in size4decimal
	for i in range(len(size4decimal)):
		for j in range(len(size4decimal[i])):	
			size4decimal[i][j].sort()
	for i in range(len(size4decimal)):
		for j in range(len(size4decimal[i])):
			if size4decimal[i][j] not in u[i]:
				u[i].append(size4decimal[i][j]) 				
	size4decimal=u





	if num_var==4:												#as then only size 8 variable will be used
		for i in range(len(size4)-1):								#used to store in size8
			for j in range(len(size4[i])):
				for k in range(len(size4[i+1])):
					vary=0
					comp1=str(size4[i][j])							#comp1 is used to store 1st variable that has to be compare 
					comp2=str(size4[i+1][k])						#comp2 is used to store 2nd variable that has to be compare

					for c in range(num_var):
						if comp1[c]!=comp2[c]:
							vary=vary+1
							changed=c 								#changed is used to store the location no that is not same in both

					if vary==1:										#this means it has to be size 8 implicants
						no=str(size4[i][j])
						size8decimal[i].append(size4decimal[i][j]+size4decimal[i+1][k])
						size8[i].append(no[:changed]+"-"+no[changed+1:])
						size4copy[i][j]=str(size4copy[i][j])+"*"					# * means it has already being taken i.e not prime implicant
						size4copy[i+1][k]=str(size4copy[i+1][k])+"*"





	PI=[]																			# PI is used to store essential prime implicants 
	PIdecimal=[]

	#used to store decimal as well as binary values of prime essentials
	for i in range(len(size8)):														#for size8												
		for j in range(len(size8[i])):
			if size8[i][j] not in PI and size8[i][j]!="":
				PI.append(size8[i][j])
				PIdecimal.append(size8decimal[i][j])

	for i in range(len(size4copy)):													#for size4
		for j in range(len(size4copy[i])):
			if size4copy[i][j] not in PI and "*" not in size4copy[i][j]:
				PI.append(size4copy[i][j])
				PIdecimal.append(size4decimal[i][j])
	for i in range(len(size2copy)):													#for size2
		for j in range(len(size2copy[i])):
			if size2copy[i][j] not in PI and "*" not in size2copy[i][j]:
				PI.append(size2copy[i][j])
				PIdecimal.append(size2decimal[i][j])

	PIdecimalcopy=copy.deepcopy(PIdecimal)
	PIcopy=copy.deepcopy(PI)
																			
	done=[]																			#consiss of minterms that will be constituted in EPI i.e.ans
	count=[]																		#used to store nos of time it repeats in different compinations associated in PE
	left=[]																			#used to store what necessary minterms left after adding some into EPI

	for i in range(len(necessary)):
		countt=0
		for j in range(len(PIdecimal)):
			for k in range(len(PIdecimal[j])):
				if str(necessary[i])==str(PIdecimal[j][k]):
					countt=countt+1
		count.append(countt)




	for i in range(len(count)):
		if count[i]==1:
			for j in range(len(PIdecimal)):
				for k in range(len(PIdecimal[j])):
					if str(PIdecimal[j][k])==str(necessary[i]):
						EPI.append(PI[j])
						done.append(PIdecimal[j])
		


	#used to find what is left what has not been added to EPI
	donee=[]
	for i in range(len(done)):
		for j in range(len(done[i])):
			if int(done[i][j]) not in donee:
				donee.append(int(done[i][j]))
	donee.sort()

	for i in necessary:
		if i not in donee:
			left.append(i)

	


	#used to find no of left variables that are available in each PI
	count=[]
	for i in range(len(PIdecimal)):
		countt=0
		for j in range(len(PIdecimal[i])):
			if PIdecimal[i][j] in left:
				countt=countt+1
		count.append(countt)

	if empty=='n':
		if max(count)>1:
			while max(count)>1:
				for i in range(len(count)):
					if count[i]==max(count):
						EPI.append(PI[i])
						for j in range(len(PIdecimal[i])):
							for k in range(len(left)-1,-1,-1):
								if PIdecimal[i][j]==left[k]:
									del left[k]
				#used to find no of left variables that are available in each PI
				count=[]
				for i in range(len(PIdecimal)):
					countt=0
					for j in range(len(PIdecimal[i])):
						if PIdecimal[i][j] in left:
							countt=countt+1
					count.append(countt)

	
	for i in range(len(left)-1,-1,-1):
		updated='n'
		for j in range(len(PIdecimal)):
			if updated=='y':
				break
			for k in range(len(PIdecimal[j])):	
				if (str(left[i])==str(PIdecimal[j][k])):
					EPI.append(PI[j])
					updated='y'
					break
	

	#following is used to make final ans in terms of w,x,y,z and save it into ans
	ans=[]

	if num_var==4:
		for i in range(len(EPI)):
			anss=""
			for j in range(len(EPI[i])):
				if j==0 and EPI[i][j]=="1":
					anss=anss+"w"
				elif j==0 and EPI[i][j]=="0":
					anss=anss+"w'"
				elif j==1 and EPI[i][j]=="1":
					anss=anss+"x"
				elif j==1 and EPI[i][j]=="0":
					anss=anss+"x'"
				elif j==2 and EPI[i][j]=="1":
					anss=anss+"y"
				elif j==2 and EPI[i][j]=="0":
					anss=anss+"y'"
				elif j==3 and EPI[i][j]=="1":
					anss=anss+"z"
				elif j==3 and EPI[i][j]=="0":
					anss=anss+"z'"
			ans.append(anss)
	elif num_var==3:
		for i in range(len(EPI)):
			anss=""
			for j in range(len(EPI[i])):
				if j==0 and EPI[i][j]=="1":
					anss=anss+"w"
				elif j==0 and EPI[i][j]=="0":
					anss=anss+"w'"
				elif j==1 and EPI[i][j]=="1":
					anss=anss+"x"
				elif j==1 and EPI[i][j]=="0":
					anss=anss+"x'"
				elif j==2 and EPI[i][j]=="1":
					anss=anss+"y"
				elif j==2 and EPI[i][j]=="0":
					anss=anss+"y'"
			ans.append(anss)
	elif num_var==2:
		for i in range(len(EPI)):
			anss=""
			for j in range(len(EPI[i])):
				if j==0 and EPI[i][j]=="1":
					anss=anss+"w"
				elif j==0 and EPI[i][j]=="0":
					anss=anss+"w'"
				elif j==1 and EPI[i][j]=="1":
					anss=anss+"x"
				elif j==1 and EPI[i][j]=="0":
					anss=anss+"x'"
			ans.append(anss)

	ans.sort()

	#following is used to remove repeating elemets from the ans
	finalans=[]							#stores new string where duplicate elements are not there
	for i in ans:
		if i not in finalans:
			finalans.append(i)
	finalans.sort()
	ans=finalans
	anss=""
	for i in range(len(ans)):
		if i == len(ans)-1:
			anss=anss+ans[i]
		else:
			anss=anss+ans[i]+"+"



	

	return anss											#as anss consists of final ans		





if __name__=='__main__':
	var=int(input("enter no of variables : "))
	strin=input("enter function : ")
	xyz=minFunc(var, strin)
	print(xyz)
