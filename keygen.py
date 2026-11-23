#!/usr/bin/env python3
"""OWNER ONLY - never share this file. Usage: python3 keygen.py XXXX-XXXX-XXXX-XXXX"""
import hmac, hashlib, sys
SECRET = bytes.fromhex("7defb3f991c3ee1cc089b354419b0470c7312fe31f302270")
if len(sys.argv) != 2: sys.exit(__doc__)
d = hmac.new(SECRET, sys.argv[1].strip().upper().encode(), hashlib.sha256).hexdigest().upper()[:20]
print("-".join(d[i:i+5] for i in range(0, 20, 5)))
