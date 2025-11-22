# VERTIGO_GAMES_DATA_ANALYST-CASE-2



Bu analizde bana verilen günlük kullanıcı aktivitelerinin yer aldığı dataset’i kullanarak oyuncu davranışlarını daha iyi anlamaya çalıştım. İlk olarak, kullanıcıların oyunu yükledikleri ilk gün nasıl davrandıklarını inceleyerek bir “first-day engagement” segmentasyonu oluşturdum. Bunun için oturum sayısı, toplam oyun süresi, maç başlangıcı/bitirimi, kazanma oranı ve ilk gün üretilen gelir gibi metrikleri birleştirip her kullanıcıya ait davranış profilini çıkardım. Ardından bu profilleri K-Means kümeleme yöntemine sokarak kullanıcıları düşük, orta ve yüksek etkileşimli olmak üzere üç ana gruba ayırdım. Bu segmentler, kullanıcıların oyuna ne kadar hızlı adapte olduklarını anlamayı ve yüksek potansiyelli oyuncuları erken aşamada tespit etmeyi sağladı.

Segmentasyonun ardından, oyuncu aktivitesinin zaman içindeki değişimini inceleyebilmek için günlük ve “days-since-install” bazında ortalama oturum süresi eğilimlerine baktım. Bu analizde amaç, oyuncular oyunda daha fazla zaman geçirdikçe oturum sürelerinin uzayıp uzamadığını veya oyundan sıkılıp daha kısa sürelerle oynayıp oynamadıklarını görmekti. Ayrıca retention oranlarını, monetization dağılımını (IAP & Ad Revenue), payer vs non-payer davranış farklarını ve ülke bazlı performansı inceleyerek dataset üzerinde daha geniş kapsamlı bir davranış analizi yaptım.

Son olarak, kullanıcı yaşam döngüsüne (lifecycle) göre session davranışlarını inceledim; böylece yeni oyuncularla uzun süredir oyunda olan oyuncular arasındaki kalıplar ortaya çıkarıldı. Bu analiz, oyunun uzun vadeli bağlılığı nasıl etkilediğini görmeme yardımcı oldu.


# Kritik noktalar 


1 . Kodun vermiş olduğu default output   analiz summary olarak dosyalandı ve konuldu 




<img width="4165" height="2963" alt="first_day_metrics_comparison" src="https://github.com/user-attachments/assets/2e0d4f5a-d85b-45b3-a1e3-0fc1253a7b8d" />
<img width="2754" height="1898" alt="first_day_revenue_analysis" src="https://github.com/user-attachments/assets/8806ec7d-e94e-4737-a822-5112845eb422" />
<img width="1841" height="1513" alt="first_day_segment_distribution" src="https://github.com/user-attachments/assets/e2e35a76-6c64-48b1-9b52-35554ecc86b7" />
<img width="4165" height="1762" alt="gameplay_behavior" src="https://github.com/user-attachments/assets/2c7b1643-f7d6-4316-a838-15cb2cf2ce6e" />
<img width="4167" height="1765" alt="geographic_analysis" src="https://github.com/user-attachments/assets/14eff28b-ce8a-448e-8b7f-a11015449eaf" />
<img width="4161" height="2963" alt="monetization_analysis" src="https://github.com/user-attachments/assets/51a2804b-c3ac-406e-a7b2-eaf2037d1732" />
<img width="4162" height="1762" alt="session_duration_and_count_trends" src="https://github.com/user-attachments/assets/eea77e8e-ade7-4cfc-b63c-48d960be6ba4" />
<img width="4167" height="1764" alt="session_duration_by_days_since_install" src="https://github.com/user-attachments/assets/05ef8679-43a9-46b1-a822-b5759401c17a" />
<img width="3566" height="1764" alt="session_duration_by_lifecycle" src="https://github.com/user-attachments/assets/c8e6900f-e282-451f-a27f-fd2e06d8124e" />
<img width="4167" height="1763" alt="session_duration_daily_trend" src="https://github.com/user-attachments/assets/dcdbb769-322f-4718-8014-d05a0a5d1ba4" />
<img width="4167" height="1764" alt="user_retention" src="https://github.com/user-attachments/assets/2cdc462a-b034-4e5e-a668-6c92ff50aa85" />
