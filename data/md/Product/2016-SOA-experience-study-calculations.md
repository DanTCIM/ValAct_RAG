<img src="https://cdn.mathpix.com/cropped/2024_04_13_77542591393347e2e981g-001.jpg?height=513&width=1114&top_left_y=85&top_left_x=923" alt="image" style="width:100%;height:auto;">

# Experience Study Calculations 

<img src="https://cdn.mathpix.com/cropped/2024_04_13_77542591393347e2e981g-001.jpg?height=1440&width=1676&top_left_y=995&top_left_x=234" alt="image" style="width:100%;height:auto;">

October 2016 (revised March 2024)

## Experience Study Calculations

AUTHORS

DAVID B. ATKINSON, FSA, MBA

JOHN K. MCGARRY, ASA, PhD

## Caveat and Disclaimer

This paper is published by the Society of Actuaries (SOA) and contains information from a variety of sources. The paper is for informational purposes only and should not be construed as professional or financial advice. The SOA does not recommend or endorse any particular use of the information provided in this study. The SOA makes no warranty, express or implied, or representation whatsoever and assumes no liability in connection with the use or misuse of this study.

## TABLE OF CONTENTS

Preface: Revisions Made to this Report Subsequent to October 2016 ..... 6
June 2023 Updates ..... 6
January 2019 Updates ..... 6
June 2018 Updates ..... 6
January 2018 Updates ..... 6
November 2016 Updates ..... 6
October 2017 Updates
1 Acknowledgements ..... 8
2 Introduction ..... 9
2.1 Scope ..... 9
2.2 Guide to Usage ..... 9
3 Experience Study Overview ..... 11
3.1 Basic Terminology ..... 11
3.2 Experience Study Segmentation ..... 12
4 Simple Mortality Study Examples ..... 14
4.1 Cohort Study with Deaths only..... ..... 14
4.1.1 Summary Rates with Deaths Only. ..... 15
4.2 Cohort Study with Deaths and Withdrawals ..... 15
4.2.1 Individual Exposure Calculation ..... 17
4.2.2 Grouped Exposure Calculation ..... 18
4.2.3 Summary Rates with Deaths and Withdrawals..... ..... 18
4.3 Period Study with Deaths and Withdrawals ..... 19
4.3.1 Individual Exposure Calculation ..... 20
4.3.2 Grouped Exposure Calculation ..... 21
4.4 Amount-Weighted Studies. ..... 23
4.4.1 Individual Amount Weights ..... 23
4.4.2 Grouped Amount Weights ..... 24
5 Distributed Exposure ..... 26
5.1 Period Study ..... 27
6 Fractional Rates ..... 29
6.1 Half-Year Period Study ..... 30
6.2 Average Fractional Rates ..... 30
6.3 Annual Period Study by Calendar Year ..... 33
7 Average Daily Rates and Exposure ..... 35
7.1 Period Study with Daily Exposure ..... 36
8 Average Force of Mortality ..... 38
8.1 Period Study with Constant Force ..... 39
8.2 Changing Force of Mortality ..... 39
9 Distributions of Deaths ..... 42
9.1 Comparison of Distributions ..... 43
9.1.1 Balducci Hypothesis ..... 44
9.1.2 Uniform Distribution of Deaths ..... 45
9.1.3 Constant Mortality Rates. ..... 47
9.1.4 Increasing Force. ..... 47
9.2 Estimating Errors ..... 51
10 Decrement Studies ..... 54
10.1 Decrement Types. ..... 54
10.2 Rate Intervals ..... 54
10.2.1 Partial Rate Intervals ..... 55
10.3 Time Intervals ..... 55
10.4 Discrete Decrements. ..... 57
10.5 Population States. ..... 57
11 Simple Withdrawal Study Example ..... 59
11.1 Period Study ..... 59
11.1.1 Exposure Calculation ..... 59
12 Actual to Expected Analysis ..... 61
12.1 Period Study with Deaths and Withdrawals ..... 62
12.2 Amount-Weighted Period Study ..... 62
12.3 Period Study with Calendar Year ..... 63
12.4 Half-Year Study ..... 63
12.5 Half-Year Study with Daily Decrement Rates ..... 64
13 Central Rates ..... 66
13.1 Annual Period Study ..... 67
13.2 Force of Decrement ..... 68
14 Dependent Rates ..... 69
14.1 Cohort Study with Deaths and Withdrawals ..... 69
14.2 Period Study with Deaths and Withdrawals ..... 70
14.3 Population Projection ..... 72
14.4 Formula Derivation. ..... 73
15 Utilization Studies ..... 75
15.1 Frequency and Severity ..... 75
15.2 Utilization of Maximum Limits ..... 76
15.3 Loss Ratio ..... 77
15.4 Variable Annuity Withdrawal Utilization ..... 77
16 Exposure and Rate Comparisons ..... 79
17 Practical Considerations ..... 81
17.1 Amount-Weighted Distortions ..... 81
17.2 Data Extracts for Multi-Year Studies ..... 81
17.3 Homogeneity of Data ..... 81
17.4 Reporting Lags ..... 82
17.5 Non-Uniform Distribution of Events ..... 82
17.6 Partial Policy Years ..... 83
17.6.1 Overview ..... 83
17.6.2 Inclusion of Partial Policy Years ..... 84
17.6.3 Overview of Exposure Methods ..... 84
17.6.4 Annual Exposure Method ..... 84
17.6.5 Distributed Exposure Method ..... 85
18 Product-Related Considerations ..... 86
18.1 Individual Life Insurance ..... 86
18.1.1 Grace Period ..... 86
18.1.2 Compromised and Denied Claims ..... 86
18.1.3 Study Variables Changing Over Time ..... 86
18.1.4 Treatment of Reinsured Amounts ..... 87
18.1.5 Use of Net Amount at Risk. ..... 87
18.1.6 Inclusion of Substandard or Uninsurable Lives . ..... 87
18.1.7 Backdated New Business. ..... 87
18.2 Group Life Insurance ..... 88
18.3 Morbidity Products. ..... 88
18.3.1 Claim Incidence Studies ..... 89
18.3.2 Claim Severity Studies ..... 89
18.3.3 Claim Termination Studies ..... 90
18.4 Disability Income ..... 90
18.4.1 Elimination Periods ..... 90
18.4.2 Partial Disability Benefits ..... 91
18.4.3 Recovery Followed by Relapse. ..... 91
18.4.4 Claim Settlements ..... 91
18.4.5 Other DI Considerations ..... 92
18.5 Long-Term Care ..... 92
18.5.1 Elimination Period ..... 92
18.5.2 Inflation Protection ..... 93
18.5.3 Benefit Utilization Rate. ..... 93
18.5.4 Other LTC Considerations ..... 93
18.6 Deferred Annuities ..... 93
18.6.1 Deferred Annuity Utilization Rates ..... 94
18.6.2 Contract Year Data Challenges ..... 95
18.7 Payout Annuities ..... 95
18.8 Retirement Pensions ..... 96
18.9 Credit Life and Disability ..... 96
18.9.1 Credit Life Insurance ..... 96
18.9.2 Credit Disability Income. ..... 97
Standard Method Error Derivation ..... 99
19.1 Errors from Fractional Exposure Method ..... 99
19.1.1 Error for Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$ ..... 99
19.1.2 Error for Partial Year Running from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$ ..... 100
19.1.3 Error for Fractional Period ..... 101
19.2 Errors for Annual Exposure Method ..... 101
19.2.1 Error for Partial Year Running from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$ ..... 102
19.2.2 Error for Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$ ..... 102
19.2.3 Error for Fractional Period ..... 103
19.3 Errors from Distributed Exposure Method ..... 104
19.3.1 Error for Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$ ..... 104
19.3.2 Error for Partial Year Running from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$ ..... 105
19.3.3 Error for Fractional Period ..... 106
20 Linear Force Method ..... 108
20.1 Formula Development ..... 108
20.1.1 Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$ ..... 108
20.1.2 Partial Year from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$ ..... 109
20.1.3 Fractional Periods ..... 110
20.2 Increasing Force Example ..... 111
21 Glossary ..... 112
22 About the Society of Actuaries ..... 116

## Preface: Revisions Made to this Report Subsequent to October 2016

## March 2024 Updates

- In Section 14.4, the derivation of the formula to calculate dependent rates from independent rates was revised.


## June 2023 Updates

- $\quad$ The 2 table in section 4.4.1 were updated to add Life F for consistency with other sections.


## January 2019 Updates

- $\quad$ Section 9.1.1, page 43 was clarified and corrected as follows:
- $t=0$ was defined as representing the start of the first fractional period.

○ ${ }_{f} q_{x}=f q_{x} /\left(1-(1-f) q_{x}\right)$ was replaced using values of $t=0$ and $f=1 / 12$ :

$$
{ }_{1 / 12} q_{x}=\frac{1}{12} q_{x} /\left(1-\left(1-\frac{1}{12}\right) q_{x}\right)=\frac{1}{12} q_{x} /\left(1-\frac{11}{12} q_{x}\right)=q_{x} /\left(12-11 q_{x}\right)
$$

- An intermediate step was added to explain the derivation of the formula for the probability of dying between age $x+f t$ and age $x+f(t+1)$.

० ${ }_{f} q_{x+f t}=1-\left(1-{ }_{f t} q_{x}\right) /\left(1-{ }_{f(t-1)} q_{x}\right)$ was corrected to:

${ }_{f} q_{x+f t}=1-\left(1-{ }_{f(t+1)} q_{x}\right) /\left(1-{ }_{f t} q_{x}\right)$.

## June 2018 Updates

- Section 4.2 was updated to clarify the connection between the annual exposure method and the Balducci Hypothesis.
- Section 4.3 was updated to clarify exposure for partial ages and discuss the limitations of the annual exposure method in a calendar year study.
- Section 5 was enhanced to include a discussion of the in-period/hybrid exposure method and distortions associated with splitting exposure between calendar years.
- $\quad$ Sections 6.2, 7, and 8 were updated to discuss the limitations of average fractional rate, average daily rate and constant force methods for ages with a small number of lives.
- $\quad$ Subsection 18.3.1 was updated to reflect that a disability claim incidence study generally uses the claim frequency method and is not a decrement study. It was also augmented to address the potential of multiple disability claims on a single policy and their effect on exposure.


## January 2018 Updates

- Section 4.3 was updated to address the calculation of exposure for the event under study for the partial year at the beginning of the study period.


## November 2016 Updates

- $\quad$ Credentials were added to the names of the members of the Project Oversight Group on page 7.
- The formula in the middle of page $21, \frac{112}{} E_{65 \frac{1}{2}}=1 / 2 l_{66}+{ }_{1 / 2} d_{65 \frac{1}{2}}+1 \frac{1 / 4}{1 / 2} w_{65 \frac{1}{2} 2}$, was corrected to be $\frac{1 / 2}{} E_{65 \frac{1}{2}}=1 / 2 l_{66}+1 / 2{ }_{1 / 2} d_{65 \frac{1}{2}}+1 / 4_{1 / 2} w_{65 \frac{1}{2} /}$.
- $\quad$ Other minor wording clarifications were made throughout the document.


## October 2017 Updates

- Section 6.3, first paragraph, "at time $t$ in the year" was corrected to "at time 1-t in the year". Additional wording added throughout section 6.3 for clarification.


## 1 Acknowledgements

The Society of Actuaries (SOA) and the authors extend their gratitude to the following members of the Project Oversight Group who contributed their expertise and insights, served as a sounding board for ideas and oversaw the development of this report.

## Project Oversight Group:

- John A. Bettano, FSA, MAAA
- Carl Desrochers, FSA, MAAA, FCIA
- Steven C. Ekblad, FSA, MAAA
- Christopher H. Hause, FSA, MAAA
- Barry M. Koklefsky, FSA, MAAA, FCIA
- Michael J. Lane, FSA, MAAA
- Marianne C. Purushotham, FSA, MAAA
- Joel C. Sklar, ASA, MAAA


## SOA Staff:

Cynthia MacDonald, FSA, MAAA

Korrel Rosenberg

## 2 Introduction

### 2.1 Scope

The design and maintenance of insurance programs, pensions and many forms of finance are underpinned by rates of many different sorts, such as interest rates, mortality rates and claim utilization rates. This paper presents and explains the methods for determining rates based on experience, such as mortality and claim utilization rates. While this paper can be applied to calculate certain rates related to asset behavior, such as default and prepayment rates, it does not apply to rates based on elaborate econometric models, such as those sometimes used for interest rates, convexity and the like.

The objective of experience studies is to develop rates or probabilities based on data collected from sources such as insurance companies, consulting firms, or governmental bodies. These rates and probabilities can be used by actuaries to develop assumptions for financial planning, valuation, pricing and risk management.

Many types of experience studies take place on a regular basis. While most companies perform their own studies, the most far-reaching studies are those that gather data from across an industry:

- Many large life insurers regularly contribute data that is compiled to produce industry mortality studies every few years. Additionally, many life insurers perform mortality studies using their own data, with results often compared to industry averages.
- Insurers perform annual claim utilization studies of both frequency and severity of claims. Annual studies are needed to keep up with rapid changes in the use and cost of medical services. Separate studies are often performed for large employers.
- Because of the relatively high volume of lapses and significant variations by company, most life insurers perform their own lapse studies rather than relying on industry studies, which are produced less frequently.
- Pension mortality studies are done to provide current information across employers for use in setting pension plan valuation assumptions. Due to some difficulty in gathering data from employers, these studies have historically been performed less often than life insurance mortality studies.
- $\quad$ Products with smaller market shares and fewer market participants, such as Long-Term Care (LTC) and Individual Disability Income (IDI), tend to have less frequent studies. Additionally, such products present complexities not found in life insurance.
- U.S. insurers of credit life, credit disability and deferred annuity products use consulting firms to conduct experience studies for these products, with a high level of industry participation.

The goal of this report is to illuminate the calculations that underlie such studies.

### 2.2 Guide to Usage

This report can be used in different ways:

1. It can be used as a primer to learn about the fundamentals of experience rate calculations or as an aid when building a new experience study from scratch. For these purposes, the reader may want to focus on the fundamental chapters outlined below.
2. It can serve as a resource for a practitioner looking for new ideas or wanting to validate a new or existing approach. A scan of the Table of Contents or a search for key words should lead the reader to areas of interest.
3. Those skeptical of the Annual Exposure Method (often called the "Actuarial Method") can see how it compares to alternative methods. Someone looking for the most appropriate exposure method for a particular situation can review the pros and cons of each method. Chapters 5 through 9 examine and compare the various exposure methods, Chapter 19 derives error formulas for each exposure method and Chapter 20 presents the "linear force
method," a new approach to modeling rates that change continuously over time and facilitates the estimation of errors.

The fundamentals of experience rate calculations are covered by the following chapters:

- $\quad$ Chapter 3, Experience Study Overview
- $\quad$ Chapter 4, Simple Mortality Study Examples
- Chapter 11, Simple Withdrawal Study Example
- $\quad$ Chapter 12, Actual to Expected Analysis

Additionally, it is recommended that the reader scan Chapter 17, Practical Considerations, and Chapter 18, ProductRelated Considerations, for relevant topics.

## 3 Experience Study Overview

### 3.1 Basic Terminology

This paper uses the following terms to describe the calculations for experience studies:

Study Period: The period of time for which data has been gathered for the experience study. Study periods most commonly consist of one to many calendar years of data. When multiple years are included, it is possible to study trends.

Study Population: The population from which the experience study's data has been drawn. The population would normally consist of people (insureds, employees, retirees, citizens, etc.) or contracts (individual insurance policies, pension plans, group insurance plans, bonds, mortgages, etc.).

Cell: An experience study is typically subdivided into many cells. For example, an experience study might subdivide its data into cells for each combination of issue age, sex, smoker/nonsmoker, and policy year.

Experience Rates: The main results of an experience study. Most often, an experience rate is either a decrement rate or a utilization rate. One experience rate is calculated for each cell in the study.

Rate Interval: The cell's experience rate is calculated for an interval of time. While the most common rate intervals are annual and monthly, other intervals such as daily and weekly are sometimes used. The interval is chosen to capture important variations of rates over time, as in the following examples:

- While most financial products use annual rate intervals, there are exceptions. Deferred annuities are more apt to be surrendered, with the proceeds invested in a new contract, in the months after a surrender charge runs out. Insurance products are more prone to lapsation in the month or two after a steep premium increase takes effect. In such cases, an analysis of the policyholder behavior for a monthly rate interval may be required to accurately represent the experience.
- Some products offer a benefit that changes monthly, such as credit insurance designed to pay off an amortizing loan. A monthly study interval would better reflect the decreasing benefit amounts.
- Disability recovery rates change dramatically in the early stages of disability, so monthly or weekly rate intervals are used for the first two or more years following the onset of disability. Once recovery rates stabilize, annual rate intervals are used.

Rate Year: The type of year upon which rates are based. Rate year is usually a policy year, life year or calendar year:

- Policy Year: Cells are defined with reference to the underlying contract's date of inception. Policy year 1 is the first policy year. Policy year $t$ starts at $t-1$ years after inception and ends just prior to $t$ years after inception. Most individual insurance studies use policy years. When the data underlying the study is submitted by calendar year, there will be partial policy years at the beginning and end of the study. In some studies, policy years are referred to as policy durations. Sometimes duration and policy year are synonymous. Other times, duration is equal to policy year minus one, with the first policy year denoted as duration zero.
- Life Year: Cells are defined with reference to the person's date of birth. The life year for age $x$ runs from the birthday at age $x$ to the birthday at age $x+1$. Most pension studies use life years. When the data underlying the study is submitted by calendar year, there will be partial life years at the beginning and end of the study.
- $\quad$ Calendar Year: Cells are defined with reference to a calendar year. Group health studies typically use calendar years.

Rate Type: There are two very different kinds of rates that are the objects of experience studies: Decrement rates and utilization rates, which are treated separately in this paper.

- Decrement rates are probabilities that range from 0 to 1 . The event being studied represents a decrement, transition or termination and removes the person or contract from the study's population. Most decrements, such as death, lapse, full withdrawal, and contract expiry, can happen only once per person or contract. Other decrements, such as disability, may represent a transition from one status (active) to another status (disabled) and can happen more than once.
- Utilization rates are not probabilities and can exceed 1. Most often, utilization measures the frequency or severity of the event under study. Utilization does not remove the person or contract from the study's population. It is possible for a life (or contract) to utilize the event under study more than once. Medical claims and partial withdrawals are examples of utilization.


### 3.2 Experience Study Segmentation

An experience study's population is subdivided into cells to examine possible variations in experience rates across segments of the population, as well as to group experience into homogenous subsegments. Cells are defined by a subset of the attributes that have been collected for the population under study. The study's population is then grouped into the resulting cells. Often, studies investigate multiple segmentations to determine which attributes are the most significant.

An experience rate is calculated for each cell. Each cell represents an interval of time that matches the experience rate interval. For example, if monthly rates are to be calculated, then separate cells are needed for each month in the study period.

Time is usually a key variable in experience studies. Time may take the form of calendar year, observation year, life year, policy year, or other variables that change over time. For example:

- For payout annuity and pension mortality studies, life year, defined earlier in this chapter, is typically the time dimension.
- For individual life insurance, where initial underwriting and selection of the insured are important drivers of experience rates, both mortality rates and lapse rates are generally studied by policy year.
- A multi-year study could have two time variables, with each life year or policy year split between the two calendar years it spans. Looked at another way, each calendar year would be split between two consecutive life years or policy years.

Excluding the above time-related variables, most other variables that define cells are attributes that are unchanging during the study period, effectively defining subpopulations that may exhibit different rates. For example:

- $\quad$ Experience can vary by size of benefit or premium: Larger life insurance face amounts are underwritten more thoroughly, involve a larger commitment and often result in lower mortality and lapse rates. On the other hand, sufficiently large disability income benefits can make disability financially attractive in certain situations, so are sometimes associated with higher rates of disability. As a result of these and other situations, it is not uncommon to subdivide cells by size of benefit.
- When an experience study includes some issue ages calculated using age last birthday ("ALB") and others using age nearest birthday ("ANB"), both as of the issue date of the policy, it is customary to have separate cells for ALB and ANB. On the average, an ALB issue age is about a half-year older than the same issue age on an ANB basis.
- $\quad$ Experience rates can also vary by many other possible variables, such as gender, tobacco usage and health status, to name just a few. The variations studied depend on the data available, the credibility of cell data and the nature of the rate and business being studied.

Some variables change over time, such as benefit amount, employee status for pension studies (active, retired, or disabled), claim level for disability income studies (full payment or partial payment) and type of long-term care claim for LTC studies (home health care, assisted living or nursing home). In some cases, such as for changing benefit amounts, the study may choose to use the initial, mean or final value for each rate interval. In other cases, it may be important to perform separate studies for each value or "state" of a key variable, such as LTC claim type. Such a study is called a multi-state study:

- $\quad$ Changes in state are referred to as transitions, which are treated as decrements from one state and new entrants to another state.
- The populations for each state are then studied separately, with a time variable for the time spent within each state, instead of for the time since entering the full population.

As a result of the many ways in which rates can vary, a single experience study can be composed of hundreds or thousands of cells. Other than adjustments for partial intervals, the same experience rate calculations apply for all cells.

While most experience rates are tied to insurance, annuities and pensions, there are other applications. For example, experience studies can be performed to calculate default rates and pre-payment rates for bonds and mortgages.

## 4 Simple Mortality Study Examples

In this chapter, we start with some simple examples that will serve as the foundation for later, more complex material.

### 4.1 Cohort Study with Deaths only

Consider a practical example of 1,000 lives with year of birth 1945. All became pensioners at exact age 65 in 2010 and can only leave the study through death. This is called a cohort study: It tracks a group of lives of the same age from the start year through the following years, typically until all lives have died. The table below shows the lives and deaths for each year of age over four years, plus the number of lives reaching age 69.

| Age | Lives | Deaths |
| :---: | ---: | :---: |
| 65 | 1,000 | 7 |
| 66 | 993 | 8 |
| 67 | 985 | 9 |
| 68 | 976 | 10 |
| 69 | 966 |  |
| Total |  | 34 |

The Lives column shows the count of pensioners alive at their birthday in each year, while the Deaths column has the count of pensioners who died within that year of age. At each age, the number of lives is equal to the number of lives at the prior age minus the deaths for the prior age.

For example:

- Life $\mathrm{A}$ is a pensioner who turned 65 on May $10^{\text {th }}, 2010$, and is alive throughout the study. Life A contributes a count of one life for each age and year of the study.
- Life B is a pensioner who turned 65 on September $27^{\text {th }}, 2010$, and died on February $16^{\text {th }}, 2012$. Life B contributes one life for ages 65 and 66, and one death for age 66.

Going forward, we will use the following notation for these columns:

- $\quad l_{x}$ is the number of surviving lives alive at exact age $x$.
- $d_{x}$ is the number of deaths over the year of age $x$.

It follows that

$$
l_{x+1}=l_{x}-d_{x} .
$$

For those alive at the beginning of the year of age $\mathrm{x}$, the probability of dying during year $x$, also known as the mortality rate, is

$$
q_{x}=d_{x} / l_{x}
$$

The probability of surviving or persisting to the end of age $x$ is

$$
p_{x}=l_{x+1} / l_{x}=1-q_{x}
$$

Collectively, $l_{x}, d_{x}, q_{x}$ and $p_{x}$ form what is called a "life table" or "actuarial table," as shown below. A life table contains the elements of a basic experience study. In this case, the life table is a single decrement table, as only one decrement, mortality, is considered.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | :---: | :---: |
| 65 | 1,000 | 7 | 0.00700 | 0.99300 |
| 66 | 993 | 8 | 0.00806 | 0.99194 |
| 67 | 985 | 9 | 0.00914 | 0.99086 |
| 68 | 976 | 10 | 0.01025 | 0.98975 |
| 69 | 966 |  |  |  |
| Total |  | 34 |  |  |

### 4.1.1 Summary Rates with Deaths Only

Summary rates for the duration of the study can sometimes be useful. The average annual mortality rate over the study can be calculated as the weighted average of the rates for each year using $l_{x}$, the number of lives at the beginning of each year, as the weights, for $x=65$ to 68 :

$$
q=\Sigma\left(l_{x} q_{x}\right) / \Sigma l_{x}=\Sigma d_{x} / \Sigma l_{x}=34 / 3,954=0.00860
$$

The probabilities of a life aged 65 dying within four years (denoted as ${ }_{4} q_{65}$ ) or surviving for four years (denoted as 4p65) can be calculated directly from the starting lives and total deaths as:

$$
\begin{aligned}
& { }_{4} q_{65}={ }_{4} d_{65} / l_{65}=34 / 1,000=0.03400 \text { and } \\
& { }_{4} p_{65}=\left(l_{65}-{ }_{4} d_{65}\right) / l_{65}=l_{69} / l_{65}=966 / 1,000=0.96600 .
\end{aligned}
$$

Alternatively, the four-year survival rate can be calculated as the product of the yearly survival rates:

$$
{ }_{4} p_{65}=p_{65} p_{66} p_{67} p_{68}=0.99300 * 0.99194 * 0.99086 * 0.98975=0.96600
$$

The four-year mortality rate can then be calculated from the four-year survival rate:

$$
{ }_{4} q_{65}=1-{ }_{4} p_{65}=1-0.96600=0.03400 .
$$

### 4.2 Cohort Study with Deaths and Withdrawals

In most situations, it is not possible to follow all lives from entry into the study until their ultimate death, as people may withdraw from the study for a variety of reasons unrelated to death. We will define a new variable to reflect such withdrawals:

$w_{x}$ will represent the number of withdrawals for any reason other than death, such as surrender, lapse, expiry, maturity and conversion, over the year of age $x$.

The number of surviving lives at each age is now reduced by both deaths and withdrawals since the previous age, that is:

$$
l_{x+1}=l_{x}-d_{x}-w_{x}
$$

A new life table with surviving lives, deaths and withdrawals is given below.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: |
| 65 | 1,000 | 7 | 5 |
| 66 | 988 | 8 | 4 |
| 67 | 976 | 9 | 6 |
| 68 | 961 | 10 | 4 |
| 69 | 947 |  |  |
| Total |  | 34 | 19 |

The previous mortality rate formula $\left(q_{x}=d_{x} / l_{x}\right)$ is no longer accurate in the presence of withdrawals because deaths that occur after withdrawal will not be known. Therefore, the withdrawing life is only exposed to the risk of death in the study from exact age $x$ up to the date of withdrawal. We need to adjust the mortality rate formula to compensate for this reduced exposure to the risk of death.

We will compensate for withdrawals by replacing the number of lives at exact age $x,\left.\right|_{x}$, with the exposure over the year of age $x$, which we will denote as $E_{x}$. The annual exposure method will calculate exposure based on the amount of time each life was exposed to the risk of death during the year of age $x$, as follows:

- $\quad$ Lives active at the start and end of the year of age $x$ will be assigned exposure of one year.
- Deaths during the year of age $x$ will be assigned exposure of one year. This results in a mortality rate that:

$\circ$ is independent of when deaths occur during the year and

- cannot exceed one.
- $\quad$ Withdrawals during the year of age $x$ will be assigned exposure equal to the fraction of the year from exact age $x$ to the date of withdrawal.

The mortality rate for age $x$ can then be calculated as deaths for exact age $x$ divided by exposure for exact age $x$ :

$$
q_{x}=d_{x} / E_{x}
$$

Due to withdrawals, the survival rate $p_{x}$ cannot be calculated as $l_{x+1} / l_{x}$. Instead, the mortality survival rate is calculated as

$$
p_{x}=1-q_{x}
$$

Both the mortality rate and the mortality survival rate can be referred to as single decrement or independent rates, because they are calculated to be independent of withdrawal decrements. Since the exposure is based on the lives at the start of the year of age $x$, the exposure can be referred to as initial exposure, and the resulting rates as initial rates.

While the annual exposure method's calculation for withdrawal exposure is intuitive, it implicitly assumes a distribution of the deaths. The exposure description above can be expressed formulaically, where there are $l_{x}$ lives at the start of age $x$, with $M$ lives withdrawing during the year, and each life $i$ withdrawing at time $t_{i}$ in the year:

$$
E_{x}=\left(l_{x}-\mathrm{M}\right)+\sum_{i=1}^{M}\left(t_{i}\right)=l_{x}-\sum_{i=1}^{M}\left(1-t_{i}\right)
$$

Substituting this exposure formula into the mortality rate formula gives:

$$
q_{x}=d_{x} /\left(l_{x}-\sum_{i=1}^{M}\left(1-t_{i}\right)\right)
$$

Rearranging the above formula, the number of deaths can be expressed as:

$$
d_{x}=l_{x} q_{x}-\sum_{i=1}^{M}\left(1-t_{i}\right) q_{x}
$$

The second term is an approximation for the number of deaths that occur after withdrawal, assuming the mortality rate from the date of withdrawal to the end of the year of age is proportional to the annual rate over the year, that is:

$$
{ }_{1-t_{i}} q_{x+t_{i}} \approx\left(1-t_{i}\right) q_{x}
$$

The above assumption allows exposure and mortality rates for withdrawals to be easily approximated, but at a cost: The assumption implies that mortality rates decrease over the year. While this result is not obvious, a simple example illustrates this: Consider a full-year rate of $20 \%$. The assumption results in a $10 \%$ rate for the second half of the year. The rate for the first half of the year is therefore equal to $1-(1-20 \%) /(1-10 \%)=11.11 \%$, which exceed the $10 \%$ rate for the second half of the year.

As actual mortality rates generally increase over the year, the above assumption can introduce errors into the final rates. As withdrawals are generally small compared to the total population, these errors are usually small and are usually ignored. In the United States and Canada, this assumption is called the Balducci Hypothesis, although in the United Kingdom, it is referred to as "a convenient but unsatisfying approximation."

### 4.2.1 Individual Exposure Calculation

Exposure that is calculated directly from the underlying dates is referred to as the direct or individual exposure method. This is the method used by most experience studies, as the seriatim calculation of individual exposures is both simple and more accurate. To illustrate with a cohort study, consider the following lives:

- Life A is a pensioner who turned 65 on May $10^{\text {th }}, 2010$, and remained alive throughout the study.
- $\quad$ Life B is a pensioner who turned 65 on September $27^{\text {th }}, 2010$, and died on February $16^{\text {th }}, 2012$.
- $\quad$ Life C is a pensioner who turned 65 on July $3^{\text {rd }}, 2010$, and withdrew on October $21^{\text {st }}, 2012$.

The table below shows, for each life, the exposure start date for each age $x$, which also serves as the exposure end date for the prior age $x-1$.

| $\boldsymbol{x}$ | 65 | 66 | 67 | 68 | 69 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Life A | $5 / 10 / 2010$ | $5 / 10 / 2011$ | $5 / 10 / 2012$ | $5 / 10 / 2013$ | $5 / 10 / 2014$ |
| Life B | $9 / 27 / 2010$ | $9 / 27 / 2011$ | $9 / 27 / 2012$ |  |  |
| Life C | $7 / 3 / 2010$ | $7 / 3 / 2011$ | $7 / 3 / 2012$ | $10 / 21 / 2012$ |  |

Dates of note for individual lives and ages are:

- Life A, age 69, is exposed to the study end date.
- Life $B$, age 67 , is exposed to the birthday following the date of death, because exposure for a death is equal to one.
- Life $\mathrm{C}$, age 68, is exposed to the date of withdrawal.

The number of days exposed for each life in each rate year is calculated as Date $(x+1)-\operatorname{Date}(x)$.

| $\boldsymbol{x}$ | $\mathbf{6 5}$ | $\mathbf{6 6}$ | $\mathbf{6 7}$ | $\mathbf{6 8}$ |
| :---: | :---: | :---: | :---: | :---: |
| Life A | 365 | 366 | 365 | 365 |
| Life B | 365 | 366 |  |  |
| Life C | 365 | 366 | 110 |  |

The exposure for each life for each year of age is found by dividing the number of days in the year of age by the total number of days in that year of age.

| $\boldsymbol{x}$ | 65 | 66 | 67 | 68 |
| :---: | :---: | :---: | :---: | :---: |
| Life A | 1.000 | 1.000 | 1.000 | 1.000 |
| Life B | 1.000 | 1.000 |  |  |
| Life C | 1.000 | 1.000 | 0.301 |  |

### 4.2.2 Grouped Exposure Calculation

Exposure calculated from aggregate data, such as a life table, is referred to as the grouped or census exposure method. Before computers were widely available, the grouped exposure method was the only viable way of calculating exposure. If decrements are assumed to occur uniformly over the year of age $x$, then the exposure as defined above can be estimated by the following formula which gives deaths a full year of exposure in the year of death and withdrawals a half year of exposure:

$$
\begin{aligned}
E_{x} & =l_{x+1}+d_{x}+1 / 2 w_{x} \\
& =l_{x}-d_{x}-w_{x}+d_{x}+1 / 2 w_{x} \\
& =l_{x}-1 / 2 w_{x}
\end{aligned}
$$

That is, estimated exposure is the lives at the start of age $x$ less half the withdrawals over age $x$.

Rather than assuming that all withdrawals are exposed for half a year, a study could be performed on a representative sample to determine a more accurate average exposure for withdrawals. For most individual life business, withdrawals would typically be exposed to the risk of death for more than half a year because lapses occur only on premium due dates at the end of a policy month, quarter, half-year or year.

An enhanced life table, with exposure added, is shown below. This is a multiple decrement table, as both mortality and withdrawal decrements are considered in the cohort study.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| ---: | ---: | ---: | ---: | ---: | :---: | :---: |
| 65 | 1,000 | 7 | 5 | 997.5 | 0.00702 | 0.99298 |
| 66 | 988 | 8 | 4 | 986.0 | 0.00811 | 0.99189 |
| 67 | 976 | 9 | 6 | 973.0 | 0.00925 | 0.99075 |
| 68 | 961 | 10 | 4 | 959.0 | 0.01043 | 0.98957 |
| 69 | 947 |  |  |  |  |  |
| Total |  | 34 | 19 | $3,915.5$ | 0.00868 |  |

### 4.2.3 Summary Rates with Deaths and Withdrawals

The average annual mortality rate over a multiple decrement study is the weighted average of the rates for each year, just as it was for a single decrement study, for $x=65$ to 68 :

$$
q=\Sigma\left(E_{x} q_{x}\right) / \Sigma E_{x}=\Sigma d_{x} / \Sigma E_{x}=34 / 3,915.5=0.00868
$$

A four-year mortality survival rate must be calculated as the product of the mortality survival rates for each of the four years:

$$
{ }_{4} p_{65}=p_{65} p_{66} p_{67} p_{68}=(0.99298)(0.99189)(0.99075)(0.98957)=0.96564
$$

To properly reflect exposure, the four-year mortality rate must be calculated as one minus the four-year mortality survival rate:

$$
{ }_{4} q_{65}=1-{ }_{4} p_{65}=1-0.96564=0.03436
$$

### 4.3 Period Study with Deaths and Withdrawals

The preceding cohort study examples took a single cohort of lives entering at the same age and followed them through subsequent years until all lives had died or withdrawn. This approach is rarely practical, given the long remaining life span of the lives at entry.

A period study or static study fixes the study between a start date and an end date, then captures the experience between those dates. The experience before the start date and after the end date is excluded. In survival analysis, these excluded periods are called left-truncated and right-censored, respectively.

For a period study, the definition of exposure needs to be extended to include fractional ages that arise at the start and end of the study period. Exposure will reflect the amount of time each life was exposed to the risk of death during the year of age $x$ and will be calculated as follows:

- $\quad$ Lives active at both the start and end of the year of age $x$ will be assigned exposure of one year.
- $\quad$ Deaths during the year of age $x$, for lives active at the start of the year of age, will be assigned exposure of one year.
- $\quad$ Withdrawals during the year of age $x$ will be assigned exposure for the fraction of the year from exact age $x$ to the date of withdrawal.
- $\quad$ Lives active at the end of the study period during the year of age $x$ will be assigned exposure for the fraction of the year from exact age $x$ to the end date.
- $\quad$ Lives active at the start of the study period during the year of age $x$ will be assigned exposure for the fraction of the year from the start date to the exact age $x+1$.
- $\quad$ Deaths during the year of age $x$ for lives active at the start of the study period will be assigned exposure for the fraction of the year from the start date to the exact age $x+1$.

A word on dates: We will assume that all events occur at 11:59 pm on the day before a given date. This means that studies consisting of one or more calendar years will start and stop on January 1. Also, this means exposure for a year of age includes the birthday at the start of the year of age and excludes the birthday at the end of the year of age. Similarly, exposure for a policy year includes the policy anniversary at the start of the policy year and excludes the policy anniversary at the end of the policy year. For a lapse on a policy anniversary, using 11:59 pm on the day before the anniversary assures that the lapse is allocated to the proper policy year. The date assumption may need to be adjusted for certain events under study. For example, a death on the policy anniversary would be incorrectly assigned to the prior policy year by using 11:59 on the day before. Deaths should therefore be assumed to occur at 11:59 pm on the date of death, not the prior day.

Exposure for the partial years at the start and end of the study assumes partial year rates are proportional to the annual rate, i.e. the Balducci Hypothesis. However, unlike for withdrawals, this assumption is applied to the entire population for those partial years. Hence, the errors arising will be more significant, although they may be minimized under certain conditions.

For the partial ages at the start and end of the study, lives active throughout the partial ages are assigned exposure for the fraction of the year in the study. For the partial ages at the end of a study, deaths are assigned a full year of exposure which ensures that as the number of deaths increases to equal the number of lives, the rate increases to, but does not exceed, $100 \%$. However, this will result in the annual rate being understated and, when exposure is interpreted as the amount of time, it may seem as though deaths are being assigned exposure past the end of the study period.

For the partial ages at the start of the study, deaths are only assigned exposure for the fraction of year in the study, which will result in the annual rate being overstated and can result in rates greater than $100 \%$ when the number of decrements is large relative to the number of lives. For example, assuming policies are issued mid-year, if the number of deaths is greater than half the number of lives, the rate will be greater than $100 \%$. This can occur where
the number of lives is small in absolute terms or where the decrement rate is high such as for older age mortality or post-level-term renewal lapses. However, in a full study, the exposure for an age will include partial ages at the start and end of the study from different birth years, The errors arising in these partial ages at the start and end of the study will offset and, under certain conditions, net to zero.

### 4.3.1 Individual Exposure Calculation

Detailed information for each life is usually available and can be used to calculate exposure more exactly. The seriatim calculation of individual exposures is both simpler and more accurate. To illustrate the calculation of individual exposure from underlying dates, we will examine details for three new pensioners (Lives D, E and F), along with the three previous ones (Lives A, B and C). As in the previous example, our study will have a start date of $1 / 1 / 2010$ and an end date of $1 / 1 / 2014$ and a minimum age of 65 .

Here is the study data for the two new pensioners (Details for pensioners A, B and C are shown in Section 4.2.1):

