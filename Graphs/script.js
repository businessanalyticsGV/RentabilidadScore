    // d3.select(".target");
    // d3.style("stroke-width",8);

var svg = d3.select("#vis_Visualization1")
    svg.append("circle")
  .attr("cx", 2).attr("cy", 50).attr("r", 40).style("fill", "blue");
    svg.append("circle")
  .attr("cx", 140).attr("cy", 50).attr("r", 40).style("fill", "red");
    svg.append("circle")
  .attr("cx", 300).attr("cy", 50).attr("r", 40).style("fill", "green");