def conf_password(s: str):
    return hex(abs(hash(s)))


def check_user_agent(r):
    if 'XMessenger' == r.form.get('User-Agent'):
        return
    if 'XMessenger' == r.args.get('User-Agent'):
        return
    raise ValueError('User-Agent error')