- Life D turned 65 on February $12^{\text {th }}, 2009$ and did not die or withdraw during the study.
- $\quad$ Life E turned 65 on October $30^{\text {th }}, 2009$ and died on December $27^{\text {th }}, 2013$.
- $\quad$ Life F turned 65 on July $5^{\text {th }}, 2009$ and died on March $17^{\text {th }}, 2010$.

The following table illustrates a period study using individual exposure calculations. It shows the start and end dates for each pensioner at each age. Other than the initial start date and the final end date, the end date for one age is the same birthday that serves as the start date for the next age.

| $\boldsymbol{x}$ | 65 | 66 | 67 | 68 | 69 | 70 |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| Life A | $5 / 10 / 2010$ | $5 / 10 / 2011$ | $5 / 10 / 2012$ | $5 / 10 / 2013$ | $1 / 1 / 2014$ |  |
| Life B | $9 / 27 / 2010$ | $9 / 27 / 2011$ | $9 / 27 / 2012$ |  |  |  |
| Life C | $7 / 3 / 2010$ | $7 / 3 / 2011$ | $7 / 3 / 2012$ | $10 / 21 / 2012$ |  |  |
| Life D | $1 / 1 / 2010$ | $2 / 12 / 2010$ | $2 / 12 / 2011$ | $2 / 12 / 2012$ | $2 / 12 / 2013$ | $1 / 1 / 2014$ |
| Life E | $1 / 1 / 2010$ | $10 / 30 / 2010$ | $10 / 30 / 2011$ | $10 / 30 / 2012$ | $10 / 30 / 2013$ | $10 / 30 / 2014$ |
| Life F | $1 / 1 / 2010$ | $7 / 5 / 2010$ |  |  |  |  |

For Lives B and C, the dates and exposure calculations are the same as for the Cohort Study above, while Life A is now exposed to the end date of the study, which precedes its $69^{\text {th }}$ (next) birthday. Exposure for Lives D, E and $F$ is determined as follows:

- The initial start date for Lives $D, E$ and $F$ is the start date of the study, since they turned 65 before the start date.
- The final end date for Life $D$ is the end date of the study, since it had neither died nor withdrawn by the end date of the study.
- The final end dates for Lives $\mathrm{E}$ and $\mathrm{F}$ are the birthdays following the dates of death, since the death occurred within the study period and deaths are exposed until the next birthday.

The following table shows the number of days exposed for each life at each age, calculated as Date $(x+1)-\operatorname{Date}(x)$ :

| $\boldsymbol{x}$ | 65 | 66 | 67 | 68 | 69 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Life A | 365 | 366 | 365 | 236 |  |
| Life B | 365 | 366 |  |  |  |
| Life C | 365 | 366 | 110 |  |  |
| Life D | 42 | 365 | 365 | 366 | 323 |
| Life E | 302 | 365 | 366 | 365 | 365 |
| Life F | 185 |  |  |  |  |

The exposure for each life at each age is found by dividing the number of days of exposure by the number of days between consecutive birthdays.

| $\boldsymbol{x}$ | 65 | 66 | 67 | 68 | 69 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Life A | 1.000 | 1.000 | 1.000 | 0.647 |  |
| Life B | 1.000 | 1.000 |  |  |  |
| Life C | 1.000 | 1.000 | 0.301 |  |  |
| Life D | 0.115 | 1.000 | 1.000 | 1.000 | 0.885 |
| Life E | 0.827 | 1.000 | 1.000 | 1.000 | 1.000 |
| Life F | 0.507 |  |  |  |  |

Note that there are three kinds of partial years of exposure in the table above:

- Life $\mathrm{A}$ is exposed from its 67th birthday in 2013 to the $1 / 1 / 2014$ study end date,
- Life D is exposed from its 68th birthday in 2013 to the $1 / 1 / 2014$ study end date,
- Life $\mathrm{C}$ is exposed from its birthday in 2013 to its withdrawal date of 10/21/2012 and
- $\quad$ Lives D, E and F are exposed from the 1/1/2010 study start date to their $66^{\text {th }}$ birthdays in 2010.

The individual exposure method lends itself to automation. In the above example, separate records would be created for year of age for each life. Then, knowing only the study start and end dates and each life's entry date and termination date and reason (i.e., death or withdrawal), a simple algorithm can be devised to calculate exposure and deaths for each year of age for each life. Results can then be summed by age or other attributes.

To illustrate the scope of attributes that can be collected in an industry study, please see the Guaranteed Issue/Simplified Issue Data Request. Only a fraction of the attributes collected in this data call were useful. Since each attribute corresponds to an added dimension, this is to be expected: There is rarely sufficient data to perform a credible n-dimensional study when $\mathrm{n}$ is larger than 4 or 5 . However, some attributes are useful for identifying and excluding fractions of the data that are not homogenous with the bulk of the data.

### 4.3.2 Grouped Exposure Calculation

When detailed information for each life is not available, the grouped exposure method can be used to approximate the exposure. The grouped exposure method is often used for at least a portion of group mortality and disability studies because many large employers provide only summary information to group insurers.

To accommodate the fractional ages at the start and end of the study period, the time spent in the study, $T_{x}$, will be incorporated into the exposure formula. We will use the following notation:

- $\quad T_{x}$ will represent the time spent in the study during age $x$,
- $\quad{ }_{\mathrm{t}} E_{x}$ will represent exposure from exact age $x$ to exact age $x+t$,
- $l_{x+t}$ will represent lives at exact age $x+t$,
- $\quad{ }_{\mathrm{t}} d_{x}$ will represent deaths from exact age $x$ to exact age $x+t$, and
- $\quad{ }_{\mathrm{t}} w_{x}$ will represent withdrawals from exact age $x$ to exact age $x+t$.

The study will consist of lives born in 1944 who enter the study part way through their year of age 65 in 2010. There were 994 lives at the start of the study. Lives will exit the study no later than the study end date. The table below shows the number of lives and deaths by age.

The following example illustrates a period study using grouped exposure calculations. All lives are aged 65 at the study start date $(1 / 1 / 2010)$. The number of lives, $l_{65}$, is as of the study start date, not at exact age 65 in 2009 . The last age, 69, runs from exact age 69 to the study end date (1/1/2014).

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: |
| 65 | 994 | 4 | 2 |
| 66 | 988 | 8 | 4 |
| 67 | 976 | 9 | 6 |
| 68 | 961 | 10 | 4 |
| 69 | 947 | 5 | 2 |
| Total |  | 36 | 18 |

Assuming that withdrawals are spread uniformly over the year of age, the formula for exposure can be adapted to incorporate $T_{x}$ as follows:

For the partial year at the end of the study starting at age $x$ with $t=T_{x}$, deaths are exposed to the end of the year, and the exposure is given by

$$
{ }_{\mathrm{t}} E_{x}=T_{x} l_{x+t}+{ }_{\mathrm{t}} d_{x}+1 / 2 T_{x}{ }_{\mathrm{t}} w_{x}
$$

For the partial year at the start of the study starting at age $x$ with $1-t=T_{x}$, deaths are not exposed for the period prior to the study, as they are alive at the start of the study, and exposure is given by

$$
{ }_{1-\mathrm{t}} E_{x+t}=T_{x} l_{x+t}+T_{x 1-\mathrm{t}} d_{x+t}+1 / 2 T_{x 1-\mathrm{t}} w_{x+t}
$$

Assuming that birthdays are spread uniformly over the calendar year, the study will use $T_{65}$ and $T_{69}$ equal to 0.5 , since, on the average, the study begins halfway through age 65 , and ends halfway through age 69 . All other ages will have a full year of exposure, with $T_{x}$ equal to 1.0.

Using the exposure definition above, the exposure for lives aged 69 , who leave the study at an average age of $691 / 2$ with $T_{69}=1 / 2$, is:

$$
{ }_{1 / 2} E_{69}=1 / 2 l_{691 / 2}+{ }_{1 / 2} d_{69}+1 / 4 \frac{1 / 2}{} w_{69}
$$

Note that deaths are assigned a full year of exposure. (To simplify the formula, withdrawals were assumed to be uniformly distributed over a half-year. If this assumption were deemed unacceptable, the formula could be adjusted.) The result is that withdrawals are exposed for one-quarter of a year on average. Replacing the ending lives with lives at the start of the year, i.e., $l_{69 \frac{1}{2}}=l_{69}-{ }_{1 / 2} d_{69}-{ }_{1 / 2} w_{69}$, produces a formula for an alternate point of view: It shows that, if the beginning lives are exposed for half a year, then deaths must be exposed for an additional half-year and exposure for withdrawals must be reduced by a quarter-year.

$$
1 / 2 E_{69}=1 / 2 l_{69}+1 / 2{ }_{1 / 2} d_{69}-1 / 4 \frac{1 / 2}{} w_{69} .
$$

The exposure for lives aged 65 , who enter the study at exact age $65 \frac{1}{2}$, with time $T_{65}=1 / 2$ in the study, is adjusted to reflect deaths:

$$
{ }_{1 / 2} E_{651 / 2}=1 / 2 l_{66}+1 / 2{ }_{1 / 2} d_{651 / 2}+1 / 4{ }_{1 / 2} w_{651 / 2}
$$

Replacing the ending lives with lives at the start of the year, using $l_{66}=l_{65 \frac{11 / 2}{}}-\frac{1 / 2}{} d_{65 \frac{1}{2}-}-{ }_{1 / 2} w_{65 \frac{1}{2}}$, and then simplifying, we have:

$$
{ }_{1 / 2} E_{65^{1 / 2}}=1 / 2 l_{65^{1 / 2}}-1 / 4_{1 / 2} w_{65^{1 / 2}}
$$

Note that the end of period formula differs from the above beginning of period formula: There is no need to expose deaths for an additional half-year in the latter formula since they have already been exposed to the end of age $x$.

The table below, using the full-year notation for simplicity, includes the exposure calculation and rates.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | :---: | :---: | :---: | :---: |
| 65 | 994 | 4 | 2 | 0.5 | 496.5 | 0.00806 | 0.99194 |
| 66 | 988 | 8 | 4 | 1.0 | 986.0 | 0.00811 | 0.99189 |
| 67 | 976 | 9 | 6 | 1.0 | 973.0 | 0.00925 | 0.99075 |
| 68 | 961 | 10 | 4 | 1.0 | 959.0 | 0.01043 | 0.98957 |
| 69 | 947 | 5 | 2 | 0.5 | 475.5 | 0.01052 | 0.98948 |
| Total |  | 36 | 18 |  | $3,890.0$ | 0.00925 |  |

Imagine a group of lives such that new entrants, annual aging and deaths exactly offset to produce a stable population with the same number of lives at each age, year after year. Further assume that their birthdays are uniformly distributed over the calendar year. When this stable population is studied, each age will have a partial year at the start of the study period with a corresponding partial year at the end of the study period. Together, these two partial years produce the same result as the full-year exposure formula. For such an imaginary population, the full-year exposure formula can be used for all ages.

### 4.4 Amount-Weighted Studies

So far, lives have been equally weighted for study purposes. More often, each life in a study is weighted by an amount that is a measure of premium, volume or size associated with that life. Typically, the amount is a benefit amount. For each life in an amount-weighted study, the same weight is used for both the event under study (such as death) and its exposure calculation.

We will use the following notation for amount-weighted results. While " $B$ " comes from "Benefit amount," it could represent any kind of amount.

$$
\begin{aligned}
& B_{x} \text { will represent the benefit amount for age } \mathrm{x}, \\
& { }_{B} l_{x} \text { will represent amount-weighted lives in force, } \\
& { }_{B} d_{x} \text { will represent amount-weighted deaths, } \\
& { }_{B} w_{x} \text { will represent amount-weighted withdrawals, } \\
& { }_{B} E_{x} \text { will represent amount-weighted exposure, and } \\
& { }_{B} q_{x} \text { will represent the amount-weighted mortality rate. }
\end{aligned}
$$

As usual, the mortality rate is calculated as deaths divided by exposure:

$$
{ }_{B} q_{x}={ }_{B} d_{x} /{ }_{B} E_{x} .
$$

Notation indicating amount-weighting would only be included when required by the context, such as when lifeweighted and amount-weighted formulas are used together. Normally, life-weighted notation (i.e., without the B subscript) would be used for amount-weighted.

### 4.4.1 Individual Amount Weights

Each life usually has its own amount weight. The amount-weighted exposure for each life is equal to the exposure for the life times its amount weight. The next table illustrates amount weights that differ by life and amountweighted exposure by age, for five lives. Lives $A$ and $C$ withdrew, while lives B and E died. Only life D survived from the beginning to the end of the study period.

| $\boldsymbol{x}$ | $\mathrm{B}_{\mathbf{x}}$ | 65 | 66 | 67 | 68 | 69 |
| :---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Life A | 1,000 | 1,000 | 1,000 | 1,000 | 647 |  |
| Life B | 1,500 | 1,500 | 1,500 |  |  |  |
| Life C | 800 | 800 | 800 | 241 |  |  |
| Life D | 1,200 | 138 | 1,200 | 1,200 | 1,200 | 1,062 |
| Life E | 2,000 | 1,655 | 2,000 | 2,000 | 2,000 | 2,000 |
| Life F | 1,700 | 862 |  |  |  |  |

The above results match the individual life exposures shown in the last table in Section 4.3.1 times the amount weights for each life.

Summarizing the above results by age into the following life table, we see exposure for all five ages, deaths only at ages 66 and 69 and, not surprisingly because of the small number of lives, highly volatile mortality rates:

| $\boldsymbol{x}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | :---: | :---: |
| 65 | 5,955 | 1,700 | 0.28550 | 0.71450 |
| 66 | 6,500 | 1,500 | 0.23077 | 0.76923 |
| 67 | 4,441 | 0 | 0.00000 | 1.00000 |
| 68 | 3,847 | 0 | 0.00000 | 1.00000 |
| 69 | 3,062 | 2,000 | 0.65319 | 0.34681 |
| Total | 23,804 | 5,200 | 0.21845 |  |

### 4.4.2 Grouped Amount Weights

When data on individual lives is not available, it is usually possible to calculate different average benefit amounts for deaths, withdrawals and lives in force. To illustrate this, we will start our example with the following life table:

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | :---: | :---: | :---: | :---: |
| 65 | 994 | 4 | 2 | 0.5 | 496.5 | 0.00806 | 0.99194 |
| 66 | 988 | 8 | 4 | 1.0 | 986.0 | 0.00811 | 0.99189 |
| 67 | 976 | 9 | 6 | 1.0 | 973.0 | 0.00925 | 0.99075 |
| 68 | 961 | 10 | 4 | 1.0 | 959.0 | 0.01043 | 0.98957 |
| 69 | 947 | 5 | 2 | 0.5 | 475.5 | 0.01052 | 0.98948 |
| Total |  | 36 | 18 |  | $3,890.0$ | 0.00925 |  |

The following average benefit amounts will apply:

- $B_{l_{65}}$ will denote the average benefit in force at the beginning of the study, which will be $\$ 1,500$,
- $B_{d_{x}}$ will denote the average benefit paid on death, which will vary by age, ranging from $\$ 1,350$ to $\$ 1,450$, and
- $\quad B_{w_{x}}$ will denote the average death benefit for withdrawals, which will be $\$ 1,500$ for all ages.

The following relationships will be used to develop amount-weighted results based on average benefit amounts:

- ${ }_{B} l_{65}=B_{l_{65}} l_{65}$
- ${ }_{B} d_{x}=B_{d_{x}} d_{x}$
- ${ }_{B} w_{x}=B_{w_{x}} w_{x}$, and
- ${ }_{B} l_{x+1}={ }_{B} l_{x}-{ }_{B} d_{x}-{ }_{B} w_{x}$.

Average benefit amounts are shown below, along with the amount-weighed life table. Amount-weighted lives, deaths, and withdrawals are per thousand.

| $\boldsymbol{x}$ | $\boldsymbol{B}_{\boldsymbol{d}_{\boldsymbol{x}}}$ | $\boldsymbol{B}_{\boldsymbol{w}_{\boldsymbol{x}}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{l}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{w}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | ---: | ---: |
| 65 | $\$ 1,400$ | $\$ 1,500$ | $1,491.0$ | 5.6 | 3.0 |
| 66 | $\$ 1,450$ | $\$ 1,500$ | $1,482.4$ | 11.6 | 6.0 |
| 67 | $\$ 1,375$ | $\$ 1,500$ | $1,464.8$ | 12.4 | 9.0 |
| 68 | $\$ 1,425$ | $\$ 1,500$ | $1,443.4$ | 14.3 | 6.0 |
| 69 | $\$ 1,350$ | $\$ 1,500$ | $1,423.2$ | 6.8 | 3.0 |
| Total | $\$ 1,400$ |  |  | 50.6 | 27.0 |

Exposure, which is also per thousand, will be calculated using the following formula, which assumes that decrements are uniformly distributed over each year of age:

$$
{ }_{B} E_{x}=T_{x B} l_{x}-1 / 2 T_{x{ }_{B}} w_{x} .
$$

As usual, mortality rates are calculated as deaths divided by exposure, to obtain the following results:

| $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{l}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{p}_{\boldsymbol{x}}$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 65 | $1,491.0$ | 5.6 | 3.0 | 0.5 | 744.8 | 0.00752 | 0.99248 |
| 66 | $1,482.4$ | 11.6 | 6.0 | 1.0 | $1,479.4$ | 0.00784 | 0.99216 |
| 67 | $1,464.8$ | 12.4 | 9.0 | 1.0 | $1,460.3$ | 0.00847 | 0.99153 |
| 68 | $1,443.4$ | 14.3 | 6.0 | 1.0 | $1,440.4$ | 0.00989 | 0.99011 |
| 69 | $1,423.2$ | 6.8 | 3.0 | 0.5 | 714.2 | 0.00945 | 0.99055 |
| Total |  | 50.6 | 27.0 |  | $5,839.1$ | 0.00866 |  |

The above amount-weighted mortality rates are lower than the corresponding life-weighted mortality rates shown near the beginning of this section. This is not surprising since amount-weighted deaths had lower average death benefits than did amount-weighted exposure.

## 5 Distributed Exposure

Readers focused on fundamentals may choose to bypass Chapters 5 and 6, which present important alternatives. Chapters 5 and 6 are recommended but not essential reading. Readers focused on fundamentals should skip or skim Chapters 7-10 and resume at Chapter 11.

In Chapter 4, we saw that the annual exposure method assigned a full year of exposure to deaths in the partial year at the end of the study. However, deaths in the partial year at the beginning of the study were assigned exposure only from the beginning of the study to the end of the year of age.

An alternative is the distributed exposure method, which allocates exposure more evenly to the partial years at the beginning and end of the study. A full year of annual exposure is distributed between the two partial years that constitute the rate year (e.g., policy year) of death. For the partial rate years at the start and end of the study period:

- Exposure for each death in a rate year (e.g., policy year) that begins in the last calendar year of the study is calculated from the beginning of the rate year to the study end date. If deaths are uniformly distributed, this produces an average of a half-year of exposure for each death, or half as much exposure as the annual exposure method. The remainder of the annual exposure for these deaths is distributed to the calendar year at the beginning of a subsequent study that starts where the current study left off.
- $\quad$ Exposure for each death in the rate year (e.g., policy year) ending in the first calendar year of the study are exposed from the study start date to the end of the rate year. This will include exposure on some deaths that occurred prior to the study start date, namely the remainder of the annual exposure from the prior study that is distributed to the beginning of the current study, which starts where the prior study left off.

The distributed exposure method requires inclusion of roughly half of the deaths that occurred in the year before the study period. These deaths will only be used to calculate exposure and will not be counted as deaths in the study.

With this approach, exposure for each partial year is proportional to the full annual exposure, which implies a uniform distribution of deaths. To investigate this, first consider the partial year from $x$ to $x+\mathrm{t}$ that occurs at the end of the study period. The number of lives at the start of age $x$, is $N=l_{x}$, and for each life $i$ the study ends at time $t_{i}$ in the year. Using the definition of exposure above, the number of deaths should be equal to the lives exposed multiplied by the mortality rate for each life, where ${ }_{t_{i}} q_{x}$ is the mortality rate experienced from age $x$ to age $x+t_{i}$ :

$$
d_{x}=\sum_{i=1}^{N}\left(t_{i} q_{x}\right)
$$

To simplify this, the partial year mortality rate, $t_{i} q_{x}$, is assumed to be proportional to the full year mortality rate:

$$
t_{i} q_{x}=t_{i} q_{x}
$$

The formula for deaths then becomes:

$$
d_{x}=\sum_{i=1}^{N}\left(t_{i} q_{x}\right)=q_{x} \sum_{i=1}^{M}\left(t_{i}\right)
$$

Solving for $q_{x}$, we have:

$$
q_{x}=d_{x} / \sum_{i=1}^{N}\left(t_{i}\right)
$$

The denominator in the formula above equals exposure, so:

$$
E_{x}=\sum_{i=1}^{N}\left(t_{i}\right)
$$

For the partial year from age $x+t$ to $x+1$ at the start of the study period, let the number of lives at the start of age $x$, before the start of the study, be $N=l_{x}$ and, for each life $i$, including deaths before the study start date, the study starts at time $t_{i}$ in the year of age. Using the definition of exposure above, the number of deaths should equal the lives exposed multiplied by the mortality rate for each life, where ${ }_{1-t_{i}} q_{x+t_{i}}$ is the mortality rate experienced from age $x+t_{i}$ to age $x+1$ :

$$
d_{x}=\sum_{i=1}^{N}\left({ }_{1-t_{i}} q_{x+t_{i}}\right) .
$$

To simplify this, assume that the partial year mortality rate, ${ }_{1-t_{i}} q_{x+t_{i}}$, is proportional to the mortality rate for the full year:

$$
{ }_{1-t_{i}} q_{x+t_{i}}=\left(1-t_{i}\right) q_{x}
$$

The formula for deaths then becomes:

$$
\begin{aligned}
d_{x} & =\sum_{i=1}^{N}\left(\left(1-t_{i}\right) q_{x}\right) \\
& =q_{x} \sum_{i=1}^{N}\left(1-t_{i}\right)
\end{aligned}
$$

Solving for $q_{x}$, we have:

$$
q_{x}=d_{x} /\left(\sum_{i=1}^{N}\left(1-t_{i}\right)\right) .
$$

Once again, the denominator in the formula above equals exposure:

$$
E_{x}=\sum_{i=1}^{N}\left(1-t_{i}\right)
$$

In practice, the partial ages at the start of the study period do not include exposure arising from deaths prior to the study start date. Hence, the partial ages at the start of the study assume that deaths are distributed by the Balducci hypothesis, while the partial ages at the end of the study assume that deaths are uniformly distributed. This method is called the in-period exposure method, reflecting that deaths are only assigned exposure equal to the period in which the death falls. This method is also called the hybrid exposure method, indicating that different underlying assumptions are used for the partial ages at the start and end of the study. When exposure is calculated and split by both policy year and calendar year, exposure for deaths may or may not be carried forward into the following calendar year, depending on whether each calendar year is considered a separate study.

Compared to the annual exposure method, this method will reduce, but not eliminate, the overstatement of the rates calculated after the policy anniversary, but can result in rates greater than $100 \%$ if the number of decrements is large relative to the number of lives. However, while these errors will be offset in a full study, there is no longer a symmetry between the errors arising before and after the policy anniversary, since the errors arise from different underlying assumptions.

### 5.1 Period Study

Using the period study example from the end of Section 4.3, the exposure for full years is unchanged, but the exposure formulas for the partial years at the start and end of the study become:

$$
\begin{aligned}
& { }_{1 / 2} E_{69}=1 / 2 l_{69}-1 / 4_{1 / 2} w_{69} . \\
& { }_{1 / 2} E_{65 \frac{1}{2} 2}=1 / 2 l_{65^{1 / 2}}-1 / 4_{1 / 2} w_{65 \frac{1}{2}}+1_{1 / 2}{ }_{1 / 2} d_{65}
\end{aligned}
$$

As a reminder, for simplicity, the above formulas assume that withdrawals are uniformly distributed over each halfyear. In practice, most studies would reflect exact dates of deaths and withdrawals rather than using approximations such as those shown above.

The following table shows the exposure and rates using the distributed exposure method. Compared to the results in Section 4.3, the exposure for age 65.5 has increased by 1.5 (one-half-year of exposure on the three deaths from the first half of age 65) and the exposure for age 69 has decreased by 2.5 (one half-year of exposure on the five deaths for age 69). The table includes the decrements for the first half of age 65.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: | ---: | ---: | :---: | :---: |
| 65.0 |  | 3 | 3 |  |  |  |  |
| 65.5 | 994 | 4 | 2 | 0.5 | 498.0 | 0.00803 | 0.99197 |
| 66.0 | 988 | 8 | 4 | 1.0 | 986.0 | 0.00811 | 0.99189 |
| 67.0 | 976 | 9 | 6 | 1.0 | 973.0 | 0.00925 | 0.99075 |
| 68.0 | 961 | 10 | 4 | 1.0 | 959.0 | 0.01043 | 0.98957 |
| 69.0 | 947 | 5 | 2 | 0.5 | 473.0 | 0.01057 | 0.98943 |
| Total |  | 36 | 18 |  | $3,889.0$ | 0.00926 |  |

## 6 Fractional Rates

To this point, we have dealt only with annual rates. In practice, there are a number of situations where rates vary considerably over the course of a year. In such situations, it is common to develop fractional rates for fractional periods such as weeks or months. This enables more accurate weekly or monthly calculations.

Fractional rates can also be used in situations where the fractional rate is not expected to change over the year:

- In some cases, fractional rates can be used to reduce distortions created when annual exposure calculations are applied to partial years.
- The average of a year's worth of fractional rates can be converted to an equivalent annual rate.

We will use the following notation:

- $\quad N$ will denote the number of fractional periods per year; for monthly, $N=12$,
- $\quad f=1 / N$ will denote the length of a fractional period of time; for monthly, $f=1 / 12$, and
- $t$ will denote a fractional period within the year, with $t$ ranging from 0 to $N-1$; for monthly, the months are numbered 0 through 11.

The exposure for each fractional period is given below. Each fractional period is assigned a full period of exposure, not a fraction of a year, as rates are being calculated for the fraction of a year. For example, for a monthly period, exposure is calculated in months and the resulting rate is a monthly rate.

Deaths are exposed to the end of the fractional period, not to the end of the year. For monthly, the death would be exposed to the end of the month of death. The exposure formula for a fractional period is similar to that for a oneyear period:

$$
\begin{aligned}
{ }_{f} E_{x+f t} & =l_{x+f(t+1)}+{ }_{f} d_{x+f t}+1 / 2{ }_{f} w_{x+f t} \\
& =l_{x+f t}-1 / 2{ }_{f} w_{x+f t} .
\end{aligned}
$$

The mortality rate for the fractional period is given by:

$$
{ }_{f} q_{x+f t}={ }_{f} d_{x+f t} /{ }_{f} E_{x+f t}
$$

For example, a monthly rate is calculated as deaths for one month divided by exposure for one month.

For those not used to working with fractional rates, it can be helpful to convert them to equivalent annualized rates to allow comparison to existing annual rates. The first step is to calculate the fractional survival rate:

$$
{ }_{f} p_{x+f t}=1-{ }_{f} q_{x+f t} .
$$

The equivalent annualized mortality rate, ${ }_{\mathrm{f}} q_{x+t}^{A}$, can then be calculated as:

$$
{ }_{f} q_{x+f t}^{A}=1-\left({ }_{f} p_{x+f t}\right)^{N}
$$

Alternately, where deaths are not uniformly distributed, the annualized survival rate can be calculated as the product of a year's worth of fractional survival rates:

$$
p_{x}=\Pi_{f} p_{x+f t}
$$

The annual equivalent decrement rate is then:

$$
q_{x}=1-p_{x}
$$

### 6.1 Half-Year Period Study

To illustrate fractional calculations, we will calculate half-year or semi-annual rates for half-years, with $N=2$

periods per year and $f=1 / 2$ of a year per period.

Other than some minor changes to the headings, the first four columns in the table below are identical to those from the table in Section 4.3. The fifth column now shows values of 1.0 instead of 0.5 , because a half-year is now being treated as a full period. That one difference causes exposure to double and the mortality rate to halve in the next two columns. In the final column, you will find the annualized equivalent of each half-year rate, which closely approximates the mortality rate from the example in Section 4.3.

| $x$ | ${ }_{f} l_{x+f t}$ | ${ }_{f} d_{x+f t}$ | $f w_{x+f t}$ | $T_{x+f t}$ | ${ }_{f} E_{x+f t}$ | ${ }_{f} q_{x+f t}$ | ${ }_{f} \boldsymbol{q}_{x+f t}^{A}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 65.5 | $1,491.0$ | 5.6 | 3.0 | 1.0 | $1,489.5$ | 0.00376 | 0.00751 |
| 66.0 | $1,482.4$ | 5.8 | 3.0 | 1.0 | $1,480.9$ | 0.00392 | 0.00782 |
| 66.5 | $1,473.6$ | 5.8 | 3.0 | 1.0 | $1,472.1$ | 0.00394 | 0.00786 |
| 67.0 | $1,464.8$ | 6.2 | 4.5 | 1.0 | $1,462.6$ | 0.00423 | 0.00844 |
| 67.5 | $1,454.1$ | 6.2 | 4.5 | 1.0 | $1,451.9$ | 0.00426 | 0.00851 |
| 68.0 | $1,443.4$ | 7.1 | 3.0 | 1.0 | $1,441.9$ | 0.00494 | 0.00986 |
| 68.5 | $1,433.3$ | 7.1 | 3.0 | 1.0 | $1,431.8$ | 0.00498 | 0.00993 |
| 69.0 | $1,423.2$ | 6.8 | 3.0 | 1.0 | $1,421.7$ | 0.00475 | 0.00947 |
| Total |  | 50.6 | 27.0 | 8.0 | $11,652.3$ | 0.00434 | 0.00866 |

### 6.2 Average Fractional Rates

An alternative to calculating annual exposure is to assume that the mortality rate is uniform for the year and then calculate an average fractional rate for the year. Such a rate can be calculated in either of two equivalent ways:

- As the sum of deaths for the year divided by the sum of fractional exposure for the year, or
- As the weighted average of fractional rates, where fractional exposure is used as the weight.

We will use ${ }_{f} \bar{q}_{x}$ to represent the average fractional rate for the year of age $x$. We will calculate it as the weighted average of the fractional rates, ${ }_{f} q_{x+f t}$, weighted by fractional exposure, ${ }_{f} E_{x+f t}$ :

$$
{ }_{f} \bar{q}_{x}=\Sigma\left({ }_{f} E_{x+f t f} q_{x+f t}\right) / \Sigma_{f} E_{x+f t} .
$$

Substituting for rates, which equal decrements divided by exposure, we have:

$$
{ }_{f} \bar{q}_{x}=\Sigma_{f} d_{x+f t} / \Sigma_{f} E_{x+f t}=d_{x} / \Sigma_{f} E_{x+f t}
$$

This shows that the weighted average of the fractional rates is indeed equal to decrements divided by the sum of fractional exposure.

Assuming a constant mortality rate over the year, the average fractional rate can be annualized using the formula developed in the prior section:

$$
{ }_{f} \bar{q}_{x}^{A}=1-\left(1-{ }_{f} \bar{q}_{x}\right)^{N}
$$

In practice, for ages with only a small number of lives, such as for the youngest and oldest ages, the constant mortality assumption does not hold and the method breaks down. To illustrate, consider a cell with one life that dies at the end of the year of age. With exposure calculated in half years, the two fractional rates would be $0 \%$ and $100 \%$ for an average fractional rate of $50 \%$. The result would be an annualized fractional rate of $75 \%$, rather than the $100 \%$ rate one would expect.

We can relate annual exposure, $E_{x}$, to average fractional exposure, $f \Sigma_{f} E_{x+t}$, as follows:

- Annual exposure gives each death an exposure of one per year in the year of death, whereas fractional exposure gives an exposure of one per fractional period in the period of death.
- $\quad$ This translates to total fractional exposure of $t+1$ per year for deaths in period $t$ and an average fractional exposure for all periods combined of $(N+1) / 2$.
- $\quad$ Dividing by $N$ to convert to the annual equivalent, we have an average fractional exposure of $(N+1) / 2 N=$ $1 / 2(1+f)$ for all deaths combined. Hence, the annual equivalent exposure assigned to deaths using a fractional approach is $1 / 2(1-f)$ per year less than the annual exposure. This assumes a uniform distribution of deaths.
- All other components of annual exposure are exactly equal to the sum of their fractional counterparts divided by $N$ (or multiplied by $f$ ).

Applying the above relationships, we have:

$$
E_{x}=f \Sigma_{f} E_{x+t}+1 / 2(1-f) d_{x}
$$

This leads to the following relationship between the average fractional rate, $f \bar{q}_{x}$, and the annual rate, $q_{x}$ :

$$
{ }_{f} \bar{q}_{x}=f d_{x} /\left(E_{x}-1 / 2(1-f) d_{x}\right)=f q_{x} /\left(1-1 / 2(1-f) q_{x}\right)
$$

The first five columns in the following table restate the results of the half-yearly example shown at the end of Section 6.1. Results for two half-years were combined for ages 66, 67 and 68 , with the sums of two fractional exposures divided by two to convert them to their annual equivalents. The last two columns illustrate the results of annualizing the average fractional rates.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | ${ }_{1 / 2} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{f}} \overline{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{A}}$ | ${ }_{\boldsymbol{f}} \overline{\boldsymbol{p}}_{\boldsymbol{x}}^{\boldsymbol{A}}$ |
| :---: | :---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 65 | $1,491.0$ | 5.6 | 3.0 | 0.5 | 744.8 | 0.00751 | 0.99249 |
| 66 | $1,482.4$ | 11.6 | 6.0 | 1.0 | $1,476.5$ | 0.00784 | 0.99216 |
| 67 | $1,464.8$ | 12.4 | 9.0 | 1.0 | $1,457.2$ | 0.00847 | 0.99153 |
| 68 | $1,443.4$ | 14.3 | 6.0 | 1.0 | $1,436.9$ | 0.00989 | 0.99011 |
| 69 | $1,423.2$ | 6.8 | 3.0 | 0.5 | 710.8 | 0.00947 | 0.99053 |
| Total |  | 50.6 | 27.0 | 4.0 | $5,826.2$ | 0.00866 | 0.99134 |

The next table compares annual rates and exposure from the amount-weighted period study in Section 12.2 with annualized fractional rates and exposure from the above table.

