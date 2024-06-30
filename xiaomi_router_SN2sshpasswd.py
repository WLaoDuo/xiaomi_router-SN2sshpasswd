import hashlib
import sys

salt = {
    'r1d': 'A2E371B0-B34B-48A5-8C40-A7133F3B5D88',
    'others': 'd44fb0960aa0-a5e6-4a30-250f-6d2df50a'
}

def get_salt(sn):
    if '/' in sn:
        return swap_salt(salt['others'])
    else:
        return salt['r1d']

def swap_salt(s):
    return '-'.join(reversed(s.split('-')))

def get_passwd(sn):
    md5 = hashlib.md5((sn + get_salt(sn)).encode())
    # md5.update((sn + get_salt(sn)).encode())
    return md5.hexdigest()[:8]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} SN")
        sys.exit(1)

    SN = sys.argv[1]
    passwd = get_passwd(SN)
    print(f"decrypt password: {passwd}")
