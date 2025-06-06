# commands/quit.py
def handle(bot, msg, args, admin_cmd):
    """
    Quit the bot: .quit <reason>
    """
    reason = ' '.join(args) if args else "Bye!"
    target = msg.params[0] if msg.params[0].startswith('#') else msg.prefix.nick
    if admin_cmd:
        for admin_nick in bot.config.admi:
            if admin_nick in msg.prefix.nick:
                bot.send("PRIVMSG", target, f":{msg.prefix.nick} I'm quitting: {reason}")
                bot.send("QUIT", reason)
                bot.exit(0, reason)
        else:
            bot.send("PRIVMSG", target, f":{msg.prefix.nick} You are not an admin!")
            return