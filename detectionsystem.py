MIN_BILYE=10
MAX_AGIRLIGIFARKLI_BILYESAYISI=1
MIN_AGIRLIGIFARKLI_BILYESAYISI=0
MIN_AGIRLIK_SINIRI=1
agirlik=0
hatasiz_kutu=0
uretim_hatasi=0
ikinci_bilye_agirlik=0
onceki_bilyeagirlik=0
agirligifarkli_bilyesayisi=0
kabul_edilen_bilye=0
iade_bilye=0
tumbilyeler_esitkutu=0
birbilye_dahaagir_kutu=0
birbilye_dahahafif_kutu=0
dahaagir_bilye=0
dahahafif_bilye=0
birbilye_dahaagir_kutu_agirlikfarktoplami=0
birbilye_dahahafif_kutu_agirlikfarktoplami=0
birbilye_dahaagir_kutu_agirlikfarkyuzdesi=0
birbilye_dahahafif_kutu_agirlikfarkyuzdesi=0
tumbilyeesitkutu_max_bilye=0
tumbilyeesitkutu_birbilyeagirlik=0
tumbilyeesitkutu_maxagirlik_birbilye=0
tumbilyeesitkutu_maxagirlikkutu_bilyesayisi=0
max_agirlik_farki=0
max_agirlik_farkiyuzdesi=0
max_agirlik_farkiisareti=""
min_fark_yuzde_farkisareti=""
min_fark_yuzde_farkdegeri=0
min_fark_yuzde=100
kutu_varmi='e' #0'a bölünmeme hatası için yeterli veri girişi yapılacağından dolayı ilk kutuya otomatik giriyor.
while kutu_varmi in ["e","E"]:
    bilye_sayisi=int(input("Kutu içerisindeki bilye sayısını giriniz: "))
    while bilye_sayisi<MIN_BILYE:
        print("Bilye sayısı minimum 10 olmalıdır.Lütfen tekrar giriniz!")
        bilye_sayisi=int(input("Kutu içerisindeki bilye sayısını giriniz: "))
    bilye_no=1
    agirligifarkli_bilyesayisi=0
    agirlik_farki=0
    agirlik_farki_yuzdesi=0
    birinci_bilyeagirlik=int(input("1.bilyenin ağırlığını miligram cinsinden giriniz: ")) #bazı kontrollerin sağlanması için 1.bilyenin ağırlığını farklı bir değişkene ek olarak kaydettim.
    while birinci_bilyeagirlik<MIN_AGIRLIK_SINIRI:
        print("Lütfen 0 dan büyük bir değer giriniz!")
        birinci_bilyeagirlik=int(input("1.bilyenin ağırlığını miligram cinsinden giriniz giriniz: "))
    onceki_bilyeagirlik=birinci_bilyeagirlik
    while bilye_no+1<bilye_sayisi+1:
        agirlik=int(input(f"{bilye_no+1}.bilyenin ağırlığını miligram cinsinden giriniz: "))
        if bilye_no+1==2: #bazı kontrollerin sağlanması için 2.bilyenin ağırlığını farklı bir değişkene ek olarak kaydettim.
            ikinci_bilye_agirlik=agirlik
        while agirlik<MIN_AGIRLIK_SINIRI:
           print("Lütfen bilyelerin ağırlığını pozitif bir değer girin!")
           agirlik=int(input(f"{bilye_no+1}. bilyenin ağırlığını miligram cinsinden giriniz: "))
        if birinci_bilyeagirlik>ikinci_bilye_agirlik and ikinci_bilye_agirlik==agirlik:
            agirlik_farki=birinci_bilyeagirlik-ikinci_bilye_agirlik
            agirlik_farki_yuzdesi = ((birinci_bilyeagirlik/agirlik) * 100)
            if agirlik_farki>max_agirlik_farki:
                max_agirlik_farki=agirlik_farki
                max_agirlik_farkiyuzdesi = ((agirlik_farki / agirlik)*100)
                if max_agirlik_farkiyuzdesi<0: #yuzdenin negatif çıkma durumunda çıktıda pozitif yazılması için -1 ile çarptım.
                    max_agirlik_farkiyuzdesi*=-1
                if max_agirlik_farki>0:
                    max_agirlik_farkiisareti="+"
                else:
                    max_agirlik_farkiisareti="-"
            if agirlik_farki_yuzdesi<min_fark_yuzde:
                min_fark_yuzde=agirlik_farki_yuzdesi
                min_fark_yuzde_farkdegeri=agirlik_farki
                if agirlik_farki>0:
                    min_fark_yuzde_farkisareti="+"
                else:
                    min_fark_yuzde_farkisareti="-"
            if agirlik_farki_yuzdesi<min_fark_yuzde:
                min_fark_yuzde=agirlik_farki_yuzdesi
                min_fark_yuzde_farkdegeri=agirlik_farki
                if min_fark_yuzde_farkdegeri<0:
                    min_fark_yuzde_farkisareti="+"
                else:
                    min_fark_yuzde_farkisareti="-"
        if birinci_bilyeagirlik<ikinci_bilye_agirlik and ikinci_bilye_agirlik==agirlik:
            agirlik_farki=birinci_bilyeagirlik-ikinci_bilye_agirlik
            agirlik_farki_yuzdesi = ((birinci_bilyeagirlik/ikinci_bilye_agirlik) * 100)
            if agirlik_farki>max_agirlik_farki:
                max_agirlik_farki=agirlik_farki
                max_agirlik_farkiyuzdesi = ((agirlik_farki / agirlik)*100)
                if max_agirlik_farkiyuzdesi<0: #yuzdenin negatif çıkma durumunda çıktıda pozitif yazılması için -1 ile çarptım.
                    max_agirlik_farkiyuzdesi*=-1
                if max_agirlik_farki>0:
                    max_agirlik_farkiisareti="+"
                else:
                    max_agirlik_farkiisareti="-"
            if agirlik_farki_yuzdesi<min_fark_yuzde:
                min_fark_yuzde=agirlik_farki_yuzdesi
                min_fark_yuzde_farkdegeri=agirlik_farki
                if agirlik_farki>0:
                    min_fark_yuzde_farkisareti="+"
                else:
                    min_fark_yuzde_farkisareti="-"
            if agirlik_farki_yuzdesi<min_fark_yuzde:
                min_fark_yuzde=agirlik_farki_yuzdesi
                min_fark_yuzde_farkdegeri=agirlik_farki
                if min_fark_yuzde_farkdegeri<0:
                    min_fark_yuzde_farkisareti="+"
                else:
                    min_fark_yuzde_farkisareti="-"
        if agirlik!=onceki_bilyeagirlik and agirlik!=birinci_bilyeagirlik:
            agirligifarkli_bilyesayisi+=1
            agirlik_farki = agirlik-onceki_bilyeagirlik
            agirlik_farki_yuzdesi=((agirlik/onceki_bilyeagirlik)*100)
            if agirlik_farki>max_agirlik_farki:
                max_agirlik_farki=agirlik_farki
                max_agirlik_farkiyuzdesi = ((agirlik_farki / onceki_bilyeagirlik)*100)
                if max_agirlik_farkiyuzdesi<0: #yuzdenin negatif çıkma durumunda çıktıda pozitif yazılması için -1 ile çarptım.
                    max_agirlik_farkiyuzdesi*=-1
                if max_agirlik_farki>0:
                    max_agirlik_farkiisareti="+"
                else:
                    max_agirlik_farkiisareti="-"
            if agirlik_farki_yuzdesi<min_fark_yuzde:
                min_fark_yuzde=agirlik_farki_yuzdesi
                min_fark_yuzde_farkdegeri=agirlik_farki
                if min_fark_yuzde_farkdegeri<0:
                    min_fark_yuzde_farkisareti="+"
                else:
                    min_fark_yuzde_farkisareti="-"
        if agirligifarkli_bilyesayisi>MAX_AGIRLIGIFARKLI_BILYESAYISI:
            iade_bilye+=bilye_sayisi
            uretim_hatasi+=1
            print("Bu kutuda hata var. İade edilmiştir!")
            break
        onceki_bilyeagirlik=agirlik
        bilye_no+=1
    if agirligifarkli_bilyesayisi==MIN_AGIRLIGIFARKLI_BILYESAYISI:
        tumbilyeler_esitkutu+=1
        hatasiz_kutu+=1
        kabul_edilen_bilye+=bilye_sayisi
        print("Tüm bilyeler eşit ağırlıktadır.")
        if bilye_sayisi>tumbilyeesitkutu_max_bilye:
            tumbilyeesitkutu_max_bilye=bilye_sayisi
            tumbilyeesitkutu_birbilyeagirlik=agirlik
        if agirlik>tumbilyeesitkutu_maxagirlik_birbilye:
            tumbilyeesitkutu_maxagirlik_birbilye = agirlik
            tumbilyeesitkutu_maxagirlikkutu_bilyesayisi=bilye_sayisi
    if agirligifarkli_bilyesayisi == MAX_AGIRLIGIFARKLI_BILYESAYISI:
        kabul_edilen_bilye+=bilye_sayisi
        hatasiz_kutu+=1
        if agirlik_farki>0:
                dahaagir_bilye += 1
                birbilye_dahaagir_kutu_agirlikfarktoplami += agirlik_farki
                birbilye_dahaagir_kutu_agirlikfarkyuzdesi += agirlik_farki_yuzdesi
                birbilye_dahaagir_kutu += 1
                print(f"Farklı olan bilye diğer bilyelere göre daha ağır! ve aralarındaki fark: {agirlik_farki:.2f} "
                      f"ve bu farkın yüzdesi %{agirlik_farki_yuzdesi:.2f}")
        else:
            dahahafif_bilye += 1
            birbilye_dahahafif_kutu_agirlikfarktoplami +=agirlik_farki
            birbilye_dahahafif_kutu_agirlikfarkyuzdesi += agirlik_farki_yuzdesi
            birbilye_dahahafif_kutu += 1
            print(f"Farklı olan bilye diğer bilyelere göre daha hafif! ve aralarındaki fark: { agirlik_farki:.2f} ve "  
                f"bu farkın yüzdesi %{agirlik_farki_yuzdesi:.2f}")
    kutu_varmi=input("Başka kutu var mı(e/E/h/H)?: ")
