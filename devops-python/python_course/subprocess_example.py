import subprocess
import argparse
import logging
import sys

basarisiz = []

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('--command', help='Command to run')
args = parser.parse_args()

result = subprocess.run(
    args.command.split(),
    capture_output=True,
    text=True)

logging.info("Return code: %d", result.returncode)
print("Output:")
print(result.stdout)

log = logging.getLogger(__name__)
log.info("Kontrol başladı")
log.warning("a.com yavaş: 2.3 sn")
log.error("b.com ERİŞİLEMEZ (timeout)")


if basarisiz:
    logging.error("Başarısız olan komutlar: %s", ', '.join(basarisiz))
    sys.exit(1)
else:
    logging.info("Tüm komutlar başarıyla tamamlandı.")
    sys.exit(0)