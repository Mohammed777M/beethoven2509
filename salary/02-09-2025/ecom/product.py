# id,name,description,category,tags,stock,price
class Product:
    def __init__(self,id,name,description,category,tags,stock,price):
        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.tags=tags
        self.stock=stock
        self.price=price
    def __str__(self):
        return f'[id={self.id},name={self.name},description={self.description},category={self.category},tags={self.tags},stock={self.stock},price={self.price}]'
    
    def __repr__(self):
        return self.__str__()
   
mobile_oneplus=Product(1001,'Oneplus 13','Good camera quality','Mobile','Electronics',10,2000)
print(mobile_oneplus)

mobile_Samsung=Product(1002,description='Good camera',name='samsung s24 ultra',category='mobile',tags='electronics',stock=10,price=100000)
print(mobile_Samsung)