toplam_kutu=hatasiz_kutu+uretim_hatasi
uretim_hatasikutu_yuzde = (uretim_hatasi / toplam_kutu) * 100
tumbilyeleresit_kutuyuzde = (tumbilyeler_esitkutu / hatasiz_kutu) * 100
birbilye_dahaagir_kutuyuzde = (birbilye_dahaagir_kutu / hatasiz_kutu) * 100
birbilye_dahaagir_kutu_agirlikfarkort = birbilye_dahaagir_kutu_agirlikfarktoplami / dahaagir_bilye
birbilye_dahaagir_kutu_agirlikfarkyuzdeort = birbilye_dahaagir_kutu_agirlikfarkyuzdesi / dahaagir_bilye
birbilye_dahahafif_kutuyuzde = (birbilye_dahahafif_kutu / hatasiz_kutu) * 100
birbilye_dahahafif_kutu_agirlikfarkort = birbilye_dahahafif_kutu_agirlikfarktoplami / dahahafif_bilye
birbilye_dahahafif_kutu_agirlikfarkyuzdeort = birbilye_dahahafif_kutu_agirlikfarkyuzdesi / dahahafif_bilye
print(f"Üretim hatası olan kutu sayısı {uretim_hatasi:.2f} ve tüm kutular içindeki yüzdesi %{uretim_hatasikutu_yuzde:.2f}'dır.")
print(f"İade edilen toplam bilye sayısı {iade_bilye} ve kabul edilen toplam bilye sayısı {kabul_edilen_bilye}'dır.")
print(f"Tüm bilyelerin eşit olduğu kutu sayısı {tumbilyeler_esitkutu} ve bunun hatasız kutular içindeki yüzdesi %{tumbilyeleresit_kutuyuzde:.2f}\n"
      f"bir bilyenin diğerlerinden daha ağır olduğu kutu sayısı {birbilye_dahaagir_kutu} ve bunun hatasız kutular içindeki yüzdesi {birbilye_dahaagir_kutuyuzde:.2f}\n"
      f"ve bir bilyenin diğerlerinden daha hafif olduğu kutu sayısı {birbilye_dahahafif_kutu} ve bunun hatasız kutular içindeki yüzdesi {birbilye_dahahafif_kutuyuzde:.2f}")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı ortalaması {birbilye_dahaagir_kutu_agirlikfarkort:.2f}"
      f" ve ağırlık fark yüzdelerinin ortalaması {birbilye_dahaagir_kutu_agirlikfarkyuzdeort:.2f}")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı ortalaması {birbilye_dahahafif_kutu_agirlikfarkort:.2f}"
      f" ve ağırlık fark yüzdelerinin ortalaması {birbilye_dahahafif_kutu_agirlikfarkyuzdeort:.2f}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bilye sayısı {tumbilyeesitkutu_max_bilye:.2f}"
      f" ve o kutudaki bir bilyenin ağırlığı {tumbilyeesitkutu_birbilyeagirlik:.2f}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bilye sayısı {tumbilyeesitkutu_maxagirlikkutu_bilyesayisi:.2f}"
      f" ve o kutudaki bir bilyenin ağırlığı {tumbilyeesitkutu_maxagirlik_birbilye:.2f}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu aralıkta farkın değeri: {max_agirlik_farki:.2f}\n"
      f"farkın yüzdesi %{max_agirlik_farkiyuzdesi:.2f} ve bunun işareti {max_agirlik_farkiisareti}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu"
      f" ağırlık farkının değeri: {min_fark_yuzde_farkdegeri:.2f}\nfarkın yüzdesi %{min_fark_yuzde:.2f} ve bunun işareti {min_fark_yuzde_farkisareti}")
