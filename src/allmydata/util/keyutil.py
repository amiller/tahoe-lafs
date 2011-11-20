from pycryptopp.publickey import ed25519

BadSignatureError = ed25519.BadSignatureError

# in base32, keys are 52 chars long (both signing and verifying keys)
# in base62, keys is 43 chars long
# in base64, keys is 43 chars long
#
# We can't use base64 because we want to reserve punctuation and preserve
# cut-and-pasteability. The base62 encoding is shorter than the base32 form,
# but the minor usability improvement is not worth the documentation and
# specification confusion of using a non-standard encoding. So we stick with
# base32.

def make_keypair():
    sk, vk = ed25519.create_keypair()
    return (sk.to_ascii(prefix="priv-v0-", encoding="base32"),
            vk.to_ascii(prefix="pub-v0-", encoding="base32"))

def parse_privkey(privkey_vs):
    sk = ed25519.SigningKey(privkey_vs, prefix="priv-v0-", encoding="base32")
    vk = sk.get_verifying_key()
    return (sk, vk.to_ascii(prefix="pub-v0-", encoding="base32"))

def parse_pubkey(pubkey_vs):
    return ed25519.VerifyingKey(pubkey_vs, prefix="pub-v0-", encoding="base32")
