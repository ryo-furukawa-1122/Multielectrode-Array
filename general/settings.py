class Settings():
    def set_basic_params(self):
        """Return the basic parameters"""
        self.FS:int = 20e3
        self.CHS:int = 64
        self.DURATION:int = 100e-3  # in s
        self.STIM_TIMING:int = 50e-3  # in s
        self.TRIALS:int = 20

        return self.FS, self.CHS, self.DURATION, self.STIM_TIMING, self.TRIALS