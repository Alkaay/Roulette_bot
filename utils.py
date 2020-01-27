def thread_rolling():
    from threading import Thread
    from rolling import roll
    roll_thread = Thread(target=roll, args=(10,))
    roll_thread.start()
    print('Rolling started')

