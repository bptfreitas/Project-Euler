#!/usr/bin/python


def depth_sum(tree,depth,node):
	if depth== len(tree)-1:
		return tree[depth][node]
	else:
		l=depth_sum(tree,depth+1,node)
		r=depth_sum(tree,depth+1,node+1)
		return tree[depth][node]+ (l if l > r else r)


data=open('problema18.txt')

mat=[]
for line in data:
	mat_line=[]
	for el in line.split():
		mat_line.append(int(el))
	mat.append(mat_line)

print mat[0][0]

x=depth_sum(mat,0,0)

print "max sum:" + str(x)
