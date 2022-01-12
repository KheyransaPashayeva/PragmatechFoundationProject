# 1.Sual-display:flex xüsusiyyətinin əsas neçə alt xüsusiyyəti var və bunlar nə işə yarayır?
##### Cavab: Flex, xüsusilə mürəkkəb layihələrdə veb tərtibatçılarının işini asanlaşdıran, veb-saytdakı elementləri üfüqi və şaquli olaraq uyğunlaşdıran bu gün ən populyar CSS layoutlarından biridir.Flex xüsusiyyətləri: justify-content,align-items,flex-direction,flex-wrap,flex-flow,align-content,order bu kimi alt xususiyyetleri vardir.
##### -justify-content xassəsi X oxundakı elementləri, yəni üfüqi düzləşdirməyə xidmət edir. Aşağıdakı dəyərləri qəbul edə bilər:

##### flex-start: Elementləri flexbox konteynerinin sol tərəfinə uyğunlaşdırır.flex-end: Elementləri flexbox konteynerinin sağ tərəfinə düzəldir.center: Elementləri flexbox konteynerinin mərkəzinə uyğunlaşdırır.space-between : Elementlər üfüqi olaraq bərabər şəkildə yerləşdirilir.space-around: Elementlər etraflarinda eyni məsafə də ayrılır və üfiqi şəkildə düzülür.
##### -Align-items xassəsi Y oxundakı elementləri, yəni şaquli istiqamətdə sıralamağa xidmət edir. Aşağıdakı dəyərləri qəbul edə bilər:

##### flex-start: Elementləri flexbox konteynerinin yuxarı hissəsinə uyğunlaşdırır.flex-end: Flexbox konteynerinin açağı hissəsinə elementləri sıralayır.center: Elementləri flexbox konteynerinin şaquli mərkəzinə uyğunlaşdırır.baseline: Elementləri flexbox konteynerinin mətn əsas xəttinə uyğunlaşdırır.stretch: Elementlər flexbox konteyneri hündürlüyündə uzanır.
##### -Flex-direction xüsusiyyəti hansı istiqamət də elementlərinin yerləşdirildiyini müəyyən edir. Aşağıdakı dəyərləri qəbul edə bilər:row: Elementlər mətn istiqaməti ilə eyni istiqamətdə yerləşdirilir.row-revese: elementlər mətnin əks istiqamətində yerləşdirilir.column: elementlər yuxarıdan aşağıya yerləşdirilir.column-revese: elementlər aşağıdan yuxarıya yerləşdirilir.
##### -Flex-wrap xüsusiyyəti birdən çox sətirdə göstəriləcək elementlərin davranışını müəyyən etmək üçün istifadə olunur. Aşağıdakı dəyərləri qəbul edə bilər:nowrap: Bütün elementlər bir sətir də düzülür.wrap: Elementlər sətirlərə bölünür.wrap-reverse: Elementlər tərs qaydada sətirlərə bölünür.\
##### -flex-flow Xüsusiyyəti:Flex-direction və flex-wrap qaydaları flex-flow qısa sintaksis qaydası ilə birlikdə yazıla bilər. Bu qısa sintaksis qaydası iki qaydanın dəyərlərini aralarında boşluq olmaqla götürür. Bu qısa sintaksis qaydası iki qaydanın dəyərlərini aralarında boşluq olmaqla götürür.
##### -Align-content qaydası ilə sətirləri ayıra bilərsiniz. Bu qayda aşağıdakı dəyərləri alır:flex-start: Sıralar flex konteynerin yuxarı hissəsində toplanır.flex-end: Sıralar flex konteynerin altında toplanır.center: Sıralar flex konteynerin şaquli mərkəzində toplanır.space-between: Sıralar aralarında bərabər məsafə ilə düzülür.space-around: Sıralar onların ətrafında bərabər şəkildə düzülür.stretch: Sıralar  flex container’ı  olcusunu tutmaq üçün uzanır.
##### -Oder Xüsusiyyəti:Bəzən row ya da column yerləşdirməsini tərsinə çevirmək kifayət etmir. Belə hallarda sifariş qaydası ilə əşyaları bir-bir sıralaya bilərik. Elementlərin ilkin sıra dəyəri 0-dır, lakin biz bu dəyəri müsbət və ya mənfi qiymətə təyin edə bilərik.
# 2.display:grid xüsusiyyətinin alt xüsusiyyətləri hansılardır və qısaca nə işə yaradığını yazın?
##### Cavab:grid-template-rows, grid-template-columns, grid-template-areas, grid-auto-rows, grid-auto-columns, and the grid-auto-flow kimi alt xususiyyetleri vardir.Grid-template-areas adlandırılmış grid elementlərindən istifadə edərək sütun və sətirlərin necə göstəriləcəyini müəyyən edir,grid-template-rows şəbəkə düzümündə cərgələrin ölçüsünü müəyyən edir,grid-template-columns sütunların ölçüsünü və şəbəkə tərtibatında neçə sütun olduğunu müəyyən edir
# 3.sizə görə flex və grid layout arasında ən əhəmiyyətli fərqlər hansılardır?
##### Cavab:flexbox bir ölçülü, CSS Grid isə iki ölçülüdür. Flexbox elementləri ya üfüqi, ya da şaquli ox boyunca yerləşdirir, ona görə də siz sıra əsaslı və ya sütun əsaslı düzüm istəməyinizə qərar verməlisiniz.Əgər siz layout daxilində elementlərin mövqeyini dəqiq idarə etmək istəyirsinizsə, CSS Grid istifadə etməlisiz.flex de bir elementin olcusunu deyisdikde digerinde serbest sekilde olur,gridde ise olculer avtomatik sekilde grid terefinden duxelir.
# display:inline-block,display:flex və display:grid xüsusiyyətlər hansı hallarda istifadə olunmalıdı və səbəbləri nələrdir?

# UL-lesson11 tapsiriq suallari
### display:inline və display:inline-block arasında fərqlər nədir?
##### inline elementler olculenmirler yeni width ve height deyerlerin almir ve olduqlari yeri tuturlar butun setiri tutmur.inline-block verildikde olcu vrmek mumkun olur ve yene de setir boyu deyil sadece oz heciminde yer tutur.
### semantik veb nə deməkdir izah edin
##### 
  