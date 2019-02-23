# Scrape Paul Graham Essays

## Why
The hour is late and I am before a flight. I wanted reading material for the plane
so I wrote this quick and dirty scraper for getting all of Paul Graham's essays.
This is by no means beautiful code, but it got the job done. The next idea is to make a simple android client for reading his essays, bookmarking them etc. Stay tuned...

### Text manipulations
find ./ -type f -exec sed -i '' -e 's/size="2"/size="10"/g' {} \;
find ./ -type f -exec sed -i '' -e 's/width="435"/width="100%"/g' {} \;
