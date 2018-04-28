def make(label):
    def echo(msg):
        print(label + ' : ' + msg)
    return echo

if __name__ == "__main__":
    F = make('spam')
    F('Ham')
    print(dir(F))
    import pdb; pdb.set_trace()