import setigen as stg
from random import seed
from random import random
from astropy import units as u


class Simulated(object):

    def __init__(self):
        self.name = "Simulated"
    def draw(fchans, tchans):
        random_num = int(random()*fchans/2)
        random_num_2 = int(random()*fchans/2)

        frame = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz)
        noise = frame.add_noise(x_mean=5, x_std=2, x_min=0)
        frame.add_signal(stg.constant_path(f_start=frame.get_frequency(random_num),
                                            drift_rate=0.5*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        frame.add_signal(stg.constant_path(f_start=frame.get_frequency(random_num_2),
                                            drift_rate=0.1*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        unique = int(random()*fchans/2)
        driftrate_unique = int(random()*2)-1
        frame.add_signal(stg.constant_path(f_start=frame.get_frequency(unique),
                                            drift_rate=driftrate_unique*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))


        frame2 = stg.Frame(fchans=fchans*u.pixel,
                            tchans=tchans*u.pixel,
                            df=2.7939677238464355*u.Hz,
                            dt=18.25361108*u.s,
                            fch1=6095.214842353016*u.MHz)
        noise = frame2.add_noise(x_mean=5, x_std=2, x_min=0)
        frame2.add_signal(stg.constant_path(f_start=frame2.get_frequency(random_num),
                                            drift_rate=0.5*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        frame2.add_signal(stg.constant_path(f_start=frame2.get_frequency(random_num_2),
                                            drift_rate=0.1*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        unique = int(random()*fchans/2)
        driftrate_unique = int(random()*2)
        frame2.add_signal(stg.constant_path(f_start=frame2.get_frequency(unique),
                                            drift_rate=driftrate_unique*u.Hz/u.s),
                        stg.constant_t_profile(level=30),
                        stg.gaussian_f_profile(width=20*u.Hz),
                        stg.constant_bp_profile(level=1))
        return frame.get_data(),frame2.get_data()
