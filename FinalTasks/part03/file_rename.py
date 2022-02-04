import os
movcud_fayl= input('komputerimizde movcud olan fayl adini daxil edin: ')
new_fayl = input('deyismek istediyiiz yeni fayl adini daxil edin: ')
if os.path.exists(movcud_fayl):
  os.rename(movcud_fayl, new_fayl)