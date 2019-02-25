# Climbing Area Data Analysis

## Where are the best places to live for rock climbing?

### All Climbing Disciplines

![](./heatmaps/all.jpg)

### Sport

![](./heatmaps/sport.jpg)

### Bouldering

![](./heatmaps/boulder.jpg)

### Trad

![](./heatmaps/trad.jpg)

### Toprope

![](./heatmaps/toprope.jpg)

### Aid

![](./heatmaps/aid.jpg)

### Alpine

![](./heatmaps/alpine.jpg)

### Snow

![](./heatmaps/snow.jpg)

### Ice

![](./heatmaps/ice.jpg)

### Mixed

![](./heatmaps/mixed.jpg)

## How are these made?

For every zipcode in the United States, we calculate that zipcode's climbing score using the following formula.

<img src="./equation.png" width="450">

After creating [a score for each zipcode](./data/geo-scores), we then create the heatmap using Matplotlib in conjunction with shapefiles provided by the 2017 US Census.

Since [not every area in the US is covered by a zipcode](https://www.reddit.com/r/MapPorn/comments/938z9e/map_of_us_zip_code_regions/), we use US counties as a fallback which are less granular than zipcodes but cover all areas in the US.

## Datasets

- [2017 US Census Zipcode Shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census County Shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census State Shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census Zipcode Latitude and Longitude](https://gist.github.com/erichurst/7882666)
- [2017 US Census County Latitude and Longitude](https://www.census.gov/geo/maps-data/data/gazetteer2017.html)
- [Rock Climbing Data](https://github.com/alexcrist/mountain-project-scraper)
