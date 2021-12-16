def conf_password(s: str):
    return hex(abs(hash(s)))


async def check_user_agent(r):
    if r.form.get('User-Agent') != 'XMessenger':
        raise Exception('User-Agent error')
