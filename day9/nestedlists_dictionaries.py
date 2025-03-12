capitals ={
    "france":"Paris",
    "England":"London",
    "US":"Washington DC"
}

travel_log ={
    "france":["Paris","Lille","Dijon"],
    "England":["London","Manchestor","Edinburgh"],
    "US":["Austin","Washington","Los Angeles "]
}

print(travel_log["france"][2])


nested_list =["a","b",["c","d"]]
print(nested_list[2][0])


travel_log2= {
  "India":  {
        "citiesvisited":["Agra","Delhi","Chennai"],
        "noOfPlacesVisited":3
    }
  ,
    "England":  {
        "citiesvisited":["London","Manchester","Winston"],
        "noOfPlacesVisited":3
    }
}

print(travel_log2["England"]["citiesvisited"][2])