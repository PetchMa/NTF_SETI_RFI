import setigen as stg
from random import seed
from random import random
from astropy import units as u
import numpy as np

class Simulated(object):

    def __init__(self):
        self.name = "Simulated"

    def draw(self, frame, seed, drift = 0.5,noise_toggle = False):
        if noise_toggle:
            noise = frame.add_noise(x_mean=5, x_std=2, x_min=0)
        frame.add_signal(stg.constant_path(f_start=frame.get_frequency(seed),
                                            drift_rate=drift*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        return frame


    def draw_2(self, fchans, tchans):
        random_num = int(random()*fchans/2)
        random_num_2 = int(random()*fchans/2)

        frame = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz)
        frame  = self.draw(frame = frame, seed= random_num, drift=0.5, noise=True)
        frame  = self.draw(frame = frame, seed = random_num_2, drift=0.1, noise=False)


        unique = int(random()*fchans/2)
        driftrate_unique = int(random()*2)-1
        frame = self.draw(frame = frame, seed=unique, drift=driftrate_unique, noise=False)
  
        frame2 = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz)
        frame2  = self.draw(frame = frame, seed= random_num, drift=0.5, noise=True)
        frame2  = self.draw(frame = frame, seed = random_num_2, drift=0.1, noise=False)

        unique = int(random()*fchans/2)
        driftrate_unique = int(random()*2)-1
        frame2 = self.draw(frame = frame, seed=unique, drift=driftrate_unique, noise=False)
            

        return frame.get_data(),frame2.get_data()
    

    def draw_n(self, tchans, fchans, same, diff):
        random_set = np.random.uniform((same)) *fchans/2
        unique_set = np.random.uniform((diff)) *fchans/2
        
        frame = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz) 
        for i in range (same):
           frame = self.draw(frame=frame, seed=random_set[i], drift=0.5, noise_toggle=False) 
        for t in range (diff):
           frame = self.draw(frame=frame, seed=unique_set[i], drift=0.5, noise_toggle=False) 
       
        frame2 = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz)
        unique_set = np.random.uniform((diff))*fchans/2 
        for k in range (same):
           frame2 = self.draw(frame=frame2, seed=random_set[k], drift=0.5, noise_toggle=False) 
        for h in range (diff):
            frame2 = self.draw(frame=frame2, seed=unique_set[h], drift=0.5, noise_toggle=False) 
        return frame.get_data(), frame2.get_data() 
