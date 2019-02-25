# Climbing Data Analysis

## Where are the best places to live for rock climbing?

<details open>
  <summary><b>All Climbing Disciplines</b></summary>
  <img src="./heatmaps/all.jpg">
</details>

<br/>

<details>
  <summary><b>Sport</b></summary>
  <img src="./heatmaps/sport.jpg">
</details>

<br/>

<details>
  <summary><b>Bouldering</b></summary>
  <img src="./heatmaps/boulder.jpg">
</details>

<br/>

<details>
  <summary><b>Trad</b></summary>
  <img src="./heatmaps/trad.jpg">
</details>

<br/>

<details>
  <summary><b>Toprope</b></summary>
  <img src="./heatmaps/toprope.jpg">
</details>

<br/>

<details>
  <summary><b>Aid</b></summary>
  <img src="./heatmaps/aid.jpg">
</details>

<br/>

<details>
  <summary><b>Alpine</b></summary>
  <img src="./heatmaps/alpine.jpg">
</details>

<br/>

<details>
  <summary><b>Snow</b></summary>
  <img src="./heatmaps/snow.jpg">
</details>

<br/>

<details>
  <summary><b>Ice</b></summary>
  <img src="./heatmaps/ice.jpg">
</details>

<br/>

<details>
  <summary><b>Mixed</b></summary>
  <img src="./heatmaps/mixed.jpg">
</details>

<br/>

## How are these heatmaps created?

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