| $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{1}{ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | $\boldsymbol{f}_{\boldsymbol{\boldsymbol { q }}} \overline{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{A}}$ | $\boldsymbol{q}_{\boldsymbol{x}}-{ }_{\boldsymbol{f}} \overline{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{A}}$ |
| ---: | ---: | ---: | :---: | :---: | :--- |
| 65 | 744.8 | 744.8 | 0.00752 | 0.00751 | $1.4 \times 10^{-5}$ |
| 66 | $1,479.4$ | $1,476.5$ | 0.00784 | 0.00784 | $3.0 \times 10^{-8}$ |
| 67 | $1,460.3$ | $1,457.2$ | 0.00847 | 0.00847 | $3.8 \times 10^{-8}$ |
| 68 | $1,440.4$ | $1,436.9$ | 0.00989 | 0.00989 | $6.1 \times 10^{-8}$ |
| 69 | 714.2 | 710.8 | 0.00945 | 0.00947 | $-2.2 \times 10^{-5}$ |
| Total | $5,839.1$ | $5,826.2$ | 0.00866 | 0.00866 | $-3.9 \times 10^{-7}$ |

Except for the age 65 partial year, the annual exposure in the above table is greater than the average of the two half-year exposures. This is because annual exposure exposed deaths for a full year, while each half-year exposure, which was divided by two, exposed deaths for only a half-year. For the full years, the relationship between these two exposures, assuming decrements are uniformly distributed, is:

$$
E_{x}=1 / 2\left(\frac{1 / 2}{} E_{x}+1 / 2 E_{x+1 / 2}\right)+1 / 4 d_{x}
$$

The annual rates in the above table match the annualized fractional rates very closely, to the order of $10^{-8}$, for the full years of ages 66 to 68 . For the partial year at the start of the study, age 65 , the annual rate is larger by $1.4 \times 10^{-5}$. For the partial year at the end of the study, age 69 , the annual rate is smaller by $-2.2 \times 10^{-5}$. For all ages combined, the average annual rate matches the average annualized fractional rate to the order of $10^{-7}$ because differences at the start and end of the study largely offset each other.

The following table shows the formulas used for annual rates, annualized half-year rates, and the difference between them for the partial years at the start and end of the study.

| Age | Annual Rates | Annualized Half-Year Rates | Difference |
| :---: | :---: | :---: | :---: |
| $65 \frac{1 / 2}{}$ | $2\left(\frac{1 / 2}{} q_{65 \frac{1}{2}}\right)$ | $1-\left(1-{ }_{1 / 2} q_{651 / 2}\right)^{2}$ | $+\left({ }_{1 / 2} q_{65 \frac{1}{2}}\right)^{2}$ |
| 69 | $2\left({ }_{1 / 2} q_{69} /\left(1+_{1 / 2} q_{69}\right)\right)$ | $1-\left(1-{ }_{1 / 2} q_{69}\right)^{2}$ | $-\left(1 / 29 q_{69}\right)^{2}$ |

If we approximate a half-year mortality rate as half of an annual mortality rate, the above difference formulas can be approximated in terms of the annual rates as follows:

| Age | Difference | Approximate <br> Difference |
| :---: | :---: | :---: |
| $65 \frac{11 / 2}{}$ | $+\left(1 / 2 q_{651 / 2}\right)^{2}$ | $+1 / 4\left(q_{65}\right)^{2}$ |
| 69 | $-\left(\frac{11 / 2}{} q_{69}\right)^{2}$ | $-1 / 4\left(q_{69}\right)^{2}$ |

The above differences are essentially the square of a mortality rate divided by four, so the closeness of fit is not surprising for small mortality rates.

These differences arise from the underlying assumptions for each method. For annual exposure, the underlying assumption is that the mortality rate for the partial year is proportional to the rate for the full year. This means the mortality rate for half a year would be half of the annual rate. The mortality rate for the half-year starting at age $651 / 2$ is, therefore, assumed to be $1 / 2 q_{65}$.

For age 69, the proportional assumption is applied to the half-year after the end of the study. In other words, the mortality rate for the half-year that is not included in the study is assumed to be $1 / 2 q_{69}$. In order to reproduce the annual rate, $q_{69}$, the mortality rate for half-year starting at age 69 must equal the following:

$$
1 / 2 q_{69} /\left(1-1 / 2 q_{69}\right) .
$$

By examining the above formula, we see that the mortality rate for the first half of the year will always be greater than that for the second half of the year. In other words, assuming a proportionate mortality rate for the second half of the year results in decreasing mortality.

By contrast, the assumption underlying the annualized half-yearly rate is that the mortality rate is the same for each half-year. In order to reproduce the annual rate, each half-year rate would have to equal the following:

$$
1-\left(1-1 / 2 q_{x}\right)^{2} .
$$

As mortality rates will generally increase over the year, neither assumption holds true: the annual exposure method implies that rates decrease over the year, while the fractional exposure method implies that rates are constant over the year. For increasing mortality rates, the constant rate assumption will produce smaller errors than the decreasing rate assumption. Where rates are decreasing over the year, such as for lapses, which method produces smaller errors will depend on the degree of decrease.

### 6.3 Annual Period Study by Calendar Year

It is not uncommon to split data for each calendar year into two ages. This allows for additional trending of the study results but introduces partial years into each calendar year. The exposure formulas developed previously can be generalized for policies issued at time $1-t$ in the year at age $x$, where $t$ is the time from the policy anniversary to the end of the calendar year.

From the beginning of the policy year at age $x$ to the end of the calendar year, we have:

$$
{ }_{t} E_{x}=l_{x+t} t+{ }_{t} d_{x}+1 / 2 t{ }_{t} t
$$

From the end of the calendar year to the next policy anniversary at age $x+1$, we have:

$$
{ }_{1-t} E_{x+t}=l_{x+t}(1-t)-1 / 2{ }_{1-t} w_{x+t}(1-t)
$$

For mid-year policy issues, with $t=1 / 2$, the two half-years of exposure can be calculated as:

${ }_{1 / 2} E_{x}=1 / 2 l_{x+t}+{ }_{1 / 2} d_{x}+1 / 4_{1 / 2} w_{x}$, for exposure from age $\mathrm{x}$ at mid calendar year to end of the calendar year, and

$\frac{1 / 2}{} E_{x+1 / 2}=1 / 2 l_{x+1 / 2}-1 / 4 \frac{1 / 2}{} w_{x+1 / 2}$, for exposure from the end of the calendar year to age $x+1$ at next mid calendar year.

The above formulae can be expressed in terms of lives at the start of the policy year using

$l_{x+1 / 2}=l_{x}-{ }_{1 / 2} d_{x}-{ }_{1 / 2} w_{x}$ :

${ }_{1 / 2} E_{x}=1 / 2 l_{x}+1 / 2_{1 / 2} d_{x}-1 / 4_{1 / 2} w_{x}$, for exposure from age $\mathrm{x}$ at mid calendar year to end of the calendar year, and

${ }_{1 / 2} E_{x+1 / 2}=1 / 2 l_{x}-1 / 2{ }_{1 / 2} d_{x}-1 / 2{ }_{1 / 2} w_{x}-1 / 4_{1 / 2} w_{x+1 / 2}$ for exposure from the end of the calendar year to age $x+1$ at next mid calendar year.

Comparing this formula to the formula for the first half of the year, it is clear that the second half's exposure will always be less than the first half's exposure, except in the trivial case where there are no deaths or lapses. With deaths split evenly between the first and second half, this means mortality rates will always be higher for the second half-year.

Adding the above two half-year exposure formulas, while assuming that withdrawals are evenly split between the two half-years, you will see that the result is the formula for a full year of exposure.

These relationships are illustrated in the following life table showing results for half-years of age:

| $\boldsymbol{y}$ | $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{l}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | ---: | :---: | :---: | :---: | :---: |
| 2010 | 65.5 | $1,491.0$ | 5.6 | 3.0 | 0.5 | 744.8 | 0.00752 | 0.99248 |
| 2010 | 66.0 | $1,482.4$ | 5.8 | 3.0 | 0.5 | 743.4 | 0.00780 | 0.99220 |
| 2011 | 66.5 | $1,473.6$ | 5.8 | 3.0 | 0.5 | 736.1 | 0.00788 | 0.99212 |
| 2011 | 67.0 | $1,464.8$ | 6.2 | 4.5 | 0.5 | 734.4 | 0.00843 | 0.99157 |
| 2012 | 67.5 | $1,454.1$ | 6.2 | 4.5 | 0.5 | 725.9 | 0.00852 | 0.99148 |
| 2012 | 68.0 | $1,443.4$ | 7.1 | 3.0 | 0.5 | 724.5 | 0.00983 | 0.99017 |
| 2013 | 68.5 | $1,433.3$ | 7.1 | 3.0 | 0.5 | 715.9 | 0.00995 | 0.99005 |
| 2013 | 69.0 | $1,423.2$ | 6.8 | 3.0 | 0.5 | 714.2 | 0.00945 | 0.99055 |
| Total |  |  | 50.6 | 27.0 |  | $5,839.1$ | 0.00866 |  |

As expected, exposure for the first half-year of age (e.g., 66.0) is always higher than that for the second half-year of age (e.g., 66.5), while the mortality rate for the first half-year of age is always lower than that for the second half-
year of age. Aggregating exposures and deaths for the two halves of each age (e.g., 66.0 and 66.5) will reproduce the original results for each full year of age.

The difference terms previously shown for the partial years can be generalized to each half-year of age:

| Age | Difference | Approximate <br> Difference |
| :---: | :---: | :---: |
| $x$ | $-\left({ }_{1 / 2} q_{\mathrm{x}}\right)^{2}$ | $-1 / 4\left(q_{\mathrm{x}}\right)^{2}$ |
| $x+1 / 2$ | $+\left(\frac{112}{} q_{\mathrm{x}+1 / 2}\right)^{2}$ | $+1 / 4\left(q_{\mathrm{x}}\right)^{2}$ |

So, for age $x$, the annual rates are larger by $1 / 4\left(q_{x}\right)^{2}$, while for age $x+1 / 2$, rates are smaller by $1 / 4\left(q_{x}\right)^{2}$. The discussion above regarding partial years at the start and end of the study applies when the results for each calendar year are split into two partial years: In effect, each calendar year becomes its own study, containing nothing but the two partial years at the start and end of the study.

Using the distributed exposure method, the results are

| $\boldsymbol{y}$ | $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{l}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{p}_{\boldsymbol{x}}$ |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2010 | 65.5 | $1,491.0$ | 5.6 | 3.0 | 0.5 | 746.9 | 0.00750 | 0.99250 |
| 2010 | 66.0 | $1,482.4$ | 5.8 | 3.0 | 0.5 | 740.5 | 0.00783 | 0.99217 |
| 2011 | 66.5 | $1,473.6$ | 5.8 | 3.0 | 0.5 | 739.0 | 0.00785 | 0.99215 |
| 2011 | 67.0 | $1,464.8$ | 6.2 | 4.5 | 0.5 | 731.3 | 0.00846 | 0.99154 |
| 2012 | 67.5 | $1,454.1$ | 6.2 | 4.5 | 0.5 | 729.0 | 0.00849 | 0.99151 |
| 2012 | 68.0 | $1,443.4$ | 7.1 | 3.0 | 0.5 | 721.0 | 0.00988 | 0.99012 |
| 2013 | 68.5 | $1,433.3$ | 7.1 | 3.0 | 0.5 | 719.5 | 0.00990 | 0.99010 |
| 2013 | 69.0 | $1,423.2$ | 6.8 | 3.0 | 0.5 | 710.8 | 0.00950 | 0.99050 |
| Total |  | $11,665.8$ | 50.6 | 27.0 | 4.0 | $5,837.8$ | 0.00866 | 0.99134 |

Compared to the preceding table, exposures and mortality rates for the two halves of each year of age are much closer to each other: The small differences are due to the effect of withdrawals. The closeness in the rates is due to the distribution of deaths being uniform.

## 7 Average Daily Rates and Exposure

Readers focused on fundamentals should skip or skim Chapters 7-10 and resume at Chapter 11.

Fractional rates can be calculated for increasingly shorter periods. The practical limit is daily rates, with $N=365$, with the study calculating exposure in whole days, and all decrements assumed to occur at the end of the day.

To examine the exposure for fractional periods of one day, $E_{x}^{\text {Day }}$ will represent the sum of daily exposure for all 365 or 366 days of the year. Assuming all decrements occur at the end of the day, daily exposure is equal to the sum of the lives in force at the start of each day of the year. With $N=365$ and $f=1 / 365$, that is:

$$
E_{x}^{\text {Day }}=\sum_{t=0}^{N-1}{ }_{f} E_{x+f t}=\sum_{t=0}^{N-1}{ }_{f} l_{x+f t} .
$$

The same result can be reached by summing the lives in a different way, by figuring the number of days each life is in force during the year and summing that over all lives. To express this, let

$M$ represent the total number of lives,

$t$ represent the day of the year of age $x$, ranging from 1 to 365 or 366 ,

$l_{x+f t}^{i}=1$ for each life $i$ contributing exposure for day $t$ of the year of age $x$,

StartDate $_{i}$ be the date life $i$ enters age $x$, usually the birthday for age $x$, and

EndDate $_{i}$ be the date life $i$ exits age $x$, either the birthday for age $x+1$ or the date of decrement.

Most dates, including the above dates, typically would be calculated and stored as the number of days since an absolute starting date, such as the first day of 1800 .

Using $l_{x}=\sum_{i=1}^{M} l_{x}^{i}$, the daily exposure can be restated as:

$$
\begin{aligned}
E_{x}^{D a y} & =\sum_{t=0}^{N-1} \Sigma_{i=1}^{M} l_{x+f t}^{i} \text { (the sum of the number of lives in force for each day) } \\
& =\sum_{i=1}^{M} \Sigma_{t=0}^{N-1}{ }_{f} l_{x+f t}^{i} \text { (the sum of the number of days in force for each life) } \\
& =\sum_{i=1}^{M}\left(\text { EndDate }_{i}-\text { StartDate }_{i}\right) .
\end{aligned}
$$

This shows that $E_{x}^{D a y}$ is the sum of the number of days in force for each life, with the number of days calculated as the end date minus the start date.

Recalling the relationship between annual and fractional exposure shown in Section 6.2, we have:

$$
E_{x}=f \sum_{f} E_{x+t}+1 / 2(1-f) d_{x}
$$

Using $f=1 / 365$, rearranging terms and substituting for daily exposure, we have:

$$
E_{x}^{\text {Day }}=365\left(E_{x}-1 / 2\left(1-\frac{1}{365}\right) d_{x}\right),
$$

which yields the following approximation:

$$
E_{x}^{\text {Day }} \approx 365\left(E_{x}-1 / 2 d_{x}\right) .
$$

For shorthand, let ${ }_{\text {Day }} \bar{q}_{x}$ be the average daily decrement rate. Then:

$$
{ }_{D a y} \bar{q}_{x}={ }_{1 / 365} \bar{q}_{x}=d_{x} / E_{x}^{\text {Day }} .
$$

The annualized daily rate is then given by:

$$
{ }_{D a y} \bar{q}_{x}^{A}=1-\left(1-{ }_{\text {Day }} \bar{q}_{x}\right)^{365}
$$

In practice, for ages with only a small number of lives, such as for the youngest and oldest ages, the constant mortality assumption does not hold and the method breaks down. To illustrate this breakdown, consider a cell with one life that dies at the end of the year of age. With daily exposure, the daily mortality rate would be $1 / 365$, which annualizes to a rate of $63 \%$ rather than the $100 \%$ rate that one would expect.

### 7.1 Period Study with Daily Exposure

Daily exposure is readily calculated for the whole and partial years that make up the study period. We will use the information available from a life table and the number of days in the study for each age. Let:

$D_{x}$ be the number of days in the study for age $x$, and

$N_{x}$ be the number of days in the full year.

Assuming a uniform distribution of deaths and withdrawals, the daily exposure is:

$$
E_{x}^{\text {Day }}=D_{x}\left(l_{x}-1 / 2 d_{x}-1 / 2 w_{x}\right)
$$

And the annualized daily mortality rate, using standard annual notation, is:

$$
q_{\mathrm{x}}=1-\left(1-{ }_{\text {Day }} \bar{q}_{x}\right)^{N_{x}}
$$

Starting from the period study example in Section 4.3, the following table adds daily exposure, average daily rates, days per year and annualized mortality rates.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{D}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\text {Day }}$ | $\overline{\boldsymbol{q}}_{\boldsymbol{x}}$ | $\boldsymbol{N}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | ---: | :---: | :---: | :---: | :---: |
| 65 | 994 | 4 | 2 | 181 | 179,371 | 0.0000223001 | 365 | 0.00811 |
| 66 | 988 | 8 | 4 | 365 | 358,430 | 0.0000223196 | 365 | 0.00811 |
| 67 | 976 | 9 | 6 | 366 | 354,471 | 0.0000253899 | 366 | 0.00925 |
| 68 | 961 | 10 | 4 | 365 | 348,210 | 0.0000287183 | 365 | 0.01043 |
| 69 | 947 | 5 | 2 | 184 | 173,604 | 0.0000288012 | 365 | 0.01046 |
| Total |  | 36 | 18 |  |  |  |  |  |

The following table compares the annualized daily mortality rates with those previously calculated using annual and half-yearly exposure. (The half-yearly rates were weighted by lives and not by benefit amount as previously shown.)

| $\boldsymbol{x}$ | Annual | Half Yearly | Daily |
| :---: | :---: | :---: | :---: |
| 65 | 0.00806 | 0.00804 | 0.00811 |
| 66 | 0.00811 | 0.00811 | 0.00811 |
| 67 | 0.00925 | 0.00925 | 0.00925 |
| 68 | 0.01043 | 0.01043 | 0.01043 |
| 69 | 0.01052 | 0.01054 | 0.01046 |

For ages 65 and 69 , the annual rates using half-yearly exposure assumed the half-years are exactly one half of the full calendar year. That is, $T_{65}=T_{69}=0.5$. The annual rates using daily exposure calculated each half-year using the exact number of days, so that

$$
\begin{aligned}
& T_{65}=181 / 365=0.49589, \text { and } \\
& T_{69}=184 / 365=0.50411 .
\end{aligned}
$$

So for age 65, the annualized rate resulting from half-year exposure implicitly assumes the calendar year has 362 days (two 181-day halves), or $99.2 \%$ of a full year, while for age 69 , the implicit assumption is 368 days or $100.8 \%$ of
a full year. Daily exposure reflects the exact number of days, so the age 65 rate is appropriately increased and the age 69 rate is appropriately reduced to reflect exactly one year.

For ages 66 to 68, the annual rates match for all exposure methods.

## 8 Average Force of Mortality

As the number of intervals in a fractional rate study increases and the intervals become shorter, the fractional rate becomes increasingly smaller. However, the relationship between the daily and annual exposure shown above implies that the annualized fractional rate approaches a limit as the frequency goes to zero. That is, as $N$ is increasingly large, the annualized fractional rate, $f \bar{q}_{x} / f$, approaches a limit that can be approximated as follows:

$$
{ }_{f} \bar{q}_{x} / f \approx q_{x} /\left(1-1 / 2 q_{x}\right)
$$

assuming a constant decrement rate over the rate year.

As the frequency approaches a limit of zero, the annualized fractional rate approaches the annualized instantaneous mortality rate, better known as the average force of mortality and denoted as $\bar{\mu}_{x}$.

Assuming that the mortality rates are constant for each interval over the year and, hence, the force of mortality is also constant, then:

$$
\bar{\mu}_{x}=\lim _{f \rightarrow 0} \bar{q}_{x} / f
$$

For practical purposes, the average force can be closely approximated by the average daily mortality rate multiplied by the number of days in the year. With $f=1 / 365$, we have:

$$
\bar{\mu}_{x} \approx{ }_{1 / 365} \bar{q}_{x} /(1 / 365)=365_{\text {Day }} \bar{q}_{x}=365\left(d_{x} / E_{x}^{\text {Day }}\right) .
$$

Similarly, daily exposure can be converted to an annual "force" exposure, $E_{x}^{F}$ :

$$
E_{x}^{F}=E_{x}^{\text {Day }} / 365
$$

This force exposure can then be used to calculate the average force:

$$
\bar{\mu}_{x} \approx d_{x} / E_{x}^{F}
$$

By compounding the average fractional survival rate, we can determine the annual survival rate, which is then subtracted from one to give the annual mortality rate:

$$
q_{x}={ }_{f} \bar{q}_{x}^{A}=1-\left({ }_{f} \bar{p}_{x}\right)^{N} .
$$

Applying limits to the compounded fractional survivorship, we have:

$$
\lim _{N \rightarrow \infty}\left({ }_{f} \bar{p}_{x}\right)^{N}=\lim _{N \rightarrow \infty}\left(1-\left({ }_{f} \bar{q}_{x} / f\right) / N\right)^{N}=e^{-\bar{\mu}_{x}}
$$

The mortality rate is then:

$$
q_{x}=1-e^{-\bar{\mu}_{x}} \approx 1-e^{-d_{x} / E_{x}^{F}}
$$

In practice, for ages with only a small number of lives, such as for the youngest and oldest ages, the constant force assumption does not hold and the method breaks down. To illustrate, consider a cell with one life that dies at the end of the year of age. With annual force exposure, the calculated rate would be $63 \%$ rather than the $100 \%$ rate one would expect.

Turning the above formula around, the average force can be calculated from the annual mortality rate:

$$
\bar{\mu}_{x}=-\log _{e}\left(1-q_{x}\right)
$$

There will be a small discrepancy between:

- An annual rate calculated directly from the average daily rate and
- An annual rate calculated using an approximate force of mortality based on the average daily rate.

In other words, the following expressions are not exactly equal, but can be used interchangeably with a high level of accuracy:

$$
\begin{aligned}
& q_{\mathrm{x}}=1-\left(1-{ }_{\text {Day }} \bar{q}_{x}\right)^{365}, \text { and } \\
& q_{x}=1-e^{-365_{\text {Day }} \bar{q}_{x}}
\end{aligned}
$$

For fractional periods, the average force for the fractional period is simply the fraction of the annual average force:

$$
{ }_{f} \bar{\mu}_{x+f t}=f \bar{\mu}_{x}
$$

### 8.1 Period Study with Constant Force

The following table uses deaths and daily exposure to calculate a daily rate, ${ }_{\text {Day }} \bar{q}_{x}$. The daily rate is then used with the number of days in the year of age, $\boldsymbol{N}_{\boldsymbol{x}}$, to estimate both the average force of mortality, $\bar{\mu}_{\boldsymbol{x}}$, and the annualized daily rate, $q_{x}$, which match those developed in the Section 7.1 period study:

| $\boldsymbol{x}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{D a y}}$ | $\boldsymbol{D a y}_{\boldsymbol{y}} \overline{\boldsymbol{q}}_{\boldsymbol{x}}$ | $\boldsymbol{N}_{\boldsymbol{x}}$ | $\overline{\boldsymbol{\mu}}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 65 | 4 | 179,371 | 0.0000223001 | 365 | 0.00814 | 0.00811 |
| 66 | 8 | 358,430 | 0.0000223196 | 365 | 0.00815 | 0.00811 |
| 67 | 9 | 354,471 | 0.0000253899 | 366 | 0.00929 | 0.00925 |
| 68 | 10 | 348,210 | 0.0000287183 | 365 | 0.01048 | 0.01043 |
| 69 | 5 | 173,604 | 0.0000288012 | 365 | 0.01051 | 0.01046 |

In each case, the average force of mortality is slightly greater than its mortality rate counterpart. This makes sense because the force is applied continuously to a decreasing number of survivors over the year of age, while the mortality rate is applied to the lives at the start of the year.

### 8.2 Changing Force of Mortality

An average fractional rate is used to summarize the fractional rates over the year, which vary for each fractional period. Similarly, the average force of mortality summarizes the force of mortality over the year. The force of mortality at each exact age $x+s, \mu_{x+s}$, is defined as:

$\mu_{x+s}=\lim _{f \rightarrow 0} q_{x+s+f} / f$

Unlike the mortality rate, $q_{x}$, and average force of mortality, $\bar{\mu}_{x}$, which are defined for discrete, integer ages, the force of mortality, $\mu_{x+s}$, is defined continuously at each exact age $x+s$. Just as the relationship between the mortality rates across individual ages is non-linear, the relationship between the forces at exact ages $x+s$ within each year of age $x$ is also non-linear. For adults, mortality rates become increasingly larger with age. Likewise, the force of mortality typically increases over time.

When we assume that the force of mortality is constant for a year at a time, it means the force for the year of age $x-1$ is $\bar{\mu}_{x-1}$ and the force for the year of age $x$ is $\bar{\mu}_{x}$. At exact age $x$, the force of mortality is not well defined.

The formula for calculating average force directly from force or daily exposure does not require the constant mortality rate assumption. This is because daily exposure reflects the actual distribution of deaths by exposing each death through the day of death. Therefore, the following formula holds true for all distributions of deaths:

$$
\bar{\mu}_{x} \approx d_{x} / E_{x}^{F}
$$

For continuous decrements, the average force of mortality is approximately equal to the force of mortality at exact age $x+1 / 2$, the midpoint of the year of age. That is,

$$
\mu_{x+1 / 2} \approx \bar{\mu}_{x}=-\log _{e}\left(1-q_{x}\right)
$$

This approximation is only accurate if deaths are uniformly distributed. It is not accurate if we assume a constant or increasing force of mortality. The force of mortality at exact age $x$ can be estimated by averaging the average force of mortality for consecutive ages, i.e.:

$$
\mu_{x} \approx 1 / 2\left(\bar{\mu}_{x-1}+\bar{\mu}_{x}\right)=-1 / 2\left(\log _{e}\left(1-q_{x-1}\right)+\log _{e}\left(1-q_{x}\right)\right)
$$

Using this estimate of the force at exact age $x$, the increase in the force over the year of age $x, \Delta \mu_{x}$, is the difference between the forces at exact ages $x+1$ and $x$ :

$$
\Delta \mu_{x}=\mu_{x+1}-\mu_{x}
$$

Substituting for $\mu_{x+1}$ and $\mu_{x}$, using $\mu_{x} \approx 1 / 2\left(\bar{\mu}_{x-1}+\bar{\mu}_{x}\right)$, and then simplifying, we have:

$$
\Delta \mu_{x}=1 / 2\left(\bar{\mu}_{x+1}-\bar{\mu}_{x-1}\right) .
$$

The increase in the force from exact age $x$ to exact age $x+1$ is equal to half of the two-year increase in the average force. Note that these two average forces are approximately equal to the forces at age $x-1 / 2$ and age $x+1 \frac{1}{2}$, i.e., from half a year before exact age $x$ to half a year after exact age $x+1$.

Where mortality rates are increasing, a reasonable assumption would be that the force of mortality linearly increases over the age of $x$. This assumption would result in the following linear formula for calculating the force at exact age $x+s$ :

$$
\mu_{x+s}=\bar{\mu}_{x}+(s-1 / 2) \Delta \mu_{x} .
$$

This formula ensures that the average force of mortality remains the same, with $\mu_{x+1 / 2}=\bar{\mu}_{x}$. The force at fractional age $x+s$ can now be calculated in terms of average forces:

$$
\mu_{x+s}=\bar{\mu}_{x}+1 / 2(s-1 / 2)\left(\bar{\mu}_{x+1}-\bar{\mu}_{x-1}\right) .
$$

With this approach, the force at exact age $x$ could have two different values, one based on age $x-1$ with $s=1$ and another based on age $x$ with $s=0$. That is, under the linear assumption, the force at the start of the year is:

$$
\mu_{x+0}=\bar{\mu}_{x}-1 / 4\left(\bar{\mu}_{x+1}-\bar{\mu}_{x-1}\right) .
$$

This inconsistency at exact age $x$ is a reflection of the linear assumption. While it reduces the inconsistency when compared to the constant force assumption, it cannot eliminate it: The overall distribution will be non-linear: While the force follows a linear pattern between ages, there will be discontinuities at each age.

The rate at which the force increases or decreases over the year is given by the slope in the linear assumption, which is the relative increase in the force over the year, calculated as:

$$
\Delta_{x}=\Delta \mu_{x} / \bar{\mu}_{x}
$$

$\Delta_{x}$ can be thought of as the annual percentage change in the force of mortality. To illustrate the calculation of average force, increase in force, and relative increase in force, we have used the VBT 2015 mortality table for male non-smokers for ages 65 to 69 :

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\overline{\boldsymbol{\mu}}_{\boldsymbol{x}}$ | $\boldsymbol{\mu}_{\boldsymbol{x}}$ | $\boldsymbol{\Delta} \boldsymbol{\mu}_{\boldsymbol{x}}$ | $\boldsymbol{\Delta}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 65 | 0.006880 | 0.006904 | 0.006562 | 0.000715 | $10.36 \%$ |
| 66 | 0.007620 | 0.007649 | 0.007276 | 0.000776 | $10.14 \%$ |
| 67 | 0.008420 | 0.008456 | 0.008052 | 0.000847 | $10.02 \%$ |
| 68 | 0.009300 | 0.009344 | 0.008900 | 0.000949 | $10.16 \%$ |
| 69 | 0.010300 | 0.010353 | 0.009848 | 0.001096 | $10.59 \%$ |

The next table shows the same information for decennial ages from 50 to 90 :

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\overline{\boldsymbol{\mu}}_{\boldsymbol{x}}$ | $\boldsymbol{\mu}_{\boldsymbol{x}}$ | $\boldsymbol{\Delta} \boldsymbol{\mu}_{\boldsymbol{x}}$ | $\boldsymbol{\Delta}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | 0.001920 | 0.001922 | 0.001877 | 0.000115 | $6.00 \%$ |
| 60 | 0.004080 | 0.004088 | 0.003938 | 0.000351 | $8.60 \%$ |
| 70 | 0.011470 | 0.011536 | 0.010945 | 0.001295 | $11.23 \%$ |
| 80 | 0.038260 | 0.039011 | 0.036750 | 0.004920 | $12.61 \%$ |
| 90 | 0.136900 | 0.147225 | 0.138445 | 0.017959 | $12.20 \%$ |

The above table shows that relative increases in force of 10\% over the year of age are not unusual for adult mortality.

The average force for each fractional period is derived from the exact force at the start and end of the fractional period multiplied by the fractional period. For example, for a half-year study with $f=1 / 2$, starting at age $x$, the average force is:

$$
\begin{aligned}
{ }_{1 / 2} \bar{\mu}_{x} & =f\left(1 / 2\left(\mu_{x+0}+\mu_{x+1 / 2}\right)\right) \\
& =1 / 2\left(\bar{\mu}_{x}-1 / 4 \Delta \mu_{x}\right) \\
& =1 / 2 \bar{\mu}_{x}\left(1-1 / 4 \Delta_{x}\right) .
\end{aligned}
$$

More generally, the average force for the fractional period is:

$$
\begin{aligned}
{ }_{f} \bar{\mu}_{x+f t} & =f\left(\bar{\mu}_{x}-\Delta \mu_{x}(1 / 2(N-1)-t) / N\right) \\
& =f \bar{\mu}_{x}\left(1-\Delta_{x}(1 / 2(N-1)-t) / N\right) .
\end{aligned}
$$

## 9 Distributions of Deaths

When calculating annual rates, assumptions are required regarding how the deaths are distributed over the year, both for dealing with withdrawals, and for dealing with partial years arising at the start and end of the study period.

- When calculating annual rates for partial years, the assumption implicit in the annual exposure formula is that the mortality rate for the partial year is proportional to the rate for the full year, i.e., the Balducci Hypothesis.
- When calculating annual rates for partial years using the distributed exposure method, the assumption implicit in the annual exposure formula is that the deaths are uniformly distributed over the year.
- When calculating annualized fractional mortality rates, the mortality rate is assumed to be constant over all the fractional periods.

These assumptions are used to enable or simplify exposure calculations for withdrawals and for partial years at the start and end of the study period. Differences between assumed and actual distributions will introduce errors into the estimated annual rates developed from partial years. It is useful to understand the nature of such errors.

These assumptions assume that decrements act continuously over the year.

A uniform distribution of deaths (UDD) assumes that, for $d_{x}$ deaths in the year of age $x$, the deaths within a fraction of the year $t$ are equal to $t d_{x}$. This means that the mortality rate for the fraction of the year from time 0 to time $t$ is proportional to the mortality rate for the full year, i.e.,

$$
{ }_{t} q_{x}=t q_{x}
$$

This assumption was used when calculating distributed exposure. The UDD assumption results in fractional rates that increase over the year.

The UDD mortality rate for the fraction of the year from time $t$ to the end of the year is not so simple:

$$
\begin{aligned}
{ }_{1-t} q_{x} & =1-\left(1-q_{x}\right) /\left(1-t q_{x}\right) \\
& =\left((1-t) q_{x}\right) /\left(1-t q_{x}\right)
\end{aligned}
$$

This is not the assumption used when adjusting annual exposure for withdrawals or for partial years that start at the beginning or middle of the year, as it would make the calculations more difficult. UDD produces fractional mortality rates that increase during the year, since the number of deaths for each period stays constant, while the number of surviving lives decreases.

Instead, to produce another linear formula, the exposure reductions for withdrawals and partial years assume that the mortality rate for the partial year from time $t$ to the end of the year is proportional to the mortality rate for the full year, i.e.,

$$
{ }_{1-t} q_{x+t}=(1-t) q_{x}
$$

This is called the Balducci Hypothesis. It produces a mortality rate for the fraction of the year from time 0 to time $t$ that is not as simple:

$$
{ }_{t} q_{x}=t q_{x} /\left(1-(1-t) q_{x}\right)
$$

While UDD produces fractional rates that increase during the year, the Balducci Hypothesis produces fractional rates that decrease during the year. Interestingly, the absolute values of these rates of increase and decrease are equal.

The assumption used for calculating annualized fractional mortality rates for partial years is that the mortality rate is constant over all of the fractional periods. This means the mortality rate from the start of the year up to time $t$ can be calculated as:

$$
{ }_{t} q_{x}=1-\left(1-q_{x}\right)^{t}
$$

### 9.1 Comparison of Distributions

To recap, the uniform distribution of death assumption results in mortality rates that increase over the year, while annualized fractional rates assume constant mortality rates. The Balducci assumption results in mortality rates that decrease over the year. The differences between the three distributions are negligible for small mortality rates, but significant for large mortality rates. The graph below illustrates monthly mortality rates resulting from the three distribution assumptions, using an annual mortality rate of $12 \%$. While none of the assumptions are consistent with increasing adult mortality rates, UDD is at least directionally correct for most adult ages.

For the Balducci Hypothesis (BH) and the uniform distribution (UDD), the slope of the monthly rates is roughly equal to the size of the rate, but opposite in direction. For a $12 \%$ mortality rate, the monthly rates for the Balducci Hypothesis decrease by $12 \%$ over the year, while for the UDD, they increase by $12 \%$ over the year. The constant mortality rate (CMR) assumption produces a level $12 \%$ mortality rate.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_77542591393347e2e981g-043.jpg?height=648&width=1247&top_left_y=814&top_left_x=385" alt="image" style="width:100%;height:auto;">

We will examine each of the three assumptions in more depth using the same one-year monthly study that begins with 1,000 lives at the start of the year of age $x$, and applies a single decrement with a $12 \%$ annual decrement rate. For the annual study, we have:

$$
\begin{aligned}
& E_{x}=l_{x}=1,000 \text { and } \\
& d_{x}=E_{x} q_{x}=120 .
\end{aligned}
$$

For the monthly study, with $N=12$ and $f=1 / 12$, we will use the fractional notation already introduced, with $t$ used to denote a fractional period ranging from 0 to 11 . In each case, the distribution of deaths will be driven by the assumption being illustrated. We will first calculate monthly mortality rates, ${ }_{f} q_{x+f t}$, for each assumption, and then use the monthly mortality rates to calculate monthly survivors, ${ }_{f} l_{x+f t}$, and deaths, ${ }_{f} d_{x+f t}$, as follows:

$$
\begin{aligned}
& { }_{f} d_{x+f t}={ }_{f} l_{x+f t} \cdot{ }_{f} q_{x+f t} \text { and } \\
& { }_{f} l_{x+f(t+1)}={ }_{f} l_{x+f t}-{ }_{f} d_{x+f t} .
\end{aligned}
$$

Once the survivors and deaths have been calculated, formulas for exposures and rates can be applied.

Monthly tables will show how monthly rates and exposure change over the year. In addition, half-year results will show how partial year rates based on annual exposure and annualized monthly rates compare to the annual rate.

### 9.1.1 Balducci Hypothesis

Since the Balducci Hypothesis is the assumption backing the adjustments that reduce annual exposure for withdrawals and for partial years, it will be considered first.

Using fractional notation, with $t=0$ representing the start of the first fractional period, the cumulative mortality rate from the start of age $x$ through the fractional period beginning at age $x+f t$ and ending at age $x+f(t+1)$ is:

$$
f(t+1) q_{x}=f(t+1) q_{x} /\left(1-(1-f(t+1)) q_{x}\right)
$$

Using $t=0$ and $f=1 / 12$, the mortality rate for the first month is:

$$
{ }_{1 / 12} q_{x}=\frac{1}{12} q_{x} /\left(1-\left(1-\frac{1}{12}\right) q_{x}\right)=\frac{1}{12} q_{x} /\left(1-\frac{11}{12} q_{x}\right)=q_{x} /\left(12-11 q_{x}\right)
$$

The probability of surviving from age $x+f t$ to age $x+f(t+1)$ is equal to:

- The probability of surviving from age $x$ to age $x+f(t+1)$ divided by
- The probability of surviving from age $x$ to age $x+f t$.

Therefore, the probability of dying between age $x+f t$ and age $x+f(t+1)$ is equal to:

$$
{ }_{f} q_{x+f t}=1-\left(1-{ }_{f(t+1)} q_{x}\right) /\left(1-{ }_{f t} q_{x}\right)
$$

The following table shows, for each month $t$, beginning number of lives, number of deaths, monthly exposure $\left({ }_{f} E_{x+f t}\right)$, monthly mortality rate and its annualized equivalent. The first mortality rate shown in the Total line is calculated as total deaths divided by total monthly exposure. The next mortality rate is its annualized equivalent.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f} \boldsymbol{t}}^{\boldsymbol{A}}$ |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $1,000.0$ | 11.2 | $1,000.0$ | 0.01124 | 0.12680 |
| 1 | 988.8 | 11.0 | 988.8 | 0.01111 | 0.12548 |
| 2 | 977.8 | 10.7 | 977.8 | 0.01099 | 0.12418 |
| 3 | 967.0 | 10.5 | 967.0 | 0.01087 | 0.12291 |
| 4 | 956.5 | 10.3 | 956.5 | 0.01075 | 0.12167 |
| 5 | 946.2 | 10.1 | 946.2 | 0.01064 | 0.12045 |
| 6 | 936.2 | 9.9 | 936.2 | 0.01053 | 0.11925 |
| 7 | 926.3 | 9.6 | 926.3 | 0.01042 | 0.11808 |
| 8 | 916.7 | 9.5 | 916.7 | 0.01031 | 0.11693 |
| 9 | 907.2 | 9.3 | 907.2 | 0.01020 | 0.11581 |
| 10 | 898.0 | 9.1 | 898.0 | 0.01010 | 0.11470 |
| 11 | 888.9 | 8.9 | 888.9 | 0.01000 | 0.11362 |
| Total |  | 120.0 | 11309.6 | 0.01061 | 0.12015 |

The monthly rates decrease over the year because of the "uniform distribution of deaths" assumption associated with the Balducci Hypothesis. The annualized monthly mortality rate in the Total line $(0.120152)$ is slightly higher than the $12 \%$ annual rate.

The following table illustrates that the annual exposure method which, when applied to each month, produces twelve monthly rates that match the annual mortality rate. This is because deaths were distributed according to the Balducci Hypothesis, the same assumption that underlies the annual exposure method.

| $\boldsymbol{t}$ | $\boldsymbol{f}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{f}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: | :---: |
| 0 | $1,000.0$ | 11.2 | 93.63 | 0.120000 |
| 1 | 988.8 | 11.0 | 91.55 | 0.120000 |
| 2 | 977.8 | 10.7 | 89.54 | 0.120000 |
| 3 | 967.0 | 10.5 | 87.59 | 0.120000 |
| 4 | 956.5 | 10.3 | 85.71 | 0.120000 |
| 5 | 946.2 | 10.1 | 83.89 | 0.120000 |
| 6 | 936.2 | 9.9 | 82.12 | 0.120000 |
| 7 | 926.3 | 9.6 | 80.41 | 0.120000 |
| 8 | 916.7 | 9.5 | 78.75 | 0.120000 |
| 9 | 907.2 | 9.3 | 77.14 | 0.120000 |
| 10 | 898.0 | 9.1 | 75.59 | 0.120000 |
| 11 | 888.9 | 8.9 | 74.07 | 0.120000 |
| Total |  | 120.0 | $1,000.00$ | 0.120000 |

To illustrate the partial years arising at the start and end of a period study, the next table shows a half-year study.

| $\boldsymbol{t}$ | $\boldsymbol{f}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: | :---: |
| 0 | $1,000.0$ | 63.83 | 531.91 | 0.120000 |
| 1 | 936.2 | 56.17 | 468.09 | 0.120000 |
| Total |  | 120.00 | $1,000.00$ | 0.120000 |

For both half-years, the semi-annual rate matches the annual rate because deaths were projected using the Balducci assumption. The first half-year, from age $x$ to $x+1 / 2$, would apply to a partial year that occurs at the end of a study period. The second half-year, from age $x+1 / 2$ to $x+1$, would apply to a partial year that occurs at the start of a study period.

### 9.1.2 Uniform Distribution of Deaths

The distributed exposure method assumes a uniform distribution of deaths.

Using fractional notation, the deaths can be calculated directly as:

$$
{ }_{f} d_{x+f t}=f d_{x}
$$

The following table has the same structure as the prior table showing monthly rates:

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{A}}$ |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $1,000.0$ | 10.00 | $1,000.0$ | 0.01000 | 0.11362 |
| 1 | 990.0 | 10.00 | 990.0 | 0.01010 | 0.11470 |
| 2 | 980.0 | 10.00 | 980.0 | 0.01020 | 0.11581 |
| 3 | 970.0 | 10.00 | 970.0 | 0.01031 | 0.11693 |
| 4 | 960.0 | 10.00 | 960.0 | 0.01042 | 0.11808 |
| 5 | 950.0 | 10.00 | 950.0 | 0.01053 | 0.11925 |
| 6 | 940.0 | 10.00 | 940.0 | 0.01064 | 0.12045 |
| 7 | 930.0 | 10.00 | 930.0 | 0.01075 | 0.12167 |
| 8 | 920.0 | 10.00 | 920.0 | 0.01087 | 0.12291 |
| 9 | 910.0 | 10.00 | 910.0 | 0.01099 | 0.12418 |
| 10 | 900.0 | 10.00 | 900.0 | 0.01111 | 0.12548 |
| 11 | 890.0 | 10.00 | 890.0 | 0.01124 | 0.12680 |
| Total |  | 120.0 | $11,340.0$ | 0.010582 | 0.11985 |

The monthly rates increase over the year because of the "uniform distribution of deaths" assumption. The average annualized monthly mortality rate in the Total line (0.11985) is slightly lower than the $12 \%$ annual rate.

