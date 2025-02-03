import requests
import json
import base64

wp_site = "http://wordpress_container:80"
wp_user = "ahmetuman"
wp_password = "123698745asd"

auth_string = f"{wp_user}:{wp_password}"
auth_encoded = base64.b64encode(auth_string.encode()).decode()

post_id = 1 

response = requests.post(
    f"{wp_site}/wp-json/wp/v2/posts/{post_id}",
    auth=(wp_user, wp_password),
    json={
        "title": "Güncellenmiş Blog Başlığı",
        "content": "Bu içerik, otomatik olarak Python betiğiyle değiştirildi."
    }
)

if response.status_code == 200:
    print("Blog yazısı başarıyla güncellendi.")
else:
    print(f"Bir hata oluştu: {response.status_code}")
