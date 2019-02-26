# 🏞️ Climbing Data Analysis

> An analysis of outdoor rock climbing data

## 🌄 Where are the best places to live for rock climbing?

<details open>
  <summary><b>All climbing types</b></summary>
  <img src="./heatmaps/all.jpg">
  <br/>
</details>

<details>
  <summary>Individual climbing types</summary>

  <b>Sport</b>
  <img src="./heatmaps/sport.jpg">
  <br/>

  <b>Bouldering</b>
  <img src="./heatmaps/boulder.jpg">
  <br/>

  <b>Trad</b>
  <img src="./heatmaps/trad.jpg">
  <br/>

  <b>Toprope</b>
  <img src="./heatmaps/toprope.jpg">
  <br/>

  <b>Aid</b>
  <img src="./heatmaps/aid.jpg">
  <br/>

  <b>Alpine</b>
  <img src="./heatmaps/alpine.jpg">
  <br/>

  <b>Snow</b>
  <img src="./heatmaps/snow.jpg">
  <br/>

  <b>Ice</b>
  <img src="./heatmaps/ice.jpg">
  <br/>

  <b>Mixed</b>
  <img src="./heatmaps/mixed.jpg">
  <br/>

</details>

## ⚗️ How are these heatmaps created?

For each zipcode in the United States, we calculate that zipcode's climbing score using the following formula.

<img src="./equation.png" width="450">

After creating [a score for each zipcode](./data/geo-scores), we then create the heatmap using Matplotlib in conjunction with shapefiles provided by the 2017 US Census.

Since [not every area in the US is covered by a zipcode](https://www.reddit.com/r/MapPorn/comments/938z9e/map_of_us_zip_code_regions/), we use US counties as a fallback which are less granular than zipcodes but cover all areas in the US.

## 🗂️ Datasets

- [2017 US Census zipcode shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census county shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census state shapefiles](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html)
- [2017 US Census zipcode latitude and longitude](https://gist.github.com/erichurst/7882666)
- [2017 US Census county latitude and longitude](https://www.census.gov/geo/maps-data/data/gazetteer2017.html)
- [Rock climbing data](https://github.com/alexcrist/mountain-project-scraper)
