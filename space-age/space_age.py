class SpaceAge(object):
    EARTH = "earth"
    MERCURY = "mercury"
    VENUS = "venus"
    MARS = "mars"
    JUPITER = "jupiter"
    SATURN = "saturn"
    URANUS = "uranus"
    NEPTUNE = "neptune"

    def __init__(self, seconds):
        self.seconds = seconds

    def convert(self, on_planet):
        earth_year = 365.25 * 24 * 60 * 60

        conversion_factor = {
            self.EARTH: 1,
            self.MERCURY: 0.2408467,
            self.VENUS: 0.61519726,
            self.MARS: 1.8808158,
            self.JUPITER: 11.862615,
            self.SATURN: 29.447498,
            self.URANUS: 84.016846,
            self.NEPTUNE: 164.79132
        }

        planet_year = conversion_factor[on_planet] * earth_year
        return round(self.seconds / planet_year, 2)

    def on_earth(self):
        return self.convert(self.EARTH)

    def on_mercury(self):
        return self.convert(self.MERCURY)

    def on_venus(self):
        return self.convert(self.VENUS)

    def on_mars(self):
        return self.convert(self.MARS)

    def on_jupiter(self):
        return self.convert(self.JUPITER)

    def on_saturn(self):
        return self.convert(self.SATURN)

    def on_uranus(self):
        return self.convert(self.URANUS)

    def on_neptune(self):
        return self.convert(self.NEPTUNE)