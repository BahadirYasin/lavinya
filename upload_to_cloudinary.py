import os
import cloudinary
import cloudinary.uploader
from pathlib import Path

# Cloudinary configuration
cloudinary.config(
    cloud_name='your-cloud-name',  # Cloudinary cloud name'inizi buraya yazın
    api_key='your-api-key',        # Cloudinary API key'inizi buraya yazın
    api_secret='your-api-secret'   # Cloudinary API secret'ınızı buraya yazın
)

def upload_media_files():
    """Mevcut media dosyalarını Cloudinary'ye yükler"""
    media_dir = Path('media')
    
    if not media_dir.exists():
        print("Media klasörü bulunamadı!")
        return
    
    for root, dirs, files in os.walk(media_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, 'media')
                
                print(f"Yükleniyor: {relative_path}")
                
                try:
                    result = cloudinary.uploader.upload(
                        file_path,
                        public_id=f"lavinya/{relative_path.replace('/', '_').replace('.', '_')}",
                        resource_type="image"
                    )
                    print(f"✅ Başarılı: {result['secure_url']}")
                except Exception as e:
                    print(f"❌ Hata: {file} - {str(e)}")

if __name__ == "__main__":
    print("Media dosyaları Cloudinary'ye yükleniyor...")
    upload_media_files()
    print("Tamamlandı!") 