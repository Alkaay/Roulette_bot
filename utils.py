def thread_rolling(seconds, bot):
    from threading import Thread
    from rolling import roll
    roll_thread = Thread(target=roll, args=(seconds, bot))
    print('Rolling started')
    roll_thread.start()


