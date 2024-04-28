SOCIETY OF ACTUARIES

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-01.jpg?height=515&width=862&top_left_y=81&top_left_x=1179" alt="image" style="width:100%;height:auto;">

Predictive Models on Conversion Studies for the Level Premium Term Plans

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-01.jpg?height=920&width=1925&top_left_y=1405&top_left_x=73" alt="image" style="width:100%;height:auto;">

## Predictive Models on Conversion Studies for the Level Premium Term Plans

SPONSOR

Reinsurance Section

Produce Development Section

Committee on Life Insurance Research
AUTHORS

Richard Xu, FSA, Ph.D.

Minyu Cao, FSA, CERA

Anthony Woods, Ph.D.

Mark Li, ASA

RCA

## Caveat and Disclaimer

The opinions expressed and conclusions reached by the authors are their own and do not represent any official position or opinion of the Society of Actuaries or its members. The Society of Actuaries makes no representation or warranty to the accuracy of the information.

Copyright (C) 2017 by the Society of Actuaries. All rights reserved.

## CONTENTS

	Section 1: Introduction ..... 4
	1.1 Disclaimer of Liability ..... 4
	Section 2: Executive Summary . ..... 5
	Section 3: Data ..... 6
	3.1 Conversion Rate Model ..... 6
	3.2 Post-Conversion Mortality Model ..... 6
	3.3 Post-Conversion Lapse Model ..... 6
	Section 4: Modeling Approach. ..... 7
	Section 5: Key Model Findings ..... 8
	5.1 Conversion Rate Model ..... 8
	5.1.1 Risk Class and Duration ..... 9
	5.1.2 Issue Age and Duration ..... 10
	5.1.3 Face Amount and Duration ..... 11
	5.2 Point-in-Scale Mortality Model ..... 12
	5.2.1 Face Amount and Duration since Conversion ..... 13
	5.2.2 Duration since Conversion and Conversion Group ..... 14
	5.2.3 Issue Age Group and Duration since Conversion ..... 15
	5.3 Post-Conversion Lapse Model ..... 16
	5.3.1 Gender ..... 17
	5.3.2 Duration since Conversion and Duration at Conversion. ..... 18
	5.3.3 Face Amount and Duration since Conversion ..... 19
	Section 6: Conclusion ..... 20
	Section 7: Acknowledgments ..... 21
	Appendix A: Sample Cohorts ..... 22
	Appendix B: Underwriting Class Groupings ..... 24
	Appendix C: Actual Claim Counts in the Point-in-Scale Mortality Model. ..... 26

## Predictive Models on Conversion Studies for the Level Term Premium Plans

## Section 1: Introduction

