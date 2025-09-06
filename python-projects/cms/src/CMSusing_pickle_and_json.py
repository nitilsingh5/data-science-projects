import pickle
import json

# Buisness Logic Layer
class Customer:
  cus_list=[]

  def __init__(self):
    self.id=''
    self.name=''
    self.age=''
    self.mob=''

  def addCustomer(self):
    Customer.cus_list.append(self)
  
  def searchCustomer(self):
    for cus in Customer.cus_list:
      if cus.id==self.id:
        self.id=cus.id
        self.name=cus.name
        self.age=cus.age
        self.mob=cus.mob
        return
  
  def deleteCustomer(self):
    for cus in Customer.cus_list:
      if cus.id==self.id:
        Customer.cus_list.remove(cus)
        return
  
  def modifyCustomer(self):
    for cus in Customer.cus_list:
      if cus.id==self.id:
        cus.name=self.name
        cus.age=self.age
        cus.mob=self.mob
        return

  @staticmethod
  def saveToPickle():
    f=open(r"C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\pickle.txt",'wb')
    pickle.dump(Customer.cus_list,f)
    f.close()

  @staticmethod
  def loadFromPickle():
    f=open(r"C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\pickle.txt",'rb')
    Customer.cus_list=pickle.load(f)
    f.close()
  
  @staticmethod
  def sort_criteria(cus):
    return cus.id 
  @staticmethod
  def sortID():
    Customer.cus_list.sort(key=Customer.sort_criteria)

  @staticmethod
  def convToDict(cus):
    return cus.__dict__
  @staticmethod
  def saveToJson():
    f=open(r"C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\json.txt",'w')
    json.dump(Customer.cus_list,f,default=Customer.convToDict)
    f.close()
  
  @staticmethod
  def convToObject(d):
    cus=Customer()
    cus.id=d['id']
    cus.name=d['name']
    cus.age=d['age']
    cus.mob=d['mob']
    return cus
  @staticmethod
  def loadFromJson():
    f=open(r"C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\json.txt",'r')
    Customer.cus_list=json.load(f,object_hook=Customer.convToObject)



# Presentation Layer
if (__name__)==('__main__'):
  print('Welcome to CMS')

  def getID():
    while(1):
      id=input('Enter Customer ID: ')
      if id.isdecimal():
        if not any(cus.id==id for cus in Customer.cus_list):
          return id
        else:
          print('duplicate id please enter unique id')
      else:
        print('please enter id  only in digits')
    
  def getAge():
    while(1):
      age=input('Enter Customer age: ')
      if age.isdecimal():
        if int(age)>=10 and int(age)<=60:
          return age
        else:
          print('please enter age between 10 and 60')
      else:
        print('Please Enter age only in digits')

  def getMob():
    while(1):
      mob=input('Enter Customer Mob: ')
      if mob.isdecimal():
        if len(mob)==10:
          return mob
        else:
          print('Please Enter mob in 10 digits')
      else:
        print('Please enter mob only in digits')

  def showCust(cus):
    print('Cus ID:',cus.id,'Cus Name:',cus.name,'Cus Age:',cus.age,'Cus Mob:',cus.mob)

  while(1):
    ch=input('Enter choice: 1. add customer 2. search customer 3. delete customer 4. modify customer 5. display all customers 6. save to picle 7. load from pickle  8. sort 9.save to json 10.load from json 11.exit: ')
    if ch=='1':
      cus=Customer()
      cus.id=getID()
      cus.name=input('Enter Customer Name: ')
      cus.age=getAge()
      cus.mob=getMob()
      cus.addCustomer()
      print('Customer Added')

    elif ch=='2':
      cus=Customer()
      cus.id=input('Enter Customer ID to Search: ')
      cus.searchCustomer()
      showCust(cus)
    
    elif ch=='3':
      cus=Customer()
      cus.id=input('Enter Customer ID to Delete: ')
      cus.deleteCustomer()
      print('Customer Deleted')
    
    elif ch=='4':
      cus=Customer()
      cus.id=input('Enter Customer ID to Modify: ')
      cus.name=input('Enter Customer Name: ')
      cus.age=getAge()
      cus.mob=getMob()
      cus.modifyCustomer()
      print('Customer Modified')
    
    elif ch=='5':
      for cus in Customer.cus_list:
        showCust(cus)

    elif ch=='6':
      Customer.saveToPickle()
      print('Saved in pickle')

    elif ch=='7':
      Customer.loadFromPickle()
      print('Loaded from pickle')

    elif ch=='8':
      Customer.sortID()
      print('Sorted')
    
    elif ch=='9':
      Customer.saveToJson()
      print('Saved in Json')
    
    elif ch=='10':
      Customer.loadFromJson()
      print('Loaded from Json')
    
    elif ch=='11':
      print('Thank You for using CMS')
      break

    else:
      print('incorrect choice')