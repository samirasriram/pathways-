# Pathway 2

## Procedure
The yelp dataset contained 5 files and I decided to use the business data. 

The JSON files were too large to be usable within R. so I undertook the following steps

1. I did an initial `grep -i` for restaurants which whittled down the data to 122,471 results - the output is in file rest.json. (This file has not been included in this repo as it is over 100mb)
2. This, however, targetted keywords that were in all business. To only get businesses with the category "restaurant" I removed one of the attributes with the string "RestaurantsPriceRange" using `grep -v`. The output is in  rest1.json and has 11,183 results. 
3. On further observation I realized there were a number of other "restauraunt???" strings that needed to be excluded. I did this and got rest2.json with 4321 results. 
4. I modified rest2.json to make each individual JSON record into a full JSON array by using `vi` to `:%s/$/,` and adding an array open brace on line 1 and closing brace on the last line thereby making rest3.json a syntactically correct json array.
5. I read rest3.json into R. (Please review `analytics.Rmd` file for detailed code and comments.)  I found which cities these restaurants were in. I decided to use Toronto and Pittsburgh as base cases as Toronto had the largest sample size of restaurants (322) and Pittsburgh (with n =245) is an east-coast city comparable to Boston.
6. I created two dataframes, one for each city, that had restaurants with more than 4.5 stars and more than 10 reviews. These are random metrics I chose to see subjectively see which restaurants are successful in each city. 
7. Then using the larger yelp data I found which cateogories and attributes were characteristic of these top restaurants, and their frequency. 

Comments:
* For a deeper analysis, one could cross reference the user and review data with the business data to only get reviews from "credible users". 
* Smaller or new restaurants may not have 10+ reviews yet

## Recommendation
I found that Japanese, Mediterranean, and Vietnamese cuisines were the most popular (with Mediterranean restaurants being the most successful, and Vietnamese and Japanese coming in second). Another category freqeunt among top restaurants were outdoor seating, had TV, and nightlife. 

Of course, this recommendation would be much stronger if we had a look at the Boston restaurant demographic. (The dataset included no cities in MA). 

Additionally, Cambridge is home to lots of colleges, it would be interesting to see then if the restaurant market was already flooded with bars/nightlife venues. 

## My Final Suggestion
A Mediterranean restaurant, with a bar, outdoor seating, and a TV would likely be the most successful in Cambridge, MA.