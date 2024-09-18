**First Project (Space race with Data science Final IBM Data Science Certification Presentation)**
This project aims to develop a machine learning pipeline to predict the success of SpaceX's Falcon 9 rocket landings. By achieving a high success rate, the project seeks to enable Space Y to offer competitive services and reduce launch costs significantly.

Methodology The data collection involved two primary methods

API Requests: Data was collected from SpaceX's API. Web Scraping: Additional data was obtained from Wikipedia using BeautifulSoup.

The data underwent extensive wrangling, including handling missing values and applying one-hot encoding to categorical features. Exploratory Data Analysis (EDA) was performed using visualization techniques and SQL queries to uncover insights. Interactive visual analytics were created using Folium and Plotly Dash. Finally, predictive models were developed using various classification algorithms, and hyperparameters were tuned using GridSearchCV. image Results: Key findings from the analysis include: Launch Site Success Rates: KSC LC-39A had the highest success rate among all launch sites. Payload and Orbit Analysis: Heavy payloads tend to have higher success rates for specific orbits like PolarLEO and ISS, while GTO orbits showed mixed results. Yearly Trends: The success rate of launches has steadily increased since 2013, reaching its peak in 2020.

The decision tree classifier emerged as the best-performing model for predicting landing success, with a high accuracy score. However, the model's confusion matrix revealed some issues with false positives, indicating areas for further improvement

image Conclusion The project successfully developed a predictive model that can help Space Y optimize their launch processes and reduce costs. The insights gained from the EDA and the interactive visualizations provide valuable information for decision-making and strategic planning. The continuous improvement of the model and further analysis of additional features will enhance the accuracy and reliability of the predictions. image
***********************************************************************************************************************
**Second Project ( Titanic - Machine Learning from Disaster)**

The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).
*************************************************************************************************************************************************************************************************************************************************************************
