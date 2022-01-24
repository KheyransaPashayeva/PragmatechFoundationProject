# 1)Bir dənə Restoran classı yaradın. Bu classa init() metdou bu classın adını (restaurant_name) və mətbəx növü 
# (cuisine_type) adlı iki atribitunu saxlamalıdır. describe_restaurant() adlı bir metod yaradın hansı ki restoranın
# adını və mətbəxin növünü ekrana print etsin. Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa 
#bit metdi yaradın. Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını, mətbəxinin növünü, restoran
#haqqında məlumatları və açıq olmasını çapa verin. Bu Restoran classından daha iki obyek yaradın və describe_restaurant
#metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.
class Restoran:

    def __init__(self,restorant_name,cuisine_type,_open,il,unvan):
       self._restorant_name = restorant_name
       self._cuisine_type = cuisine_type
       self._open = _open
       self.il = il
       self.unvan = unvan

    def describe_restaurant(self): 
     print(f'Restoranin adi:{self._restorant_name}')
     print(f'Metbex novu :{self._cuisine_type}')
     print(f'Restoranin yaranma tarixi: {self.il}')
     print(f'Restoranin yerlesdiyi unvan: {self.unvan}')

    def open_restaurant(self):
        print(f'Restoran {self._open}')
restoran = Restoran('Papa Jons', 'Italian','Aciqdir',1956,'28 May')
restoran.describe_restaurant()
restoran.open_restaurant()