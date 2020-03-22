def basediez (num,bor,bde) :
	dec=0
	c = 1
	pl = 1
	dig = 0
	while num > 0 :
		residuo = num % 10
		num = num // 10
		dig = dig + 1
		c = pl * residuo
		pl = pl * bor
		dec = dec + c
	else :
		return(dec)
def basex (num,bor,bde) :
	num2 = 0 
	i = 0
	while num > 1 :
		r = num % bde
		num2 = num2+10**i*r
		i = i + 1
		num = num // bde
	else :
		res = num2+10**i*num
		return (res)
print("Ingrese el numero que desea convertir a otra base: " )
num=int(input())
print("En cual base esta el numero que desea converir: " ) 
bor=int(input())
print("A cual base desea convertir el numero: " ) 
bde=int(input())
if bor != 1 and bde != 1 :
	result = basediez(num,bor,bde)
	result1 = basex (result,bor,bde)
	print ( "El numero convertido a base " , bde , " es: " , result1 ) 