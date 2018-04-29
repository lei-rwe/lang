class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        import pdb; pdb.set_trace()
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass