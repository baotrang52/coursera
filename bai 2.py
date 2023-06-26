print("Nhap vao 2 so a,b: ")
a= int(input())
b= int(input())
count = 0
for i in range (a,b+1,1):
    if i%3 == 0 and i%10==3: 
        count += 1
print(count)




