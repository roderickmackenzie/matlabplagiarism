#!/usr/bin/env python
import os
import sys
import pygtk
import glob
import subprocess
import difflib

def do_diff(out,f0,f1):
	fromlines = open(f0, 'U').readlines()
	tolines = open(f1, 'U').readlines()

	diff = difflib.HtmlDiff().make_file(fromlines,tolines,f0,f1)


	a = open(out, "w")
	a.write(diff)
	a.close()


def gen_vector(name):
	f=open(name)
	config = f.readlines()
	f.close()
	out=[]

	for i in range(0, len(config)):
		config[i]=config[i].rstrip()
		config[i]=config[i].replace(" ", "")
		config[i]=config[i].replace("\t", "")
		if config[i].count("%")>0:
			config[i]=config[i].split('%')[0]
		config[i]=config[i].lower()
		if len(config[i])>100:
			config[i]=""

		if config[i]=="end":
			config[i]=""

		if config[i]!="":
			out.append(config[i])

	#vector=[]
	#for ii in range(0, len(out)):
	#	found=out[ii]#test(config[ii])
		#print config[ii],"/",found
	#	if len(found)>0:
	#		vector.append(found)

	return out

def cmp_vec(v0,v1):
	match=0
	match_len=4
	tot=0
	if len(v0)-match_len>0:
		if len(v1)-match_len>0:
			for i in range(0,len(v0)-match_len):
				for ii in range(0,len(v1)-match_len):
					found=True
					for iii in range(0,match_len):
						if v0[i+iii]!=v1[ii+iii]:
							found=False
					if found==True:
						#print v0[i:i+match_len]
						match=match+1
						break
					tot=tot+1
	if tot<5:
		return 0

	if match*match_len>15:
		return match
	else:
		return 0.0

argc = len(sys.argv)


found_inc_lib=[]
def_old=[]
d=[]
year="2014"
path_to_walk=os.path.join(os.getcwd(),"lib",year)
for root, dirs, files in os.walk(path_to_walk):
    for myfile in files:
        if myfile.endswith(".m") or myfile.endswith(".M"):
			found_inc_lib.append(os.path.join(root, myfile))
			def_old.append(True)
			d.append(os.path.join(year,os.path.dirname(os.path.join(root, myfile))[len(path_to_walk)+1:].split("/")[0]))

path_to_walk=os.path.join(os.getcwd(),"extracted")
for root, dirs, files in os.walk(path_to_walk):
    for myfile in files:
        if myfile.endswith(".m") or myfile.endswith(".M"):
			found_inc_lib.append(os.path.join(root, myfile))
			def_old.append(False)
			d.append(os.path.dirname(os.path.join(root, myfile))[len(path_to_walk)+1:].split("/")[0])



files=[]
vec=[]
done=[]
old=[]
dirs=[]

for i in range(0,len(found_inc_lib)):
	v=gen_vector(found_inc_lib[i])
	if len(v)>15:
		vec.append(v)
		files.append(found_inc_lib[i])
		done.append([])
		old.append(def_old[i])
		dirs.append(d[i])
#v0=gen_vector(found[3])
#v1=gen_vector(found[2])
f0=[]
f1=[]
v0=[]
v1=[]
value=[]
d0=[]
d1=[]
n=len(vec)
for i in range(0,n):
	print i,n
	for ii in range(0,n):
		if old[i] == False or old[ii] == False: 
			if os.path.dirname(files[i]) != os.path.dirname(files[ii]):
				if ii not in done[i] and i not in done[ii]:
					v=cmp_vec(vec[i],vec[ii])
					done[i].append(ii)
					done[ii].append(i)
					if v!=0.0:
						print "r=",v
						f0.append(files[i])
						f1.append(files[ii])
						d0.append(dirs[i])
						d1.append(dirs[ii])
						print dirs[i]
						v0.append(vec[i])
						v1.append(vec[ii])
						value.append(v)


value,f0, f1,v0,v1,d0,d1 = zip(*sorted(zip(value,f0, f1 , v0,v1,d0,d1), reverse=True))

#print value
if os.path.isdir("out")==False:
	os.makedirs("out")
my_max=25
if my_max>len(value):
	my_max=len(value)

for i in range(0,my_max):
	print i,value[i]
	dirname0=d0[i]
	dirname1=d1[i]
	output_dir=os.path.join(os.getcwd(),"out",dirname0,dirname1)

	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	html_out=os.path.join(output_dir,str(i)+".html")
	pdf_out=os.path.join(output_dir,str(i)+".pdf")
	print d0[i],d1[i],value[i],v0[i],v1[i]
	print f0[i],f1[i],value[i],v0[i],v1[i]

	do_diff(html_out,f0[i],f1[i])
	os.system("wkhtmltopdf -O landscape "+html_out+" "+pdf_out)


