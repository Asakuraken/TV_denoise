import re
import pandas as pd


log_file = 'log.txt'

with open(log_file, 'r') as f:
    log = f.readlines()

snr_pattern = re.compile(r'SNR Before: ([\d.]+), After: ([\d.]+)')
psnr_pattern = re.compile(r'PSNR Before: ([\d.]+), After: ([\d.]+)')

snr_before, snr_after, psnr_before, psnr_after = [], [], [], []

for line in log:
    snr_match = snr_pattern.search(line)
    psnr_match = psnr_pattern.search(line)
    if snr_match:
        snr_before.append(float(snr_match.group(1)))
        snr_after.append(float(snr_match.group(2)))
    if psnr_match:
        psnr_before.append(float(psnr_match.group(1)))
        psnr_after.append(float(psnr_match.group(2)))

snr_before_avg = sum(snr_before) / len(snr_before)
snr_after_avg = sum(snr_after) / len(snr_after)
psnr_before_avg = sum(psnr_before) / len(psnr_before)
psnr_after_avg = sum(psnr_after) / len(psnr_after)

print(f"SNR Before: {snr_before_avg:.4f}, After: {snr_after_avg:.4f}")
print(f"PSNR Before: {psnr_before_avg:.4f}, After: {psnr_after_avg:.4f}")

