"""Short example of how frbpoppy works.

The first time you run frbpoppy, a series of cosmological databases will be
constructed to set up subsequent runs. This first run can take ~2h on a 4 core
machine. Subsequent runs will take mere seconds.
"""
from frbpoppy import CosmicPopulation, Survey, SurveyPopulation, plot

# Set up an FRB population of one-offs
cosmic_pop = CosmicPopulation.default(1e5, n_days=0.23)

# Generate your FRB population
cosmic_pop.generate()

# Setup a survey
survey = Survey('htru')
survey.set_beam(model='gaussian', n_sidelobes=0.5)

# Observe the FRB population
survey_pop = SurveyPopulation(cosmic_pop, survey)

# Check the detection rates
print(survey_pop.source_rate)

# Plot populations in a browser
plot(cosmic_pop, survey_pop, frbcat='parkes')
