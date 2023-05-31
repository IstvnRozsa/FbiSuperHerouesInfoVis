//console.table(superheroes_json);


/*
criminals_json.forEach((item) => {
  console.log(item.place_of_birth, item.longitude, item.latitude, item.country_name, item.country_code_a2, item.country_code_a3);
});
*/


// Define the margins and dimensions of the chart
const margin = {top: 20, right: 20, bottom: 60, left: 60};
const width = 500 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

function highlightPoints(point){
  console.log("Highlight Point", point);
}

var highlightedCountries = criminals_json.map(item => item.country_code_a3);
const criminals_map_svg = d3.select("#criminals_map").attr("viewBox", [0, 0, width, height - 100]);


let projection = d3.geoMercator()
    .scale(90)
    .translate([width / 2.45, (height - 45) / 2]);

const pathGenerator = d3.geoPath().projection(projection);

let g = criminals_map_svg.append("g");

d3
    .json(
        "https://raw.githubusercontent.com/iamspruce/intro-d3/main/data/countries-110m.geojson"
    )
    .then((data) => {
        g
            .selectAll("path")
            .data(data.features)
            .join("path")
            .attr("d", pathGenerator)
            .attr("id", function (d) {
                return d.id;

            })
            .attr("class", "country").style("fill", function (d) {
                if (highlightedCountries.includes(d.id)) {
                    // Highlight the country in red if it's in the list of highlighted countries
                    return "rgba(228, 113, 46, 1)";
                }
            })
        ;
    });