The following table illustrates that the distributed exposure method, when applied to each month, produces twelve monthly rates that match the annual mortality rate. This is because deaths were distributed uniformly, the same assumption that underlies the distributed exposure method.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: | :---: |
| 0 | $1,000.0$ | 10.00 | 83.33 | 0.12000 |
| 1 | 990.0 | 10.00 | 83.33 | 0.12000 |
| 2 | 980.0 | 10.00 | 83.33 | 0.12000 |
| 3 | 970.0 | 10.00 | 83.33 | 0.12000 |
| 4 | 960.0 | 10.00 | 83.33 | 0.12000 |
| 5 | 950.0 | 10.00 | 83.33 | 0.12000 |
| 6 | 940.0 | 10.00 | 83.33 | 0.12000 |
| 7 | 930.0 | 10.00 | 83.33 | 0.12000 |
| 8 | 920.0 | 10.00 | 83.33 | 0.12000 |
| 9 | 910.0 | 10.00 | 83.33 | 0.12000 |
| 10 | 900.0 | 10.00 | 83.33 | 0.12000 |
| 11 | 890.0 | 10.00 | 83.33 | 0.12000 |
| Total |  | 120.0 | $1,000.00$ | 0.120000 |

To illustrate the partial years arising at the start and end of a period study, the next table shows a half-year study.

| $\boldsymbol{t}$ | $\boldsymbol{f}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ |
| ---: | ---: | ---: | ---: | :---: |
| 0 | $1,000.0$ | 60.00 | 500.00 | 0.12000 |
| 1 | 940.0 | 60.00 | 500.00 | 0.12000 |
|  |  | 120.00 | $1,000.00$ | 0.12000 |

For both half-years, the semi-annual rate matches the annual rate because deaths were uniformly distributed. The first half-year, from age $x$ to $x+1 / 2$, would apply to a partial year that occurs at the end of a study period. The second half-year, from age $x+1 / 2$ to $x+1$, would apply to a partial year that occurs at the start of a study period.

### 9.1.3 Constant Mortality Rates

The constant mortality rate assumption is assumed when annualizing average fractional rates.

The monthly mortality rate that is equivalent to a $12 \%$ annual mortality rate can be directly calculated:

$$
{ }_{\mathrm{f}} q_{x+f t}={ }_{f} \bar{q}_{x}=1-\left(1-q_{x}\right)^{f}=1-(0.88)^{1 / 12}=0.01060
$$

The following table has the same structure as the prior table.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{A}}$ |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $1,000.0$ | 10.6 | $1,000.0$ | 0.01060 | 0.12000 |
| 1 | 989.4 | 10.5 | 989.4 | 0.01060 | 0.12000 |
| 2 | 978.9 | 10.4 | 978.9 | 0.01060 | 0.12000 |
| 3 | 968.5 | 10.3 | 968.5 | 0.01060 | 0.12000 |
| 4 | 958.3 | 10.2 | 958.3 | 0.01060 | 0.12000 |
| 5 | 948.1 | 10.0 | 948.1 | 0.01060 | 0.12000 |
| 6 | 938.1 | 9.9 | 938.1 | 0.01060 | 0.12000 |
| 7 | 928.1 | 9.8 | 928.1 | 0.01060 | 0.12000 |
| 8 | 918.3 | 9.7 | 918.3 | 0.01060 | 0.12000 |
| 9 | 908.6 | 9.6 | 908.6 | 0.01060 | 0.12000 |
| 10 | 899.0 | 9.5 | 899.0 | 0.01060 | 0.12000 |
| 11 | 889.4 | 9.4 | 889.4 | 0.01060 | 0.12000 |
| Total | $12,204.8$ | 120.0 | $11,324.8$ | 0.01060 | 0.12000 |

The annualized monthly rates are constant over the year and match the $12 \%$ annual rate.

Again, to illustrate the partial years arising at the start and end of a period study, the next table shows a half-year study.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{t}}$ |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $1,000.0$ | 61.9 | $5,843.3$ | 0.01060 | 0.12000 |
| 1 | 938.1 | 58.1 | $5,481.5$ | 0.01060 | 0.12000 |
| Total |  | 120.0 | $11,324.8$ | 0.01060 | 0.12000 |

For both half-years, the annualized fractional rate matches the annual rate. If annual exposure and rates had been calculated using the above distribution of deaths, differences to the annual rates would have arisen due to the constant rate assumption.

### 9.1.4 Increasing Force

In the section, we will compare rates calculated from the annual exposure methods (Balducci Hypothesis and Uniform Distribution of Deaths) and the fractional rate exposure method while assuming a realistic pattern of mortality: We will assume that the force of mortality increases linearly and use a mortality rate of $q_{x}=0.01$. Additionally, we will use a relative increase of force of $10 \%$, which is representative of data from the VBT table presented at the end of Section 8.2, a section you may want to reference as you progress through the following example.

The average force of mortality equivalent to a mortality rate of 0.01 is calculated as:

$$
\bar{\mu}_{x}=-\log _{e}(1-0.01)=0.01005
$$

With a mortality rate of 0.01 and a relative increase in force of $\Delta_{x}=10 \%$, the increase in force over the year is:

$$
\Delta \mu_{x}=0.10 \bar{\mu}_{x}=(0.10)(0.01005)=0.001005 .
$$

The average monthly force for each month is:

$$
{ }_{f} \bar{\mu}_{x+f t}=f\left(\bar{\mu}_{x}-\Delta \mu_{x}(1 / 2(N-1)-t) / N\right) .
$$

The above formula can be restated by substituting $f$ for $1 / N$ :

$$
{ }_{f} \bar{\mu}_{x+f t}=f\left(\bar{\mu}_{x}-\Delta \mu_{x}(1 / 2(1-f)-f t)\right) .
$$

Monthly mortality rates can then be calculated as:

$$
{ }_{f} q_{x+f t}=1-e^{-{ }_{f} \bar{\mu}_{x+f t}} .
$$

The table below shows the underlying monthly average forces, calculated using the above "increasing force" formula, and the resulting monthly mortality rates. The last two columns show the annualized equivalent force and mortality rates.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \overline{\boldsymbol{\mu}}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \overline{\boldsymbol{\mu}}_{\boldsymbol{x}+\boldsymbol{f t} \boldsymbol{t}}^{\boldsymbol{A}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{A}}$ |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0.00080 | 0.00080 | 0.00959 | 0.00954 |
| 1 | 0.00081 | 0.00081 | 0.00967 | 0.00963 |
| 2 | 0.00081 | 0.00081 | 0.00976 | 0.00971 |
| 3 | 0.00082 | 0.00082 | 0.00984 | 0.00979 |
| 4 | 0.00083 | 0.00083 | 0.00992 | 0.00988 |
| 5 | 0.00083 | 0.00083 | 0.01001 | 0.00996 |
| 6 | 0.00084 | 0.00084 | 0.01009 | 0.01004 |
| 7 | 0.00085 | 0.00085 | 0.01018 | 0.01012 |
| 8 | 0.00085 | 0.00085 | 0.01026 | 0.01021 |
| 9 | 0.00086 | 0.00086 | 0.01034 | 0.01029 |
| 10 | 0.00087 | 0.00087 | 0.01043 | 0.01037 |
| 11 | 0.00088 | 0.00088 | 0.01051 | 0.01046 |

$\begin{array}{lll}\text { Total } & 0.01005 \quad 0.01000\end{array}$

In the next table, the above monthly mortality rates were applied to the number of lives at the start of each month to calculate monthly deaths. Annual rates for each month were then calculated as monthly deaths divided by one month of exposure, based on each of the three exposure methods:

- Annual exposure, based on the Balducci Hypothesis (BH)
- Fractional exposure, based a constant mortality rate (CMR)
- $\quad$ Distributed exposure, based on a uniform distribution of deaths (UDD)

The annual rates are shown in the columns labeled BH, CMR and UDD.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x + f \boldsymbol { t }}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{B H}$ | $\boldsymbol{C M R}$ | $\boldsymbol{U D D}$ |
| :---: | ---: | ---: | :---: | :---: | :---: |
| 0 | $1,000.00$ | 0.80 | 0.00950 | 0.00954 | 0.00959 |
| 1 | 999.20 | 0.81 | 0.00959 | 0.00963 | 0.00966 |
| 2 | 998.40 | 0.81 | 0.00968 | 0.00971 | 0.00974 |
| 3 | 997.58 | 0.82 | 0.00977 | 0.00979 | 0.00981 |
| 4 | 996.77 | 0.82 | 0.00986 | 0.00988 | 0.00989 |
| 5 | 995.94 | 0.83 | 0.00995 | 0.00996 | 0.00996 |
| 6 | 995.11 | 0.84 | 0.01005 | 0.01004 | 0.01004 |
| 7 | 994.28 | 0.84 | 0.01014 | 0.01012 | 0.01011 |
| 8 | 993.43 | 0.85 | 0.01023 | 0.01021 | 0.01019 |
| 9 | 992.58 | 0.86 | 0.01032 | 0.01029 | 0.01026 |
| 10 | 991.73 | 0.86 | 0.01041 | 0.01037 | 0.01034 |
| 11 | 990.87 | 0.87 | 0.01051 | 0.01046 | 0.01041 |
| Total |  | 10.00 | 0.01000 | 0.01000 | 0.01000 |

The annual rates for all three exposure methods increase over the year and are relatively similar. In the Total line, you can see that annual rates, calculated as annual deaths divided by annual exposure for each of the three exposure methods, match the underlying $1 \%$ mortality rate used to generate the table. The annualized monthly rates for the CMR method match the annualized monthly rates used to calculate the life table.

The following graph illustrates the annual rates from the preceding table. At the middle of the year, all three exposure methods intersect and match the $1 \%$ underlying annual rate. All three methods produce rates lower than the $1 \%$ rate in the first half of the year and higher than the $1 \%$ rate in the second half of the year. The distributed exposure method (UDD) produces the rates closest to the underlying mortality rates, which increase more steeply. The differences between the three exposure methods are largest at the start and end of the year. The annual rates for the fractional exposure method (CMR) match the annualized underlying monthly mortality rates.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_77542591393347e2e981g-049.jpg?height=767&width=1350&top_left_y=1533&top_left_x=366" alt="image" style="width:100%;height:auto;">

To simulate the partial years arising at the start and end of a period study, the next table shows a half-year study for the three exposure methods, with underlying mortality based on the same "increasing force" mortality formula.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{l}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}+\boldsymbol{f t}}$ | $\boldsymbol{B H}$ | $\boldsymbol{C M R}$ | $\boldsymbol{U D D}$ |
| :---: | ---: | ---: | :---: | :---: | :---: |
| 0 | $1,000.00$ | 4.89 | 0.00973 | 0.00975 | 0.00978 |
| 1 | 995.11 | 5.11 | 0.01028 | 0.01025 | 0.01022 |
| Total | 990.00 | 10.00 | 0.01000 | 0.01000 | 0.01000 |

The annual rates were calculated as a half-year of deaths divided by a half-year of exposure. All three exposure methods produce annual rates that are similar in both half-years. However, for an annual study, the aim is to reproduce the underlying annual rate, not the underlying rates for partial years. Annual rates based on a half-year of exposure are apt to understate or overstate the underlying annual rate. Since the errors for each half-year are equal but opposite in sign, given a stable multiple-cohort population, these errors would cancel out. For a single cohort study, such as for one year of birth or one year of issue, the rates for partial years would reflect the full error.

The graph below shows the annual rates by exposure method for each half-year, stretched over each month of the year. The graph is similar to the monthly graph above with the annual rates averaged over half-years. Again, the annual rates for the fractional exposure method (CMR) match the underlying annualized half-yearly rates.

The annual rates for the first half-year are indicative of the annual rates for partial years arising at the end of the study period, or a policy year truncated at a calendar year-end. Similarly, the annual rates for the second half-year are indicative of the annual rates for partial years arising at the start of the study period, or a truncated policy year beginning at the prior calendar year-end.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_77542591393347e2e981g-050.jpg?height=769&width=1347&top_left_y=1258&top_left_x=362" alt="image" style="width:100%;height:auto;">

Three exposure methods based on different underlying distribution of deaths have been examined. These are:

- Annual Exposure using the Balducci Hypothesis,
- Fractional Exposure using the constant rate or force
- Distributed Exposure using the uniform distribution of deaths

Given a full year of exposure, all three methods will reproduce the underlying annual rate. For partial years arising at the start and end of a study period or from the inclusion of calendar years for trending, all three methods will introduce errors.

Fractional exposure methods include both daily exposure and the force of mortality. For any partial year, fractional exposure will calculate the correct fractional rate for the partial year. The annual rate, equal to the annualized fractional rate, will only be accurate if the assumption of a constant mortality rate over the year holds. If the mortality rate increases over the year, then the annual rate will be overstated for the partial year that runs from age $x$ to the study end date. For the partial year running from the study start date to the end of the year of age $x$, the annual rate will be understated.

When the annual exposure method is applied to a partial year running from age $x$ to the study end date, deaths will be exposed to the end of the year of age $x$. In contrast, fractional exposure would run only to the study end date. This additional exposure will cause the annual rate to be lower than the annualized fractional rate. For partial years running from the study start date to the end of the year of age $x$, annual exposure will be the same as fractional exposure divided by 12 . However, the resulting annual rate is already expressed per year while the fractional rate is expressed per partial year and needs to be annualized. Therefore, the annual rate will be higher than from the annualized fractional rate.

When the distributed exposure method is applied to a partial year running from age $x$ to the study end date, deaths will be exposed to the study end date, the same as for fractional exposure. The rate for distributed exposure is already expressed annually while the fractional exposure is expressed per partial year, so the fractional rate needs to be annualized. Hence the annual rate will be higher than the annualized fractional rate. For partial years running from the study start date to the end of the year of age $x$, deaths from the prior partial period will be included in the exposure. This additional exposure will cause the annual rate to be lower than the annualized fractional rate.

### 9.2 Estimating Errors

The error from using the average fractional rates can be calculated by assuming a linearly increasing force.

Using the half-year study to illustrate, the force for the first half-year is

$$
{ }_{1 / 2} \bar{\mu}_{x+1 / 2}=1 / 2\left(\bar{\mu}_{x}-1 / 4 \Delta \mu_{x}\right) .
$$

The half-year rate is

$$
{ }_{f} q_{x+f t}=1-e^{-1 / 2\left(\bar{\mu}_{x}-1 / 4 \Delta \mu_{x}\right)}
$$

The annualized half-year rate is

$$
\begin{aligned}
& 1-\left(1-{ }_{f} q_{x+f t}\right)^{2} \\
= & 1-\left(e^{-1 / 2\left(\bar{\mu}_{x}-1 / 4 \Delta \mu_{x}\right)}\right)^{2} \\
= & 1-e^{-\bar{\mu}_{x}+1 / 4 \Delta \mu_{x}} \\
= & 1-\left(1-q_{x}\right) e^{+1 / 4 \Delta \mu_{x}} .
\end{aligned}
$$

The difference between the underlying annual rate and the annualized half-year rate is

$$
\begin{aligned}
& q_{x}-\left(1-\left(1-q_{x}\right) e^{+1 / 4 \Delta \mu_{x}}\right) \\
= & \left(1-q_{x}\right)\left(e^{+1 / 4 \Delta \mu_{x}}-1\right) \\
\approx & \left(1-q_{x}\right)\left(+1 / 4 \Delta \mu_{x}\right) .
\end{aligned}
$$

A more useful error estimate, substituting using the relative increase $\Delta_{x}=\Delta \mu_{x} / \bar{\mu}_{x}$, is

$$
\begin{aligned}
& \left(1-q_{x}\right)\left(+1 / 4 \Delta \mu_{x} / \bar{\mu}_{x}\right) \bar{\mu}_{x} \\
= & -\left(1-q_{x}\right)\left(+1 / 4 \Delta_{x}\right) \log _{e}\left(1-q_{x}\right) \\
\approx & \left(1-q_{x}\right)\left(+1 / 4 \Delta_{x}\right) q_{x} .
\end{aligned}
$$

To the first order of $q_{x}$, the error estimate is therefore

$$
1 / 4 q_{x} \Delta_{x}
$$

which is one-quarter of the relative increase in force multiplied by the mortality rate. The percentage error for the half-year rate is therefore

$$
+1 / 4 \Delta_{x}
$$

For the second half-year of age, the error is equal but opposite in sign.

The difference between annual rates calculated using annual and half-year exposures for the first half-year has been shown to be

$$
+1 / 4\left(q_{\mathrm{x}}\right)^{2}
$$

Therefore, the error in the rate arising from the annual exposure method when compared to the underlying rate is

$$
1 / 4 q_{x}\left(\Delta_{x}+q_{x}\right)
$$

The above error is the sum of the error in the half-year rate plus the sum of the difference between the annual and half-year rates.

If the relative change over the year is a decrease equal to the mortality rate, i.e., $q_{x}=-\Delta_{x}$, which is the Balducci Hypothesis, the error is zero.

The error in the rate arising from the distributed exposure method when compared to the underlying rate is

$$
1 / 4 q_{x}\left(\Delta_{x}-q_{x}\right)
$$

If the relative change over the year is equal to the mortality rate, i.e., $q_{x}=\Delta_{x}$, which is exactly the case for the uniform distribution of deaths, the error is zero.

The condition for which method is more accurate is as follows:

- Annual Exposure is more accurate when $\Delta_{x}<-1 / 2 \mathrm{q}_{x}$.
- Half-year Exposure is more accurate when $-1 / 2 \mathrm{q}_{x}<\Delta_{x}<1 / 2 \mathrm{q}_{x}$.
- $\quad$ Distributed Exposure is more accurate when $\Delta_{x}>1 / 2 \mathrm{q}_{x}$.

The slope of the distribution of deaths can be summarized by the ratio of the relative increase to the mortality rate, $\Delta_{x} / \mathrm{q}_{x}$, which we will call the "steepness ratio," as it indicates the steepness compared to the standard distributions:

- $\Delta_{x} / \mathrm{q}_{x}=-1$ matches the annual exposure method (Balducci Hypothesis, BH).
- $\Delta_{x} / \mathrm{q}_{x}=0$ matches the fractional exposure method (constant rate or force, CMR).
- $\Delta_{x} / \mathrm{q}_{x}=-1$ matches the distributed exposure method (uniform distribution of deaths, UDD).

To demonstrate the relative errors for each method, the following table applies the error formulas to the VBT rates presented at the end of Section 8.2, and shows steepness ratio (SR), the error percentages for each method and the ratios of the errors between the three methods.

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $\mathrm{SR}$ | $\mathrm{BH}$ | $\mathrm{CMR}$ | UDD | BH/CMR | CMR/UDD | BH/UDD |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | 0.00192 | 31.2 | $1.55 \%$ | $1.50 \%$ | $1.45 \%$ | $103 \%$ | $103 \%$ | $107 \%$ |
| 60 | 0.00408 | 21.1 | $2.25 \%$ | $2.15 \%$ | $2.05 \%$ | $105 \%$ | $105 \%$ | $110 \%$ |
| 70 | 0.01147 | 9.8 | $3.09 \%$ | $2.81 \%$ | $2.52 \%$ | $110 \%$ | $111 \%$ | $123 \%$ |
| 80 | 0.03826 | 3.3 | $4.11 \%$ | $3.15 \%$ | $2.20 \%$ | $130 \%$ | $144 \%$ | $187 \%$ |
| 90 | 0.13690 | 0.9 | $6.47 \%$ | $3.05 \%$ | $-0.37 \%$ |  |  |  |

For ages 50 to 80, the steepness ratio ranges from 31 down to 3, much steeper than the UDD's steepness of 1 , but UDD is closest. At age 90, the steepness ratio is less than one, but still closest to the UDD, but the error for UDD has now changed sign.

The error terms can be generalized to any fractional period.

The error in the annualized fractional rates for each fractional period is approximately

$$
q_{x} \Delta_{x}(1 / 2(N-1)-t) / N
$$

The error in the annual rates for each fractional period is approximately

$$
q_{x}\left(\Delta_{x}+\mathrm{q}_{x}\right)(1 / 2(N-1)-t) / N
$$

The error in the annual rates using distributed exposure for each fractional period is approximately

$$
q_{x}\left(\Delta_{x}-\mathrm{q}_{x}\right)(1 / 2(N-1)-t) / N
$$

## 10 Decrement Studies

Life tables and mortality studies were used in the previous chapters to illustrate core study principles, notation and calculations. Those studies had the following attributes:

- Decrement Type: Death.
- Time Interval: Age, i.e., the number of complete years since birth.
- Population States Tracked: Only one - being alive in the population.

In this chapter, we will explore decrement studies more generally.

### 10.1 Decrement Types

Decrements reduce the surviving study population. Often, studies must deal with more than one type of decrement. For example, life insurance studies often include both mortality and withdrawal (i.e., lapse or surrender) decrements. Active life studies for disability and long-term care must handle claim and lapse decrements. Disabled life studies involve decrements for both recovery from disability and death.

We will generalize the notation for decrement studies so that $d_{x}$ and $E_{x}$ relate to the decrement under study while $w_{x}$ relates to all other decrements:

- $d_{x}$ is the number of occurrences of the decrement under study over the year of age $x$,
- $w_{x}$ is the number of occurrences of decrements not under study over the year of age $x$,
- $E_{x}$ is the exposure for the decrement under study over the year of age $x$, and
- $\quad q_{x}=d_{x} / E_{x}$ is the probability of the decrement under study, the decrement rate, over the year of age $x$.

We have used a subscript of $x$ to denote age. The subscript would be driven by the nature of the study. For example, the subscript might be $x$ for attained age, $[x]$ for issue age, $t, y$ or $p y$ for policy year, $c y$ for calendar year and " $[x]+t$, ," $x+t$, , " $[x], t$ " or " $x, t$ " for a combination of issue age and policy year.

Some studies calculate rates for more than two decrements. To distinguish between the various decrements, the superscript " $k$ " can be used to denote the decrement under study and the superscript "- $k$ " superscript can denote all decrements other than decrement $k$, which are often combined when calculating exposure for decrement $k$ :

- $d_{x}^{k}$ is the number of occurrences of decrement $k$ over the year of age $x$,
- $d_{x}^{-k}$ is the number of occurrences of decrements other than decrement $k$ over the year of age $x$,
- $\quad E_{x}^{k}$ is the exposure for decrement $k$ over the year of age $x$, and
- $\quad q_{x}^{k}=d_{x}^{k} / E_{x}^{k}$ is the probability of decrement $k$, the decrement $k$ rate, over the year of age $x$.

Where there are only two decrements, the use of the " $k$ " and " $-k$ " superscripts can be avoided by using $d_{x}$ for the decrement under study and $w_{x}$ for the decrement not under study. Notation for the $k^{\text {th }}$ decrement would be used only when necessary to avoid confusion.

### 10.2 Rate Intervals

In previous chapters, mortality rates were calculated by year of age. In practice, rates can be calculated for fractions of a year or for multiple years. The period for which rates are calculated is called the rate interval. The rate interval defined by age at prior birthday is called a life-year rate interval. The life-year rate interval would be used where the desired rates are to vary by age at prior birthday, such as for pension or retirement plan studies.

The rate interval can also be calculated with respect to the policy year of the underlying policy, equal to one plus the number of complete years since the issue date. Such a rate interval is called a policy-year rate interval. Another common rate interval is the calendar-year rate interval.

For life insurance, the age at issue together with the date of issue drives the premium rates of the policy. If rates are to be calculated by attained age, that age is calculated as the issue age plus the whole number of years since issue. Attained age does not increase on the insured's birthday, but on the policy anniversary.

When a calendar year rate interval is used for life insurance studies, there is more than one way to assign a single age for each calendar year. When using year-end data from the prior calendar year as the starting point of the study, age for each calendar year would be most often be defined as either:

1. the age at the birthday preceding the policy anniversary in the calendar year or
2. the issue age plus the number of complete policy years at the policy anniversary in the calendar year.

In a later section, we will explore splitting each calendar year into two partial policy years.

The rate interval used in a study is determined by the data available. Within the study, it is critical that the same rate interval definition be used for decrements, exposure, and decrement rates.

### 10.2.1 Partial Rate Intervals

Prior chapters showed that partial years (or, more generally, partial rate intervals) introduce errors in the rates calculated due to either:

- The incorrect assumption of the Balducci Hypothesis over the rate interval, or
- The incorrect assumption of the uniform distribution of deaths over the rate interval, or
- The incorrect assumption of constant fractional decrement rates over the rate interval.

Partial rate intervals arise from three sources:

1. Decrements not under study, such as withdrawals in a mortality study, where exposure to mortality stops at the withdrawal date,
2. The interaction of rate intervals with the start and end dates of a period study., and
3. The inclusion of a secondary rate interval (such as calendar year) on top of a primary rate interval (such as life year or policy year) to study a secondary trend within the study period. For example, every policy year could be split between two calendar years.

When a calendar-year rate interval is used with study start and end dates that are calendar year-ends, there are no partial rate intervals caused by the study's start and end dates.

However, when life-year or policy-year rate intervals are used with study start and end dates that are calendar yearends, partial rate intervals are created at the beginning and end of the study. These partial rate intervals are commonly excluded when their inclusion would distort the study's results.

When partial rate years are excluded from the study, with only whole rate years included between the study start and end dates, the study period is referred to generally as a rate-year study period, or more specifically as a policyyear study period.

### 10.3 Time Intervals

Most studies examine rates over time, where time is measured by what we will call the time interval. The time interval under study is often the number of years or months since entry into the population. The time interval is defined by both the entry event and the unit of time.

- For population mortality, the time interval is the number of years since birth: age.
- $\quad$ For pensioners, the time interval is the number of years since retirement: retirement years.
- For life insurance, the time interval is the number of years since issue: policy years.
- For claims, the time interval is the number of months or years since the claim incurral or loss date: claim months or claim years.

We will generalize the notation and terminology as follows:

- $d_{y}$ is the number of occurrences of the decrement under study for $y$ years since entry,
- $w_{y}$ is the number of occurrences for the decrements not under study for $y$ years since entry,
- $E_{y}$ is the exposure for the decrement under study for $y$ years since entry, and
- $\quad q_{y}=d_{y} / E_{y}$ is the probability of the decrement under study, the decrement rate, for $y$ years since entry.

For a monthly time interval, $y$ for year could be replaced by $m$ for months.

For insurance:

- Mortality studies often use policy year in conjunction with issue age up to the point where the impact of underwriting has worn off, after which attained age is used. This scheme is commonly referred to as select and ultimate.
- $\quad$ Lapse studies use policy year, often in conjunction with issue age, with lapse as the decrement under study and other decrements, such as death, expiry and conversions, treated as withdrawals.
- $\quad$ Claim termination studies use claim month in conjunction with the age at loss date (the claim age) for a number of years, after which attained age is used.

For the time interval since entry, the age at entry may be just another attribute of the life, such as gender. However, because of the importance of age at entry, from which attained age can be derived, study notation often incorporates the age at entry, using the age $x$ in square brackets. That is,

- $d_{[x], y}$ is the number of occurrences of the decrement under study for age at entry $[x]$ and $y$ years since entry,
- $w_{[x], y}$ is the number of occurrences of decrements not under study for age at entry $[x]$ and $y$ years since entry,
- $E_{[x], y}$ is the exposure for the decrement under study for age at entry $[x]$ and $y$ years since entry, and
- $q_{[x], y}=d_{[x], y} / E_{[x], y}$ is the probability of the decrement under study, the decrement rate, for age at entry $[x]$ and $y$ years since entry.

In studies where issue age is paramount and attained age is rarely used, square brackets are often omitted. However, the use of square brackets for issue age removes any ambiguity.

For mortality studies where attained age and policy year are important, if attained age is defined using the policyyear rate interval, both attained age and policy year increase at the policy anniversary. This is the standard approach in North America. For example, consider a policy issued on an "age last birthday" basis on August 22, 2010 to an insured who turned 45 on February 5, 2010:

- $\quad$ The period from August 22, 2010 to August 21, 2011 is assigned to issue age 45 and policy year 1.

Outside North America, a different approach is commonly used: Age is defined by a life-year rate interval, with age increasing at the insured's birthday, while policy year increases at the policy anniversary. This means that every policy year must be split between two ages, with one segment before and the other segment after the birthday. For example, consider a policy issued on August 22, 2010 to an insured who turned 45 on February 5, 2010:

- The period from August 22, 2010 to February 4, 2011 is assigned to age 45 and policy year 1.
- $\quad$ The period from February 5, 2011 to August 21, 2011 is assigned to age 46 and policy year 1.


### 10.4 Discrete Decrements

The preceding examples assumed a continuous distribution of decrements, which usually applies to biological decrements such as mortality and morbidity. For most behavioral decrements, such as lapse or exercise of an option, a continuous distribution assumption is not appropriate. Decrements that can occur only on a given date or dates within the rate interval or whose distribution within the rate interval is irregular are called discrete decrements.

Let us examine the consequences of the extreme case: Lapse rates for the annual premium mode, where lapse can occur only on the policy anniversary. The resulting distortion is most apparent in the calculation of lapse exposure for partial policy years. Note that the partial policy year at the beginning of the study ends with and includes the policy anniversary. The partial policy year at the end of the study period does not include a policy anniversary.

- Deaths occurring during either partial policy year are not exposed to the risk of lapse, which can only happen on the policy anniversary, so lapse exposure should be zero. Instead, deaths are exposed until the date of death.
- $\quad$ Lives surviving the partial policy year at the start of the study period should be exposed to a full year's worth of lapse risk, since the policy anniversary is part of the exposure period, but only partial year exposure is assigned, thereby contributing to an overstatement of the lapse rate.
- $\quad$ Lives surviving the partial policy year at the end of the study period are exposed to no risk of lapse, since the policy anniversary is not part of the exposure period, but partial year exposure is assigned, thereby contributing to an understatement of the lapse rate.

If you repeat the above example using a monthly premium mode, you will find that distortions that averaged half a year would now average only half a month. The distortions may be small enough that a continuous distribution assumption will produce sufficiently accurate results.

### 10.5 Population States

In a mortality study, each life has one of the following three statuses at any given time:

1. Alive and in the study population,
2. withdrawn from the study population, or
3. dead, where death occurred while in the study population.

Such a study is referred to as a single-state study, as the study examines only how lives decrement from the single state of being "alive and in the study population."

Some studies examine additional states that a life may move or transition between. For example:

- In a study of an adult population, lives may change their marital status between single and married states.
- In a pension study, the population can transition between states of actively at work, disabled and retired.
- In a disability study, insureds can move between states of being either healthy (not disabled) or claiming (disabled).

Each state within a population forms a sub-population for which a decrement study can be carried out. The decrements for each state will include decrements that remove the life from the study population, e.g., deaths and withdrawals, as well as transitions to another state. Transitions from another state are treated as new entrants into the population state under study.

A decrement study for a population state can examine a decrement that affects the main population, such as deaths, while treating the transition to other states as withdrawals, thereby mimicking a single-state study. Decrement studies that examine transitions between states are called transition studies or multi-state studies.

To illustrate, consider a simple cohort study for a disability income population of lives aged 45 . The population has two states: healthy and claiming. The initial state at time of policy issue is healthy, from which some lives move into the claiming state, and some may return to the healthy state at a later time. Deaths can occur from either state, while withdrawals can only occur from the healthy state.

First, consider the following life table for the total population:

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ |
| :---: | ---: | ---: | ---: |
| 45 | 1,000 | 3 | 5 |
| 46 | 991 | 7 | 4 |
| 47 | 982 | 7 | 6 |
| 48 | 966 | 6 | 2 |

Now consider a life table with lives split between the two states, healthy and claiming; this is referred to as a combined table. In the table below, survivors, deaths and withdrawals have been allocated to each state. The totals across the two states match the table above. Both states show the transitions between states for claim incidence, $i_{x}$, and recovery, $r_{x}$. Claims reduce the number of healthy lives and add to the claiming lives. Recoveries do the opposite.

|  | Healthy |  |  |  |  | Claiming |  |  |  |
| :---: | ---: | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{i}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{r}_{\boldsymbol{x}}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{i}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{r}_{\boldsymbol{x}}$ |
| 45 | 1,000 | 10 | 2 | 5 | 3 | 0 | 10 | 1 | 3 |
| 46 | 986 | 13 | 3 | 4 | 7 | 6 | 13 | 4 | 7 |
| 47 | 973 | 11 | 4 | 6 | 9 | 8 | 11 | 3 | 9 |
| 48 | 961 | 12 | 3 | 2 | 8 | 7 | 12 | 3 | 8 |

For each state, the number of lives, $l_{x}$, at each age $x$ is defined as:

- Healthy: $l_{x+1}=l_{x}-i_{x}-d_{x}-w_{x}+r_{x}$ and
- Claiming: $l_{x+1}=l_{x}+i_{x}-d_{x}-w_{x}-r_{x}$.

This example illustrates the principle of multi-state studies: decrement and transition rates can be calculated using the principles already outlined. In reality, for disability income, the claim state would be analyzed by time since incidence and claim age, rather than issue age and policy year, since time since claim incidence is the larger driver of recovery rates. Also, recoveries would usually be tracked monthly for the first few years in order to better reflect short-term claims.

## 11 Simple Withdrawal Study Example

### 11.1 Period Study

To illustrate a withdrawal (i.e., lapse) study using the policy-year time interval, we will reuse the example given in section 4.3 for a period study with deaths and withdrawals for lives born in 1944, except now the decrement under study will be withdrawals, and deaths will be classified as "decrements not under study." The example will use the same standard notation to illustrate the importance of the context of the study as well as the importance of defining terms used.

We will use the following notation:

$T_{y}$ will represent the time spent in the study during policy year $y$,

$w_{y}$ will represent the number of withdrawals for policy year $y$,

$d_{y}$ will represent the number of deaths for policy year $y$,

$E_{y}^{w}$ will represent the exposure for withdrawals for policy year $y$, and

$q_{y}^{w}$ will represent the probability of withdrawal, the withdrawal rate, for policy year $y$.

The life table, by policy year, for withdrawals is given below.

| $\boldsymbol{y}$ | $\boldsymbol{l}_{\boldsymbol{y}}$ | $\boldsymbol{d}_{\boldsymbol{y}}$ | $\boldsymbol{w}_{\boldsymbol{y}}$ | $\boldsymbol{T}_{\boldsymbol{y}}$ | $\boldsymbol{E}_{\boldsymbol{y}}^{\boldsymbol{w}}$ | $\boldsymbol{q}_{\boldsymbol{y}}^{\boldsymbol{w}}$ | $\boldsymbol{p}_{\boldsymbol{y}}^{\boldsymbol{w}}$ |
| ---: | ---: | ---: | ---: | ---: | ---: | :---: | :---: |
| 1 | 994 | 4 | 2 | 0.5 | 496.0 | 0.00403 | 0.99597 |
| 2 | 988 | 8 | 4 | 1.0 | 984.0 | 0.00407 | 0.99593 |
| 3 | 976 | 9 | 6 | 1.0 | 971.5 | 0.00618 | 0.99382 |
| 4 | 961 | 10 | 4 | 1.0 | 956.0 | 0.00418 | 0.99582 |
| 5 | 947 | 5 | 2 | 0.5 | 473.3 | 0.00423 | 0.99577 |
| Total |  | 36 | 18 |  | $3,880.8$ | 0.00464 |  |

While the data is the same as the example in 3.3 , the differences are:

- $\quad$ Age $x$ is replaced by policy year $y$,
- $\quad$ Exposure for withdrawals is estimated using the following formula that adjusts for deaths: $E_{y}^{w}=l_{y}-1 / 2 d_{y}$, and
- $\quad$ The withdrawal rate is calculated as $q_{y}^{w}=w_{y} / E_{y}$.


### 11.1.1 Exposure Calculation

To illustrate calculating the exposure from underlying dates, consider pensioners born in 1945, from the example in Section 4.2.3.

- Life $A$ is a pensioner who turns 65 on May $10^{\text {th }}, 2010$, and remains alive throughout the study.
- $\quad$ Life B is a pensioner who turns 65 on September $27^{\text {th }}, 2010$, and dies on February $16^{\text {th }}, 2012$.
- Life C is a pensioner who turns 65 on July $3^{\text {rd }}, 2010$, and withdraws on October $21^{\text {st }}, 2012$.

The table below shows, for each life, the exposure start date for each year $y$, which is also the exposure end date for the prior year $y-1$.

| $\boldsymbol{y}$ | 1 | $\mathbf{2}$ | 3 | $\mathbf{4}$ | $\mathbf{5}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Life A | $5 / 10 / 2010$ | $5 / 10 / 2011$ | $5 / 10 / 2012$ | $5 / 10 / 2013$ | $1 / 1 / 2014$ |
| Life B | $9 / 27 / 2010$ | $9 / 27 / 2011$ | $2 / 16 / 2012$ |  |  |
| Life C | $7 / 3 / 2010$ | $7 / 3 / 2011$ | $7 / 3 / 2012$ | $7 / 3 / 2012$ |  |

Dates of note for particular lives and ages are:

- Life A, year 5, is exposed to the study end date,
- Life B, year 3 , is exposed to the date of death, and
- $\quad$ Life $\mathrm{C}$, year 4, is exposed to the anniversary (i.e., birthday) following the date of withdrawal.

The number of days for each life in each rate year is calculated as Date $(y+1)-\operatorname{Date}(y)$.

| $\boldsymbol{y}$ | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{4}$ |
| :---: | :---: | :---: | :---: | :---: |
| Life A | 365 | 366 | 365 | 236 |
| Life B | 365 | 142 |  |  |
| Life C | 365 | 366 | 365 |  |

The exposure for each life for each year of age is found by dividing the number of days in the year of age by the total number of days in that policy year.

| $\boldsymbol{y}$ | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{4}$ |
| :---: | :---: | :---: | :---: | :---: |
| Life A | 1.000 | 1.000 | 1.000 | 0.647 |
| Life B | 1.000 | 0.388 |  |  |
| Life C | 1.000 | 1.000 | 1.000 |  |

From the table it can be seen that:

Life A: contributes a partial year for year 5 at the end of the study, Life B: contributes a partial year for year 2 in the year of death, and Life C: contributes a full year for year 3 in the year of withdrawal.

Comparing the exposures between the mortality and withdrawal studies:

- Life B, who died at age 66 in year 2, contributed a full year of exposure in the mortality study, but a partial year of exposure in the withdrawal study.
- $\quad$ Life $\mathrm{C}$, who withdrew at age 67 in year 3, contributed a partial year of exposure in the mortality study, but a full year of exposure in the withdrawal study.


## 12 Actual to Expected Analysis

Experience studies are carried out across the insurance industry by product line and decrement type to produce industry standard tables. Many insurance companies contribute to these studies and even more companies perform their own analysis, often comparing actual company results to expected results (hence, "Actual to Expected"), based on either industry tables or the company's own tables.

Company studies typically have much smaller study populations than industry studies and hence have more volatile and less credible rates at every level. Even industry studies suffer from some volatility, so rates are typically smoothed using a process called graduation, which smooths rates while preventing distortion of overall rate levels.

