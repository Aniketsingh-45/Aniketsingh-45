import re
import urllib.request
import ssl
import sys
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all image sources and markdown links
    src_urls = re.findall(r'src=["\'](https?://[^"\']+)["\']', content)
    md_img_urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', content)
    md_link_urls = re.findall(r'(?<!!)\[.*?\]\((https?://[^\)]+)\)', content)

    all_urls = sorted(set(src_urls + md_img_urls + md_link_urls))
    print(f'Checking {len(all_urls)} unique URLs in README.md...\n', flush=True)

    broken = []
    success = 0

    for url in all_urls:
        status_ok = False
        err_msg = ""
        
        # Up to 2 attempts
        for attempt in range(2):
            try:
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
                )
                res = urllib.request.urlopen(req, context=ctx, timeout=6)
                if res.status < 400 or res.status == 999: # 999 is LinkedIn's anti-bot code
                    status_ok = True
                    break
                else:
                    err_msg = f'HTTP {res.status}'
            except urllib.error.HTTPError as e:
                if e.code == 999: # LinkedIn anti-bot
                    status_ok = True
                    break
                err_msg = f'HTTP {e.code}'
            except Exception as e:
                err_msg = str(e)
                time.sleep(0.5)

        if status_ok:
            success += 1
            print(f'[OK] {url[:70]}', flush=True)
        else:
            broken.append((url, err_msg))
            print(f'[FAIL] {url[:70]} -> {err_msg}', flush=True)

    print(f'\nFinished: {success} OK, {len(broken)} failed.', flush=True)
    if broken:
        print('\nBroken URLs:', flush=True)
        for u, err in broken:
            print(f' - {u} ({err})', flush=True)
        sys.exit(1)
    else:
        print('\nAll URLs in README.md are active and valid!', flush=True)
except Exception as e:
    print('Script Error:', e, flush=True)
    sys.exit(1)
