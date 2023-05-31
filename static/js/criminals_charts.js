
// Count items by country code and name
var countsByCountry = {};
criminals_json.forEach(function(item) {
  var countryCode = item.country_code_a3;
  var countryName = item.country_name;

  var key = countryCode + '|' + countryName;
  countsByCountry[key] = (countsByCountry[key] || 0) + 1;
});

// Create an array of objects with count, country code, and country name
var result = Object.keys(countsByCountry).map(function(key) {
  var [countryCode, countryName] = key.split('|');
  return {
    criminals_count: countsByCountry[key],
    countryCode: countryCode,
    countryName: countryName
  };
});

console.log(result);