For complex tables of rates such as select and ultimate mortality rates or disability income incidence and termination rates, few companies have sufficient data to build credible tables based on their own experience. For studies of such complex rates, most companies gear their experience studies to study their experience in relation to one or more industry tables. Study results are then expressed as percentages of the industry tables, often referred to as "A/E ratios" (actual to expected ratios), where the industry table supplies the expected rates.

For companies whose results are only credible at the company level, a single, overall A/E ratio may be the only result of an experience study. When a company's results are credible for major subgroups of its business, such as female vs. male insureds, large benefit amounts vs. small benefit amounts or tobacco users vs. tobacco non-users, A/E ratios would be analyzed for various combinations of one or more attributes. Actual to expected analysis would search for combinations of attributes with the most credible and relevant differences in A/E ratios.

By applying their A/E ratios to industry tables, a company can produce a smooth set of expected rates that match their overall experience. Companies often label these adjusted industry rates as "best estimate" rates and used to project in force populations for valuation, risk management and financial planning purposes. Companies also use best estimate rates to project expected business results for the coming years. Actual experience is compared to the expected business results on an annual or more frequent basis, thereby creating another form of actual to expected analysis.

Expected results are easily added to a seriatim experience study, which typically has one record per life per policy year or calendar year. For each record in the study, the appropriate expected rate is obtained from the industry table and multiplied by the record's exposure to determine an expected amount, which is then stored in the record. Actual amounts (of the event under study) and expected amounts can then be summarized by any of the attributes stored in the records and A/E ratios calculated.

To illustrate how A/E ratios are used in industry studies, please see the 2008-2009 Individual Life Experience Report. You will find A/E ratios beginning on page 8 and continuing through page 19 . Note that the results of the study are largely explained through $\mathrm{A} / \mathrm{E}$ ratios.

When seriatim data is not available and grouped data must be used, calculating expected amounts may become quite complex unless the grouping of the data lines up with the structure of the industry table.

We will use the following notation for actual to expected analysis. Let:

$q_{x}^{e}$ be the expected rate from the expected rate table for age $x$,

$E_{x}$ be the exposure for age $x$, and

$d_{x}$ be the actual number of events for age $x$.

The expected number of events, $d_{x}^{e}$, for age $x$ is then given by:

$$
d_{x}^{e}=E_{x} q_{x}^{e}
$$

The Actual to Expected ratio, $\mathrm{A} / \mathrm{E}$, at each age $x$, is:

$$
(A / E)_{x}=d_{x} / d_{x}^{e}
$$

The overall A/E ratio for the whole population is the total actual deaths, $d$, divided by the total expected deaths, $d^{e}$. The overall $A / E$ ratio is also equal to the weighted average of the $(A / E) \times$ at each age, weighted by expected deaths, $d_{x}^{e}$, as demonstrated below:

$$
(A / E)=d / d^{e}=\Sigma d_{x} / \Sigma d_{x}^{e}=\Sigma\left(d_{x}^{e}(A / E)_{x}\right) / \Sigma d_{x}^{e}
$$

The overall expected rate for the whole population, $q^{e}$, is the average of the expected rates at each age weighted by the exposure. That is,

$$
q^{e}=\Sigma\left(E_{x} q_{x}^{e}\right) / \Sigma E_{x}=\Sigma d_{x}^{e} / \Sigma E_{x}
$$

### 12.1 Period Study with Deaths and Withdrawals

To illustrate the application of expected rates, we will use a population of healthy, female pensioners. Expected mortality rate, exposure, expected deaths, actual deaths, actual mortality rate and actual to expected ratio are shown below for each age. Expected mortality rates are from the RP2000 table.

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $(\boldsymbol{A} / \boldsymbol{E})_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | ---: | ---: | :---: | :---: |
| 65 | 0.01036 | 496.5 | 5.1 | 4 | 0.00806 | $77.7 \%$ |
| 66 | 0.01141 | 986.0 | 11.3 | 8 | 0.00811 | $71.1 \%$ |
| 67 | 0.01254 | 973.0 | 12.2 | 9 | 0.00925 | $73.8 \%$ |
| 68 | 0.01377 | 959.0 | 13.2 | 10 | 0.01043 | $75.7 \%$ |
| 69 | 0.01515 | 475.5 | 7.2 | 5 | 0.01052 | $69.4 \%$ |
| Total | 0.01260 | $3,890.0$ | 49.0 | 36 | 0.00925 | $73.5 \%$ |

The Total line includes sums of exposure and deaths, the overall average actual and expected mortality rates, and the overall A/E ratio. The overall A/E ratio indicates that 73\% of RP2000 may be a reasonable best estimate to use in projections.

### 12.2 Amount-Weighted Period Study

This example builds on the prior example by introducing amount weights, with the average benefit amounts paid on deaths less than the overall average benefits in force. The resulting amount-weighted expected events and A/E ratios for this population are shown below. Exposure, death and withdrawal amounts are per thousand.

| $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}}(\boldsymbol{A} / \boldsymbol{E})_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | ---: | ---: | :--- |
| 65 | 0.01036 | 744.8 | 7.7 | 5.6 | 0.00752 | $72.6 \%$ |
| 66 | 0.01141 | $1,479.4$ | 16.9 | 11.6 | 0.00784 | $68.7 \%$ |
| 67 | 0.01254 | $1,460.3$ | 18.3 | 12.4 | 0.00847 | $67.6 \%$ |
| 68 | 0.01377 | $1,440.4$ | 19.8 | 14.3 | 0.00989 | $71.8 \%$ |
| 69 | 0.01515 | 714.2 | 10.8 | 6.8 | 0.00945 | $62.4 \%$ |
| Total | 0.01260 | $5,839.1$ | 73.6 | 50.6 | 0.00866 | $68.7 \%$ |

The overall A/E ratio for the amount-weighed study is $4 \%$ lower than the overall A/E for the life-weighed study in the preceding table. When carrying out financial projections, or assessing financial impacts, the A/E ratio from an amount-weighted study will provide a better estimate of expected benefit amounts and other amounts.

### 12.3 Period Study with Calendar Year

Building on the example in previous section, the table below illustrates actual to expected results where ages have been split between calendar years:

| $\boldsymbol{y}$ | $\boldsymbol{x}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{B} \boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{B}}(\boldsymbol{A} / \boldsymbol{E})_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | ---: | ---: | ---: | :---: |
| 2010 | 65.5 | 0.01036 | 744.8 | 7.7 | 5.6 | 0.00752 | $72.6 \%$ |
| 2010 | 66.0 | 0.01141 | 743.4 | 8.5 | 5.8 | 0.00780 | $68.4 \%$ |
| 2011 | 66.5 | 0.01141 | 736.1 | 8.4 | 5.8 | 0.00788 | $69.0 \%$ |
| 2011 | 67.0 | 0.01254 | 734.4 | 9.2 | 6.2 | 0.00843 | $67.2 \%$ |
| 2012 | 67.5 | 0.01254 | 725.9 | 9.1 | 6.2 | 0.00852 | $68.0 \%$ |
| 2012 | 68.0 | 0.01377 | 724.5 | 10.0 | 7.1 | 0.00983 | $71.4 \%$ |
| 2013 | 68.5 | 0.01377 | 715.9 | 9.9 | 7.1 | 0.00995 | $72.3 \%$ |
| 2013 | 69.0 | 0.01515 | 714.2 | 10.8 | 6.8 | 0.00945 | $62.4 \%$ |
| Total |  | 0.01260 | $5,839.1$ | 73.6 | 50.6 | 0.00866 | $68.7 \%$ |

As a result of deaths being fully exposed to the end of the year of age in the first half of each age, exposure is higher in the first half of each age. As a consequence, expected deaths are higher and the A/E ratio is lower in the first half of each age when compared to the second half of each age.

In practice, companies typically compare actual to expected results by calendar year, quarter or month. Combining exposure and death amounts by calendar year and then recalculating mortality rates and A/E ratios, we have the following blended results:

| $\boldsymbol{y}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{E}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{B}} \boldsymbol{d}$ | ${ }_{\boldsymbol{B}} \boldsymbol{q}$ | ${ }_{\boldsymbol{B}}(\boldsymbol{A} / \boldsymbol{E})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2010 | 0.01089 | $1,488.1$ | 16.2 | 11.4 | 0.00766 | $70.4 \%$ |
| 2011 | 0.01198 | $1,470.4$ | 17.6 | 12.0 | 0.00815 | $68.1 \%$ |
| 2012 | 0.01315 | $1,450.5$ | 19.1 | 13.3 | 0.00918 | $69.8 \%$ |
| 2013 | 0.01446 | $1,430.1$ | 20.7 | 13.9 | 0.00970 | $67.1 \%$ |
| Total | 0.01260 | $5,839.1$ | 73.6 | 50.6 | 0.00866 | $68.7 \%$ |

### 12.4 Half-Year Study

For a study using fractional rate intervals, such as semi-annual, expected rates can be expressed for the rate intervals, or may continue to be expressed annually. When applying annual expected rates to such a study, it is customary (and may or may not be reasonable) to assume a constant decrement rate over the year.

For a year divided into $N$ intervals with fractional time period $f=1 / N$, let:

${ }_{f} \bar{q}_{x}^{e}$ be the constant fractional expected decrement rate with fractional period $f$ for age $x$ divided into $\mathrm{N}$ intervals.

The fractional expected rate can be calculated from the annual expected rate, $q_{x}^{e}$, as follows:

$$
{ }_{f} \bar{q}_{x}^{e}=1-\left(1-q_{x}^{e}\right)^{f}
$$

The table below shows the results of applying this fractional rate formula, with $f=1 / 2$, to the actual and expected annual rates from the first table in the previous section:

| $\boldsymbol{x}$ | $\boldsymbol{f}_{\boldsymbol{\boldsymbol { q }}}^{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{d}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}}$ | ${ }_{\boldsymbol{f}}(\boldsymbol{A} / \boldsymbol{E})_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | ---: | ---: | :---: | :---: |
| 65.5 | 0.00520 | $1,489.5$ | 7.7 | 5.6 | 0.00376 | $72.4 \%$ |
| 66.0 | 0.00572 | $1,480.9$ | 8.5 | 5.8 | 0.00392 | $68.4 \%$ |
| 66.5 | 0.00572 | $1,472.1$ | 8.4 | 5.8 | 0.00394 | $68.8 \%$ |
| 67.0 | 0.00629 | $1,462.6$ | 9.2 | 6.2 | 0.00423 | $67.3 \%$ |
| 67.5 | 0.00629 | $1,451.9$ | 9.1 | 6.2 | 0.00426 | $67.8 \%$ |
| 68.0 | 0.00691 | $1,441.9$ | 10.0 | 7.1 | 0.00494 | $71.5 \%$ |
| 68.5 | 0.00691 | $1,431.8$ | 9.9 | 7.1 | 0.00498 | $72.0 \%$ |
| 69.0 | 0.00761 | $1,421.7$ | 10.8 | 6.8 | 0.00475 | $62.4 \%$ |
| Total | 0.00632 | $11,652.3$ | 73.6 | 50.6 | 0.00434 | $68.7 \%$ |

The resulting $A / E$ ratios are very close to those produced using annual rates.

To match up half-year with annual results, the following adjustments are needed:

- Divide half-year exposure by two,
- Combine half-years of exposure and half-years of deaths for the same age.
- compound two half-year rates to determine the equivalent annual rate, and
- calculate $\mathrm{A} / \mathrm{E}$ as the ratio of the equivalent annual rates.

The following table shows the results after making the above adjustments. For simplicity, annual notation has been used.

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{E}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}$ | $(\boldsymbol{A} / \boldsymbol{E})_{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | ---: | :---: | :---: |
| 65 | 0.01036 | 744.8 | 7.7 | 5.6 | 0.00751 | $72.4 \%$ |
| 66 | 0.01141 | $1,476.5$ | 16.9 | 11.6 | 0.00784 | $68.7 \%$ |
| 67 | 0.01254 | $1,457.2$ | 18.3 | 12.4 | 0.00847 | $67.6 \%$ |
| 68 | 0.01377 | $1,436.9$ | 19.9 | 14.3 | 0.00989 | $71.8 \%$ |
| 69 | 0.01515 | 710.8 | 10.8 | 6.8 | 0.00947 | $62.5 \%$ |
| Total |  | $5,826.2$ | 73.6 | 50.6 |  |  |

For full years, the A/E ratios match the annual study, but for the partial years, there is a small discrepancy.

### 12.5 Half-Year Study with Daily Decrement Rates

To apply the expected rates in the above half-year study, it was assumed that each age was split into equal halfyears. However, each half-year will usually have a different number of days. For some studies, it is important to calculate expected decrements based on the exact number of days in the interval. This can be done through the use of an expected daily decrement rate.

Assuming the expected daily decrement rate, Day $\bar{q}_{x}^{e}$, is constant, it can be calculated from the expected annual decrement rate, $q_{x}^{e}$, assuming a 365 -day year, as follows:

$$
{ }_{D a y} \bar{q}_{x}^{e}={ }_{1 / 365} \bar{q}_{x}^{e}=1-\left(1-q_{x}^{e}\right)^{(1 / 365)}
$$

The expected decrement rate for an interval with $D$ days, and $\mathrm{f}=D / 365$, can be calculated from the expected daily decrement rate as:

$$
{ }_{f} q_{x}^{e}=1-\left(1-q_{x}^{e}\right)^{(D / 365)}=1-\left(1-{ }_{\text {Day }} \bar{q}_{x}^{e}\right)^{D}
$$

The above formulas can be enhanced to reflect the actual number of days in the year, rather than assuming 365 days.

Daily decrement rates can facilitate the calculation of decrements for any number of days, so long as the daily rate is expected to be constant over the period.

The following table illustrates the results of using daily decrement rates to calculate half-year expected rates where each half-year has its own numbers of days.

| $\boldsymbol{y}$ | $\boldsymbol{x}$ | ${ }_{\boldsymbol{f}} \boldsymbol{D}_{\boldsymbol{x}}$ | $\boldsymbol{N}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | ${ }_{\boldsymbol{D a y}} \overline{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{f}_{\boldsymbol{x}}^{\boldsymbol{e}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2010 | 65.5 | 181 | 365 | 0.01036 | 0.0000285423 | 0.00515 |
| 2010 | 66.0 | 184 | 365 | 0.01141 | 0.0000314478 | 0.00577 |
| 2011 | 66.5 | 181 | 365 | 0.01141 | 0.0000314478 | 0.00568 |
| 2011 | 67.0 | 184 | 366 | 0.01254 | 0.0000344783 | 0.00632 |
| 2012 | 67.5 | 182 | 366 | 0.01254 | 0.0000344783 | 0.00626 |
| 2012 | 68.0 | 184 | 365 | 0.01377 | 0.0000379902 | 0.00697 |
| 2013 | 68.5 | 181 | 365 | 0.01377 | 0.0000379902 | 0.00685 |
| 2013 | 69.0 | 184 | 365 | 0.01515 | 0.0000418319 | 0.00767 |

For age 66, it can be seen that instead of the former expected rate of 0.00572 for both half-years, the first year now has a higher rate of 0.00577 while the second half-year has a lower rate of 0.00568 .

## 13 Central Rates

Readers focused on fundamentals should skip or skim Chapters 13-16 and resume at Chapter 17.

So far, we have examined only initial rates, i.e., probabilities of decrement, which are based on and applied to the number of lives at the start of the rate interval, with an adjustment to exposure for decrements not under study. Alternatively, rates can be based on and applied to the amount of time lives were exposed to any decrement during the rate interval. Such a rate, called a central rate, is commonly used in population statistics but not directly used by most actuaries. While central rates can apply to any rate interval, we will focus on annual central rates applied to a year. The exposure used for central rates is called central exposure and is an estimate of the average population during the year or the population at the middle of the year.

Central exposure, denoted as $E_{x}^{c}$, is calculated based on the amount of time lives spend in the year of age $x$, as follows:

- $\quad$ Lives active at the start and end of the year of age $x$ are assigned exposure of one year.
- $\quad$ All decrements during the year of age $x$ are assigned exposure equal to the fraction of the year from exact age $x$ to the date of decrement.
- $\quad$ Lives active at the end of the study period during the year of age $x$ will be assigned exposure equal to the fraction of the year from exact age $x$ to the end date.
- $\quad$ Lives active at the start of the study period during the year of age $x$ will be assigned exposure equal to the fraction of the year from the start date to the exact age $x+1$.

The central decrement rate for each decrement, denoted as $m_{x}$, is calculated as the number of decrements divided by central exposure. Hence for deaths and withdrawals, the central rates are:

$$
\begin{aligned}
& m_{x}^{d}=d_{x} / E_{x}^{c} \text { and } \\
& m_{x}^{w}=w_{x} / E_{x}^{c}
\end{aligned}
$$

To calculate central rates for each decrement, only a single exposure calculation is required. This contrasts with initial rates, where a separate exposure calculation is required for each decrement.

The relationship between central exposure and daily exposure, and hence between central rates and daily rates and forces is simple: Central exposure is equal to daily exposure divided by the number of days in the year. For simplicity, we will assume 365 days per year:

$$
E_{x}^{c}=E_{x}^{\text {Day }} / 365
$$

From the above relationship, we see that daily rates times 365 are equal to central rates:

$$
\begin{aligned}
& 365_{\text {Day }} \bar{q}_{x}^{d}=365\left(d_{x} / E_{x}^{\text {Day }}\right)=d_{x} / E_{x}^{c}=m_{x}^{d}, \text { and } \\
& 365_{\text {Day }} \bar{q}_{x}^{w}=365\left(w_{x} / E_{x}^{\text {Day }}\right)=w_{x} / E_{x}^{c}=m_{x}^{w} .
\end{aligned}
$$

The average force of decrement is defined as the annualized instantaneous rate of decrement. It can be approximated with increasing accuracy by multiplying fractional decrement rates (i.e., monthly, daily, hourly, etc.) by the number of periods per year. In practice, the average force of decrement can be satisfactorily approximated by daily rates times the number of days in the year. Therefore, we have:

$$
\begin{aligned}
& \bar{\mu}_{x}^{d} \approx 365\left(d_{x} / E_{x}^{\text {Day }}\right)=d_{x} / E_{x}^{c}=m_{x}^{d}, \text { and } \\
& \bar{\mu}_{x}^{w} \approx 365\left(w_{x} / E_{x}^{\text {Day }}\right)=w_{x} / E_{x}^{c}=m_{x}^{w} .
\end{aligned}
$$

### 13.1 Annual Period Study

The central exposure formula can be derived directly from the definition above. For a period study, central exposure needs to be adjusted for partial years that can occur at the beginning and end of the study. Assuming the only decrements are death and withdrawal and that they are uniformly distributed, central exposure will be calculated using the following formula for full years and for partial years of age at the start and end of the study. " $t_{x}$ " denotes the fraction of the year of age $x$ that falls within the study:

$$
\begin{aligned}
E_{x}^{c} & =\left(l_{x+1}+1 / 2 d_{x}+1 / 2 w_{x}\right) T_{x} \\
& =\left(l_{x}-1 / 2 d_{x}-1 / 2 w_{x}\right) T_{x}
\end{aligned}
$$

Lives, decrements, central exposure and central mortality and withdrawal rates are shown below, based on the fouryear period study used for previous examples.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{c}}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{w}}$ |
| :---: | :---: | ---: | ---: | :---: | :---: | :---: | :---: |
| 65 | 994 | 4 | 2 | 0.5 | 495.5 | 0.00807 | 0.00404 |
| 66 | 988 | 8 | 4 | 1.0 | 982.0 | 0.00815 | 0.00407 |
| 67 | 976 | 9 | 6 | 1.0 | 968.5 | 0.00929 | 0.00620 |
| 68 | 961 | 10 | 4 | 1.0 | 954.0 | 0.01048 | 0.00419 |
| 69 | 947 | 5 | 2 | 0.5 | 471.8 | 0.01060 | 0.00424 |
| Total |  | 36 | 18 |  | $3,871.8$ | 0.00930 | 0.00465 |

Central rate studies are convenient as they allow rates for each decrement to be calculated from a single exposure measure. However, in most cases, independent rates are used when applying decrement rates. Assuming decrements are uniformly distributed over each year of age, the following exposure formulas for independent rates can be restated as central exposure plus a small adjustment:

$$
\begin{aligned}
& { }_{1 / 2} E_{65^{1 / 2}}^{d}=1 / 2 l_{65^{1 / 2}} \quad-1 / 4 W_{65^{1 / 2}}={ }_{1 / 2} E_{65^{1 / 2}}^{c}+1 / 4 d_{65^{1 / 2},} \\
& E_{x}^{d} \quad=l_{x} \quad-1 / 2 w_{x}=E_{x}^{c} \quad+1 / 2 d_{x} \text {, for } x=66,67 \text {, and } 68 \text {, and } \\
& { }_{1 / 2} E_{69}^{d}=1 / 2 l_{69}+1 / 2 d_{69}-1 / 4 w_{69}={ }_{1 / 2} E_{69}^{c}+3 / 4 d_{69} .
\end{aligned}
$$

Imagine a stable population where aging and new entrants exactly offset decrements and with birthdays uniformly distributed over the calendar year. For such a population with a study period consisting of multiple calendar years, each age with a partial year at the start of the study period will have a corresponding partial year at the end of the study period. The two partial years for each age will combine for one complete year. In this imaginary situation, the full-year exposure formula would produce accurate results for all ages.

To estimate independent rates from central rates, the following formulas for full years of age can be derived:

$$
\begin{aligned}
& q_{x}^{d}=m_{x}^{d} /\left(1+1 / 2 m_{x}^{d}\right), \text { and } \\
& q_{x}^{w}=m_{x}^{w} /\left(1+1 / 2 m_{x}^{w}\right) .
\end{aligned}
$$

From the above formulas, as central rates are positive, independent rates will be smaller than their corresponding central rates.

For the partial ages at the start and end of the study period, the $1 / 2$ factor in the above formulas must be replaced with factors of $1 / 4$ and $3 / 4$, respectively, analogous to the preceding adjustments to central exposure.

The following table illustrates independent rates estimated from central rates:

| $\boldsymbol{x}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{w}}$ |
| :---: | :---: | :---: | :---: | :---: |
| 65 | 0.00807 | 0.00404 | 0.00806 | 0.00403 |
| 66 | 0.00815 | 0.00407 | 0.00811 | 0.00407 |
| 67 | 0.00929 | 0.00620 | 0.00925 | 0.00618 |
| 68 | 0.01048 | 0.00419 | 0.01043 | 0.00418 |
| 69 | 0.01060 | 0.00424 | 0.01052 | 0.00423 |

Using central rates allows the independent rates for multiple decrements to be calculated from a single exposure measure, the central exposure, whereas directly calculating independent rates requires a separate exposure calculation for each decrement.

### 13.2 Force of Decrement

The probability of decrement can be calculated using the central rate as a close estimate of the average force of decrement, that is:

$$
\begin{aligned}
& q_{x}^{d}=1-e^{-\bar{\mu}_{x}^{d}} \approx 1-e^{-m_{x}^{d}}, \text { and } \\
& q_{x}^{w}=1-e^{-\bar{\mu}_{x}^{w}} \approx 1-e^{-m_{x}^{w}} .
\end{aligned}
$$

The following table illustrates independent rates estimated from the force of decrements:

| $\boldsymbol{x}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{m}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{w}}$ |
| :---: | :---: | :---: | :---: | :---: |
| 65 | 0.00807 | 0.00404 | 0.00804 | 0.00403 |
| 66 | 0.00815 | 0.00407 | 0.00811 | 0.00407 |
| 67 | 0.00929 | 0.00620 | 0.00925 | 0.00618 |
| 68 | 0.01048 | 0.00419 | 0.01043 | 0.00418 |
| 69 | 0.01060 | 0.00424 | 0.01054 | 0.00423 |

For age 65, the estimated mortality rate (0.00804) differs slightly from the rate based on the annual exposure method (0.00806), due to different underlying assumptions: The estimated rate assumes the force is constant over the year, while the annual exposure method assumes the rates for partial years are proportional to the full annual rate. There are similar differences for the age 69 mortality rates and the age 65 and 69 withdrawal rates.

## 14 Dependent Rates

Prior to Chapter 11, independent rates for mortality and withdrawal were calculated using exposures that were calculated separately for each decrement: Mortality rates were based on mortality exposure while withdrawal rates used withdrawal exposure. There is an alternative to calculating separate exposures: Dependent rates can be calculated using exposure based on a single composite decrement that combines deaths and withdrawals. Such rates are called dependent because their values depend on the values of one or more other decrements. For example, doubling a withdrawal rate will reduce exposure and thereby increase its dependent mortality rate, as we will see later in this chapter. While the descriptions of dependent exposure and rates may seem like those for central exposure and rates, there is important difference: Dependent exposure is based on and dependent rates are applied to the initial population, not the central population.

### 14.1 Cohort Study with Deaths and Withdrawals

We will examine a cohort study with deaths and withdrawals, starting at age 65. We will define a new, combined decrement, $a_{x}$, which will be the sum of deaths and withdrawals. In other words,

$$
a_{x}=d_{x}+w_{x}
$$

Values for the independent decrement rate, $q_{x}^{a}$, and its complement, the survival rate, $p_{x}^{a}$, are shown below.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{a}_{\boldsymbol{x}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{a}}$ | $\boldsymbol{p}_{\boldsymbol{x}}^{\boldsymbol{a}}$ |
| :---: | ---: | ---: | ---: | ---: | :---: | :---: |
| 65 | 1,000 | 7 | 5 | 12 | 0.01200 | 0.98800 |
| 66 | 988 | 8 | 4 | 12 | 0.01215 | 0.98785 |
| 67 | 976 | 9 | 6 | 15 | 0.01537 | 0.98463 |
| 68 | 961 | 10 | 4 | 14 | 0.01457 | 0.98543 |
| 69 | 947 |  |  |  |  |  |
| Total |  | 34 | 19 | 53 |  |  |

The combined decrement rate, $a_{x}$, can be split into component decrement rates, based on $d_{x}$ and $w_{x}$, which are called dependent or multiple decrement rates. They are denoted and calculated as follows:

$$
\begin{aligned}
& \hat{q}_{x}^{d}=d_{x} / l_{x} \text {, the dependent mortality rate over the year of age } x, \text { and } \\
& \hat{q}_{x}^{w}=w_{x} / l_{x} \text {, the dependent withdrawal rate over the year of age } x .
\end{aligned}
$$

From the preceding definitions, we can infer that:

$$
\begin{aligned}
& q_{x}^{a}=a_{x} / l_{x}=\left(d_{x}+w_{x}\right) / l_{x}=\hat{q}_{x}^{d}+\hat{q}_{x}^{w}, \text { and } \\
& p_{x}^{a}=1-q_{x}^{a}=1-\hat{q}_{x}^{d}-\hat{q}_{x}^{w} .
\end{aligned}
$$

Also, the dependent rates are proportional to the composite independent rates, i.e.,

$$
\hat{q}_{x}^{d}=\left(d_{x} / a_{x}\right) q_{x}^{a}, \text { and } \hat{q}_{x}^{w}=\left(w_{x} / a_{x}\right) q_{x}^{a}
$$

The next life table shows the dependent rates by decrement.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{p}_{\boldsymbol{x}}^{\boldsymbol{a}}$ |
| :---: | ---: | ---: | ---: | :---: | :---: | :---: |
| 65 | 1,000 | 7 | 5 | 0.00700 | 0.00500 | 0.98800 |
| 66 | 988 | 8 | 4 | 0.00810 | 0.00405 | 0.98785 |
| 67 | 976 | 9 | 6 | 0.00922 | 0.00615 | 0.98463 |
| 68 | 961 | 10 | 4 | 0.01041 | 0.00416 | 0.98543 |
| 69 | 947 |  |  |  |  |  |
| Total |  | 34 | 19 |  |  |  |

Because the combined decrement rate, $a_{x}$, was the only decrement in the preceding example, all lives were exposed to the combined decrement for the entire year. Therefore, the resulting exposure was equal to $l_{x}$. That same exposure was used to calculate the dependent rates.

### 14.2 Period Study with Deaths and Withdrawals

For a period study with partial years at the start and end of the study, the exposure needs to reflect the amount of time at risk during each year of age.

The exposure, $E_{x}^{a}$, used to calculate the dependent rates, is the exposure for the composite (e.g., mortality and withdrawal) decrement, $q_{x}^{a}$. Exposure for the composite decrement, denoted as $E_{x}^{a}$, is calculated using the same approach used for any independent decrement:

- $\quad$ Lives active at the start and end of the year of age $x$ are assigned exposure of one year.
- Decrements under study during the year of age $x$ are assigned exposure of one year.
- $\quad$ Decrements not under study during the year of age $x$ are assigned exposure for the fraction of the year from exact age $x$ to the date of decrement.
- $\quad$ Lives active at the end of the study period during the year of age $x$ will be assigned exposure of the fraction of the year from exact age $x$ to the end date.
- $\quad$ Lives active at the start of the study period during the year of age $x$ will be assigned exposure of the fraction of the year from the start date to the exact age $x+1$.

As both dependent decrements in the preceding example were under study and there were no other decrements, the core exposure for that example was simply the number of lives at age $x$ (ignoring the adjustments required for partial ages at the start and end of the study). Here are the resulting exposure formulas, including the adjustments for partial ages:

$$
\begin{aligned}
{ }_{1 / 2} E_{651 / 2}^{a} & =1 / 2 l_{65^{1 / 2}} \\
E_{x}^{a} & =l_{x}, \text { for } x=66,67, \text { and } 68 \text { and } \\
{ }_{1 / 2} E_{69}^{a} & =1 / 2 l_{69}+1 / 2 a_{69} .
\end{aligned}
$$

Dependent decrement rates are calculated as the number of decrements divided by composite exposure:

$$
\begin{aligned}
& \hat{q}_{x}^{d}=d_{x} / E_{x}^{a} \text { and } \\
& \hat{q}_{x}^{w}=w_{x} / E_{x}^{a} .
\end{aligned}
$$

The following life table below shows lives, decrements, exposure, dependent decrement rates and the probability of survival.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{a}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{p}_{\boldsymbol{x}}^{\boldsymbol{x}}$ |
| :---: | :---: | ---: | ---: | :---: | :---: | :---: | :---: | :---: |
| 65 | 994 | 4 | 2 | 0.5 | 497.0 | 0.00805 | 0.00402 | 0.98793 |
| 66 | 988 | 8 | 4 | 1.0 | 988.0 | 0.00810 | 0.00405 | 0.98785 |
| 67 | 976 | 9 | 6 | 1.0 | 976.0 | 0.00922 | 0.00615 | 0.98463 |
| 68 | 961 | 10 | 4 | 1.0 | 961.0 | 0.01041 | 0.00416 | 0.98543 |
| 69 | 947 | 5 | 2 | 0.5 | 477.0 | 0.01048 | 0.00419 | 0.98532 |
| Total |  | 36 | 18 |  | $3,899.0$ | 0.00923 | 0.00462 |  |

Dependent rate studies are convenient as they allow rates for each decrement to be calculated from a single composite exposure. This raises the question: Why not conduct all studies in this fashion, so that a single value of exposure can be used for all decrements? The answer is "context." Dependent rates can only be used with confidence in situations that mimic the study conditions, with the same set of dependent decrements (and no other decrements) operating in the same proportions. Therefore, independent rates are usually used when applying decrement rates.

When decrements are uniformly distributed over the year of age, independent rates can be accurately estimated by adjusting dependent exposure. For example, independent exposure formulas for deaths, denoted as $E_{x}^{d}$, can be rewritten in terms of dependent exposure, $E_{x}^{a}$, as follows:

$$
\begin{aligned}
& { }_{1 / 2} E_{65^{1 / 2}}^{d}=1 / 2 l_{65^{1 / 2}} \quad-1 / 4 w_{65^{1 / 2}}={ }_{1 / 2} E_{65^{1 / 2}}^{a}-1 / 4 w_{65^{1 / 2}}, \\
& E_{x}^{d}=l_{x} \quad-1 / 2 w_{x}=E_{x}^{a} \quad-1 / 2 w_{x} \text { for } x=66,67, \text { and } 68 \text {, and } \\
& { }_{1 / 2} E_{69}^{d}=1 / 2 l_{69}+1 / 2 d_{69}-1 / 4 w_{69}={ }_{1 / 2} E_{69}^{a}-3 / 4 w_{69} .
\end{aligned}
$$

Imagine a stable population with multiple cohorts of lives that can enter the population at any age with entrants uniformly distributed over the calendar year. Each age with a partial year at the start of the study period will have a corresponding partial year at the end of the study period. For such an imaginary population, the full-year exposure formula will produce accurate results for all ages.

Independent rates can be calculated directly from dependent rates. When there is a uniform distribution of decrements, results from the following formulas involving two decrements will exactly match the results from directly calculated independent rates. The derivation of the following formula is presented in the next section.

$$
\begin{aligned}
& q_{x}^{d}=\hat{q}_{x}^{d} /\left(1-1 / 2 \hat{q}_{x}^{w}\right) \text { and } \\
& q_{x}^{w}=\hat{q}_{x}^{w} /\left(1-1 / 2 \hat{q}_{x}^{d}\right) .
\end{aligned}
$$

In the above formulas, since the dependent rates are positive, the independent rates will be larger than their corresponding dependent rates.

The independent rate formulas also show that, while only one exposure is required to calculate multiple decrement rates, each independent rate is dependent on all decrement rates. This situation is more complex than using central exposure, where each independent rate is dependent on only the corresponding central rate.

For the partial half ages at the start and end of the study period, the $1 / 2$ factor in the independent rate formulas would be replaced with $1 / 4$ and $3 / 4$, respectively, as shown in the exposure formulas above. The following table illustrates the independent rates estimated from dependent rates.

| $\boldsymbol{x}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{w}}$ |
| :---: | :---: | :---: | :---: | :---: |
| 65 | 0.00805 | 0.00402 | 0.00806 | 0.00403 |
| 66 | 0.00810 | 0.00405 | 0.00811 | 0.00407 |
| 67 | 0.00922 | 0.00615 | 0.00925 | 0.00618 |
| 68 | 0.01041 | 0.00416 | 0.01043 | 0.00418 |
| 69 | 0.01048 | 0.00419 | 0.01052 | 0.00423 |

### 14.3 Population Projection

Before issuing life insurance contracts, a company would carry out financial projections using assumptions for decrements such as mortality and withdrawal to estimate the future cost of benefits to help set the level of premiums. Analogous projections would also be performed to calculate certain reserves, to forecast short-term financial results or to stress test capital levels. Projections often use best estimate assumptions for decrements and, for certain purposes, more adverse scenarios.

Such projections can be performed using independent or dependent rates. By using dependent rates, the interactions between decrements can be pre-calculated, simplifying later calculations.

To illustrate the use of dependent rates for projections, we will use mortality equal to $73 \%$ of the RP2000 mortality table and a withdrawal rate of $0.5 \%$ per year.

The survival rate for lives at each age is the product of the independent survival rates for each decrement, that is:

$$
p_{x}^{a}=p_{x}^{d} p_{x}^{w}=\left(1-q_{x}^{d}\right)\left(1-q_{x}^{w}\right)=1-q_{x}^{d}-q_{x}^{w}+q_{x}^{d} q_{x}^{w}
$$

Assuming a uniform distribution of decrements, dependent rates can be calculated from independent rates as follows:

$$
\begin{aligned}
& \hat{q}_{x}^{d}=q_{x}^{d}\left(1-1 / 2 q_{x}^{w}\right), \text { and } \\
& \hat{q}_{x}^{w}=q_{x}^{w}\left(1-1 / 2 q_{x}^{d}\right) .
\end{aligned}
$$

