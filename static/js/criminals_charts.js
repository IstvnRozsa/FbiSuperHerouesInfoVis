// Count items by country code and name
console.log(criminals_json)
var countsByCountry = {};
criminals_json.forEach(function (item) {
    var countryCode = item.country_code_a3;
    var countryName = item.country_name;

    var key = countryCode + '|' + countryName;
    countsByCountry[key] = (countsByCountry[key] || 0) + 1;
});

// Create an array of objects with count, country code, and country name
var result = Object.keys(countsByCountry).map(function (key) {
    var [countryCode, countryName] = key.split('|');
    return {
        criminalsCount: countsByCountry[key],
        countryCode: countryCode,
        countryName: countryName
    };
});

console.log(result);

result.sort(function (a, b) {
    return b.criminalsCount - a.criminalsCount;
});

result = result.slice(0, 10);
// Assuming the JSON data is stored in a variable called jsonData
var jsonData = [
    {"countrycode": "US", "countryname": "United States", "count": 100},
    {"countrycode": "GB", "countryname": "United Kingdom", "count": 75},
    {"countrycode": "CA", "countryname": "Canada", "count": 50},
    // Add more data entries here...
];

var criminalsBarchartSvg = d3.select("#criminals_barchart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Set the x and y scales
var x = d3.scaleBand()
    .range([0, width])
    .padding(0.1)
    .domain(result.map(function (d) {
        return d.countryCode;
    }));

var y = d3.scaleLinear()
    .range([height, 0])
    .domain([0, d3.max(result, function (d) {
        return d.criminalsCount;
    })]);

// Create the x and y axes
var xAxis = d3.axisBottom(x);

var yAxis = d3.axisLeft(y)
    .ticks(5);

// Append the axes to the SVG container
criminalsBarchartSvg.append("g")
    .attr("class", "axis-x")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

criminalsBarchartSvg.append("g")
    .attr("class", "axis-y")
    .call(yAxis);

// Create the bars
criminalsBarchartSvg.selectAll(".bar")
    .data(result)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function (d) {
        return x(d.countryCode);
    })
    .attr("y", function (d) {
        return y(d.criminalsCount);
    })
    .attr("width", x.bandwidth())
    .attr("height", function (d) {
        return height - y(d.criminalsCount);
    });

// Add labels to the bars
criminalsBarchartSvg.selectAll(".bar-label")
    .data(result)
    .enter().append("text")
    .attr("class", "bar-label")
    .attr("x", function (d) {
        return x(d.countryCode) + x.bandwidth() / 2;
    })
    .attr("y", function (d) {
        return y(d.criminalsCount) - 5;
    })
    .attr("text-anchor", "middle")
    .text(function (d) {
        return d.countryCode;
    });
