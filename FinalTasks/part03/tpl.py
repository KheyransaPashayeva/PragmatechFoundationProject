# Tələblər
# addToTuple metodunun vəzifəsi tpl strukturunun içinə yeni bir element əlavə edilə bilməsini təmin etməkdir
# Metod icra olunduğu zaman nəticə olaraq yeni element əlavə edilmiş formada ekranda çap olunmalıdır.
tpl=(23,45,12,67)
my_list = list(tpl) #tuple liste cevirdim uzerine add etmek ucun
eded =int(input("tpl-a istediyiniz deyeri elave edin: "))
def addToTuple(element):
    my_list.append(element)
    tpl = tuple(my_list)  # neticede yene tuple olaraq capa verdim
    print(tpl)
    pass
addToTuple(eded)