The above formulas hold true for both actual and expected rates. We will denote "best estimate" by adding a superscript of "e." The expected decrement and survival rates for each age are shown below.

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\text {ed }}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{e w}}$ | $\boldsymbol{p}_{\boldsymbol{x}}^{\text {ea }}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\text {ed }}$ | $\widehat{\boldsymbol{q}}_{x}^{\text {ew }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 65 | 0.00757 | 0.005 | 0.98747 | 0.00755 | 0.00498 |
| 66 | 0.00833 | 0.005 | 0.98671 | 0.00831 | 0.00498 |
| 67 | 0.00915 | 0.005 | 0.98589 | 0.00913 | 0.00498 |
| 68 | 0.01005 | 0.005 | 0.98500 | 0.01003 | 0.00497 |

The beginning number of lives for each year is simply multiplied by the dependent rates to determine that year's deaths and withdrawals, which in turn are used to determine the beginning number of lives for the following year.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{d}_{\boldsymbol{x}}^{\boldsymbol{e}}$ | $\boldsymbol{w}_{\boldsymbol{x}}^{\boldsymbol{e}}$ |
| :---: | ---: | ---: | ---: |
| 65 | 1,000 | 7.5 | 5.0 |
| 66 | 987 | 8.2 | 4.9 |
| 67 | 974 | 8.9 | 4.8 |
| 68 | 961 | 9.6 | 4.8 |
| 69 | 946 |  |  |
| Total |  | 34.3 | 19.5 |

### 14.4 Formula Derivation

Independent rates can be derived from dependent rates if we assume a uniform distribution of decrements.

From the definition of the dependent mortality rate, we have:

$$
d_{x}=l_{x} \hat{q}_{x}^{d}
$$

Deaths can also be calculated as exposure times the independent mortality rate:

$$
d_{x}=\left(l_{x}-1 / 2 w_{x}\right) q_{x}^{d}=l_{x}\left(1-1 / 2 \hat{q}_{x}^{w}\right) q_{x}^{d}
$$

By combining the above two equations and solving for $q_{x}^{d}$, we can derive the following relationship between the independent mortality rate and the two dependent decrement rates:

$$
q_{x}^{d}=\hat{q}_{x}^{d} /\left(1-1 / 2 \hat{q}_{x}^{w}\right) .
$$

If we presume $\hat{q}_{x}^{w}$ is positive, then the independent mortality rate, $q_{x}^{d}$ is always greater than the dependent mortality rate, $\hat{q}_{x}^{d}$. On the other hand, exposure is always less than $l_{x}$.

We can similarly derive an analogous formula for the independent withdrawal rate:

$$
q_{x}^{w}=\hat{q}_{x}^{w} /\left(1-1 / 2 \hat{q}_{x}^{d}\right) .
$$

To derive the formula for calculating dependent rates in term of independent rates, first rearrange the above formulae for independent rates, $\hat{q}_{x}^{d}=q_{x}^{d}\left(1-1 / 2 \hat{q}_{x}^{w}\right)$ and $q_{x}^{w}=\hat{q}_{x}^{w} /\left(1-1 / 2 \hat{q}_{x}^{d}\right)$ as

$$
\begin{aligned}
& \hat{q}_{x}^{d}=q_{x}^{d}\left(1-1 / 2 \hat{q}_{x}^{w}\right) . \\
& \hat{q}_{x}^{w}=q_{x}^{w}\left(1-1 / 2 \hat{q}_{x}^{d}\right) .
\end{aligned}
$$

Substitute the formula for $\hat{q}_{x}^{w}$ in that for $\hat{q}_{x}^{d}$ to get:

$$
\hat{q}_{x}^{d}=q_{x}^{d}\left(1-1 / 2 q_{x}^{w}\left(1-1 / 2 \hat{q}_{x}^{d}\right)\right) .
$$

Expand the terms on the right-hand side:

$$
\hat{q}_{x}^{d}=q_{x}^{d}-1 / 2 q_{x}^{d} q_{x}^{w}+1 / 4 q_{x}^{d} q_{x}^{w} \hat{q}_{x}^{d}
$$

Rearranging gives $\hat{q}_{x}^{d}$ in terms of the independent rates:

$$
\hat{q}_{x}^{d}=q_{x}^{d}\left(1-1 / 2 q_{x}^{w}\right) /\left(1-1 / 4 q_{x}^{d} q_{x}^{w}\right)
$$

For small $q_{x}^{d}$ and $q_{x}^{w}, 1-1 / 4 q_{x}^{d} q_{x}^{w} \approx 1$, so

$$
\hat{q}_{x}^{d} \approx q_{x}^{d}\left(1-1 / 2 q_{x}^{w}\right) .
$$

An analogous formula can be similarly derived for the dependent withdrawal rate:

$$
\hat{q}_{x}^{w}=q_{x}^{w}\left(1-1 / 2 q_{x}^{d}\right)
$$

## 15 Utilization Studies

To this point, the events under study have involved lives exiting the population, i.e., decrements. There may be other events or activities that can occur while the life is active in the population that do not result in the life leaving the population. For insurance contracts, these relate to the insured's utilization of benefits, such as claims or partial withdrawals, and options, such as exercising guaranteed rights, provided by the insurance or annuity contract.

A utilization study can examine the rates of such activities against several meaningful benchmarks, such as the following:

- $\quad$ The frequency of claims compared to the amount of time that lives have spent within the population, i.e., the central exposure,
- The severity of claims, that is, the average claim amount paid,
- Loss ratio: the claim amounts incurred compared to the premiums paid, and
- Annuity withdrawal utilization rates, i.e., the ratio of annual withdrawals to the sum of Maximum Allowable Annual Withdrawals, for contracts with a guaranteed lifetime withdrawal benefit (GLWB).


### 15.1Frequency and Severity

To illustrate frequency and severity rates, consider a four-year period study of claims for prescription drugs under a health plan. The following notation is used:

$n_{x}$ is number of claims incurred over the year of age $x$.

$C_{x}$ is total amount of claims incurred over the year of age $x$.

$E_{x}^{c}$ is central exposure over the year of age $x$.

$f_{x}$ is the claim rate, or frequency rate, of claims over the year of age $x$.

$s_{x}$ is the average claim amount per claim, or severity rate, over the year of age $x$.

Frequency and severity rates are calculated as follows:

$$
\begin{aligned}
& f_{x}=n_{x} / E_{x}^{c} \text { and } \\
& s_{x}=C_{x} / n_{x} .
\end{aligned}
$$

The following table illustrates the components of frequency and severity rates:

| $\boldsymbol{x}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{c}}$ | $\boldsymbol{n}_{\boldsymbol{x}}$ | $\boldsymbol{C}_{\boldsymbol{x}}$ | $\boldsymbol{f}_{\boldsymbol{x}}$ | $\boldsymbol{s}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | ---: | :---: | :---: |
| 65 | 495.5 | 253 | $\$ 4,496$ | 0.511 | $\$ 17.77$ |
| 66 | 982.0 | 481 | $\$ 11,385$ | 0.490 | $\$ 23.67$ |
| 67 | 968.5 | 465 | $\$ 10,186$ | 0.480 | $\$ 21.91$ |
| 68 | 954.0 | 496 | $\$ 8,949$ | 0.520 | $\$ 18.04$ |
| 69 | 471.8 | 255 | $\$ 6,193$ | 0.541 | $\$ 24.29$ |
| Total | $3,871.8$ | 1,950 | $\$ 41,209$ | 0.504 | $\$ 21.13$ |

The frequency and severity analysis can be done on both a paid and incurred basis. For the paid basis, the analysis uses actual claim payments at the paid date. For the incurred basis, the analysis uses the claim payments together with an estimate for claims incurred but not reported, usually abbreviated as IBNR, as of the study end date.

To manage claim costs, claim amounts are limited by deductibles, co-pays and contract limits, where limits may be per claim, per year or for the contract lifetime. As a result, both the gross claim submitted and the net claim paid
can be analyzed in the context of the reductions applied. The severity, or average amount per claim, does not indicate the extent to which the annual maximum has been utilized under the contract. The extent to which annual maximum limits are utilized can be a critical assumption for pricing and valuation.

### 15.2 Utilization of Maximum Limits

Annual maximums will affect the distribution of claims: fewer claims will occur towards the end of the year after annual maximums are reached. It is not reasonable to assume that claims are proportional to the amount of time spent in the year. The entire year needs to be studied as a single unit, with exposure calculated with decrements from the start of the year. Partial years arising from the study period must be excluded or used with full knowledge of the distortions.

Exposure in the presence of claim limits will be denoted $E_{x}^{M}$, with the " $\mathrm{M}$ " superscript signifying the presence of one or more maximum limits, and will be calculated as follows:

$$
E_{x}^{M}=l_{x}-d_{x}-w_{x}
$$

The table below shows the exposure calculated only for complete years of age - complete years are required when annual limits are involved, such as a maximum annual deductible, a maximum annual co-pay or a maximum annual benefit.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{M}}$ |
| :---: | :---: | ---: | ---: | ---: |
| 66 | 988 | 8 | 4 | 976 |
| 67 | 976 | 9 | 6 | 961 |
| 68 | 961 | 10 | 4 | 947 |
| Total |  | 27 | 14 | 2,884 |

We will add the following notation to capture the effect of a maximum annual benefit:

$\boldsymbol{M}_{\boldsymbol{x}}$ is the maximum annual benefit per claimant.

$\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{M}}$ is the exposure for full years, assuming decrements occur at the start of the year.

$\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}}$ is the number of lives that incurred at least one claim in the year of age $\boldsymbol{x}$.

$\boldsymbol{C}_{\boldsymbol{x}}^{\boldsymbol{l}}$ is the total amount of claims incurred for lives completing a full year of age $\boldsymbol{x}$.

$\boldsymbol{f}_{\boldsymbol{x}}^{\boldsymbol{l}}=\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}} / \boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{M}}$, is the rate of claims, i.e., the claim frequency, over the year of age $\boldsymbol{x}$.

$s_{x}^{l}=C_{x}^{l} / n_{x}^{l}$, is the average total claim per claimant over the year of age $\boldsymbol{x}$.

$u_{\boldsymbol{x}}=s_{x}^{l} / \boldsymbol{M}_{\boldsymbol{x}}$, the average proportion of the maximum claim amount utilized over year of age.

The frequency and severity of claims, along with claim utilization, are shown below.

| $\boldsymbol{x}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{M}}$ | $\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{C}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{f}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{s}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{M}_{\boldsymbol{x}}$ | $\boldsymbol{u}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 66 | 976 | 239 | $\$ 11,315$ | 0.245 | $\$ 47.34$ | $\$ 100$ | $47.34 \%$ |
| 67 | 961 | 231 | $\$ 10,107$ | 0.240 | $\$ 43.75$ | $\$ 100$ | $43.75 \%$ |
| 68 | 947 | 246 | $\$ 8,884$ | 0.260 | $\$ 36.11$ | $\$ 100$ | $36.11 \%$ |
| Total | 2,884 | 716 | $\$ 30,306$ | 0.248 | $\$ 42.33$ | $\$ 100$ | $42.33 \%$ |

### 15.3 Loss Ratio

The premiums paid for an insurance contract reflect the cost of claims, expenses and profit. The cost of claims is often expressed as a percentage of the premiums paid, which is referred to as the loss ratio. Often, product pricing anticipates a certain loss ratio. In the face of rising medical costs, future premium adjustments may be necessary to keep the loss ratio within an acceptable range. Let:

$P_{x}$ be the total premiums paid over the age $x$ and

$(L R)_{x}=C_{x} / P_{x}$ be the loss ratio for year of age $x$.

The premium rate is $\$ 20$ per year, paid monthly. In practice, the premium amounts, usually referred to as earned premium, are usually calculated directly from premium payments with adjustments for accounting liabilities such as unearned, advance and due premiums. For this simple example, premiums are calculated as the premium rate times central exposure:

$$
P_{x}=\$ 20 \cdot E_{x}^{c}
$$

The table below shows premiums, claims and loss ratios:

| $\boldsymbol{x}$ | $\boldsymbol{P}_{\boldsymbol{x}}$ | $\boldsymbol{C}_{\boldsymbol{x}^{\mathrm{x}}}$ | $(\boldsymbol{L R})_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: |
| 65 | $\$ 9,910$ | $\$ 4,496$ | $45.37 \%$ |
| 66 | $\$ 19,640$ | $\$ 11,385$ | $57.97 \%$ |
| 67 | $\$ 19,370$ | $\$ 10,186$ | $52.59 \%$ |
| 68 | $\$ 19,080$ | $\$ 8,949$ | $46.90 \%$ |
| 69 | $\$ 9,435$ | $\$ 6,193$ | $65.64 \%$ |
| Total | $\$ 77,435$ | $\$ 41,209$ | $53.22 \%$ |

### 15.4 Variable Annuity Withdrawal Utilization

Variable annuities often offer a range of guaranteed living benefits that can be elected through riders attached to the base variable annuity contract. Utilization studies are performed to capture the rates at which such riders are elected.

To illustrate such studies, we will focus on account withdrawals (not to be confused with population withdrawals or policy surrenders) under a guaranteed lifetime withdrawal benefit (GLWB). Under this benefit option, annuitants start taking withdrawals at some time after issue up to a contractually guaranteed maximum withdrawal amount. Withdrawals can continue for the life of the contract owner even if the annuity contract value is eventually depleted. These withdrawals are sometimes set up as automatic payments. Amounts withdrawn in a contract year that are in excess of the contractual maximum can reduce future benefits. While this benefit is normally associated with variable annuities, a similar benefit is now being offered on some fixed indexed annuity products.

Utilization studies for benefits of this type examine both the frequency and severity of benefit utilization. These studies are usually done on a calendar year basis using year-end extracts. As the pattern of withdrawals over a calendar year period is not uniform, partial years arising from new business and deaths are usually excluded from studies of utilization levels.

To illustrate the methodology for a study of variable annuity GLWB utilization, we will use the same pensioner population described in earlier examples, but we will assume the data is by calendar year, instead of life year. The partial year for age 65 will be excluded, and the study will end at age 68.

The exposure, denoted $E_{x}^{V A}$, with the "VA" superscript used to distinguish it from the other exposures previously defined, is given by:

$$
E_{x}^{V A}=l_{x}-d_{x}-w_{x}
$$

The table below shows the exposure calculated only for complete years of age.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{M}}$ |
| :---: | :---: | ---: | ---: | ---: |
| 66 | 988 | 8 | 4 | 976 |
| 67 | 976 | 9 | 6 | 961 |
| 68 | 961 | 10 | 4 | 947 |
| Total |  | 27 | 14 | 2,884 |

We will add the following notation to capture the effect of a maximum annual benefit:

$\boldsymbol{M}_{\boldsymbol{x}}$ is the maximum annual withdrawal amount per withdrawing annuitant, which is assumed to be the same for all annuitants in the year of age $\boldsymbol{x}$.

$\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{V A}}$ is the exposure for full years, assuming decrements occur at the start of the year.

$\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}}$ is the number of lives who made at least one withdrawal in the year of age $\boldsymbol{x}$.

$\boldsymbol{W}_{\boldsymbol{x}}^{\boldsymbol{l}}$ is the total amount of withdrawals for lives completing a full year of age $\boldsymbol{x}$.

$\boldsymbol{f}_{\boldsymbol{x}}^{\boldsymbol{l}}=\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}} / \boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{V A}}$, is the proportion of the population withdrawing, i.e., the withdrawal frequency, over the year of age $\boldsymbol{x}$.

$\boldsymbol{s}_{\boldsymbol{x}}^{\boldsymbol{l}}=\boldsymbol{W}_{\boldsymbol{x}}^{\boldsymbol{l}} / \boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}}$, is the average total withdrawal per withdrawing annuitant over the year of age $\boldsymbol{x}$.

$\boldsymbol{u}_{\boldsymbol{x}}=\boldsymbol{s}_{\boldsymbol{x}}^{\boldsymbol{l}} / \boldsymbol{M}_{\boldsymbol{x}}$, the average proportion of the maximum withdrawal amount utilized over year of age.

The frequency and severity of withdrawals, along with withdrawal utilization, are shown below.

