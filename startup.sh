#!/bin/bash

echo "Compose 1: WordPress ve MySQL"
docker-compose -f docker-compose-wordpress.yml up -d

echo "WordPress ve MySQL basladi, kontrol ediliyor..."
sleep 10  

if docker ps | grep -q "wordpress_container"; then
    echo "WordPress ve MySQL basladi."
    echo "Compose 2: SQL, NoSQL, Redis ve Python betikleri"
    docker-compose -f docker-compose-multi.yml up --build -d
else
    echo "WordPress hata."
    exit 1
fi

echo "Baslatma tamamlandi."
