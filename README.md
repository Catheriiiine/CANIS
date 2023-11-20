This project was done for the 2023 CANIS Hackathon: Data Visualization and Foreign Interference

## Inspiration
There are growing concerns about foreign interference emerging as the most significant strategic threat to Canada's national security. Social media has become one of the easiest and quickest ways for content to be shared worldwide. Therefore, a deeper examination of major content outlets across various social media platforms can provide valuable insights into the extent of this influence. It's important to note that all the data in this dataset pertains exclusively to China, so any conclusions drawn may not be applicable to other countries.

## What it does
This project focuses on 758 Chinese social media entities with accounts across six different platforms: X (Twitter), Facebook, Instagram, Youtube, Threads, and Tiktok. We analyze China's influence on social media from various angles, including cross-regional, cross-platform, and cross-entity type perspectives. We delve deeper into the top 12 Twitter accounts with the most followers, examining their impact on typical social media engagement metrics. Additionally, we compare CGTN Accounts (owned by China Media Group (CMG)) and Chinese Embassy Accounts (Ministry of Foreign Affairs) to identify usage patterns. Our findings are presented in slides, combining graphics and text.

## How we built it
We processed the dataset as a pandas dataframe in Python. Visualizations were created using a combination of Python libraries such as matplotlib, numpy, venn, radar_factor, and others. In addition to the provided dataset, we conducted research on social media and global demographics to gather additional data to support our findings.

## Challenges we ran into
The dataset offered limited information, providing only the account follower count and account handle as a link. Due to recent API restrictions, scraping other account or post-specific data proved challenging. Nonetheless, we successfully integrated the provided dataset with our own research results, enabling us to focus on a smaller subset of accounts and conduct in-depth analyses.

## Accomplishments that we're proud of
We have discovered several intriguing patterns in social media use. Notably, English-speaking countries tend to be the primary focus region, while accounts focusing on other regions are predominantly Chinese Embassy accounts. Additionally, despite a large follower base, engagement rates are generally low. Most engagement is concentrated on cultural and entertainment content or personal accounts of Foreign Ministry spokespeople, with official accounts being less popular.

## What we learned
Through this project, we have gained a deeper understanding of the concept of foreign interference and its impact. We have also learned how analyzing and visualizing social media data can potentially help in assessing the scale of foreign interference.

## What's next for Scale of China’s influence on Social Media
While this project has yielded interesting findings, it is limited by the available data. Based on our conclusions, we believe that future studies could delve deeper into each social media platform. For example, analyzing user demographics would help determine which age groups are exposed to the content. Studying longitudinal data on followers and post engagements would aid in assessing the growth rate of accounts, how quickly they are expanding, and thus the extent of their influence.