The Society of Actuaries (SOA), along with the Product Development Section, Reinsurance Section and Committee for Life Insurance Research, engaged RGA Reinsurance Company (RGA) to undertake a research project on term conversion experience with a particular focus on conversion rates and mortality experience of converted policies. As an addendum to that research, the SOA allowed RGA to further explore the term conversion experience in conversion rates and post-conversion experience using predictive analytics. The models presented in this paper are an extension of previous work completed for the May 2016 "Report on the Conversion Experience Study for Level Premium Term Plans," which is available on the SOA website (https://www.soa.org/Research/Research-Projects/Life-Insurance/2016report-conversion-experience-term-plans.aspx), referenced as the "Conversion Study" in this paper.

The models presented in this report aim to provide improved insights into the understanding of the term conversion experience.

Specifically, three models are developed with the following objectives:

The Conversion Rate Model: to understand the drivers that impact the policyholder conversion behavior that may or may not be discovered through traditional experience studies

The Point-in-Scale Mortality Model: to understand the difference between post-conversion mortality and term mortality

The Post-Conversion Lapse Model: to understand the drivers that impact the post-conversion policyholder behavior that may or may not be discovered through traditional experience studies.

### 1.1 Disclaimer of Liability

This report is intended for use by actuaries and other professionals familiar with the conversion option on term products, underwriting and marketing techniques used by U.S. life insurance companies and predictive modeling. The results and analyses presented are derived from the responses to data call. Although a good faith effort has been made to analyze the reasonableness of each response, the final report is ultimately reliant on the accuracy of the underlying data.

The results provided herein come from a variety of life insurance companies with unique product structures, target markets, underwriting philosophies and distribution methods. As such, these results should not be deemed directly applicable to any particular company or representative of the life insurance industry as a whole.

RGA Reinsurance Company (RGA), its directors, officers and employees, disclaim liability for any loss or damage arising or resulting from any error or omission in RGA's analysis and summary of the survey results or any other information contained herein. The report is to be reviewed and understood as a complete document.

This report is published by the Society of Actuaries (SOA) and contains information based on input from companies engaged in the U.S. life insurance industry. The information published in this report was developed from actual historical information and does not include any projected information.

The opinions expressed and conclusions reached by the authors are their own and do not represent any official position or opinion of RGA or the SOA or its members. The SOA makes no representations regarding the accuracy or completeness of the content of this study. It is for informational purposes only. The SOA does not recommend, encourage or endorse any particular use of the information provided in this study. The study should not be construed as professional or financial advice. The SOA makes no warranty, express or implied, guarantee or representation whatsoever and assumes no liability or responsibility in connection with the use or misuse of this study.

## Section 2: Executive Summary

In the past few years, the use of predictive analytics has been gradually adopted by life insurers across the value chain of the business. Predictive analytics provides enhanced insights and quantifiable competitive advantage in solving complex problems. In this paper, the use of predictive modeling provides a deeper understanding of the interaction between product design and policyholder behavior. In the United States, term products generally offer an option to convert to a permanent policy within a certain period. Additional underwriting is usually not required to exercise this option. Thus, policyholders can choose between getting re-underwritten for a new policy and converting into a permanent policy. As a result, the element of anti-selection is rooted in those policies that were converted.

This paper uses a multivariate approach to further analyze policyholders' behavior:

- What drives the policyholders to convert policies in the term period
- How different post-conversion mortality is from term mortality experience
- What drives the policyholders to lapse the policies during the post-conversion period.

With a multivariate approach, one can disentangle the separate impacts of various variables; it isolates the "pure" effect of one particular variable, which may be somewhat difficult to see from univariate analysis alone.

A comprehensive model was built for each of the data sets. This paper only highlights some of the model findings that provide more insightful understanding of the relationship between product feature and policyholder behavior.

Key model findings include the following:

- Conversion Rate Model:

o The model illustrates differentiable and quantifiable power of risk class, issue age and face amount in driving the conversion behavior

- Post-Conversion Point-in-Scale Mortality Model

o Duration at conversion, face amount and issue age have significant impacts in Point-in-Scale Mortality

o Point-in-Scale Mortality also relates to premium payment mode, distribution system and whether the conversion is full or partial

- Post-Conversion Lapse Model:

o Gender, duration at conversion and face amount have significant impacts in the experience

o Policy characteristics such as distribution system, underwriting requirement and billing options are not found to drive the experience in this model

Consistent anti-selective trends in face amount drove experience across all three models.

## Section 3: Data

The model creation starts with the same "Core" data set used to develop the 2016 SOA Report on the Conversion Experience Study for Level Term Plans (hereafter called the Conversion Study). The experience study contains policies from the term business including five-year, 10-year, 15-year and other year level plans. Since the different level term plans will have different patterns, the data for the model are restricted to 10 -year term policies. This restriction gives a more homogeneous grouping with the potential for a simpler and sharper pattern.

For each of the models, when applicable, data from any of the companies that contributed more than $35 \%$ of the incidences are ratioed down to this threshold. The ratios were applied only to the exposure count and conversion, claim or lapse count. The approach is consistent with the 2016 Conversion Study; however, the actual ratio applied may vary. For a more in-depth understanding of the source data, data validation and methodology, please refer to the Conversion Study on the SOA website.

### 3.1 Conversion Rate Model

The exposures and conversions from Section 4 of the Conversion Study are the primary source of data used to develop the model. Again, the scope of the data is restricted to the term business for 10 -year level term plans. An open question was whether the surges in conversions seen in the traditional study are mainly because of the conversion privilege periods ending. To address this question, the data are further restricted to those policies known to have a conversion privilege period of 10 years, which includes about $15 \%$ of the conversion counts from 10 -year level term plans.

| Conversion Rate Model | Model Exposure Count | Model Conversion Count |
| :---: | :---: | :---: |
|  | $3,112,537$ | 22,095 |

### 3.2 Post-Conversion Mortality Model

The exposures and claims from Section 5 of the Conversion Study are the primary source of the data used to develop the models. For the converted permanent business, the scope of the model was restricted to the conversions from 10year level term business only. For the nonconverted term business, the model includes all term data within level term periods.

| Term Mortality | Model Exposure Count | Model Claim Count |
| :---: | :---: | :---: |
|  | $84,370,015$ | 119,517 |
| Post-Conversion Mortality | Model Exposure Count | Model Claim Count |
|  | 587,399 | 3,274 |

### 3.3 Post-Conversion Lapse Model

The exposures and lapses from Section 6 of the Conversion Study are the primary source of data used to develop the model, but restricted to policies converted from the 10-year level term business only. Unlike the conversion rate model, this model includes all conversion privilege periods; this means that conversions other than 10 years are included on 10 -year term policies.

| Post-Conversion Lapse Model | Model Exposure Count | Model Lapse Count |
| :---: | :---: | :---: |
|  | 468,227 | 15,548 |

## Section 4: Modeling Approach

A multivariate regression model is used to study the target variable in this study. Compared to the traditional actuarial experience study, which is univariate in nature, the advantages of the multivariate analysis include the following:

1. The multivariate approaches consider all variables simultaneously. This can eliminate potential bias of overor underestimation of assumptions that may occur in a univariate approach, especially when certain variables are highly correlated.
2. A statistical modeling approach compared to an experience study can be a very efficient way to study the data. Traditional actuarial analysis often relies on a minimal number of events to reach a conclusion, whereas statistical regression is a global approach that handles data more efficiently and provides more statistical measures, such as confidence intervals, which allow for more informed decision making to take place.
3. Modeling of data will normally result in a smoothed curve when analyzing data with certain variables, such as age or face amount, whereas a traditional study intrinsically would bring the fluctuations in data into the result. This would require additional smoothing of the results to develop an assumption.
4. The statistical approach provides a distribution of outcomes, including the mean and uncertainty of the events, unlike a traditional study, which calculates only the mean values of the results.
5. A cross-term (combination of two or more variables) can be included in the model to capture the interrelationship among the variables, thus improving the model fit. Cross-terms are considered in all three models. For example, a cross-term between issue age and policy year is included in the Conversion Rate Model to track the difference in conversion behavior by policy year in different issue ages.

Model variables were initially selected from the data set based on their ability to predict outcomes. In this process, we excluded the company variable to protect the company identity. Contributions by specific variables to the overall quality of the model are identified through use of a statistical criterion, which forces a balance between model simplicity and likelihood maximization.

However, using a statistics-based criterion alone cannot guarantee an effective and robust predictive model. Relying solely on a statistical approach tends to build complex models as it increases the accuracy of the result. Business applications, however, favor simpler models that are easy to interpret and implement. One of the major objectives when modeling for actuarial applications is to achieve a balance between complexity, accuracy and simplicity that involves a close collaboration between business knowledge and modeling expertise.

For the models presented in this paper, accuracy of the data and consistency of the variables over time were considered when selecting the appropriate variables, in addition to the statistical criterion. Business knowledge and experience played equally important roles in determining the selection of variables for the final model.

## Section 5: Key Model Findings

### 5.1 Conversion Rate Model

A comprehensive conversion rate model was built. The model developed describes the actual data well. Figure 1 shows a close agreement between the model's predictions and the values actually observed. The validation result shown in Figure 1 is based on the data set not used in the model development.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-08.jpg?height=827&width=1582&top_left_y=600&top_left_x=323" alt="image" style="width:100%;height:auto;">

* Because our model focused only on 10-year term business with conversion privilege period of 10 years, we do not see conversion rate blips in duration 2 and duration 5, which are shown in Chart 4.2 of the Conversion Study.

The highlighted conversion rate model findings are listed in this paper. In addition to those illustrated, the model also finds that premium payment mode as well as two other variables, underwriting requirement and distribution system, add lift to explain the conversion behavior. Although some of the findings of these variables are consistent with the Conversion Study, for others, additional insights were found comparing to the traditional experience studies. Underwriting requirement (medical, paramedical, nonmedical) and distribution system views were not able to be shown in the Conversion Study because of data limitations and confidentiality of data requirements; therefore, these will not be specifically demonstrated here.

Note: The illustrative model prediction graphs (Figures 2, 3 and 4) are calculated based on Sample Cohort A in Appendix A.

### 5.1.1 Risk Class and Duration

The impact of risk class in conversion rate is somewhat difficult to draw from the experience analysis because of the limited amount of data (refer to Chart 4.18 of the Conversion Study). However, the model discovers that risk class indeed drives the conversion behavior. Shown in Figure 2 is that the preferred nonsmoker has a lower conversion rate compared to a standard nonsmoker and smoker, respectively. The difference is material only in duration 10. More specifically, in duration 10 , the conversion rate of a smoker is $17.3 \%$ higher than a standard nonsmoker and $35.7 \%$ higher than a preferred nonsmoker, which could be evidence of anti-selection because the smoking class is more likely to be declined when applying for a new policy.

Figure 2: Illustrative Model Prediction by Risk Class

for Sample Cohort A

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-09.jpg?height=786&width=1578&top_left_y=797&top_left_x=336" alt="image" style="width:100%;height:auto;">

*Please refer to Appendix B for the details on risk class grouping.

### 5.1.2 Issue Age and Duration

The impact of issue age changes throughout the life of a policy. In early durations, although the difference is small, younger issue ages drives comparatively higher conversion rates. In later durations, the older the issue age, the higher the conversion rate. This is more evident in the shock conversion rate in duration 10. The model considers individual issue age; the result is aggregated by issue age group for illustration purposes in Figure 3.

The result in Figure 3 shows a different pattern comparing to the result in Chart 4.16 from the Conversion Study. The conversion rate trend is somewhat difficult to grasp in the Conversion Study while the model is able to illustrate the isolated impact of issue age. The model clearly illustrates that issue age group $<40$ has the highest conversion rate in early durations but the lowest rate after duration 5 .

In the Conversion Study, issue age group 50-59 has the highest conversion rate in duration 10, while in this modeling exercise, the issue age group 60+ has the highest conversion rate, which is more consistent with the trend of age. The difference here may be because of the slightly different data sets used for both studies.

Figure 3: Illustrated Model Prediction by Issue Age Group
<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-10.jpg?height=822&width=1576&top_left_y=922&top_left_x=336" alt="image" style="width:100%;height:auto;">

### 5.1.3 Face Amount and Duration

The model finds an interesting relationship between the duration and face amount band in duration 10 . Prior to the end of the privilege period, the conversion rate trend by duration at each face amount follows a consistent pattern. However, this pattern is reversed at the end of the privilege period, when in duration 10, large face amounts drive higher conversion behavior. It is also important to note that large face amounts are highly anti-selected across all three models. Refer to Figures 6 and 12 for more information.

It is easy to see that the trend in Figure 4 is somewhat consistent with the result in Chart 4.14 from the Conversion Study, but the model result exhibits a different magnitude in the conversion rate. For example, given everything else equal, in duration 10 , the model shows that the conversion rate in the $1 \mathrm{M}+$ band is $90 \%$ higher than the rate in the $<100 \mathrm{~K}$ band. In the Conversion Study, the rate, which is a raw ratio that includes all risk factors and is not properly adjusted, is only about $40 \%$ higher.

## Figure 4: Illustrated Model Prediction by Face Amount

## for Sample Cohort A

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-11.jpg?height=699&width=1591&top_left_y=865&top_left_x=337" alt="image" style="width:100%;height:auto;">

A. $<100 \mathrm{~K} \longrightarrow$ B. $100 \mathrm{~K}-249 \mathrm{~K} \longrightarrow$ C. $250 \mathrm{~K}-999 \mathrm{~K} \longrightarrow$ D. $1 \mathrm{M}+$

### 5.2 Point-in-Scale Mortality Model

A comprehensive Point-in-Scale Mortality model was built. The Point-in-Scale Mortality model developed describes the actual data well. The Point-in-Scale Mortality in this paper is calculated in consistency with the methodology in Section 5 of the Conversion Study. Figure 5 shows a close agreement between the model's predictions and the values actually observed by duration since conversion. The validation result shown in Figure 5 is based on the data set not used in the model development.

Figure 5: Point-in-Scale Mortality Model Validation Result

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-12.jpg?height=762&width=1594&top_left_y=622&top_left_x=317" alt="image" style="width:100%;height:auto;">

* In Section 5 of the Conversion Study, the Point-in-Scale Mortality in duration since conversion 1 is lower comparing to other durations because of the off-anniversary conversion exposure calculation. Since it is a known issue, the model was not forced to follow the dip in duration since conversion at 1.

The highlighted Point-in-Scale Mortality model findings are listed later. In addition to these illustrated, the model also finds premium payment mode, distribution system and whether the conversion is full or partial add lift to explain the conversion behavior. Although some of the findings of these variables are consistent with the Conversion Study, for others, additional insights were found comparing to the traditional experience studies. Distribution system views could not be shown in the Conversion Study because of data limitations and confidentiality of data requirements; therefore, they will not be specifically demonstrated here.

Note: The illustrative model prediction graphs (Figures 6, 7 and 8) are calculated based on Sample Cohort B in Appendix A.

### 5.2.1 Face Amount and Duration since Conversion

Figure 6 shows model predicted Point-in-Scale Mortality by duration since conversion at each face amount band. The model shows that the higher the face amount of the policy, the higher the Point-in-Scale Mortality. More specifically, we can determine the relative factors of Point-in-Scale Mortality for face amount after all risk factors have been adjusted. Relative to the $<100 \mathrm{~K}$ face amount group, the $100 \mathrm{~K}-249 \mathrm{~K}$ group has $22.7 \%$, the $250 \mathrm{~K}-999 \mathrm{~K}$ group has $62.2 \%$ and the $1 \mathrm{M}+$ group has $76.5 \%$ higher Point-in-Scale Mortality. The results in Chart 5.19 from the Conversion Study are a bit too volatile to interpret.

Again, anti-selection is present in high face amounts. From Figure 4, it is clear that large face amount policies convert the most and are coupled with high Point-in-Scale Mortality rates.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-13.jpg?height=862&width=1591&top_left_y=699&top_left_x=337" alt="image" style="width:100%;height:auto;">

*Please refer to Appendix C for actual claim counts in each face amount band.

### 5.2.2 Duration since Conversion and Conversion Group

Figure 7 shows the model predicted Point-in-Scale Mortality by duration since conversion for each conversion group. The model considers individual duration at conversion, but for illustration purposes, the result is aggregated by the same conversion group used in the Conversion Study. The timing of when policyholders convert makes a significant difference in the Point-in-Scale Mortality, especially for the late converters. This relationship is difficult to observe in Chart 5.25 of the Conversion Study because of the fluctuation in trends. In contrast, the model clearly illustrates that the Point-in-Scale Mortality ratio declines fairly quickly for the late converters, whereas the Point-in-Scale Mortality ratio for the early and mid-converters appears to be flat. This pattern indicates severe anti-selection for the converted policies in the later durations of term policies.

Figure 7: Illustrated Predicted Point-in-Scale Mortality Ratio by Conversion Group

for Sample Cohort B

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-14.jpg?height=707&width=1461&top_left_y=812&top_left_x=337" alt="image" style="width:100%;height:auto;">

*Please refer to Appendix C for actual claim counts in each conversion group.

### 5.2.3 Issue Age Group and Duration since Conversion

The predicted Point-in-Scale Mortality trends by issue age group in Figure 8 reveal that issue age does have an impact on Point-in-Scale Mortality. The issue age group $<40$ has the highest predicted Point-in-Scale Mortality; the impacts of issue age groups 40-49 and 59-59 are similar.

This result differs from the result in Chart 5.20 from the Conversion Study. The Point-in-Scale Mortality for issue age group < 40 in the Conversion Study does not have the highest Point-in-Scale Mortality, compared to other issue ages. This is likely because of the difference in the face amount mix at each issue age group, because issue age group $<40$ is highly concentrated in the lower face amount. Since face amount has a positive impact in Point-in-Scale Mortality (refer to Figure 6), the face amount mix causes the Point-in-Scale Mortality in issue age $<40$ to appear low in the Conversion Study. In contrast, the model is able to remove any correlated impact from face amount and isolates the true impact of issue age $<40$ on Point-in-Scale Mortality.

Figure 8: Illustrated Predicted Point-in-Scale Mortality Ratio by Issue Age Group for Sample Cohort B

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-15.jpg?height=754&width=1591&top_left_y=951&top_left_x=321" alt="image" style="width:100%;height:auto;">

*Please refer to Appendix C for actual claim counts in each issue age group.

### 5.3 Post-Conversion Lapse Model

A comprehensive post-conversion lapse model was built. The model developed describes the actual population data well as shown in Figure 9, where a close agreement is seen between the model's predictions and the values actually observed by policy year. The validation result shown in Figure 9 is based on the data set not used in the model development.

## Figure 9: Post-Conversion Lapse Model Validation Result

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-16.jpg?height=778&width=1570&top_left_y=565&top_left_x=337" alt="image" style="width:100%;height:auto;">

The highlighted post-conversion lapse model findings are listed in the following discussion. In addition to those illustrated, the model also finds that age, underwriting class and conversion product type add lift to explain the conversion behavior. Although some of the findings of these variables are consistent with the Conversion Study, for others, additional insights were found comparing to the traditional experience studies. Conversion product type could not be shown in the conversion experience study because of data limitations and confidentiality of data requirements; therefore, it will not be specifically demonstrated here.

On the other hand, variables such as full or partial conversion indicator, distribution system, underwriting requirement and billing options do not show statistical significance in driving the post-lapse experience.

Note: The illustrative model prediction graphs (Figures 10, 11 and 12) are calculated based on the Sample Cohort C in Appendix A.

### 5.3.1 Gender

The model reveals that gender is statistically significant in driving the post-conversion lapse experience; however, the difference between male and female is tiny, as seen in Figure 10. Therefore, depending on the application of this model, one may decide in practice not to include gender as a variable.

Figure 10: Illustrated Predicted Lapse Rate by Gender

for Sample Cohort C

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-17.jpg?height=716&width=1594&top_left_y=607&top_left_x=339" alt="image" style="width:100%;height:auto;">

— Female Male

### 5.3.2 Duration since Conversion and Duration at Conversion

Figure 11 shows the model predicted lapse rate by duration since conversion for those conversions occurring at single policy years 1,5 and 10 . It reveals that the lapse rate possesses a similar trend by duration since conversion at each duration at conversion. Furthermore, the lapse rate is lower for those policies that convert later. In other words, late converters tend to hold on to the converted policy longer than early converters do. The model illustrates distinguishable trends between early and mid-converters, while volatility makes it difficult to see the actual result from Chart 6.3 in the Conversion Study. For late converters in the term product, the low lapse rate, combined with high conversion rate, clearly illustrates a strong anti-selective trend in this cohort. The highest mortality experience in the Point-in-Scale Mortality model is also a result of the duration 10 conversions.

Figure 11: Illustrated Predicted Lapse Rate by Duration at Conversion

for Sample Cohort C

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-18.jpg?height=734&width=1591&top_left_y=820&top_left_x=337" alt="image" style="width:100%;height:auto;">

### 5.3.3 Face Amount and Duration since Conversion

In early durations, the larger face amounts have lower lapse rates. Anti-selection occurs heavily in these large face amounts, shown earlier in Figures 4 and 6.

The result in Figure 12 is fairly consistent with Chart 6.9 in the Conversion Study at the early durations since conversion. The lapse trends start to merge in later durations.

Figure 12: Illustrated Predicted Lapse Rate by Face Amount

for Sample Cohort C

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-19.jpg?height=754&width=1588&top_left_y=664&top_left_x=323" alt="image" style="width:100%;height:auto;">

## Section 6: Conclusion

As seen, using a multivariate analysis, such as predictive models, provides improved insights in understanding the relationships between product design and policyholder behavior in the conversion business.

Although some of the findings of the variables are consistent with the Conversion Study, for others, we did find additional insights comparing to the traditional experience studies.

Differences from the SOA Conversion study versus the model results include the impact of issue age and face amount on conversion rates, conversion group and issue age group on Point-in-Scale Mortality, and gender on lapses.

The analysis presented in this paper only highlights some of the findings of the models.

With improved data quality and a wider array of the data fields, more vibrant models and in-depth analysis can be developed to further enhance the assumption setting, product design, as well as the potential financial impact of conversions.

## Section 7: Acknowledgments

The authors would like to thank the SOA and the following members of the Project Oversight Group and SOA staff for their guidance and support on this research project, whose comments, feedback and direction have greatly improved the value of this project:

Christine Chui

David Moran

James Filmore

Jean-Marc Fix

Michael Palace

Sebastian Kleber

Tom Edwalds (Chair)

Tony Phipps

Vera Ljucovic

Jack Luff (SOA)

Jan Schuh (SOA)

Ronora Stryker (SOA)

The authors would also like to thank the following for their valuable feedback and contribution to the final models and the original SOA Conversion Study: Mark Ma, Donna Megregian and Lindsay Meisinger. Finally, the authors would like to express our sincere thanks to Ethan Edwards and Dominic Moore for their significant contributions during the data understanding phase of this project.

## Appendix A: Sample Cohorts

## Sample Cohort A

The illustrated model predictions graphs in the conversion rate model are calculated based on the cohort in Table A.1.

For example, for Figure 2, the model prediction is calculated by using the values of issue age, gender, distribution system, premium payment mode, face amount band and underwriting requirement in Table A.1, aggregated by risk class.

Table A. 1 Sample Cohort A

| Variable | Value |
| :--- | :--- |
| Issue Age | 35 |
| Gender | Female |
| Distribution System | Career Agent |
| Premium Payment Mode | Annual |
| Face Amount Band | B. 100K-249K |
| Risk Class | Preferred NS |
| Underwriting Requirement | Paramedical |

## Sample Cohort B

The illustrated model prediction graphs in the Point-in-Scale Mortality model are calculated based on the cohort in Table A.2.

For example, for Figure 6, the model prediction is calculated by using the values of issue age, gender, distribution system, premium payment mode, risk class and conv[ersion] full/partial in Table A.2, aggregated by face amount band.

| Table A.2 Sample Cohort B |  |
| :--- | :--- |
| Variable | Value |
| Issue Age | 40 |
| Distribution System | Male |
| Premium Payment Mode | Career Agent |
| Face Amount Band | Monthly |
| Risk Class | B. 100K-249K |
| Conv Full/Partial | Standard NS |

## Sample Cohort C

The illustrated model predictions graphs in the post-conversion lapse model are calculated based on the cohort in Table A.3.

For example, for Figure 10, the model prediction is calculated by using the values of issue age, premium payment mode, face amount band, risk class and conversion product in Table A.3, aggregated by gender.

Table A. 3 Sample Cohort C

| Variable | Value |
| :--- | :--- |
| Attained Age | 50 |
| Gender | Male |
| Premium Payment Mode | Monthly |
| Face Amount Band | B. 100K-249K |
| Risk Class | Standard NS |
| Conversion Product | Whole Life |

## Appendix B: Underwriting Class Groupings

In the Conversion Study, the data request asked for three fields of underwriting class data used to develop the underwriting class groupings shown in Tables B. 1 and B. 2 for nonsmokers and smokers, respectively. Two of the variables are the total number of smoker and nonsmoker risk classes available for that policy record. The other variable is the risk class rank. In an example of a nonsmoker with three nonsmoker risk classes, the risk class rank would be populated with N1 (the best nonsmoker risk class), N2 (the next best nonsmoker risk class after N1) or N3 (the next best nonsmoker risk class after N2). Depending on the total number of classes and the risk class rank, the underwriting classes are grouped into 10 classes: the six underwriting class names listed in Table B. 1 for nonsmokers, the three underwriting class names in Table B. 2 for smokers and the aggregate risk class.

In the model, the underwriting classes are further grouped into the three broader categories of Preferred Nonsmoker, Standard Nonsmoker and Smoker, as seen in Table B.3.

Table B. 1

Underwriting class names and abbreviation shown by number of underwriting classes (Nonsmoker)

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-24.jpg?height=1331&width=1515&top_left_y=896&top_left_x=305" alt="image" style="width:100%;height:auto;">

Table B. 2

Underwriting class names and abbreviations

shown by number of underwriting classes (Nonsmoker)

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-25.jpg?height=631&width=1114&top_left_y=389&top_left_x=500" alt="image" style="width:100%;height:auto;">

Table B. 3

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-25.jpg?height=271&width=569&top_left_y=1171&top_left_x=778" alt="image" style="width:100%;height:auto;">

Standard Nonsmoker UW Classes

<img src="https://cdn.mathpix.com/cropped/2024_04_13_987724e57cba743e67c8g-25.jpg?height=116&width=567&top_left_y=1563&top_left_x=779" alt="image" style="width:100%;height:auto;">

Smoker UW Classes

Preferred (S)

Undifferentiated (S)

Nonpreferred (S)

## Appendix C: Actual Claim Counts in the Point-in-Scale Morality Model

For Figure 6, the actual claim count by face amount band is shown in Table C.1.

| Table C. 1 |  |
| :--- | ---: |
| Conversion Group | Claim Count |
| Early | 853 |
| Middle | 982 |
| Late | 1,440 |
| Total | 3,274 |

For Figure 7, the actual claim count by conversion group is shown in Table C.2.

| Table C.2 |  |
| :--- | ---: |
| Face Amount Band | Claim Count |
| A. $<100 \mathrm{~K}$ | 1,465 |
| B. $100 \mathrm{~K}-249 \mathrm{~K}$ | 1,111 |
| C. $250 \mathrm{~K}-999 \mathrm{~K}$ | 506 |
| D. $1 \mathrm{M}+$ | 192 |
| Total | 3,274 |

For Figure 8, the actual claim count by issue age group is shown in Table C.3.

Table C. 3

| Issue Age Group | Claim Count |
| :--- | ---: |
| $<40$ | 602 |
| $40-49$ | 718 |
| $50-59$ | 1,111 |
| $60+$ | 843 |
| Total | 3,274 |

