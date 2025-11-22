# VERTIGO_GAMES_DATA_ANALYST-CASE-2



Bu analizde bana verilen günlük kullanıcı aktivitelerinin yer aldığı dataset’i kullanarak oyuncu davranışlarını daha iyi anlamaya çalıştım. İlk olarak, kullanıcıların oyunu yükledikleri ilk gün nasıl davrandıklarını inceleyerek bir “first-day engagement” segmentasyonu oluşturdum. Bunun için oturum sayısı, toplam oyun süresi, maç başlangıcı/bitirimi, kazanma oranı ve ilk gün üretilen gelir gibi metrikleri birleştirip her kullanıcıya ait davranış profilini çıkardım. Ardından bu profilleri K-Means kümeleme yöntemine sokarak kullanıcıları düşük, orta ve yüksek etkileşimli olmak üzere üç ana gruba ayırdım. Bu segmentler, kullanıcıların oyuna ne kadar hızlı adapte olduklarını anlamayı ve yüksek potansiyelli oyuncuları erken aşamada tespit etmeyi sağladı.

Segmentasyonun ardından, oyuncu aktivitesinin zaman içindeki değişimini inceleyebilmek için günlük ve “days-since-install” bazında ortalama oturum süresi eğilimlerine baktım. Bu analizde amaç, oyuncular oyunda daha fazla zaman geçirdikçe oturum sürelerinin uzayıp uzamadığını veya oyundan sıkılıp daha kısa sürelerle oynayıp oynamadıklarını görmekti. Ayrıca retention oranlarını, monetization dağılımını (IAP & Ad Revenue), payer vs non-payer davranış farklarını ve ülke bazlı performansı inceleyerek dataset üzerinde daha geniş kapsamlı bir davranış analizi yaptım.

Son olarak, kullanıcı yaşam döngüsüne (lifecycle) göre session davranışlarını inceledim; böylece yeni oyuncularla uzun süredir oyunda olan oyuncular arasındaki kalıplar ortaya çıkarıldı. Bu analiz, oyunun uzun vadeli bağlılığı nasıl etkilediğini görmeme yardımcı oldu.


# Kritik noktalar 


1 . Kodun vermiş olduğu default output   analiz summary olarak dosyalandı ve konuldu 


2.  Tekrardan oluşturulan analiz görselleri output files olarak yüklendi 

