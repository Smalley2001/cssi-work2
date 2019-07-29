# class Car(object):
#     def __init__(self,model,make):
#         self.carMake = make
#         self.carModel = model
#
#     def printCarInfo(self):
#         print(self.carMake + " " + self.carModel)
#
#
#
# car1 = Car("ford", "mustang")
# print(car1.carMake)



from google.appengine.ext import ndb

class Car(ndb.Model):
    carMake = ndb.StringProperty(required=True)
    carModel= ndb.StringProperty(required=True)

    def printCarInfo(self):
        print(self.carMake + " " + self.carModel)

car1 = Car(carMake= "ford", carModel= "mustang")
car2 = Car(carMake= "toyota", carModel= "prius")
car1.printCarInfo()
car1.put()
car2.printCarInfo()
car2.put()