| $\boldsymbol{x}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{V A}}$ | $\boldsymbol{n}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{W}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{f}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{s}_{\boldsymbol{x}}^{\boldsymbol{l}}$ | $\boldsymbol{M}_{\boldsymbol{x}}$ | $\boldsymbol{u}_{\boldsymbol{x}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 66 | 976 | 201 | $\$ 1,006,627$ | $21 \%$ | $\$ 5,013$ | $\$ 6,000$ | $84 \%$ |
| 67 | 961 | 238 | $\$ 1,201,488$ | $25 \%$ | $\$ 5,051$ | $\$ 6,000$ | $84 \%$ |
| 68 | 947 | 257 | $\$ 1,343,981$ | $27 \%$ | $\$ 5,236$ | $\$ 6,000$ | $87 \%$ |
| Total | 2,884 | 695 | $\$ 3,552,096$ | $24 \%$ | $\$ 5,108$ | $\$ 6,000$ | $85 \%$ |

## 16 Exposure and Rate Comparisons

This paper has presented many alternatives for calculating exposure and rates. This chapter compares results for various combinations of alternatives. These results were calculated in previous chapters: Independent mortality rates in Section 4.3.2, independent withdrawal rates in Section 11.1.1, central rates in Section 13.1 and dependent rates in Section 14.2 .

The following table compares the exposures used to calculate independent mortality and withdrawal rates, dependent rates and central rates. Note that dependent and central rates require only one exposure calculation for all decrement rates, from which independent rates can be estimated.

| $\boldsymbol{x}$ | $\boldsymbol{l}_{\boldsymbol{x}}$ | $\boldsymbol{d}_{\boldsymbol{x}}$ | $\boldsymbol{w}_{\boldsymbol{x}}$ | $\boldsymbol{T}_{\boldsymbol{x}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{a}}$ | $\boldsymbol{E}_{\boldsymbol{x}}^{\boldsymbol{c}}$ |
| :---: | :---: | ---: | ---: | ---: | :--- | :--- | :--- | :--- |
| 65 | 994 | 4 | 2 | 0.5 | 496.5 | 496.0 | 497.0 | 495.5 |
| 66 | 988 | 8 | 4 | 1.0 | 986.0 | 984.0 | 988.0 | 982.0 |
| 67 | 976 | 9 | 6 | 1.0 | 973.0 | 971.5 | 976.0 | 968.5 |
| 68 | 961 | 10 | 4 | 1.0 | 959.0 | 956.0 | 961.0 | 954.0 |
| 69 | 947 | 5 | 2 | 0.5 | 475.5 | 473.3 | 477.0 | 471.8 |
| Total |  | 36 | 18 |  | $3,890.0$ | $3,880.8$ | $3,899.0$ | $3,871.8$ |

The next table compares independent, dependent and central rates, separately for mortality and withdrawal:

| $\boldsymbol{x}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{d}}$ | $\boldsymbol{m}_{x}^{\boldsymbol{d}}$ | $\boldsymbol{q}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\widehat{\boldsymbol{q}}_{\boldsymbol{x}}^{\boldsymbol{w}}$ | $\boldsymbol{m}_{x}^{\boldsymbol{w}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 65 | 0.00806 | 0.00805 | 0.00807 | 0.00403 | 0.00402 | 0.00404 |
| 66 | 0.00811 | 0.00810 | 0.00815 | 0.00407 | 0.00405 | 0.00407 |
| 67 | 0.00925 | 0.00922 | 0.00929 | 0.00618 | 0.00615 | 0.00620 |
| 68 | 0.01043 | 0.01041 | 0.01048 | 0.00418 | 0.00416 | 0.00419 |
| 69 | 0.01052 | 0.01048 | 0.01060 | 0.00423 | 0.00419 | 0.00424 |

The above estimates are only valid if decrements are uniformly distributed over the year.

The following table compares a mortality rate, calculated using its own exposure, with an estimate derived from dependent rates, with no observable difference:

| $\boldsymbol{x}$ | Actual | Estimate | Difference |
| :---: | :---: | :---: | :---: |
| 65 | 0.00806 | 0.00806 | $0.00 \mathrm{E}+00$ |
| 66 | 0.00811 | 0.00811 | $0.00 \mathrm{E}+00$ |
| 67 | 0.00925 | 0.00925 | $0.00 \mathrm{E}+00$ |
| 68 | 0.01043 | 0.01043 | $0.00 \mathrm{E}+00$ |
| 69 | 0.01052 | 0.01052 | $0.00 \mathrm{E}+00$ |

Comparing the same independent mortality rate to an estimate derived from central rates, we again see no differences:

| $\boldsymbol{x}$ | Actual | Estimate | Difference |
| :---: | :---: | :---: | :---: |
| 65 | 0.00806 | 0.00806 | $0.00 \mathrm{E}+00$ |
| 66 | 0.00811 | 0.00811 | $0.00 \mathrm{E}+00$ |
| 67 | 0.00925 | 0.00925 | $0.00 \mathrm{E}+00$ |
| 68 | 0.01043 | 0.01043 | $0.00 \mathrm{E}+00$ |
| 69 | 0.01052 | 0.01052 | $0.00 \mathrm{E}+00$ |

Comparing the same independent mortality rate to an estimate derived from using central rates as the force of decrement for mortality, we see some small differences:

| $\boldsymbol{x}$ | Actual | Estimate | Difference |
| :---: | :---: | :---: | :---: |
| 65 | 0.00806 | 0.00804 | .0000162 |
| 66 | 0.00811 | 0.00811 | $4.47 \mathrm{E}-08$ |
| 67 | 0.00925 | 0.00925 | $6.63 \mathrm{E}-08$ |
| 68 | 0.01043 | 0.01043 | $9.50 \mathrm{E}-08$ |
| 69 | 0.01052 | 0.01054 | -.0000276 |

## 17 Practical Considerations

Readers focused on fundamentals should skim this chapter for relevant material.

### 17.1 Amount-Weighted Distortions

While amount-weighted rates are essential for those wishing to reproduce or analyze financial results, they can introduce distortions, such as a skewed mortality rate caused by a single large claim.

A common analytic tactic is to compare amount-weighted and population-weighted rates. Where there is a large discrepancy between the two, it is usually advisable to investigate further. One of the following is usually indicated:

- One or a few large amounts have distorted the numerator of the amount-weighted rate: Usually, this can be determined through a search of the data for unusually large utilization or decrement amounts.
- This type of distortion is not easily remedied. Unusually large amounts could be spread across many cells, such that the resulting overall rates still reproduce actual experience. Some companies simply cap the maximum amount included in the study and do the same for exposure calculations.
- Risks or behaviors differ significantly by amount: This can argue for adding a "size band" that groups the population by size ranges for the amount, further subdividing cells.

Amount-weighted rates may be correlated with income levels, socioeconomic class, education levels, and so on. Amount-weighted rates may also be correlated with behaviors, with very small amounts sometimes representing little commitment, care or interest and very large amounts sometimes tied to intentions to defraud.

### 17.2 Data Extracts for Multi-Year Studies

Experience from multiple years is often combined to produce an experience study with added credibility. It also reduces distortions caused by reporting lags: The earliest data in the study should have fewer issues related to late reporting.

Multi-year studies are not simply the sum of single-year studies. Multi-year experience data is constructed using the latest information available, including some transactions reported long after their effective dates. The data construction process is nearly identical to that used for a one-year study. The main difference is that each member of the study population has the possibility of populating many more cells due to the larger number of rate intervals included in a multi-year study. The inclusion of a study-year or calendar-year variable in a multi-year study allows for the study of trends.

### 17.3 Homogeneity of Data

Care should be taken to ensure that study data is homogenous. Results should be examined to see how they vary by each significant attribute. For example, significant changes in underwriting practices over the years may require a mortality study to examine results by groups of issue years. A lapse study might look at results separately for each mode and method of payment. Also, there may be outliers that should be excluded from a study, such as excluding substandard lives from a study of mortality rates.

### 17.4 Reporting Lags

All businesses are subject to lags in reporting. For example:

- Health claims can be submitted for insurance reimbursement months after they were incurred. Many health plans have a cut-off date, such as April 1 of the year following the claim's incurral, after which prior year claims will not be reimbursed.
- Death claims for life insurance policies are often received months or even years after the insured died, and sometimes not at all. This is especially true for policies that have not had a premium payment for many years. After the insured dies, beneficiaries may not realize that the insured had an in-force life insurance policy, so no claim is submitted.
- Individual disability income and long-term care insurance policies typically have an elimination period of months or more. Insureds will often delay reporting claims until the elimination period has run its course, with the expectation of collecting benefits soon after filing the claim.
- $\quad$ Direct writers and employers sometimes get behind in reporting claims to reinsurers and group insurers, respectively, a process known as "shoe boxing". This can occasionally delay the reporting of claims for a year or more.
- Immediate annuity and disability payments sometimes mistakenly continue after the annuitant or insured has died. This is commonly dealt with through a periodic confirmation that the person is still alive, with the occasional result that deaths are not confirmed until well after the fact.

A typical approach to address the natural claim reporting lag is to wait several to many months after the close of the study period before gathering data for an experience study. For example, the mortality study for calendar year 2016 may need to wait until the end of September 2017 before gathering claims data for 2016 deaths, in order to allow sufficient time for the great majority of 2016 death claims to be reported.

Each time an experience study is performed, a fresh study of incurred but not reported claims ("IBNR") can also be performed. Over time, improved estimates of IBNR can be developed and used to better estimate IBNR for the latest experience study. If unreported claims are deemed material, the gathering of data for the study could be delayed to allow more time for claims to be reported. Alternatively, IBNR data could be used to estimate claims not included in the study, with an adjustment made to study results to compensate.

Unknown lags can wreak havoc. A "perfect storm" example was the Australian superannuation disability market in the early 2010s. "Superannuation" refers to a group pension fund that also purchases life and disability insurance for its members. For years, many fund members did not realize they were covered by disability insurance and therefore did not claim their disability benefits. In the span of two years, a wave of realization swept the market and claims were retroactively made. Insurers and reinsurers of this business, charging premiums that did not reflect the unclaimed benefits, collectively suffered a loss of over one billion Australian dollars.

### 17.5 Non-Uniform Distribution of Events

Many of the exposure formulas in this paper were simplified by assuming a uniform distribution of events. Not all events cooperate with this assumption. For example:

- Lapses vary greatly by month because most lapses occur on premium due dates, which are dictated by the premium frequency. This is very significant for level premium term policies at the end of the level term period, and for long-term care policies that are subject to a significant premium rate increase. In such cases, the use of a monthly rate interval can overcome the distortions inherent in an annual rate interval.
- At the oldest ages where the likelihood of surviving another year is relatively constant and approximately equal to 0.5 , the number of survivors will decrease by a constant percentage each month. When annual rates are prorated at the oldest ages, deaths are underestimated in the first half of the year and overestimated in the second half of the year.

There are ways to compensate for non-uniform distributions:

1. Switch to an interval with a shorter frequency for the period of time most affected by the distortion.
2. Determine factors that can be used to adjust the results distorted by the non-uniform distribution, such as a premium adjustment factor or a weighted average policy month of decrement.
3. For old-age mortality, use a constant force of decrement to model more deaths in the first half of the year.

### 17.6 Partial Policy Years

This section addresses two different questions involving partial policy years in relation to three different exposure methods. The questions are:

- When study start and end dates create partial policy years, should the study include those partial policy years?
- When it's desirable to simultaneously allocate experience by policy year and calendar year, how best to do so?


### 17.6.1 Overview

The answers to the above questions are closely tied to the errors that can result from various choices. With any errors, it is not the relative size that matters, but the materiality of the financial impact of the errors.

Errors arising from partial policy years can be eliminated by using a policy year study period that includes only complete policy years and excludes the partial policy years. In this case, the results will be the same no matter which exposure method is used. Industry studies often use a policy year study period.

The errors in rate estimation that arise from the use of the partial years were explored in Section 9.2 and will be explored in more depth in Chapter 19. All exposure methods generate errors when the actual distribution of events does not match the distribution implicitly assumed by the exposure method. This is always the case.

While the method with a distribution assumption closest to the actual distribution will have the smallest errors, these errors may still be material. On the other hand, the relative difference between the errors for each method may be small, in which case the choice of method is not critical.

For each exposure method, the errors arising from the partial years at the start and end of the study period are roughly equal and opposite in sign. For a study across multiple cohorts (e.g. multiple years of birth or years of issue), errors will largely offset and result in a reduced net error. For a perfectly stable population, the errors would net to zero for all ages. From a practical perspective, the errors over the main range of ages or years for the population may well be stable enough. In addition, the stability assumption only needs to be "local". For example, for lives aged 65 in a single calendar year, "stable enough" may be achieved if there were a similar number of lives in the prior and following cohorts. Errors arising at the youngest and oldest ages, which lack offsets, may be immaterial due to the size of the population at those ages.

The purpose of the study should be a consideration. For a study illustrating the financial impact of an aging population, each year's projection will have similar errors such that the year-to-year change will be relatively unaffected. For valuation purposes, rates are usually not selected directly from an experience study but by applying percentages of an appropriate industry standard table. In this case, the final rates will be weighted by the overall experience, with understatements and overstatements of rates largely offsetting.

Partial year errors are related to both the size of the rates and the difference between the actual distribution of events and the distribution implicit to the exposure method used. Discrete decrements can be viewed as the limiting case, such as when lapses occur only at the end of the policy year: An entire year's worth of exposure occurs on a single day. It is common practice to use a policy-year study period and exclude partial policy years in these situations.

Partial year errors will vary greatly. None of the exposure methods will be ideal for every situation. At the same time, it may not be practical or desirable to use different exposure methods for different events, products, ages and the like.

### 17.6.2 Inclusion of Partial Policy Years

If the event under study is distributed fairly evenly through the policy year, it is customary for the study to include the partial policy years created by the study start and end dates. This is typically the case for biologically-driven rates such as mortality and morbidity. Also, for biologically-driven rates, allocation of policy year results between calendar years is not uncommon.

When the event under study is not evenly distributed through the policy year, results can be distorted by partial policy years, so careful consideration should be given to the decision to include or exclude partial policy years from the study. Partial policy years are often excluded for behavioral-driven rates such as lapse, withdrawal, and option election. Also, for behavioral-driven rates, likely distortions often make it unwise to allocate policy year results between calendar years.

### 17.6.3 Overview of Exposure Methods

When fractional rates can be assumed to be constant, the issue of which exposure method to use can be sidestepped by calculating average fractional rates, such as monthly or daily rates. The calculation of daily exposure for partial policy years is intuitive: The days exposed start no earlier than the start date of the study and end no later than the end date of the study.

The choice of annual or distributed exposure for partial policy years is more complex: The traditional "annual exposure method" is consistent with the Balducci Hypothesis. The more intuitive "distributed exposure method" is consistent with a uniform distribution for the decrement under study. Each has its advantages and shortcomings. The two methods differ only in their treatment of exposure for the decrement under study. While sometimes more accurate, the distributed exposure method requires data on deaths for the year preceding the study.

### 17.6.4 Annual Exposure Method

Under the annual exposure method, decrements under study are exposed to the end of the next policy anniversary, even when the next policy anniversary is beyond the end of the study period. On the surface, this may seem incorrect, but there is both logic and an offset described in the next paragraph. When the rates under study increase over time, the annual exposure method produces rates for the partial policy year at the end of the study that are understated and rates for the partial policy year at the beginning of the study that are overstated. The degree of understatement and overstatement becomes noticeable as rates approach $5 \%$ and significant as rates approach $50 \%$.

The annual exposure method's extension of exposure beyond the end of the study period can be rationalized in a couple of ways: First and foremost, it makes sense from the standpoint of calculating probability as the number of events divided by the number of trials. Secondly, the partial policy year at the beginning of a study does not include any exposure for the decrements under study that occurred before the study's start date. The annual exposure method captures this otherwise missing exposure in the partial policy year at the end of the preceding study. These
offsetting differences allow the results of sequential studies to be added together with no gaps or overlaps. The same is true for the distributed exposure method.

### 17.6.5 Distributed Exposure Method

Some companies simultaneously allocate exposure and decrements by both policy year and calendar year, for the entire duration of multi-year studies. Chapter 9 showed that, when underlying rates are increasing, the distributed exposure method produces more accurate partial year rates than the annual exposure method. However, when the underlying rates are decreasing, the opposite is true.

The distributed and annual exposure methods produce the same total annual exposure for each policy year, but the allocation between calendar years differs. The distributed exposure method can be described as "Exposure that happens in a calendar year, stays in that calendar year." The difference between the distributed and annual exposure methods is in the allocation of exposure for the decrement under study. The following outline is an algorithm for calculating distributed exposure for a policy year $t$ that starts in calendar year $\mathrm{CY}$ and ends in calendar $\mathrm{CY}+1$.

1. Total Annual Exposure for policy year $t$ is calculated in the usual fashion, with deaths exposed to the end of the policy year of death, using data from both calendar years.
2. First-Half Exposure (i.e., annual exposure for policy year $t$ in calendar year $\mathrm{CY}$ ) is calculated as follows:

a. Decrements under study that occur during $\mathrm{CY}$ are exposed from the policy anniversary to the end of $\mathrm{CY}$.

b. Other decrements that occur in $\mathrm{CY}$ are exposed from the policy anniversary to their decrement dates.

c. Lives that survive to the end of $\mathrm{CY}$ are exposed from the policy anniversary to the end of $\mathrm{CY}$.

3. Second-Half Exposure (i.e., annual exposure for the remainder of policy year $t$, which occurs in calendar year $C Y+$ 1), is then calculated as Total Annual Exposure minus First-Half Exposure.

The difference between the distributed and annual exposure methods involves the exposure, for decrements under study occurring in calendar year $\mathrm{CY}$, for the period that runs from the end of calendar year $\mathrm{CY}$ to the next policy anniversary:

- Under the annual exposure method, this exposure is included in the exposure for calendar year CY.
- Under the distributed exposure method, this exposure is included in the exposure for calendar year CY +1 .

The partial policy year at the very beginning of a multi-year study does not lend itself to the above algorithm, as it requires policy year data from the calendar year before the study start date. Distributed exposure for this partial policy year must therefore be calculated directly, as follows:

1. Decrements under study are exposed from the study start date to the policy anniversary.
2. Other decrements are exposed from the study start date to their decrement dates.
3. Lives that survive the policy year are exposed from the study start date to the policy anniversary.
4. Decrements under study (for the same policy year) that occurred in the prior calendar year are exposed from the study start date to the policy anniversary.

The first three items in the above list are readily calculated from normal experience study data. The fourth item requires knowledge of deaths that occurred in the year before the study start date. With some planning, this data can be obtained.

## 18 Product-Related Considerations

Readers focused on fundamentals should skim this chapter for relevant material.

### 18.1 Individual Life Insurance

### 18.1.1 Grace Period

In the U.S. and Canada, individual insurance policies must include a grace period, varying by state or province from a low of 30 days to a high of 60 days. If the insured dies during the grace period, the company must pay the death benefit even though premiums are up to 60 days overdue. When death occurs during the grace period, the beneficiary receives the death benefit net of the overdue premiums. Deaths and lapses during the grace period are handled as follows:

- A death during the grace period would be effective on the date of death for the full death benefit. In general, death benefits are not adjusted for premiums due, premiums paid beyond the date of death or interest due from date of death to date of claim settlement, as these adjustments serve to maintain equity between the insurer and the beneficiary.
- A lapse during the grace period would be exposed to its paid-to-date at the beginning of the grace period, not at the end of it. For example, if the annual premium for policy year 11 is not paid, lapse would be effective at the end of policy year 10 and would count as a policy year 10 lapse, even though the grace period extended 30 or 60 days beyond the anniversary.


### 18.1.2 Compromised and Denied Claims

A small but meaningful percentage of life insurance claims are settled by compromise or are denied, especially in the policy's first two years, when U.S. insurers have a right to contest misrepresentations made by the insured or applicant.

A denied claim means the contract was declared null and void. As such, it should not count as a death claim in a mortality study, nor should it contribute to exposure in any study.

A compromised claim can occur for a variety of reasons. Many times, it is less expensive for an insurance company to pay a reduced claim amount than to pay the legal fees necessary to successfully deny a claim, although such a practice invites more contested claims. In other cases, it may be unclear which side would prevail in a court of law, so a compromise can potentially save time and money and reduce uncertainty for both parties. A prudent approach would be to treat compromised claims as death claims, but for a reduced amount equal to the compromised claim amount, with a commensurate adjustment to exposure.

### 18.1.3 Study Variables Changing Over Time

Other than a few variables such as policy year and attained age, most of the variables contained in experience studies are expected to remain unchanged over time. When changes do occur, study results can be distorted. Here are two examples that show how administrative systems can distort lapse studies:

- Some administration systems will change a lapsed policy's plan code when nonforfeiture options such as extended term insurance (ETI) or reduced paid-up insurance (RPU) are exercised. The lapse would then be recorded under the ETI or RPU plan code, thereby understating lapses for the original plan.
- Some administration systems change the billing frequency and mode to monthly direct billing (i.e., cash or check) as a last-ditch effort to keep the policy in force if the premium has been overdue for a month or two. This would cause the preponderance of lapses to fall into the monthly direct bill category and understate lapses for other billing frequencies and modes.


### 18.1.4 Treatment of Reinsured Amounts

Some companies ignore reinsured amounts when performing individual life mortality studies. However, when more than a small percentage of its business is reinsured, a company may conduct an additional study using exposure amounts and death claim amounts net of reinsurance, to measure mortality for the business it retains. The company could also perform a study focused solely on reinsured amounts, although the results would typically be less credible than those for its retained business.

### 18.1.5 Use of Net Amount at Risk

Permanent products, such as whole life and universal life, typically build large reserves and cash values in later policy years. The net cost to the insurer at the time of death is equal to the net amount at risk, equal to the death benefit paid less the reserve released at death. Alternatively, the net amount at risk could be calculated as the death benefit less the cash value. A study with exposure amounts and death claim amounts based on net amounts at risk would more accurately reflect the net cost of death. However, the cost and difficulty of obtaining net amounts at risk may exceed the value of the extra refinement. In practice, net amounts at risk are rarely used for term insurance mortality studies but sometimes used for mortality studies of permanent products.

### 18.1.6 Inclusion of Substandard or Uninsurable Lives

Substandard lives, i.e., insureds with significantly higher than normal mortality levels for their age and gender, are typically excluded from mortality studies, as they would distort the resulting mortality rates. However, in an actual to expected study, substandard lives are often included by increasing their expected mortality commensurate with their underwriting classifications. For example, a life expected to have $100 \%$ extra mortality would have its expected mortality doubled.

In the U.S., joint and last survivor (J\&LS) insurance policies are purchased to offset estate taxes due at the second death of married couples. Sometimes, one of the two lives is uninsurable and the J\&LS policy is issued based on the expected mortality of just the insurable life. Mortality on such J\&LS policies is expected to be close to single life mortality and therefore must be studied separately from J $\& L$ policies where both lives were insurable.

### 18.1.7 Backdated New Business

It is not uncommon for new life insurance policies to be "backdated," that is, given an issue date requested by the applicant that is more than a few days in the past. This is most often done to secure a lower issue age with a lower premium. Since the policy can't lapse or have a death claim before it was applied for, it could make sense to calculate exposure starting at the later of the issue date and the date the policy became in force. In practice, such a refinement is rarely made, for two reasons:

- The practice of backdating reduces deaths claims in the first policy year. This is often viewed as a fair trade-off for the lower premium. Counting exposure from the issue date captures the appropriate reduction in the first-year mortality rate.
- The actual date the policy became in force is not usually available. However, the in-force date can often be estimated based on when it first appeared on an extract for valuation, experience studies or other purposes.


### 18.2 Group Life Insurance

Group mortality is studied annually by most group insurers and less frequently across the group life industry. Group life studies commonly use 5 -year age groupings such as attained ages $15-19,20-24,25-29$, etc. The resulting mortality rates are then assumed to apply to the central age of each 5 -year age grouping, such as attained ages 17 , $22,27,32$, etc.

Group mortality studies must adjust to the data available. While seriatim data is available to many insurers for smaller size groups, the largest groups tend to be self-administered and supply only summary data. As a result, group life studies use a combination of individually-calculated exposure, where seriatim data is available, and approximate exposure, where only summary information is available. The approximations would typically assume a uniform distribution of birthdays for each 5-year age grouping, with deaths occurring on average at the middle of each monthly, quarterly or annual reporting period.

Group insurers typically study mortality split by industry groupings, gender, central age, size of group, benefit as a percentage of salary and other, often proprietary, variables. The 2006 Group Life Study performed by the Society of Actuaries studied group mortality for 85 different industry groupings and by gender, central age and nine different group sizes, ranging from 2 to 9 lives up to 5,000 or more lives. Additionally, two different types of waiver of premium benefits were studied (lifetime benefits and benefits terminating at age 65) and two different types of accidental death and dismemberment (AD\&D) benefits were studied (basic and optional/supplemental).

Group studies often include partial years at the beginning and end of the study period: Lives are exposed from the beginning of the study period to the first birthday in the study or from the last birthday in the study to the end of the study period, with all deaths after the last birthday receiving a full year of exposure.

### 18.3 Morbidity Products

Experience studies for two morbidity products - disability income and long-term care - have many things in common that are presented in this section. Aspects that differ are presented in sections that follow for Disability Income (DI) and Long-Term Care (LTC), respectively.

DI and LTC benefits have several characteristics in common:

- Claims for both products are rarely a single payment. Instead, claims typically involve a series of payments that can last for months or years.
- Claims are typically paid monthly.
- Benefits are usually subject to an elimination period: The claim must continue for a specified number of days or months before benefits will commence. Claims that don't exceed the elimination period are "eliminated." The consumer typically has a choice of elimination periods, sometimes ranging from zero up to a full year. Premiums are higher for shorter elimination periods.
- Claims are typically limited in some fashion, such as by a maximum age (DI only), a maximum number of payments, a maximum total benefit or some combination of these.
- Both products pay claims only when the insured meets certain conditions, such as being disabled or requiring long-term care services.
- When the insured recovers, benefits stop but can restart if the insured again becomes disabled or requires longterm care services.
- Both products can pay benefits that vary according to the insured's situation:
- Many disability products pay a reduced benefit for partial disability to encourage a gradual return to work.
- Most LTC products pay a benefit that reimburses for eligible costs up to a monthly maximum.

Both products can be offered directly to individuals or sold to groups of people, typically through employers. LTC is primarily sold to individuals.

When sold to individuals, these products are carefully underwritten to screen out imminent claims, whereas group products rely on an actively-at-work requirement to ensure a good share of healthy lives. Studies of individual business often have access to more information than the often-limited information employers are willing and able to share about their employees. In spite of these and other differences, morbidity studies for group and individual business are very similar. The main differences lie in the variables studied. For example, a group study would focus on the insured's current age while an individual study might instead use issue age and policy year. Group studies would typically use calendar year for the rate year while individual studies would use policy year.

These products share the following three categories of morbidity studies:

- Studies of claim incidence rates, the probabilities of claim.
- Studies of claim severity, such as the average claim's length and/or cost.
- Studies of claim termination rates, the likelihood of claims stopping due to recovery or death.


### 18.3.1 Claim Incidence Studies

Claim incidence studies most often study all claims, combining partial and full disabilities or combining home health care, assisted living and nursing home care. An "all claims" study involves one decrement under study with adjustments to exposure for other decrements, such as lapse, death, or termination of employment.

Alternatively, different categories of claims could be separately studied. An "all claims" rate could be used as the composite independent rate under study, with each category of claims becoming a component dependent rate. Only one exposure calculation would be needed to calculate all the component dependent rates.

Amount-weighted results use the actual claim amounts for the event under study, with exposures based on each life's maximum monthly benefit.

For long-term disability insurance that continues after recovery, multiple claims can arise on a single policy. To account for claims arising after recovery, the valuation method assumes that claims can arise on disabled lives. For consistency, the claim incidence study includes disabled lives and the occurrence of a claim does not result in a decrement of the population under study. Hence, the claim incidence study uses the claim frequency method outlined in section 15.1 and not the decrement study methods. For other types of disability or morbidity insurance which terminate when the claim terminates, decrement study methods may be appropriate.

Claim incidence rates are most often annual frequencies or probabilities.

Exposure would typically use exact dates of entry and exit, when available. When employers report only the month and year for new hires and terminations, the $15^{\text {th }}$ day of each month might be used.

For claim frequencies studies, central exposure, based on the amount of time each life was able to claim during the rate interval, is typically used. For decrement studies, exposure is often calculated using the annual exposure method, where the event under study is exposed for the full rate interval. Some recent studies have begun to use daily exposure, where all decrements are exposed to their date of decrement, exposure is calculated in days, and the claim incidence rate is a daily rate. Daily rates facilitate calculations involving differing numbers of days.

### 18.3.2 Claim Severity Studies

The average length or average cost of a claim is crucial to the calculation of total cost of claims. The average length of claim would typically be calculated as total months of claims paid divided by number of claims. Average cost per
claim would be simply total claims paid divided by number of claims. Recurring claims such as those for DI and LTC make for more complex projections, especially when accurate cash flows are desired.

### 18.3.3 Claim Termination Studies

Separate termination studies are performed for recovery and death. Cessation of benefits due to reaching a maximum age, a maximum number of payments or a maximum total benefit are reflected in the calculation of exposure but not counted as claim terminations.

A disability claim will terminate when proof of ongoing disability is not received. Similarly, an LTC claim will terminate when no more requests for reimbursement of LTC costs are received. When communication with the insured or her care givers ceases, it is difficult to determine whether the insured recovered or died. As a result, while the total termination rate is accurate, the component recovery and death rates are subject to distortion. The efforts made by insurance companies to distinguish recoveries from deaths vary widely; none are totally effective.

Termination rates are typically based on a single exposure in which every claiming life is exposed while it is receiving benefits. Since exposure is based on total terminations, total terminations divided by exposure produces an independent rate, the probability of termination. Since this same exposure is used to calculate both recovery and death rates, the recovery rate and the death rate are component dependent rates of the composite independent rate (i.e., the probability of termination). Using approximations presented earlier, independent probability rates for recovery and death can be calculated from their dependent rates.

As with Claim Incidence Studies, Claim Termination Studies often use exact entry and exit dates, when available, with either annual or daily exposure. Claim terminations are studied from the date of disablement or loss date, with exposure calculated from the end of the elimination period. Claim termination rates are higher and more rapidly changing for newer claims. As a result, claim termination rates are calculated monthly for the first few years following a claim, up to as many as six years following the claim's commencement. Once termination rates start to stabilize, they switch from monthly to annual rates, typically varying by claim year until the tenth year and by attained age thereafter.

Claim termination rates also vary by age and remaining benefit period at claim commencement.

### 18.4 Disability Income

Most aspects of disability income experience study calculations are discussed above, as part of Morbidity Products. This section will discuss DI aspects that are not shared with long-term care.

The elimination period, also known as the waiting period, is an important aspect of disability income products. If the insured does not remain disabled longer than the elimination period, then no disability benefits are payable.

Benefits for short-duration disabilities are eliminated, thereby reducing the consumer cost of the product while providing benefits where they are needed the most: for longer-duration disabilities.

### 18.4.1 Elimination Periods

Disability income products are often available with a choice of elimination periods such as 3, 6, 9 or 12 months. Individual Overhead Expense products have shorter elimination periods, as low as one month. Individual Disability Buy-Out products may have a 24 -month elimination period.

Group DI products are segmented between short-term disability (STD) and long-term disability (LTD), with STD typically providing benefits only during the first 6 months of disability and LTD providing benefits thereafter. STD elimination periods would usually be between zero and three months while LTD would have a 6-month elimination
period. Another difference is that STD benefits are usually paid when the insured is disabled from her own occupation. LTD benefits typically use an "own occupation" definition through the first 24 months of disability and then switch to a more restrictive "any occupation" definition.

The elimination period for group waiver of premium disability benefits has traditionally been nine months, but six months is becoming more prevalent.

Many insureds wait until the end of the elimination period or beyond, before submitting a disability claim. There is no penalty for late claim submission, although a statute of limitations may come into play if the claim is submitted many years after the fact.

### 18.4.2 Partial Disability Benefits

More recently-issued DI products provide a partial DI benefit as an incentive for a part-time return to work. The percentage reduction in the DI benefit is usually equal to the ratio of part-time to full-time income. For example, if part-time income is $40 \%$ of full-time income, then the DI benefit would be reduced by $40 \%$ such that the partial benefit would equal $60 \%$ of the full benefit.

While partial benefits due to a part-time return to work are tracked, it is uncommon for partial disability rates to be calculated. Instead, the reduced benefits would be reflected in the total dollar amount of benefits paid and would reduce the average cost per claim.

### 18.4.3 Recovery Followed by Relapse

Sometimes a recovery from disability is followed by a relapse. When a relapse occurs within six months of the recovery, the relapse is typically treated as a continuation of the prior disability claim. This allows the insured to restart disability benefits without having to satisfy another elimination period.

Experience studies also give special treatment for a relapse that occurs within six months of a recovery:

- The recovery and relapse cancel each other out: The recovery is not counted as a claim termination, the relapse is not counted as an additional claim incidence, and exposure is calculated as if the recovery never happened.
- The reduction in disability benefits during the brief recovery would be reflected in the total dollar amount of benefits paid and would reduce the average cost per claim.


### 18.4.4 Claim Settlements

Occasionally, disability claims are eliminated by claim settlements which pay the policy owner a lump sum, in lieu of future monthly claim payments. There are two types of claim settlements:

- An administrative settlement, initiated when the insurer recognizes that a disability claimant is not likely to recover, to save administrative time and effort.
- A litigated settlement, when there is a dispute between the claimant and the insurer.

For claim termination study purposes, such claim settlements are not counted as terminations of disability. The rationale is that the timing of the settlement is not an accurate reflection of when the claim would have terminated, so counting it as a termination would distort results.

The exposure contributed to a claim termination study by claim settlements depends on the type of settlement:

- An administrative settlement would be exposed to the end of the benefit period, since recovery was not expected to occur.
- A litigated settlement would not contribute to exposure after the settlement date, since the claim cannot terminate once settled, whereas it could have terminated had it not settled.


### 18.4.5 Other DI Considerations

Individual DI insurers typically conduct their DI studies using seriatim policy information with exact dates for exposure calculations. Group DI insurers are at the mercy of the information provided to them by employers, which is rarely as detailed as that for Individual DI studies. However, group insurers are often able to study results not only by sex and age group but also by such variables as size of group, industry, region, taxability of benefits, salary group and DI benefits as a percentage of salary.

To limit distortions caused by unreported deaths, which are hard to distinguish from recoveries followed by immediate lapse, some individual DI insurers impute deaths using a published mortality table and then subtract imputed deaths from total terminations to arrive at estimated recoveries.

Because of U.S. anti-discrimination laws, male and females cannot be charged different rates for the same employer-provided benefits. Therefore, U.S. group insurers use a blend of male and female rates for premium rates while individual insurers charge sex-distinct rates. However, separate rates for males and females are always used for valuation of liabilities.

Disability income results are often compared to industry tables. To enable such comparisons, the results of a company's experience study need to match up with the structure of rates from industry tables. For example, individual DI business now uses the 2013 Individual DI Valuation Table, which has monthly termination rates for 60 months and annual rates thereafter. This table will be mandatory for valuation starting in 2020. The 1985 CIDA Table, which preceded the 2013 table, had 13 weeks of termination rates, followed by 21 months of termination rates and annual rates thereafter.

As of 2016, Group DI business was using the 2008 Long-Term Disability Experience Study as a basis for comparison, with a new table in the works.

### 18.5 Long-Term Care

Most aspects of long-term care experience study calculations are discussed above, as part of Morbidity Products. This section will discuss LTC aspects that are not shared with disability income.

While most LTC insurance is written as individual policies, some group LTC has been written. This section focuses on individual LTC business.

Long-term care policies issued over the last 20 or more years generally reimburse the policyholder for eligible longterm care costs, subject to a maximum daily benefit. Most LTC policies also specify a maximum total benefit, often in terms of the maximum daily benefit payable for a specified number of days. When actual daily benefits are less than the maximum daily benefit, the duration of benefits is typically extended until the maximum total benefit is reached.

### 18.5.1 Elimination Period

Typical elimination periods for LTC products are 30, 60, 90, 180 and 365 days. Some LTC products offer a "split" elimination period: For example, there may be a 90-day elimination period for claims for a nursing home or assisted living facility but a zero-day elimination period for home care. To encourage home care, some products credit the days of home care towards the facility elimination period.

### 18.5.2 Inflation Protection

The purchaser of a long-term care policy must consider how much the cost of long-term care will increase between purchase of the policy and possible receipt of benefits. One strategy is to buy a larger benefit amount in order to cover increasing LTC costs far into the future. Another strategy is to purchase a policy with built-in inflation protection, usually based on the Consumer Price Index or a flat annual increase, such as 5\%. Both strategies result in an increased premium. Inflation protection can add as much as $50 \%$ to the premium.

### 18.5.3 Benefit Utilization Rate

Long-term care experience studies typically produce the rates already discussed in the Morbidity Products section, plus one additional rate: The benefit utilization rate is calculated for those on claim as the ratio of actual benefits to maximum benefits over the study period, with the maximum appropriately adjusted for any inflation-protection coverage.

### 18.5.4 Other LTC Considerations

The mortality rates experienced for LTC claim terminations do not follow any established mortality table. Mortality rates tend to be very high in the months following an LTC claim after which they drop to a much lower level and then increase with advancing age.

Seriatim policy data is used to calculate exposure. These data would include issue date, issue age, benefit information (elimination period, benefit period, inflation benefit, maximum monthly benefit and maximum total benefit), termination type and termination effective date. Additionally, a history of premiums and benefits for each policy would be valuable, as inflation protection can increase LTC benefits from year to year and insurers can raise premiums from time to time, when actual experience deviates adversely from that anticipated when the product was priced.

Ideally, claim data is organized by claim, with claim start and stop dates, claim diagnosis, type of claim (home health care, assisted living facility or nursing home) and total paid. Sometimes all that is available is a history of claim payments. This can be difficult to work with, especially when retroactive claim payments show only the claim payment date. Claim diagnosis is very important, as the average length of claim varies dramatically by diagnosis, with claims attributable to mental disease or defect lasting longer than those attributable to physiological diseases or injuries.

Sometimes claims data consists of a series of claim payments that must be organized into claims. If the payments don't include the incurral dates of the expenses being reimbursed, it may not be possible to tell when the claim was incurred; this problem is compounded when new claims retroactively pay many months of benefits.

### 18.6 Deferred Annuities

Deferred annuities are individual contracts most often purchased with retirement income in mind. There are three main types of deferred annuities:

- Fixed: Typically credits interest to a single fund or account value.
- Indexed: A fixed annuity whose account value accumulates according to a formula linked to a financial index such as the S\&P 500.
- $\quad$ Variable: An annuity that allows the owner to invest in multiple funds, including a fixed fund, mutual funds or exchange-traded funds.

Deferred annuities typically offer the following benefits:

- A surrender value,
- partial withdrawals and
- an option to annuitize, that is, to convert the account value to a periodic payment stream.

Fixed annuities guarantee that funds will accumulate at no less than a minimum interest rate. Variable annuities guarantee a minimum interest rate only on fixed funds. There are no such guarantees on variable funds, which leave the primary investment risk with the variable annuity's owner.

The following decrements are studied for almost all deferred annuities:

- Full surrender,
- death and
- annuitization, which is generally all or nothing.


### 18.6.1 Deferred Annuity Utilization Rates

Utilization rates of additional benefits are also studied. Over the last three decades, there has been a steady evolution in additional benefits provided by some, but not all, deferred annuities. These include:

- Guaranteed Minimum Death Benefits (GMDBs),
- Guaranteed Minimum Accumulation Benefits (GMABs),
- Guaranteed Minimum Income Benefits (GMIBs) and
- Guaranteed Lifetime Withdrawal Benefits (GLWBs).

GMDBs provide a guaranteed minimum amount payable on the death of the annuitant. Their cost can be studied by comparing actual death benefits paid to those that would have been paid (the surrender value) in the absence of a GMDB.

GMABs provide a guaranteed minimum amount to be annuitized or paid on surrender. Their cost can be studied by comparing actual amounts annuitized or paid to those that would have been annuitized or paid in the absence of a GMAB. GMABs do not guarantee annuitization rates. There is no election of GMABs: The GMAB benefit is simply based on the annuity remaining in force.

GMIBs provide a guaranteed minimum amount to be applied to annuitization. They are a combination of accumulation and annuitization rate guarantees. The cost of GMIBs can be studied by comparing actual annuity benefits to those that would have been paid in the absence of a GMIB. Such a study would require the company to calculate and store the latter figure for each annuitization. GMIB utilization rates often vary by issue age and contract year and then by attained age starting around age 60 or 65 .

GLWBs provide a guaranteed lifetime withdrawal income equal to the contract's Maximum Allowable Annual Withdrawal (MAAW). When more than the MAAW is withdrawn in any contract year, the amount of future guaranteed income is adjusted downward, resulting in a new, lower MAAW.

For many deferred annuities, it is important to capture two amounts for each contract year:

1. The Maximum Allowable Annual Withdrawal (MAAW), which is the maximum amount that can be withdrawn during the contract year without reducing guaranteed benefits such as GMAB, GMIB and GLWB. For some simpler, pre-2000 products, this could instead be the maximum penalty-free withdrawal for the contract year.
2. Actual Annual Withdrawal (AAW) is the sum of all withdrawals made during the contract year.

Partial withdrawals can then be studied as the ratio between AAW and MAAW. These ratios would be expected to vary by issue age and contract year and then by attained age. It may be advisable to summarize the results separately between contracts with ratios over $100 \%$ and those with ratios of $100 \%$ or less.

An alternate base for measuring partial withdrawal activity is Adjusted Initial Premium, which is equal to the contract's initial premium reduced by its cumulative withdrawals in excess of cumulative MAAW.

Industry studies of deferred annuities have concentrated on GLWB utilization rates in recent years. Not surprisingly, these rates typically vary by attained age and whether the contract is qualified or non-qualified for tax purposes. Please refer to Chapter 15 for a more detailed explanation of utilization rate studies.

### 18.6.2 Contract Year Data Challenges

For many deferred annuity studies, data is not available by contract year. Instead, premium payments and withdrawals are typically available only by calendar month. Similarly, account balances may be available only as of the end of each calendar month. A common response to this data challenge is to use 13 -month averages, with weights of $1 / 24$ for the beginning and ending months, which contain two consecutive contract anniversaries, and weights of $1 / 12$ for the eleven months in between. When significant premium payments or withdrawals are made close to the anniversary, the 13-month average effectively splits them between two consecutive contract years, both limiting and ensuring some degree of inaccuracy.

### 18.7 Payout Annuities

Payout annuities include both immediate annuities and structured settlements.

Immediate annuities often attract buyers who are healthier than average: By purchasing a payout annuity, many are betting that they will live longer than average. On the other hand, someone who chooses a life annuity with a 10year certain period may suspect that their health is only average. These illustrate two dimensions that are often studied for payout annuities: the effects of self-selection and the choice of immediate annuity product.

Self-selection is commonly studied by examining mortality rates by issue age and policy year. Comparing mortality levels between different products requires a neutral method of weighting the results such that differences in distributions by age and gender do not bias the results.

As with life insurance products, larger amounts are often associated with lower mortality. In the case of immediate annuities, the best amount to study is the monthly income amount. Studying mortality by the amount of reserves is distorted as reserves decline over time.

For immediate annuities, overestimating mortality levels, whether initially or due to future mortality improvements, is one of the two major risks, the other being actual vs. expected investment returns. Immediate annuity studies are needed to quantify historical mortality improvement. This can prove difficult because so many variables need to stay constant in order to develop accurate comparisons. For example, how immediate annuities are sold or bought and what competing options are available can change over time and thereby change the average mortality level of new buyers.

Structured settlements often arise from injury lawsuits. Their terms are sometimes decreed by a court of law but are more often the result of negotiated settlements. Typically, the structure of the payments is not a single monthly amount payable for life. Instead, there may be one or more lump sums and some payments that increase over time, with a goal of providing for the injured person or, in some cases, the surviving dependents of the plaintiff.

Mortality levels for structured settlements would normally be higher than those for immediate annuities. The most severely injured payees would be expected to live shorter lives and may thus qualify for substandard underwriting, which would provide greater annuity benefits for the same amount of premium.

When studying mortality by the amount of a structured settlement, reserves are not a perfect choice for the amount but are often a better choice than a monthly income amount that varies. The premium paid to purchase the structured settlement might be a better choice of amount, but most companies don't store the premium in their administration system.

### 18.8 Retirement Pensions

Pension plan studies involve active, disabled and retired employees as well as beneficiaries of joint and survivor payout schemes. Each of these groups is included in various experience studies:

- Mortality studies are conducted for active employees. Results are often analyzed by gender, age, salary, and type of employment, such as office workers vs. others. These studies must deal with new hires and employee terminations.
- Mortality studies are conducted for disabled employees. Results are often analyzed by gender, age and years since disability.
- Mortality studies are conducted for retired employees and for beneficiaries who receive monthly payments after a retiree's death. Results are often analyzed by gender, age, annual benefit and type of employment. New retirees add to the retiree group. Beneficiaries are only studied from the time they began to receive monthly payments. Death is the only decrement for both retirees and beneficiaries.
- Mortality trends are studied by gender, age and year of birth and are used to create mortality projection factors. These factors are used to estimate future mortality levels, as pension plans must take into account the financial effect of future mortality improvements.

An example of an industry retirement pension study is the RP (for Retirement Pensions) 2014 mortality table. The RP 2014 committee studied mortality by age and years since retirement. While they found that more-recent retirees of the same age experienced slightly lower mortality rates, the differences were too small to justify the complexity of adding another dimension to the mortality table.

The RP 2014 mortality study was one of the first major U.S. studies to examine the use of daily exposure. In the end, the committee decided to use annual exposure for consistency with prior studies.

Two years before the RP 2014 mortality table was finalized, the committee released a mortality projection table referred to as "Scale BB." It was released early because its predecessor, Scale AA, released in conjunction with the RP 2000 table, was no longer a good fit.

The RP 2014 committee also developed the MP-2014 mortality projection table. It was based on the Social Security Administration's historical mortality rates, which were developed from data provided by the Centers for Disease Control and Prevention (CDC) and Medicare. It was one of the first U.S. mortality projection scales to vary improvement rates by both age and year. This allowed the table to reflect actual mortality improvement experienced from 2006, the mid-point of the experience data, to 2014 and enabled the projection of cohort effects beyond 2014.

### 18.9 Credit Life and Disability

### 18.9.1 Credit Life Insurance

Credit life insurance is sold by organizations that originate consumer loans, such as automobile dealers, banks, credit unions, finance companies and retail companies. The amount of insurance is structured to match the loan balance using level term for short term loans and balloon type loans and monthly decreasing term to cover longer term amortizing loans.

The most recent U.S. credit life mortality study was performed by the SOA's Credit Insurance Experience Committee in 2009, based on data from calendar years 2003 to 2006 . The study included companies that collectively accounted for over $70 \%$ of credit life premiums with 53,906 death claims that amounted to over half a billion dollars.

In some respects, the study was quite simple, with results by number of claims and by amount of claims for only two variables:

- $\quad$ Experience was summarized by five-year age groups, with central ages running from 22 to 72 . For each central age, claims, exposure, and mortality rate were calculated and results were compared to the 2001 CSO Male Composite Ultimate table. Overall mortality was less than 64\% of 2001 CSO Male mortality by both count and amount.
- Mortality rates were calculated by contributing company and central age.

On the other hand, the study involved two technical aspects that were interesting and unusual:

1. Many companies had exposure with skewed age distributions that defied reasonability. Some of the distortion was caused by business with unknown age that was assigned to a default age, such as 47 . The excess business at the default age was redistributed proportionately. Other skewness, such as saw tooth patterns by age, was smoothed using graduation. In both cases, care was taken to ensure total exposure was unchanged.
2. Because of the monthly changes in decreasing term amounts, all exposure calculations were performed at the calendar month level as follows:

a. Business in force for the full calendar month was exposed for the average of the amounts in force at the beginning and end of the month.

b. Business issued during the month was exposed for half a month.

c. All terminations, including deaths, were exposed for half a month in the month of termination.

d. Each half-month of exposure was considered to be $1 / 24^{\text {th }}$ of an annual exposure.

Exposure for deaths was understated because it did not include the period from the middle of the month of death to the end of the policy year of death, resulting in an average understatement of half a year for each death. To compensate, the following adjustment was made to the calculation of expected claims, in order to true-up actual to expected ratios:

Expected Claims $=($ Exposure + Actual Claims $/ 2) *$ Expected Mortality Rate.

### 18.9.2 Credit Disability Income

Credit disability income is often sold in combination with credit life insurance. Unlike credit life, which pays a lump sum when the insured dies, credit DI pays a monthly benefit that is generally designed to pay off the debt if disability continues to the end of the benefit period. Credit DI is sold for benefit periods ranging from 6 months to 10 years.

The credit DI studies published in 2004 and 2014 used a creative approach to demonstrate the suitability of the 1985 CIDA (Commissioners Individual Disability Table A) table as a valuation standard for single premium credit DI active life reserves. The challenge was the complexity of the 1985 CIDA table, with its dimensions of age, sex, elimination period and occupation class, for both incidence rates and termination rates, which would have to be applied to 13 different benefit periods.

The solution was to simplify by working from both ends to the middle:

- Industry average ages and average benefit periods were determined for each of the five elimination or retroactive periods available for credit DI, reducing over 700 possible combinations to just five average combinations.
- Weighted average CIDA rates were developed for a blend of four occupation classes for males and females, combining 8 sets of CIDA tables into one blended set of CIDA tables, with the resulting rates varying primarily by age and term of coverage. The Credit DI valuation standard used only the 7-day and 14-day elimination periods and $112 \%$ of CIDA incidence rates. The blending process was not only efficient but also necessary, as few credit insurers collected gender data and none collected occupation data.

Expected claim costs for the five elimination periods were then calculated using the blended CIDA tables for the 7day and 14-day elimination periods specified as part of the valuation standard. The result was that actual industry claim costs were about $50 \%$ lower than expected claim costs based on the valuation standard: The 1985 CIDA tables were far more than adequate; the only concern was with the considerable amount of redundancy.

## 19 Standard Method Error Derivation

Readers focused on fundamentals should skip or skim Chapters 19 and 20 and may want to review the Glossary that follows Chapter 20.

Chapter 9 gave a summary development of the errors arising under each exposure method for half-year periods. This chapter develops general error formulas for starting and ending partial years and for fractional periods. This may be useful for estimating error terms to a higher order.

The following table summarizes the error formulas developed in this chapter.

| Error | Annual Method | Fractional Method | Distributed Method |
| :---: | :---: | :---: | :---: |
| ${ }_{\mathrm{s}} e_{x}$ | $1 / 2(1-s)\left(\Delta_{x}+q_{x}\right) q_{x}$ | $1 / 2(1-s) \Delta_{x} q_{x}$ | $=1 / 2(1-s)\left(\Delta_{x}-q_{x}\right) q_{x}$ |
| ${ }_{1-\mathrm{s}} e_{x+s}$ | $-1 / 2 \mathrm{~s}\left(\Delta_{x}+q_{x}\right) q_{x}$ | $-1 / 2 \mathrm{~s} \Delta_{x} q_{x}$ | $-1 / 2 \mathrm{~s}\left(\Delta_{x}-q_{x}\right) q_{x}$ |
| ${ }_{f} e_{x+f t}$ | $(1 / 2(1-f)-f t)\left(\Delta_{x}+q_{x}\right) q_{x}$ | $(1 / 2(1-f)-f t) \Delta_{x} q_{x}$ | $(1 / 2(1-f)-f t)\left(\Delta_{x}-q_{x}\right) q_{x}$ |

### 19.1 Errors from Fractional Exposure Method

The fractional method is the simplest method with which to start investigating the errors arising from partial year exposure. Throughout this chapter, we will assume a linearly increasing force of decrement.

### 19.1.1 Error for Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$

The average force for the partial year from age $x$ to $x+s$ is given by:

$$
{ }_{s} \bar{\mu}_{x}=s\left(\bar{\mu}_{x}-1 / 2(1-s) \Delta \mu_{x}\right) .
$$

The resulting partial year rate is

$$
{ }_{\mathrm{s}} q_{x}=1-e^{-\mathrm{s}\left(\bar{\mu}_{x}-1 / 2(1-s) \Delta \mu_{x}\right)}
$$

The annualized partial year rate is

$$
\begin{aligned}
{ }_{\mathrm{s}} q_{x}^{A} & =1-\left(1-{ }_{\mathrm{s}} q_{x}\right)^{1 / s} \\
& =1-\left(e^{-\mathrm{s}\left(\bar{\mu}_{x}-1 / 2(1-s) \Delta \mu_{x}\right)}\right)^{1 / s} \\
& =1-e^{-\bar{\mu}_{x}+1 / 2(1-s) \Delta \mu_{x}} \\
& =1-\left(1-q_{x}\right) e^{+1 / 2(1-s) \Delta \mu_{x}}
\end{aligned}
$$

Therefore, the difference, or error, between the true annual rate and the annualized half-year rate is

$$
\begin{aligned}
{ }_{\mathrm{s}} e_{x}^{F M} & =q_{x}-{ }_{\mathrm{s}} q_{x}^{A} \\
& =q_{x}-\left(1-\left(1-q_{x}\right) e^{+1 / 2(1-s) \Delta \mu_{x}}\right) \\
& =\left(1-q_{x}\right)\left(e^{+1 / 2(1-s) \Delta \mu_{x}}-1\right) \\
& \approx\left(1-q_{x}\right)\left(+1 / 2(1-s) \Delta \mu_{x}\right) .
\end{aligned}
$$

A more useful error estimate is

$$
\begin{aligned}
{ }_{\mathrm{s}} e_{x}^{F M} & =\left(1-q_{x}\right)\left(1 / 2(1-s) \Delta \mu_{x} / \bar{\mu}_{x}\right) \bar{\mu}_{x} \\
& =-\left(1-q_{x}\right)\left(1 / 2(1-s) \Delta_{x}\right) \log _{e}\left(1-q_{x}\right) \\
& \approx\left(1-q_{x}\right)\left(1 / 2(1-s) \Delta_{x}\right) q_{x} .
\end{aligned}
$$

To the first order of $q_{x}$, the error estimate is

$$
{ }_{\mathrm{s}} e_{x}^{F M} \approx 1 / 2(1-s) \Delta_{x} q_{x}
$$

The percentage error for the half-year rate is therefore

$$
{ }_{\mathrm{s}} \varepsilon_{x}^{F M} \approx 1 / 2(1-s) \Delta_{x}
$$

### 19.1.2 Error for Partial Year Running from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$

For the partial year running from age $x+s$ to age $x+1$, the average force is:

$$
{ }_{1-s} \bar{\mu}_{x+s}=(1-s)\left(\bar{\mu}_{x}+1 / 2 s \Delta \mu_{x}\right) .
$$

The resulting partial year rate is

$$
{ }_{1-s} q_{x+s}=1-e^{-(1-s)\left(\bar{\mu}_{x}+1 / 2 s \Delta \mu_{x}\right)}
$$

The annualized partial year rate is

$$
\begin{aligned}
& { }_{1-s} q_{x+s}^{A}=1-\left(1-{ }_{1-s} q_{x+s}\right)^{1 /(1-s)} \\
& \quad=1-\left(e^{-(1-s)\left(\bar{\mu}_{x}+1 / 2 s \Delta \mu_{x}\right)}\right)^{1 /(1-s)} \\
& \quad=1-e^{-\bar{\mu}_{x}-1 / 2 s \Delta \mu_{x}} \\
& \quad=1-\left(1-q_{x}\right) e^{-1 / 2 s \Delta \mu_{x}}
\end{aligned}
$$

Therefore, the difference, or error, between the true annual rate and the annualized half-year rate is

$$
\begin{aligned}
{ }_{1-s} e_{x+s}^{F M} & =q_{x}-{ }_{1-s} q_{x+s}^{A} \\
& =q_{x}-\left(1-\left(1-q_{x}\right) e^{-1 / 2 s \Delta \mu_{x}}\right) \\
& =\left(1-q_{x}\right)\left(e^{-1 / 2 s \Delta \mu_{x}}-1\right) \\
& \approx\left(1-q_{x}\right)\left(-1 / 2 s \Delta \mu_{x}\right) .
\end{aligned}
$$

A more useful error estimate is

$$
\begin{aligned}
{ }_{1-s} e_{x+s}^{F M} & =\left(1-q_{x}\right)\left(-1 / 2 \mathrm{~s} \Delta \mu_{x} / \bar{\mu}_{x}\right) \bar{\mu}_{x} \\
& =-\left(1-q_{x}\right)\left(-1 / 2 \mathrm{~s} \Delta_{x}\right) \log _{e}\left(1-q_{x}\right) \\
& \approx\left(1-q_{x}\right)\left(-1 / 2 \mathrm{~s} \Delta_{x}\right) q_{x}
\end{aligned}
$$

To the first order of $q_{x}$, the error estimate is

$$
{ }_{1-\mathrm{s}} e_{x+s}^{F M} \approx-1 / 2 \mathrm{~s} \Delta_{x} q_{x}
$$

The percentage error for the half-year rate is therefore

$$
{ }_{1-s} \varepsilon_{x+s}^{F M} \approx-1 / 2 \mathrm{~s} \Delta_{x}
$$

### 19.1.3 Error for Fractional Period

For fractional rates, the average force for the partial year from age $x+f t$ to $x+f(t+1)$ is given by:

$$
{ }_{f} \bar{\mu}_{x+f t}=f\left(\bar{\mu}_{x}-(1 / 2(1-f)-f t) \Delta \mu_{x}\right) .
$$

The resulting rate for the fractional period is

$$
{ }_{f} q_{x+f t}=1-e^{-f\left(\bar{\mu}_{x}-(1 / 2(1-f)-f t) \Delta \mu_{x}\right)}
$$

The annualized partial year rate is

$$
\begin{aligned}
& { }_{f} q_{x+f t}^{A}=1-\left(1-{ }_{f} q_{x+f t}\right)^{1 / f} \\
& \quad=1-\left(e^{-f\left(\bar{\mu}_{x}-\left(\frac{1}{2}(1-f)-f t\right) \Delta \mu_{x}\right)}\right)^{1 / f} \\
& \quad=1-e^{-\bar{\mu}_{x}+(1 / 2(1-f)-f t) \Delta \mu_{x}} \\
& \quad=1-\left(1-q_{x}\right) e^{+(1 / 2(1-f)-f t) \Delta \mu_{x}}
\end{aligned}
$$

Therefore, the difference, or error, between the true annual rate and the annualized half-year rate is

$$
\begin{aligned}
& { }_{f} e_{x+f t}^{F M}=q_{x}-{ }_{f} q_{x+f t}^{A} \\
& \quad=q_{x}-\left(1-\left(1-q_{x}\right) e^{+\left(\frac{1}{2} /(1-f)-f t\right) \Delta \mu_{x}}\right) \\
& \quad=\left(1-q_{x}\right)\left(e^{+\left(\frac{1}{2}(1-f)-f t\right) \Delta \mu_{x}}-1\right) \\
& \quad \approx\left(1-q_{x}\right)(1 / 2(1-f)-f t) \Delta \mu_{x} .
\end{aligned}
$$

A more useful error estimate is

$$
\begin{aligned}
& { }_{f} e_{x+f t}^{F M}=\left(1-q_{x}\right)(1 / 2(1-f)-f t)\left(\Delta \mu_{x} / \bar{\mu}_{x}\right) \bar{\mu}_{x} \\
& \quad=-\left(1-q_{x}\right)(1 / 2(1-f)-f t) \Delta_{x} \log _{e}\left(1-q_{x}\right) \\
& \quad \approx\left(1-q_{x}\right)(1 / 2(1-f)-f t) \Delta_{x} q_{x} .
\end{aligned}
$$

To the first order of $q_{x}$, the error estimate is

$$
{ }_{f} e_{x+f t}^{F M} \approx(1 / 2(1-f)-f t) q_{x} \Delta_{x} .
$$

The percentage error for the half-year rate is therefore

$$
f_{x+f t}^{F M} \approx(1 / 2(1-f)-f t) \Delta_{x} .
$$

### 19.2 Errors for Annual Exposure Method

The simplest way to identify the error arising using the annual exposure method is to look at the difference between annual rates calculated using annual and fractional exposures. To distinguish between the exposures and rates for each method, the annual method using the Balducci Hypothesis will use a superscript of $B$.

### 19.2.1 Error for Partial Year Running from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$

The exposure for the partial year running from age $x+s$ to age $x+1$ is

$$
{ }_{1-s} E_{x+s}^{B}=(1-s)_{1-s} E_{x+s}
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{1-s} d_{\mathrm{x}+\mathrm{s}} /{ }_{1-s} E_{x+s}^{B}={ }_{1-s} d_{\mathrm{x}+\mathrm{s}} /\left((1-s)_{1-s} E_{x+s}\right),
$$

and therefore,

$$
{ }_{1-s} q_{x+s}^{B}={ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s) .
$$

The difference between the rates resulting from the fractional and annual exposure methods is examined below. The third formula substitutes for the exponent $1 /(1-s)$ using the binomial expansion to the second order.

$$
\begin{aligned}
& 1-\mathrm{s} \\
& q_{x+s}^{A}-{ }_{1-\mathrm{s}} q_{x+s}^{B} \\
&= 1-\left(1-{ }_{1-\mathrm{s}} q_{x+s}\right)^{1 /(1-s)}-{ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s) \\
& \approx 1-\left(1-{ }_{1-\mathrm{s}} q_{x+s} /(1-s)+1 / 2\left({ }_{1-\mathrm{s}} q_{x+s}\right)^{2} s /(1-s)^{2}\right)-{ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s) \\
&=-1 / 2 s\left({ }_{1-\mathrm{s}} q_{x+s} /(1-s)\right)^{2} .
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{aligned}
{ }_{1-s} q_{x+s} & =1-\left(1-{ }_{1-s} q_{x+s}^{A}\right)^{1-s} \\
& \approx(1-s)_{1-s} q_{x+s}^{A} .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
{ }_{1-\mathrm{s}} q_{x+s}^{A}-{ }_{1-\mathrm{s}} q_{x+s}^{B} & \approx-1 / 2 s\left({ }_{1-\mathrm{s}} q_{x+s}^{A}\right)^{2} \\
& \approx-1 / 2 s\left(q_{x}\left(1+1 / 2 s \Delta_{x}\right)\right)^{2} \\
& \approx-1 / 2 s\left(q_{x}\right)^{2}
\end{aligned}
$$

The error associated with the annual exposure method, for the partial year running from age $x+s$ to $x+1$, can now be approximated as follows:

$$
\begin{aligned}
{ }_{1-s} e_{x+s}^{A M} & =q_{x}-{ }_{1-s} q_{x+s}^{B} \\
& =q_{x}-{ }_{1-s} q_{x+s}^{A}+{ }_{1-s} q_{x+s}^{A}-{ }_{1-s} q_{x+s}^{B} \\
& \approx-1 / 2 s \Delta_{x} q_{x}-1 / 2 s\left(q_{x}\right)^{2} \\
& \approx-1 / 2 s\left(\Delta_{x}+q_{x}\right) q_{x} .
\end{aligned}
$$

### 19.2.2 Error for Partial Year Running from Age $\boldsymbol{x}$ to $\boldsymbol{x}+\boldsymbol{s}$

The exposure for the partial year running from age $x$ to age $x+s$ is

$$
{ }_{s} E_{x}^{B}=s_{s} E_{x}+(1-s){ }_{s} d_{x}
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{s} d_{\mathrm{x}} /{ }_{s} E_{x}^{B}={ }_{s} d_{\mathrm{x}} /\left(s_{s} E_{x}+(1-s){ }_{s} d_{x}\right),
$$

and therefore,

$$
\begin{aligned}
{ }_{s} q_{x}^{B} & =\left({ }_{s} q_{\mathrm{x}} / s\right) /\left(1+((1-s) / s){ }_{s} q_{x}\right) \\
& \approx\left({ }_{s} q_{\mathrm{x}} / s\right)\left(1-((1-s) / s){ }_{s} q_{x}\right) \\
& ={ }_{s} q_{\mathrm{x}} / s-(1-s)\left({ }_{s} q_{x} / s\right)^{2}
\end{aligned}
$$

The difference between the rates resulting from the fractional and annual exposure methods is examined below. The third formula substitutes for the exponent $1 /(1-s)$ using the binomial expansion to the second order.

$$
\begin{aligned}
& { }_{\mathrm{s}} q_{x}^{A}-{ }_{\mathrm{s}} q_{x}^{B} \\
= & 1-\left(1-{ }_{\mathrm{s}} q_{x}\right)^{1 / s}-{ }_{s} q_{\mathrm{x}} / s+(1-s)\left({ }_{\mathrm{s}} q_{x} / s\right)^{2} \\
\approx & 1-\left(1-{ }_{\mathrm{s}} q_{x} / s+1 / 2\left({ }_{\mathrm{s}} q_{x}\right)^{2}(1-s) / s^{2}\right)-{ }_{s} q_{\mathrm{x}} / s+(1-s)\left({ }_{\mathrm{s}} q_{x} / s\right)^{2} \\
= & 1 / 2(1-s)\left({ }_{\mathrm{s}} q_{x} / s\right)^{2}
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{gathered}
{ }_{\mathrm{s}} q_{x}=1-\left(1-{ }_{\mathrm{s}} q_{x}^{A}\right)^{s} \\
\approx s_{\mathrm{s}} q_{x}^{A} .
\end{gathered}
$$

Therefore,

$$
\begin{aligned}
{ }_{\mathrm{s}} q_{x}^{A}-{ }_{\mathrm{s}} q_{x}^{B} & \approx 1 / 2(1-s)\left({ }_{\mathrm{s}} q_{x}^{A}\right)^{2} \\
& \approx 1 / 2(1-s)\left(q_{x}\left(1-1 / 2(1-s) \Delta_{x}\right)\right)^{2} \\
& \approx 1 / 2(1-s)\left(q_{x}\right)^{2}
\end{aligned}
$$

The error associated with the annual exposure method, for the partial year running from age $x$ to $x+s$, can now be approximated as follows:

$$
\begin{aligned}
{ }_{s} e_{x}^{A M} & =q_{x}-{ }_{s} q_{x}^{B} \\
& =q_{x}-{ }_{s} q_{x}^{A}+{ }_{s} q_{x}^{A}-{ }_{s} q_{x}^{B} \\
& \approx 1 / 2(1-s) \Delta_{x} q_{x}+1 / 2(1-s)\left(q_{x}\right)^{2} \\
& =1 / 2(1-s)\left(\Delta_{x}+q_{x}\right) q_{x}
\end{aligned}
$$

### 19.2.3 Error for Fractional Period

The exposure for a fractional period is

$$
{ }_{f} E_{x+f t}^{B}=f_{f} E_{x+f t}+(1-f(t+1))_{f} d_{x+f t} .
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{f} d_{\mathrm{x}+\mathrm{ft}} /{ }_{f} E_{x+f t}^{B}={ }_{f} d_{\mathrm{x}+\mathrm{ft}} /\left(f_{f} E_{x+f t}+(1-f(t+1)){ }_{f} d_{x+f t}\right)
$$

and therefore,

$$
\begin{aligned}
{ }_{f} q_{x+f t}^{B} & =\left({ }_{f} q_{\mathrm{x}+f t} / f\right) /\left(1+((1-f(t+1)) / f)_{f} q_{x+f t}\right) \\
& \approx\left({ }_{f} q_{\mathrm{x}+f t} / f\right)\left(1-((1-f(t+1)) / f)_{f} q_{x+f t}\right) \\
& ={ }_{f} q_{\mathrm{x}+f t} / f-(1-f-f t)\left({ }_{\mathrm{f}} q_{x+f t} / f\right)^{2} .
\end{aligned}
$$

The difference between the rates resulting from the fractional and annual exposure methods is examined below. The third formula substitutes for the exponent $1 /(1-s)$ using the binomial expansion to the second order.

$$
\begin{aligned}
& q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{B} \\
= & 1-\left(1-{ }_{f} q_{x+f t}\right)^{1 / f}-{ }_{f} q_{\mathrm{x}+f t} / f+(1-f-f t)\left({ }_{f} q_{x+f t} / f\right)^{2} \\
\approx & 1-\left(1-{ }_{f} q_{x+f t} / f+1 / 2\left({ }_{f} q_{x+f t}\right)^{2}(1-f) / f^{2}\right)-{ }_{f} q_{\mathrm{x}+f t} / f+(1-f-f t)\left({ }_{f} q_{x+f t} / f\right)^{2} \\
= & (1 / 2(1-f)-f t)\left({ }_{\mathrm{f}} q_{x+f t} / f\right)^{2}
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{aligned}
{ }_{f} q_{x+f t}= & 1-\left(1-{ }_{f} q_{x+f t}^{A}\right)^{f} \\
& \approx f_{f} q_{x+f t}^{A} .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
{ }_{f} q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{B} & \approx(1 / 2(1-f)-f t)\left({ }_{f} q_{x+f t}^{A}\right)^{2} \\
& \approx(1 / 2(1-f)-f t)\left(q_{x}\left(1-(1 / 2(1-f)-f t) \Delta_{x}\right)\right)^{2} \\
& \approx(1 / 2(1-f)-f t)\left(q_{x}\right)^{2} .
\end{aligned}
$$

The error associated with the annual exposure method, for a fractional period, can now be approximated as follows:

$$
\begin{aligned}
{ }_{f} e_{x+f t}^{A M} & =q_{x}-{ }_{f} q_{x+f t}^{B} \\
& =q_{x}-{ }_{f} q_{x+f t}^{A}+{ }_{f} q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{B} \\
& \approx(1 / 2(1-f)-f t) \Delta_{x} q_{x}+(1 / 2(1-f)-f t)\left(q_{x}\right)^{2} \\
& =(1 / 2(1-f)-f t)\left(\Delta_{x}+q_{x}\right) q_{x} .
\end{aligned}
$$

If the relative change over the year is a decrease equal to the mortality rate, i.e., if $q_{x}=-\Delta_{x}$, which is the Balducci Hypothesis, the error is zero.

### 19.3 Errors from Distributed Exposure Method

The simplest way to identify the error arising using the distributed method is to look at the difference between annual rates calculated using distributed and fractional exposures. To distinguish between the exposures and rates for each method, the distributed method using the uniform distribution of deaths will use a superscript of $D$.

### 19.3.1 Error for Partial Year Running from Age $x$ to $x+s$

The exposure for the partial year running from age $x$ to age $x+s$ is

$$
{ }_{s} E_{x}^{D}=s_{s} E_{x} .
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{s} d_{\mathrm{x}} /{ }_{s} E_{x}^{D}={ }_{s} d_{\mathrm{x}} /\left(s_{s} E_{x}\right),
$$

and therefore,

$$
{ }_{s} q_{x}^{D}={ }_{s} q_{\mathrm{x}} / s
$$

The difference between the rates resulting from the fractional and distributed exposure methods is examined below. The third formula substitutes for the exponent $1 /(1-s)$ using the binomial expansion to the second order.

$$
\begin{aligned}
& { }_{\mathrm{s}} q_{x}^{A}-{ }_{\mathrm{s}} q_{x}^{D} \\
= & 1-\left(1-{ }_{\mathrm{s}} q_{x}\right)^{1 / s}-{ }_{s} q_{\mathrm{x}} / s \\
\approx & 1-\left(1-{ }_{\mathrm{s}} q_{x} / s+1 / 2\left({ }_{\mathrm{s}} q_{x}\right)^{2}(1-s) / s^{2}\right)-{ }_{s} q_{\mathrm{x}} / s \\
= & -1 / 2(1-s)\left({ }_{\mathrm{s}} q_{x} / s\right)^{2}
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{gathered}
{ }_{\mathrm{s}} q_{x}=1-\left(1-{ }_{\mathrm{s}} q_{x}^{A}\right)^{s} \\
\approx s_{\mathrm{s}} q_{x}^{A}
\end{gathered}
$$

Therefore,

$$
\begin{aligned}
{ }_{\mathrm{s}} q_{x}^{A}-{ }_{\mathrm{s}} q_{x}^{D} & \approx-1 / 2(1-s)\left({ }_{\mathrm{s}} q_{x}^{A}\right)^{2} \\
& \approx-1 / 2(1-s)\left(q_{x}\left(1-1 / 2(1-s) \Delta_{x}\right)\right)^{2} \\
& \approx-1 / 2(1-s)\left(q_{x}\right)^{2}
\end{aligned}
$$

The error associated with the distributed exposure method, for the partial year running from age $x$ to $x+s$, can now be approximated as follows:

$$
\begin{aligned}
{ }_{s} e_{x}^{D M}= & q_{x}-{ }_{s} q_{x}^{D} \\
& =q_{x}-{ }_{s} q_{x}^{A}+{ }_{s} q_{x}^{A}-{ }_{s} q_{x}^{D} \\
& \approx 1 / 2(1-s) \Delta_{x} q_{x}-1 / 2(1-s)\left(q_{x}\right)^{2} \\
& =1 / 2(1-s)\left(\Delta_{x}-q_{x}\right) q_{x}
\end{aligned}
$$

### 19.3.2 Error for Partial Year Running from Age $x+s$ to $x+1$

The exposure for the partial year running from age $x+s$ to age $x+1$ is

$$
{ }_{1-s} E_{x+s}^{D}=(1-s)_{1-s} E_{x+s}+(1-s)_{s} d_{x} \text {. }
$$

Eliminating the deaths from the prior partial period assuming a uniform distribution of deaths, we have:

$$
d_{x}={ }_{s} d_{x} / s={ }_{1-s} d_{x+s} /(1-s),
$$

and therefore,

$$
{ }_{1-s} E_{x+s}^{D} \approx(1-s)_{1-s} E_{x+s}+s_{1-s} d_{x+s}
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{1-s} d_{\mathrm{x}+\mathrm{s}} /{ }_{1-s} E_{x+s}^{D}={ }_{1-s} d_{\mathrm{x}+\mathrm{s}} /\left((1-s)_{1-s} E_{x+s}+s_{1-s} d_{x+s}\right),
$$

and therefore,

$$
\begin{aligned}
{ }_{1-s} q_{x+s}^{D} & =\left({ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)\right) /\left(1+(s /(1-s))_{1-s} q_{\mathrm{x}+\mathrm{s}}\right) \\
& \approx\left({ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)\right)\left(1-(s /(1-s))_{1-s} q_{\mathrm{x}+\mathrm{s}}\right) \\
& ={ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)-s\left(_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)\right)^{2} .
\end{aligned}
$$

