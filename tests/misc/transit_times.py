"""Test calculating transit times for location on Earth."""
import numpy as np
import matplotlib.pyplot as plt
import os

from tests.convenience import plot_aa_style, rel_path

TEST_TRANSIT = True

# Change working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def calc_transit_time(lat, dec, unit='deg', beamsize=20626.5):
    """Calculate total time of an object above horizon.

    Args:
        lat (float): Latitude of observatory in radians.
        dec (array): Declination of celestial object in radians.
        unit (str): 'deg' or 'rad'
        beamsize (float): Beam size in sq. deg

    Returns:
        float: Fraction of time above horizon in fractional days

    """
    if unit == 'deg':
        lat = np.deg2rad(lat)
        dec = np.deg2rad(dec)

    times = np.ones_like(dec)
    lim = np.pi/2. - lat
    always_visible = dec > lim
    never_visible = dec < -lim
    sometimes_visible = ((dec > -lim) & (dec < lim))

    sm = sometimes_visible
    times[sm] = 2*np.rad2deg(np.arccos(-np.tan(dec[sm])*np.tan(lat)))/360.

    times[always_visible] = 1.
    times[never_visible] = 0.

    return times


if TEST_TRANSIT:
    plot_aa_style()
    latitude_obs = 52.  # deg
    decs = np.linspace(-90, 90, 100)
    lat = latitude_obs
    times = calc_transit_time(lat, decs)
    plt.ylabel('Fraction of day at which visible')
    plt.xlabel('Declination sources')
    plt.plot(decs, times)
    plt.tight_layout()
    plt.savefig(rel_path('./plots/transit_times.pdf'))


def gen_times(n):
    """Generate n times (ms) for full day."""
    return np.array([0, 0.25, 0.75]).astype(np.float32)
