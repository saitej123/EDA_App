###### *This Report will show Statistics and Visualization techniques and understand the dataset and get business inferences*


### EDA Themes
- ###### Understanding our geographic spread of customers in different regions ?
- ###### Check if any geographic region or city has significantly less profit and address why?
- ###### Check for any promising states/cities to expand our business ?
- ###### Understanding which category of products have high revenue and profit?
- ###### Does shipping mode has any effect on revenue and profit ?

### Data Cleaning
*	No null values or improper values present
*	Changed Postal Code feature to object

### EDA Steps
* **Five point Descriptive Statistics** - Univariate description of both the numerical and categorical variables
* **Correlation and Pair plot** - Distribution and the relation between the numerial variables
* **Bivariate and multivariate Analysis** - Plotting Pieplot and Barplots to visualize and infer the significance of the features

### Important Graphs
1. New York and Los Angeles among top 10 Revenue contributing Cities ![alt text](/images/top_10_revenue.png "Top 10 Cities by Revenue")

2. Relatively smaller cities such as Whakatane, Xingtai,Salto have higher revenue and profit per purchase on average ![alt text](/images/avg_rev_prof_city.png "Top Avg Revenue and Profit Cities")

3. Southeast Asia Region trending in less profits because of loss in Furniture category ![alt text](/images/southeast.png "Revenue and Profit in Southeast Asia by Category")

4. Office supplies have been given high discount at times, but Furnitures have wider possible range of discount ![alt text](/images/discount.png "Discount Distribution by Category")

5. Products on technology category yields best revenue and profit per purchase ![alt text](/images/Technology.png "Technology category yields best revenue")

6. Copiers yield 10x profit per purchase comparatively ![alt text](/images/copier.png "Copiers are imp")

7. Standard Class is the most preferred. Second Class Shipping mode yield more profit per purchase ![alt text](/images/shipping.png "Shipping")


## Important Business Inferences
- In 'Southeast Asia', the **furniture** business is in loss and it is a concern to be addressed
- Company gets high revenue from popular cities such **New York, Los Angeles, Manila,Seattle**, but small cities such as **Whakatane, Xingtai,Salto** shows promise with high average revenue and profit per purchase
- **Technology** products give the best average profit per purchase
- In technology related products, **'copier'** gives **10x profit** compared with any other sub category
- Company should promote **'Second Class'** shipping modes for better revenue and profit per purchase
