#!/bin/bash

# 1. Girdi Kontrolü
if [ $# -ne 1 ]; then
    echo "Hata: Lütfen bir URL listesi dosyası belirtin."
    echo "Kullanım: $0 "
    exit 1
fi

DOSYA="$1"

if [ ! -f "$DOSYA" ]; then
    echo "Hata: '$DOSYA' dosyası bulunamadı!"
    exit 1
fi

# 2. Raporlama Hazırlığı
ZAMAN=$(date +%F_%H-%M)
LOG_DOSYASI="health_check_${ZAMAN}.log"

echo "------------------------------------------" | tee -a "$LOG_DOSYASI"
echo "Sağlık Kontrolü Başlatıldı: $(date)" | tee -a "$LOG_DOSYASI"
echo "------------------------------------------" | tee -a "$LOG_DOSYASI"

# 3. Dosyadan Okuma ve Kontrol Döngüsü
while read -r url || [ -n "$url" ]; do
    # Boş satırları atla
    [ -z "$url" ] && continue

    # HTTP İstegi ve Kod Alma
    kod=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$url")

    # Koşul Kontrolü ve Loglama
    if [ "$kod" -eq 200 ]; then
        echo "[ OK ] HTTP $kod - $url" | tee -a "$LOG_DOSYASI"
    else
        echo "[ERR] HTTP $kod - $url" | tee -a "$LOG_DOSYASI"
    fi
done < "$DOSYA"

echo "------------------------------------------" | tee -a "$LOG_DOSYASI"
echo "Rapor oluşturuldu: $LOG_DOSYASI"


