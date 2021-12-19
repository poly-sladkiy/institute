from hashlib import sha256

def conf_password(s: str):
    """Convert password to sha256 hash

    Args:
        s (str): password

    Returns:
        res (str): password hash
    """
    res = sha256(s.encode()).hexdigest()
    return res


def check_user_agent(r):
    if 'XMessenger' == r.form.get('User-Agent'):
        return
    if 'XMessenger' == r.args.get('User-Agent'):
        return
    raise ValueError('User-Agent error')