The difference between the rates resulting from the fractional and distributed exposure methods is examined below. The third formula substitutes for the exponent $1 /(1-s)$ using the binomial expansion to the second order.

$$
\begin{aligned}
& { }_{1-s} q_{x+s}^{A}-{ }_{1-s} q_{x+s}^{D} \\
& =1-\left(1-{ }_{1-\mathrm{s}} q_{x+s}\right)^{1 /(1-s)}-{ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)+s\left({ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)\right)^{2} \\
& \approx 1-\left(1-{ }_{1-s} q_{x+s} /(1-s)+1 / 2\left({ }_{1-s} q_{x+s}\right)^{2} s /(1-s)^{2}\right) \\
& -{ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)+s\left({ }_{1-s} q_{\mathrm{x}+\mathrm{s}} /(1-s)\right)^{2} \\
& =+1 / 2 s\left({ }_{1-s} q_{x+s} /(1-s)\right)^{2}
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{aligned}
{ }_{1-s} q_{x+s} & =1-\left(1-{ }_{1-s} q_{x+s}^{A}\right)^{1-s} \\
& \approx(1-s)_{1-s} q_{x+s}^{A} .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
{ }_{1-\mathrm{s}} q_{x+s}^{A}-{ }_{1-\mathrm{s}} q_{x+s}^{D} & \approx+1 / 2 s\left({ }_{1-\mathrm{s}} q_{x+s}^{A}\right)^{2} \\
& \approx+1 / 2 s\left(q_{x}\left(1+1 / 2 s \Delta_{x}\right)\right)^{2} \\
& \approx+1 / 2 s\left(q_{x}\right)^{2}
\end{aligned}
$$

The error associated with the distributed exposure method, for the partial year running from age $x+s$ to $x+1$, can now be approximated as follows:

$$
\begin{aligned}
{ }_{1-s} e_{x+s}^{D M} & =q_{x}-{ }_{1-s} q_{x+s}^{D} \\
& =q_{x}-{ }_{1-s} q_{x+s}^{A}+{ }_{1-s} q_{x+s}^{A}-{ }_{1-s} q_{x+s}^{D} \\
& \approx-1 / 2 s \Delta_{x} q_{x}+1 / 2 s\left(q_{x}\right)^{2} \\
& \approx-1 / 2 s\left(\Delta_{x}-q_{x}\right) q_{x}
\end{aligned}
$$

### 19.3.3 Error for Fractional Period

The exposure for a fractional period is

$$
{ }_{f} E_{x+f t}^{D}=f_{f} E_{x+f t}+f_{f t} d_{x}
$$

Eliminating the deaths from prior fractional periods assuming a uniform distribution of deaths, we have:

$$
d_{x}={ }_{f t} d_{x} /(f t)={ }_{f} d_{x+f t} / f
$$

and therefore

$$
{ }_{f} E_{x+f t}^{D} \approx f_{f} E_{x+f t}+f t_{f} d_{x+f t} .
$$

Dividing deaths by both sides of the above equation, we have:

$$
{ }_{f} d_{\mathrm{x}+\mathrm{ft}} /{ }_{f} E_{x+f t}^{D}={ }_{f} d_{\mathrm{x}+\mathrm{ft}} /\left(f_{f} E_{x+f t}+f t_{f} d_{x+f t}\right),
$$

and therefore,

$$
\begin{aligned}
{ }_{f} q_{x+f t}^{D} & =\left({ }_{f} q_{\mathrm{x}+f t} / f\right) /\left(1+t_{f} q_{x+f t}\right) \\
& \approx\left({ }_{f} q_{\mathrm{x}+f t} / f\right)\left(1-t_{f} q_{x+f t}\right) \\
& ={ }_{f} q_{\mathrm{x}+f t} / f-f t\left({ }_{\mathrm{f}} q_{x+f t} / f\right)^{2} .
\end{aligned}
$$

The difference between the rates resulting from the fractional and distributed exposure methods is examined below. The third formula substitutes for the exponent $1 / f$ using the binomial expansion to the second order.

$$
\begin{aligned}
& { }_{f} q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{D} \\
= & 1-\left(1-{ }_{f} q_{x+f t}\right)^{1 / f}-{ }_{f} q_{\mathrm{x}+f t} / f+f t\left({ }_{f} q_{x+f t} / f\right)^{2} \\
\approx & 1-\left(1-{ }_{f} q_{x+f t} / f+1 / 2\left({ }_{f} q_{x+f t}\right)^{2}(1-f) / f^{2}\right)-{ }_{f} q_{\mathrm{x}+f t} / f+f t\left({ }_{f} q_{x+f t} / f\right)^{2} \\
= & -(1 / 2(1-f)-f t)\left({ }_{\mathrm{f}} q_{x+f t} / f\right)^{2}
\end{aligned}
$$

The fractional rate also can be approximated using the binomial expansion:

$$
\begin{aligned}
{ }_{f} q_{x+f t} & =1-\left(1-{ }_{f} q_{x+f t}^{A}\right)^{f} \\
& \approx f_{f} q_{x+f t}^{A}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& { }_{f} q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{D} \approx-(1 / 2(1-f)-f t)\left({ }_{f} q_{x+f t}^{A}\right)^{2} \\
& \approx-(1 / 2(1-f)-f t)\left(q_{x}\left(1-(1 / 2(1-f)-f t) \Delta_{x}\right)\right)^{2} \\
& \approx-(1 / 2(1-f)-f t)\left(q_{x}\right)^{2}
\end{aligned}
$$

The error associated with the distributed exposure method, for a fractional year, can now be approximated as follows:

$$
\begin{aligned}
{ }_{f} e_{x+f t}^{D M} & =q_{x}-{ }_{f} q_{x+f t}^{D} \\
& =q_{x}-{ }_{f} q_{x+f t}^{A}+{ }_{f} q_{x+f t}^{A}-{ }_{f} q_{x+f t}^{D} \\
& \approx(1 / 2(1-f)-f t) \Delta_{x} q_{x}-(1 / 2(1-f)-f t) \\
& =(1 / 2(1-f)-f t)\left(\Delta_{x}-q_{x}\right) q_{x}
\end{aligned}
$$

If the relative change over the year is a decrease equal to the mortality rate, i.e., $q_{x}=\Delta_{x}$, which is the uniform distribution, the error is zero.

## 20 Linear Force Method

Three exposure methods for calculating annual rates have been presented, each assuming a fixed distribution of deaths over the year.

- Annual Exposure assumes the Balducci Hypothesis where the rate decreases over the year.
- Distributed Exposure assumes a uniform distribution of deaths where the rate increases over the year
- $\quad$ Fractional Exposure assumes the rate, or equivalently, the force, is constant over the year.

The linear force distribution was developed in Section 8.2 to test the robustness of these methods under more realistic distributions and to estimate the errors arising under these methods.

The linear force exposure method was developed such that:

1. The force of mortality increased linearly through the year and
2. The rate at which the force increased was commensurate with annual increases in decrement rates.

Given the nature and extent of the changes in forces from age to age or year to year, this method allows estimates of the change in force to be specified for each age or year. The estimates for change in force can be easily obtained from industry rate tables or prior company experience.

### 20.1 Formula Development

To incorporate the linear force assumption directly into an experience study, the true annual average force needs to be estimated from the force for the partial years. In addition, an explicit assumption for the relative increase, $\Delta_{x}$, is required, which may be defined a priori using expected rate assumptions, or refined using the actual distribution. In the following three subsections, we will explore this approach for each of three partial year situations:

- A partial year running from age $x$ to $x+s$, such as for the partial policy year that occurs at the end of a study ending on January 1 ,
- A partial year running from age $x+s$ to $x+1$, such as for the partial policy year that occurs at the beginning of a study starting on January 1 and
- A fractional period such as one month or one day.


### 20.1.1 Partial Year Running from Age $x$ to $x+s$

The average force for a partial year running from age $x$ to $x+s$ can be calculated as the length of the partial year, $\mathrm{s}$, times deaths for the partial year divided by exposure for the partial year:

$$
{ }_{s} \bar{\mu}_{x} \approx \mathrm{s}\left({ }_{s} d_{x} /{ }_{s} E_{x}^{F}\right) .
$$

The average force can also be calculated as the length of the partial year times the average of the forces at the beginning and end of the partial year:

$$
\begin{aligned}
\mathrm{s}^{\bar{\mu}_{x}} & =\mathrm{s}\left(1 / 2\left(\mu_{x+0}+\mu_{x+\mathrm{s}}\right)\right) . \\
& =\mathrm{s}\left(\frac{1 / 2}{}\left(\bar{\mu}_{x}-1 / 2 \Delta \mu_{x}+\bar{\mu}_{x}+\left(\mathrm{s}-\frac{1}{2}\right) \Delta \mu_{x}\right)\right) . \\
& =\mathrm{s}\left(\bar{\mu}_{x}-1 / 2(1-\mathrm{s}) \Delta \mu_{x}\right) . \\
& =\mathrm{s} \bar{\mu}_{x}\left(1-1 / 2(1-\mathrm{s}) \Delta_{x}\right) .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\bar{\mu}_{x} & ={ }_{s} \bar{\mu}_{x} /\left(\mathrm{s}\left(1-\frac{1}{2}(1-\mathrm{s}) \Delta_{x}\right)\right) \\
& \approx{ }_{s} d_{x} /\left({ }_{s} E_{x}^{F}\left(1-\frac{1}{2}(1-\mathrm{s}) \Delta_{x}\right)\right) .
\end{aligned}
$$

We will define the weighted exposure for annual force, ${ }_{\mathrm{s}} E_{x}^{W}$, assuming the force changes linearly over the year, as

$$
{ }_{\mathrm{s}} E_{x}^{W}={ }_{\mathrm{s}} E_{x}^{F}\left(1-\frac{1}{2}(1-\mathrm{s}) \Delta_{x}\right) .
$$

We will define the exposure weight, ${ }_{s} w_{x}$, as

$$
{ }_{s} w_{x}=\left(1-1 / 2(1-s) \Delta_{x}\right)
$$

Weighted exposure for the partial year can now be expressed more simply as

$$
{ }_{\mathrm{s}} E_{x}^{W}={ }_{s} w_{x \mathrm{~s}} E_{x}^{F}
$$

The average force for the partial year can also be simplified:

$$
{ }_{\mathrm{s}} \bar{\mu}_{x} \approx{ }_{\mathrm{s}} d_{x} /{ }_{\mathrm{s}} E_{x}^{W}
$$

### 20.1.2 Partial Year from Age $\boldsymbol{x}+\boldsymbol{s}$ to $\boldsymbol{x}+\mathbf{1}$

The average force for a partial year running from age $x+s$ to $x+1$ can be calculated as the length of the partial year, $(1-s)$, times deaths for the partial year divided by exposure for the partial year:

$$
{ }_{1-\mathrm{s}} \bar{\mu}_{x+\mathrm{s}} \approx(1-\mathrm{s})\left({ }_{1-\mathrm{s}} d_{x+\mathrm{s}} /{ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{F}\right)
$$

The average force can also be calculated as the length of the partial year times the average of the forces at the beginning and end of the partial year:

$$
\begin{aligned}
1-\mathrm{s} \bar{\mu}_{x+\mathrm{s}} & =(1-\mathrm{s})\left(1 / 2\left(\mu_{x+\mathrm{s}}+\mu_{x+1}\right)\right) \\
& =(1-\mathrm{s})\left(\frac{1}{2}\left(\bar{\mu}_{x}+\left(\mathrm{s}-\frac{1}{2}\right) \Delta \mu_{x}+\bar{\mu}_{x}+1 / 2 \Delta \mu_{x}\right)\right) . \\
& =(1-\mathrm{s})\left(\bar{\mu}_{x}+1 / 2 \mathrm{~s} \Delta \mu_{x}\right) . \\
& =(1-\mathrm{s}) \bar{\mu}_{x}\left(1+1 / 2 \mathrm{~s} \Delta_{x}\right) .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\bar{\mu}_{x} & ={ }_{1-\mathrm{s}} \bar{\mu}_{x+\mathrm{s}} /\left((1-\mathrm{s})\left(1+\frac{1}{2} \mathrm{~s} \Delta_{x}\right)\right) \\
& \approx{ }_{1-\mathrm{s}} d_{x+\mathrm{s}} /\left({ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{F}\left(1+\frac{1}{2} \mathrm{~s} \Delta_{x}\right)\right) .
\end{aligned}
$$

We will define the weighted exposure for annual force, ${ }_{1-s} E_{x+s}^{W}$, assuming the force changes linearly over the year, as

$$
{ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{W}={ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{F}\left(1+\frac{1}{2} \mathrm{~s} \Delta_{x}\right) .
$$

We will define the exposure weight, ${ }_{1-s} w_{x+s}$, as

$$
{ }_{1-s} w_{x+s}=\left(1+\frac{1}{2} s \Delta_{x}\right)
$$

Weighted exposure for the period can now be expressed more simply as

$$
{ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{W}={ }_{1-s} w_{x+\mathrm{s} 1-\mathrm{s}} E_{x+\mathrm{s}}^{F}
$$

The average force for the partial year can also be simplified:

$$
{ }_{1-\mathrm{s}} \bar{\mu}_{x+\mathrm{s}} \approx{ }_{1-\mathrm{s}} d_{x+\mathrm{s}} /{ }_{1-\mathrm{s}} E_{x+\mathrm{s}}^{W}
$$

### 20.1.3 Fractional Periods

The average force for a fractional period running from age $x+f t$ to age $x+f t+f$ can be calculated as the length of the period, $f$, times deaths for the period divided by exposure for the period:

$$
{ }_{f} \bar{\mu}_{x+f t}=f\left({ }_{f} d_{x+f t} /{ }_{f} E_{x+f t}^{F}\right) .
$$

The average force can also be calculated as the average of the forces at the beginning and end of the period:

$$
\begin{aligned}
{ }_{f} \bar{\mu}_{x+f t} & =f\left(1 / 2\left(\mu_{x+f t}+\mu_{x+f t+f}\right)\right) \\
& =f\left(1 / 2\left(\bar{\mu}_{x}+(f t-1 / 2) \Delta \mu_{x}+\bar{\mu}_{x}+(f t+f-1 / 2) \Delta \mu_{x}\right)\right) \\
& =f\left(1 / 2\left(2 \bar{\mu}_{x}+(2 f t+f-1) \Delta \mu_{x}\right)\right) \\
& =f\left(\bar{\mu}_{x}-(1 / 2(1-f)-f t) \Delta \mu_{x}\right) \\
& =f \bar{\mu}_{x}\left(1-(1 / 2(1-f)-f t) \Delta_{x}\right) .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\bar{\mu}_{x} & ={ }_{f} \bar{\mu}_{x+f t} /\left(f\left(1-\Delta_{x}(1 / 2(1-f)-f t)\right)\right) \\
& \approx{ }_{f} d_{x+f t} /\left({ }_{f} E_{x+f t}^{F}\left(1-\Delta_{x}(1 / 2(1-f)-f t)\right)\right) .
\end{aligned}
$$

The weighted exposure for annual force, ${ }_{f} E_{x+f t}^{W}$, assuming the force changes linearly over the year, is

$$
{ }_{f} E_{x+f t}^{W}={ }_{f} E_{x+f t}^{F}\left(1-\Delta_{x}(1 / 2(1-f)-f t)\right) .
$$

We will define the exposure weight, $f w_{x+f t}$, as

$$
{ }_{f} W_{x+f t}=\left(1-\Delta_{x}(1 / 2(1-f)-f t)\right) .
$$

Weighted exposure for the period can now be expressed more simply as

$$
{ }_{f} E_{x+f t}^{W}={ }_{f} W_{x+f t ~} E_{x+f t}^{F} .
$$

The average force for the period can also be simplified:

$$
\bar{\mu}_{x} \approx{ }_{f} d_{x+f t} /{ }_{f} E_{x+f t}^{W}
$$

### 20.2 Increasing Force Example

Using the monthly example given in Section 9.1.4, with a $1 \%$ annual mortality rate and a relative annual increase of $10 \%$, monthly results for the constant and linear force methods are shown in the table below. For monthly, $f$ is equal to $1 / 12$. The lives and deaths match the original example shown in Section 9.1.4. For each month, the table shows monthly exposure, a mortality rate (calculated as monthly deaths divided by monthly exposure), the exposure weight, weighted exposure and the annualized rate assuming linear force method, indicated by LF, which matches the underlying annual rate for every month.

| $t$ | $\boldsymbol{f}_{x+f t}$ | ${ }_{f} d_{x+f t}$ | $f^{E_{x+f t}^{F}}$ | ${ }_{f} q_{x+f t}$ | $f w_{x+f t}$ | ${ }_{f} E_{x+f t}^{W}$ | ${ }_{f} q_{x+f t}^{L F}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | $1,000.00$ | 0.80 | 83.30 | 0.00954 | 0.95417 | 79.48 | 0.01000 |
| 1 | 999.20 | 0.81 | 83.23 | 0.00963 | 0.96250 | 80.11 | 0.01000 |
| 2 | 998.40 | 0.81 | 83.17 | 0.00971 | 0.97083 | 80.74 | 0.01000 |
| 3 | 997.58 | 0.82 | 83.10 | 0.00979 | 0.97917 | 81.37 | 0.01000 |
| 4 | 996.77 | 0.82 | 83.03 | 0.00988 | 0.98750 | 81.99 | 0.01000 |
| 5 | 995.94 | 0.83 | 82.96 | 0.00996 | 0.99583 | 82.61 | 0.01000 |
| 6 | 995.11 | 0.84 | 82.89 | 0.01004 | 1.00417 | 83.24 | 0.01000 |
| 7 | 994.28 | 0.84 | 82.82 | 0.01012 | 1.01250 | 83.86 | 0.01000 |
| 8 | 993.43 | 0.85 | 82.75 | 0.01021 | 1.02083 | 84.47 | 0.01000 |
| 9 | 992.58 | 0.86 | 82.68 | 0.01029 | 1.02917 | 85.09 | 0.01000 |
| 10 | 991.73 | 0.86 | 82.61 | 0.01037 | 1.03750 | 85.71 | 0.01000 |
| 11 | 990.87 | 0.87 | 82.54 | 0.01046 | 1.04583 | 86.32 | 0.01000 |
| Tot |  | 10.00 | 995.07 | 0.01000 | 12.00000 | 994.99 | 0.01000 |

The next table has most of the same columns as the preceding table, but with results summarized by half-years. The annualized half-year rates match the underlying half-year rates, which would contribute as annual rates for partial years. The linear force rates calculated using weighted exposure, ${ }_{f} q_{x+f t}^{L F}$, match the underlying annual rate.

| $\boldsymbol{t}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{w}_{\boldsymbol{x}+\boldsymbol{f t}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{E}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{W}}$ | ${ }_{\boldsymbol{f}} \boldsymbol{q}_{\boldsymbol{x}+\boldsymbol{f t}}^{\boldsymbol{L F}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 498.78 | 0.00975 | 0.97500 | 486.31 | 0.01000 |
| 1 | 496.28 | 0.01025 | 1.02500 | 508.69 | 0.01000 |
| Total | 995.06 | 0.01000 | 2.00000 | 994.99 | 0.01000 |

## 21 Glossary

A/E ratio See actual to expected ratio.

actual to expected ratio The ratio of actual events to expected events, where expected events are calculated as an expected rate applied to actual exposure. See Chapter 12, Actual to Expected.

actuarial exposure method See annual exposure method.

actuarial table A table that shows lives, deaths, and probabilities of death and survival for a series of ages. See Section 4.1, Cohort Study with Deaths only.

amount-weighted Population, decrements, exposure and rates that are based on amounts rather than number of lives or contracts. Such amounts would usually be a measure of size, such as premiums or benefit amount. See Section 4.4, Amount-Weighted Studies.

annual exposure method The traditional method of calculating exposure, sometimes referred to as the "actuarial exposure method." This method allocates a full year of exposure to deaths (or, more generally, to the event under study), and is consistent with the Balducci Hypothesis. See Section 4.2, Cohort Study with Deaths and Withdrawals.

Balducci hypothesis The assumption that the probability of death for the remainder of a year is proportionate to the annual probability of death. See Section 4.2, Cohort Study with Deaths and Withdrawals and Chapter 9, Distribution of Deaths.

benefit utilization rate A rate that measures the amount of benefits incurred compared to the maximum that could be incurred. See Section 18.5.2, Benefit Utilization Rate.

calendar year Starts at 12:01 AM on January 1 and ends at 12:01 AM on the following January 1. See Rate Year in Section 3.1, Basic Terminology.

calendar-year rate interval A rate interval that runs from one January 1 at 12:01 AM to the next. See Section 10.2, Rate Intervals.

cell The lowest level of segmentation or grouping within an experience study. See Section 3.1, Basic Terminology.

central exposure An estimate of the average or mid-year population. See Chapter 13, Central Rates.

central rate A rate that is applied to the average or mid-year population. See Chapter 13, Central Rates.

cohort study An experience study that tracks a group of lives, often of the same age, from a start year through many following years, usually until all lives have died. See Section 4.1, Cohort Study with Deaths only.

combined table A life table that shows results for two or more population states. See States and Section 10.5, Population States.

continuous decrement A decrement that varies in a continuous fashion over time (i.e., no discontinuities). Biological decrements, such as mortality and morbidity, are sometimes assumed to be continuous but are most often calculated using annual, discontinuous rates. See Chapter 8, Average Force of Mortality.

daily exposure Exposure based on the number of days each life was exposed to the event under study. See Chapter 7, Average Daily Rates and Exposure.

decrement rate A rate for an event that removes a person or contract from the study population. See Rate Type in Section 3.1, Basic Terminology.
dependent rates Rates that are calculated from a single composite exposure that combines two or more decrements. Because different decrements use the same exposure, the rates for each decrement are dependent on the other decrement(s). See Chapter 14, Dependent Rates.

discrete decrement A decrement that can only occur on certain dates, has an irregular distribution within the rate interval or can keep a secret. See Section 10.4, Discrete Decrements.

distributed exposure method A method of distributing exposure that is consistent with the assumption of a uniform distribution of the decrement under study. See Chapter 5, Distributed Exposure.

event timing All events are assumed to occur as of 12:01 AM on the date of the event. See Section 4.3, Period Study with Deaths and Withdrawals.

experience rates Rates that are developed by an experience study. See Section 3.1, Basic Terminology.

exposure A measure that reflects how many persons or contracts were exposed to the possibility or risk of the event under study, and for how long. See Section 4.2, Cohort Study with Deaths and Withdrawals.

force of mortality The annualized instantaneous mortality rate. See Chapter 8, Average Force of Mortality.

fractional rates Rates calculated for a given fraction of a year, such as daily, weekly, monthly, quarterly or semiannual rates. See Chapter 6, Fractional Rates.

frequency rate A utilization rate that measures how often the event under study happens. See Section 15.1, Frequency and Severity.

hybrid exposure method Also known as the in-period exposure method, this method is a hybrid of the annual and distributed exposure methods and uses different underlying assumptions for the partial ages at the start and end of the study. See Chapter 5, Distributed Exposure.

in-period exposure method Also known as the hybrid exposure method, the name of this method indicates that decrements are assigned exposure for only that part of the exposure period which lies within the study period. See Chapter 5, Distributed Exposure.

increasing force The assumption that the force of mortality increases linearly within each age. See Section 9.1.4, Increasing Force and Chapter 20, Linear Force Method.

independent rate A decrement rate based on its own exposure that adjusts for terminations due to other decrements. It is therefore independent of the other decrements. See Section 4.2, Cohort Study with Deaths and Withdrawals.

initial exposure Exposure that is based on the lives or contracts at the start of the rate interval. See Section 4.2, Cohort Study with Deaths and Withdrawals.

initial rate A rate that is applied to the lives or contracts at the start of the rate interval. See Section 4.1, Cohort Study with Deaths only.

life table A table that shows lives, deaths, and probabilities of death and survival for a series of ages. See Section 4.1, Cohort Study with Deaths only.

life year A year starting on one birthday and ending just prior to the next birthday. See Rate Year in Section 3.1, Basic Terminology.

life-year rate interval A rate interval that runs from one birthday to the next. See Section 10.2, Rate Intervals.

loss ratio The cost of claims expressed as a percentage of premium. See Section 15.3, Loss Ratio.
mortality survival rate In a study involving deaths and withdrawals, the probability of not dying. See Section 4.2, Cohort Study with Deaths and Withdrawals.

multi-state study A study that includes transitions between states by members of the study population. See state and Section 3.2, Experience Study Segmentation.

multiple decrement rates See dependent rates.

multiple decrement table A table showing lives, number of decrements, and probabilities of decrement and survival, for more than one cause of decrement. See Section 4.2.2, Grouped Exposure Calculation.

partial policy year See Partial Rate Interval.

partial rate interval A rate interval that is truncated for one of three reasons and is a potential source of error. See Section 10.2.1, Partial Rate Intervals.

period study An experience study with a start date and an end date, usually one to ten years apart. Contrast with cohort study. See Section 4.3, Period Study with Deaths and Withdrawals.

policy year A measure of time since the inception date of a policy or other contract, equal to 1 at inception and increasing by 1 on each policy anniversary. See Rate Year in Section 3.1, Basic Terminology.

policy-year rate interval A rate interval that runs from one policy anniversary to the next. See Section 10.2, Rate Intervals.

rate interval The interval of time for which experience rates are calculated. See Section 3.1, Basic Terminology and Section 10.2, Rate Intervals.

rate type There are two types: decrement rate and utilization rate. I. See Section 3.1, Basic Terminology.

rate year The type of year upon which rates are based; usually a policy year, life year or calendar year. See Section 3.1, Basic Terminology.

severity rate A utilization rate that measures the average cost associated with the event under study. See Section 15.1, Frequency and Severity.

single composite decrement A decrement formed by combining two or more decrements. See Chapter 14, Dependent Rates.

single decrement rate See independent rate.

single decrement table A table showing lives, number of decrements, and probabilities of decrement and survival, with only one cause of decrement. See Section 4.1, Cohort Study with Deaths only.

single-state study A study that focuses on a single state of the study population. Most studies have only a single state. See state and Section 10.5, Population States.

study period The period of time for which data has been gathered for an experience study. See Section 3.1, Basic Terminology.

study population The population from which the experience study's data has been drawn. See Section 3.1, Basic Terminology.

state The status of a person or contract that is a member of the study population, such as healthy vs. disabled. A change in status does not remove the person from the total study population, although it may remove the person from a study of a segment of the study population. See Section 3.2, Experience Study Segmentation.
survival rate The probability that lives or contracts will not terminate over a period of time, most often a year. See Section 4.1.1, Summary Rates.

transition study See multi-state studies.

uniform distribution of deaths (UDD) The assumption that the number of deaths occurring in any fraction of the year is equal to the fraction times the total deaths for the year. See Chapter 5, Distributed Exposure and Chapter 9, Distribution of Deaths.

utilization rate A rate for an event that does not remove a person or contract from the study population. See Rate Type in Section 3.1, Basic Terminology.

withdrawals For individual life insurance: Terminations other than death, such as surrender, lapse, expiry, maturity and conversion. More generally: All decrements other than the decrement under study. See Section 4.2, Cohort Study with Deaths and Withdrawals.

## 22 About the Society of Actuaries

The Society of Actuaries (SOA), formed in 1949, is one of the largest actuarial professional organizations in the world dedicated to serving 24,000 actuarial members and the public in the United States, Canada and worldwide. In line with the SOA Vision Statement, actuaries act as business leaders who develop and use mathematical models to measure and manage risk in support of financial security for individuals, organizations and the public.

The SOA supports actuaries and advances knowledge through research and education. As part of its work, the SOA seeks to inform public policy development and public understanding through research. The SOA aspires to be a trusted source of objective, data-driven research and analysis with an actuarial perspective for its members, industry, policymakers and the public. This distinct perspective comes from the SOA as an association of actuaries, who have a rigorous formal education and direct experience as practitioners as they perform applied research. The SOA also welcomes the opportunity to partner with other organizations in our work where appropriate.

The SOA has a history of working with public policymakers and regulators in developing historical experience studies and projection techniques as well as individual reports on health care, retirement, and other topics. The SOA's research is intended to aid the work of policymakers and regulators and follow certain core principles:

Objectivity: The SOA's research informs and provides analysis that can be relied upon by other individuals or organizations involved in public policy discussions. The SOA does not take advocacy positions or lobby specific policy proposals.

Quality: The SOA aspires to the highest ethical and quality standards in all of its research and analysis. Our research process is overseen by experienced actuaries and non-actuaries from a range of industry sectors and organizations. A rigorous peer-review process ensures the quality and integrity of our work.

Relevance: The SOA provides timely research on public policy issues. Our research advances actuarial knowledge while providing critical insights on key policy issues, and thereby provides value to stakeholders and decision makers.

Quantification: The SOA leverages the diverse skill sets of actuaries to provide research and findings that are driven by the best available data and methods. Actuaries use detailed modeling to analyze financial risk and provide distinct insight and quantification. Further, actuarial standards require transparency and the disclosure of the assumptions and analytic approach underlying the work.

Society of Actuaries

475 N. Martingale Road, Suite 600

Schaumburg, Illinois 60173

www.SOA.org

