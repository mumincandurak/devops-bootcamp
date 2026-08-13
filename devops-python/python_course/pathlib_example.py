from pathlib import Path

# __file__ = bu script'in kendi dosya yolu.
# Path(__file__).parent = bu script'in içinde bulunduğu klasör.
# Neden cwd() değil de bu? Çünkü script'i hangi dizinden çalıştırırsan çalıştır
# (mesela "python python_course/pathlib_example.py" diye başka bir yerden bile
# çalıştırsan), her zaman doğru klasörü bulur.
current_dir = Path(__file__).parent

print(f"Script'in bulunduğu klasör: {current_dir.resolve()}")

# .glob(pattern) klasördeki dosyaları belirtilen desene göre listeler.
# "*.py" -> uzantısı .py olan tüm dosyalar (alt klasörlere bakmaz).
py_files = list(current_dir.glob("*.py"))
print(f"\n{len(py_files)} adet .py dosyası bulundu:")
for f in py_files:
    # .name -> sadece dosya adı (klasör yolu olmadan)
    # .stem -> uzantısız dosya adı
    # .suffix -> sadece uzantı (.py)
    print(f"  - {f.name} (isim: {f.stem}, uzantı: {f.suffix})")

# .xlsx dosyalarını da bulalım
excel_files = list(current_dir.glob("*.xlsx"))
print(f"\n{len(excel_files)} adet .xlsx dosyası bulundu:")
for f in excel_files:
    print(f"  - {f.name}")

# / operatörü ile path birleştirme
env_path = current_dir / ".env"

# .exists() -> dosya/klasör var mı?
# .is_file() -> varsa, bu bir dosya mı (klasör değil mi)?
if env_path.exists() and env_path.is_file():
    print(f"\n{env_path.name} dosyası mevcut.")
else:
    print(f"\n{env_path.name} dosyası bulunamadı.")

# Yeni bir klasör oluşturma örneği (varsa hata vermesin diye exist_ok=True)
output_dir = current_dir / "pathlib_output"
output_dir.mkdir(exist_ok=True)
print(f"\n'{output_dir.name}' klasörü hazır: {output_dir.resolve()}")