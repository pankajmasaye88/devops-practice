#list multiple values of differnt type  
list_of_cloud = ["aws", "azure", "gcp", "digital ocean", "utho", "alibaba cloud", "oracle"]

print(list_of_cloud)


#add a new cloud Salerforce
list_of_cloud.append("Salerforce")

#add a new cloud Salerforce
list_of_cloud.append("IBM cloud")
print(list_of_cloud)

#insert at location
list_of_cloud.insert(2, "Heroku")
print(list_of_cloud)


print("Number of clouds : ", len(list_of_cloud))

list_of_cloud.insert(0, "Hello Cloud : ")
print(list_of_cloud)

#for loop - iteration of list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)


for i in range(1,11):
    print(i)

for i in range(0,3):
    print("Hello Dosto")