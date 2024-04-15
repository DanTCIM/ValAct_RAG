# Research INSTITUTE 

Calibrating Interest Rate Models

October 2023

## 8SOA <br> Research <br> INSTITUTE

## Calibrating Interest Rate Models

AUTHORS Rohana Ambagaspitiya, FSA, FCIA, PhD

Charles Ford, FSA, MAAA, CFA
SPONSOR

Quantitative Finance and Investment Curriculum Committee

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-02.jpg?height=244&width=1510&top_left_y=1843&top_left_x=313)

Caveat and Disclaimer

The opinions expressed and conclusions reached by the authors are their own and do not represent any official position or opinion of the Society of Actuaries Research Institute, the Society of Actuaries or its members. The Society of Actuaries Research Institute makes no representation or warranty to the accuracy of the information.

Copyright (C) 2023 by the Society of Actuaries Research Institute. All rights reserved.

## TABLE OF CONTENTS

Executive Summary ..... 5
1 Introduction ..... 7
1.1 R Setup ..... 7
1.2 Introduction to Scenarios ..... 8
1.3 Interest Rate Markets. ..... 8
1.4 Market-Consistent Models ..... 9
1.5 The Market Price of Risk ..... 9
1.6 Parameter Uncertainty ..... 11
2 Three Continuous-Time Interest Rate Models ..... 11
2.1 The Vasicek Model ..... 11
2.1.1 Simulating paths of the Vasicek model: Euler-Maruyama discretization ..... 12
2.1.2 Simulating paths of the Vasicek model: Transition Density Method ..... 13
2.2 Cox-Ingersoll-Ross (CIR) Model ..... 15
2.2.1 Simulating paths of the CIR Model: Euler-Maruyama discretization ..... 15
2.2.2 Simulating paths of the CIR model: Transition density method ..... 17
2.3 The Two-Factor Vasicek model with correlated factors. ..... 18
2.3.1 Simulating paths of the two-factor Vasicek model: Transition density method ..... 19
3 Calibration Techniques ..... 20
3.1 The Vasicek model: real-world calibration. ..... 20
3.1.1 Maximum Likelihood Estimator Method ..... 21
3.1.2 Long Term Quantile Method. ..... 25
3.2 The Vasicek model: risk-neutral calibration ..... 27
3.3 The CIR model: real-world calibration ..... 33
3.3.1 Euler method ..... 33
3.3.2 Maximum likelihood estimate ..... 34
3.4 THE GENERALIZED METHOD OF MOMENTS ..... 36
3.5 The CIR model: risk-neutral calibration ..... 39
3.6 The two-factor Vasicek model calibration ..... 46
4 No-Arbitrage Models ..... 52
4.1 Hull-white models ..... 52
4.1.1 One factor Hull-white model. ..... 52
4.1.2 The two-factor Hull-white model ..... 54
4.1.3 Hull-white model calibration ..... 55
4.2 Yield curve interpolation: one-factor model ..... 56
4.2.1 Fitting an $\boldsymbol{n}$ degree polynomial for $\boldsymbol{r} \mathbf{0}, \boldsymbol{t}$ ..... 57
4.2.2 Fitting a Nelson-Siegel Curve to $\boldsymbol{r} \mathbf{0}, \boldsymbol{t}$ ..... 59
4.3 Calibration of the One-Factor Hull-White Model ..... 61
4.4 Calibration of the Two-Factor Hull-White Model ..... 67
5 Model Validation ..... 78
5.1 Data and Assumptions ..... 78
5.2 Investigate the Data ..... 81
5.3 Recalibrate ..... 82
5.4 Validate ..... 85
5.5 Model Governance..... ..... 86
6 Conclusion ..... 87
7 Acknowledgments ..... 88
References ..... 89
Appendix A: Zero coupon bond prices under one-factor Vasicek model . ..... 91
Appendix B: Zero coupon bond prices under the two-factor Vasicek model ..... 93
About The Society of Actuaries Research Institute ..... 98

## Calibrating Interest Rate Models

## Executive Summary

Investment Actuaries and now Valuation Actuaries need a mastery of stochastic interest rate models. This includes selecting a model appropriate for a given application, the correct use of real world versus risk neutral scenario sets, and how to calibrate and validate them properly.

Models like Vasicek and Cox-Ingersoll-Ross (CIR) are stochastic models that, when the parameters are set, determine the yield curve. They are appropriate when a stochastic model is needed and it is less important whether or not the yield curve implied by the model actually matches the "actual" observed yield curve. This setup is mainly used for US Statutory Valuation VM20, VM21 and Economic Capital calculations.

If the requirement is to price interest sensitive cash flows in a market consistent way, something else is needed. Both the CIR and Vasicek can be modified to get market consistent versions and obviously there are many other models beyond these. Examples of market-consistent applications are IFRS 17 valuation, measuring the cost of guarantees for universal life minimum interest rates, and measuring the cost of guarantees for participating insurance products. The following table summarizes what type of interest rate models should be used under different circumstances and to what they should be calibrated.

Table 1

TABLE TITLE OR DESCRIPTION

| Purpose of the Interest Rate <br> Generator | Interest Rate Model | Items Calibrated to |
| :--- | :--- | :--- |
| US Statutory Valuation | Vasicek | Historical rates, current yield <br> curve, expert opinion, and/or <br> regulatory criteria |
| Market Consistent Valuation | 2-factor Hull-White <br> Lognormal Forward Model | Current Yield curve |
| Pricing of Options | Extended CIR |  |

SOA QFI Curriculum

The existing literature presents the theory, but it can be challenging for the practitioner new to this specialty to take that theory, write code to implement it, use historical data to calibrate the model, and assess whether the resulting set of scenarios is reasonable.

This paper addresses this need by introducing practitioners to the selection and calibration of stochastic interest rate models. Six continuous time interest rate models and their calibration are presented. Actual code and data examples are added to help the practitioner implement them. The emphasis is on hands-on calibration with RStudio. The reader is assumed to have a working knowledge of RStudio, including writing R scripts.

The focus of this paper is narrow: calibrating and validating an interest rate model for default-free bond yields in a single economy. Out of scope are inflation and equity index variables, credit spreads, and factors for multiple economies such as foreign exchange.

With this focus the practitioner may begin their journey in stochastic interest rate modeling.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-06.jpg?height=244&width=1521&top_left_y=2182&top_left_x=302)

## 1 Introduction

In this paper we present calibration of six continuous time interest rate models. We use the notation in [24] and cite relevant chapters throughout the report. The emphasis is on hands-on calibration with RStudio. We assume the reader has some working knowledge of RStudio, including writing R scripts.

The focus of this paper is narrow: calibrating and validating an interest rate model for default-free bond yields in a single economy. These are outlined at a higher level in [1]. This paper adds actual code and data examples to help the practitioner implement these ideas. Out of scope are inflation and equity index variables, credit spreads, and factors for multiple economies such as foreign exchange.

In this paper the acronym ESG refers to economic scenario generators and not to environmental, social, and governance aspects of investing.

### 1.1 R SETUP

$\mathrm{R}$ is used for examples. The RStudio environment for working with $\mathrm{R}$ will be necessary for the reader to follow along and experiment with the code presented in this paper. If RStudio has not been downloaded and installed, now would be a good time to do so.

The $\mathrm{R}$ functions and examples given in this paper are available as a bundled package on the SOA website at https://www.soa.org/resources/research-reports/2023/interest-rate-model-calibration-study/ You may install "InterestCalibrationv1_1.2.0.tar.gz" in RStudio using "Tools $\rightarrow$ Install packages $\rightarrow$ Install from: $\rightarrow$ Package Archive". When you extract the package archive, its subfolders " $R$ " and "examples" contain all the functions and examples respectively. However, readers are encouraged to key in the code chunks instead of copy/pasting them.

$\mathrm{R}$ is both a software environment and a scripting language, and it may interpret certain manipulations in an unintended way. When a new session is begun it is good idea to either restart $\mathrm{R}$ or clean the workspace using:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-07.jpg?height=422&width=1392&top_left_y=1578&top_left_x=320)

### 1.2 INTRODUCTION TO SCENARIOS

This paper explores the nuances of calibrating continuous-time interest rate models. It is not an introduction to economic scenario generators (ESGs). In actual practice there are several steps to the process of setting up a model to run multiple, stochastically generated interest rate scenarios:

- The application for the modeling work should be clear to practitioners

o Derivative valuation, valuing financial guarantees such as insurance business pricing, financial planning, and economic capital or tail risk analysis

- Specify "stylized facts"

o Clarify an understanding of how economic variables are expected to evolve over time and in what circumstances the relationships between them change, such as during a recession

- Source and analyze historical data
- Calibrate the model
- Run the generator
- Confirm that the resulting scenarios are fit for purpose. How well do they conform to the predetermined stylized facts? Are changes necessary?
- Run the model of the security or business, iterating through each scenario
- Validate the model results
- Document each step so that:

o choices made can be explained in management presentations and regulatory filings

o the whole process can be run in an efficient, consistent manner when next required

This broader context is examined in Economic Scenario Generators: A Practical Guide, (SOA, 2016) (the "Practical Guide")[1]. This paper will only comment briefly on these points and suggest initial choices to provide context and a pathway through this process. Experienced practitioners will have reasons to make different judgements on these issues.

### 1.3 INTEREST RATE MARKETS

This paper assumes a context of US fixed income markets. Some other sovereign bond markets have the trading liquidity and full term structure seen in the US Treasury bond market. Practitioners in other markets are encouraged to consult with a bond analyst or trader for local market characteristics, such as liquidity and yield quoting conventions.

A word about U.S. Treasury yields. The U.S. Department of the Treasury issues intermediate and longer maturity notes (to 10 years) and bonds (longer than 10 years) every few months. Loosely speaking they are all often called "bonds", which we will do here. Consider a newly issued 10 -year bond, which is said to be "on-the-run". A 30-year bond issued 20 years ago also has 10 years until maturity, but it is said to be "offthe-run". Trading in it is less liquid and it may trade for a couple of basis points higher yield.

As time passes that newly issued 10 -year bond will no longer have 10 years until maturity, but rather 9 years 11 months, 10 months, etc. In an upwardly sloping yield curve environment these trade at a slightly lower yield than a true 10-year note. The Treasury Department does a curve fitting exercise every trading day to calculate that day's closing yield for a true 10 -year bond, and other key maturities as well. These are
said to be "constant maturity treasury" (CMT) yields ${ }^{1}$ and are often used for modeling, even though they are not actually tradable securities. CMT yields and discussion can be found by doing an internet search for "US Treasury CMT rates".

Six months after issue a new 10-year note is issued and becomes the on-the-run 10-year bond. The first bond now has just 9.5 years until maturity, and is said to be off-the-run. Trading liquidity will shift to the new on-the-run note.

### 1.4 MARKET-CONSISTENT MODELS

Before a model can be calibrated it must be selected. To select an appropriate model the practitioner must be clear on the uses to which the model will be applied.

One class is for realistic simulation of how something - an asset, a financial liability, or a business segment with both - evolves over time. By "realistic" we mean plausible given an accepted set of stylized facts about how market participants make decisions and how interest rates "should" evolve over time. These are discussed in detail in [1], chapter 6 .

A different problem is to determine a value for a security that is not frequently traded. A model can be calibrated to observed market prices of similar securities and then used to calculate (estimate) values for illiquid securities.

Either problem can be solved with a model and an economic scenario generator. If equity index variables and economic variables such as inflation need not be modeled then those factors may be set to zero, one, or otherwise not used, leaving the interest rate model the only active part of the ESG. The generator is then set up with initial conditions such as observed yields and market prices as of the desired model start date. The generator has an interest rate model component which evolves yield curves forward one time step at a time to produce one interest rate scenario. This step is repeated $1,000,10,000$, or more times to generate a set of interest rate scenarios. For each scenario, a value is calculated for each security.

These values do not automatically reproduce observed market prices at the model start date. The model must be "calibrated", that is, its parameters must be adjusted to match specific criteria.

If the task at hand is to calculate prices for infrequently traded securities that are reasonably consistent with the observed market prices of frequently traded securities, then the calibration adjusts the parameters to reproduce those prices. Such a calibration is "market-consistent". The adjusted, or calibrated, scenario set may then be used to calculate estimated market values for similar non-traded securities. It should not be used for dissimilar securities.

Note that so far nothing has been said about risk neutral or real world.

### 1.5 THE MARKET PRICE OF RISK

One stylized fact is that market participants are risk averse. Market prices embed a factor for this called the "market price of risk".[^0]

If the scenario set is only being used to value securities at the model start date, a useful mathematical tool is to assume the market price of risk is zero. The calibration step can still find parameters to match the observed securities prices, but it does so by adjusting the probability of each scenario occurring.

This is useful because the market price of risk can be estimated but not directly observed in the market. With the assumption of a zero market price of risk, the calibrated scenario set is said to be "risk-neutral." It is also market-consistent because it reproduces the observed market prices of the selected securities at the specified date. The trade-off is that this scenario set can no longer provide reliable information about future time steps or period; it is not fit for such a purpose.

It is also possible to choose a market price of risk from historical data. As with the other parameters this would need to fit the stylized facts and interact with other parameters in a reasonable way. The model calibration can then either fit the scenarios to observed market prices so as to be market consistent, or left in an equilibrium state. The latter approach might be desirable for stress testing or tail risk analysis. The former approach is necessary for estimating values of similar securities ("valuation").

Why might the former approach of setting a historically based market price of risk and calibrating to observed market prices be preferred to assuming a zero market price of risk (the risk-neutral approach)? When the item being modeled has complex future interactions, such as modeling a hedging program or embedded options in new business in a financial plan model, having scenarios and model outcomes that are intuitively understandable and can be explained to stakeholders beyond the modeling team may be important for credibility and influencing decisions. Silly-looking scenarios come with risk-neutral; they're part of the deal.

More complete discussions can be found in [23] for the latest research as well as the classic chapter 11 of [3].

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-10.jpg?height=762&width=1328&top_left_y=1554&top_left_x=431)

### 1.6 PARAMETER UNCERTAINTY

Not only is the choice of the most appropriate model a matter of judgement, the parameters of the chosen model are uncertain as well. [4] studies the Wilkie model, which models inflation, dividend yields, and an equity index return, as well as a long-term interest rate. Parameter uncertainty is found to have a significant impact on the dispersion of these four parameters. The paper applies its findings to a block of annuity contracts, finding that the distribution of outcomes is significantly wider when the parameters are recognized as instances of random variables. Developing methods to apply this insight would be an avenue for further research.

## 2 Three Continuous-Time Interest Rate Models

In this section we provide a brief description of the three models that we consider. We consider three models: the Vasicek (one and two factor) models, Cox-Ingersoll-Ross (CIR) model, and the Hull-White models (one and two factor). The Vasicek and CIR models are called equilibrium models or real-world models. The equivalent risk-neutral models can be obtained by changing the drift of those models. We assume that a one factor continuous-time interest rate model for short rate $r_{t}$ is an Itô process, i.e. $r_{t}$ follows the stochastic differential equation (SDE)

$$
d r_{t}=a\left(r_{t}\right) d t+b\left(r_{t}\right) d X_{t}
$$

where $a\left(r_{t}\right)$ and $b\left(r_{t}\right)$ are functions of $r_{t}$ and $X_{t}$ is a standard Wiener process. For a formal definition of an Itô process and an SDE one may refer to [8]. Similarly, the two-factor models satisfy the following SDE

$$
d r_{t}=a\left(r_{t}\right) d t+b_{1}\left(r_{t}\right) d X_{1, t}+b_{2}\left(r_{t}\right) d X_{2, t}
$$

with $d X_{1, t} d X_{2, t}=\rho d t$

In statistical calibrations, the underlying assumption is that data follows the model that we try to fit. Therefore, to evaluate calibration techniques we need sample paths from the interest rate model. The only way to get sample paths that follow the underlying distribution with known parameters is Monte Carlo simulation. Therefore, it is important to have an accurate method of simulating sample paths from the given SDE with known parameters. There are number of techniques to generate sample paths from a given SDE and Chapter 2 of [17] is a good introduction. However, we present two methods: Euler-Maruyama discretization and the transition density method introduced in [11]. Note that Chapter 17 of [24] only discusses implementation of Euler-Maruyama method for simulating sample paths, however we demonstrate that this method is not suitable for practical applications.

### 2.1 THE VASICEK MODEL

In the Vasicek model the risk free rate of interest $r_{t}$ is based on an SDE:

$$
d r_{t}=\gamma\left(\bar{r}-r_{t}\right) d t+\sigma d X_{t}
$$

where $X_{t}$ is the standard Wiener process and $\gamma, \bar{r}$, and $\sigma$ are strictly positive parameters. The three parameters $\gamma, \bar{r}$, and $\sigma$ have the following interpretation:

- $\bar{r}$ is the long term mean level; when the rate $r_{t}$ drifts too much from $\bar{r}$, it will be pulled back closer to that level. This is called mean reversion.
- $\quad \gamma$ is the speed of mean reversion.
- $\sigma$ is the instantaneous volatility.

The solution of the above SDE takes the following form:

$$
r_{t+s}=r_{t} e^{-\gamma s}+\bar{r}\left(1-e^{-\gamma s}\right)+\sigma e^{-\gamma s} \int_{0}^{s} e^{\gamma u} d X_{u}
$$

where $r_{t}$ is the initial point (starting point) of the process and where $s>0$.

Since $\int_{0}^{s} e^{\gamma u} d X_{u}$ is a normal random variable with mean zero and variance $\int_{0}^{s} e^{2 \gamma u} d u$, we see that $r_{t+s} \mid r_{t}$, where $\mathrm{s}>0$ (i.e. the conditional random variable of $r_{t+s}$ conditioned on $r_{t}$ ), is normally distributed with mean $\mu\left(r_{t}, s\right)$ and variance $\sigma(s)^{2}$ which are given as below:

$$
\begin{aligned}
\mu\left(r_{t}, s\right) & =\bar{r}+\left(r_{t}-\bar{r}\right) e^{-\gamma s} \\
\sigma(s)^{2} & =\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma s}\right)
\end{aligned}
$$

As the conditional distribution or $r_{t+s} \mathrm{f}$ is normal, the probability of $r_{t+s}<0$ can be calculated as below:

$$
\begin{aligned}
P\left[r_{t+s}<0 \mid r_{t}\right] & =P\left(\frac{r_{t+s}-E\left[r_{t+s} \mid r_{t}\right]}{\sigma(s)}<-\frac{E\left[r_{t+s}\right]}{\sigma(s)}\right) \\
& =\Phi\left(-\frac{E\left[r_{t+s}\right]}{\sigma(s)}\right) \\
& =\Phi\left(-\frac{\bar{r}+\left(r_{t}-\bar{r}\right) e^{-\gamma s}}{\sigma \sqrt{\frac{1-e^{-2 \gamma s}}{2 \gamma}}}\right)
\end{aligned}
$$

For example the set of values $\left(r_{t}=0.01, \bar{r}=0.05, \gamma=0.5, \sigma=0.02, s=0.1\right)$ will yield $P\left[r_{t+s}<0 \mid r_{t}\right]=$ 0.02637. This implies that there is a positive probability of negative interest rates occurring, which is generally seen as a drawback of this model (Japanese and European experience notwithstanding). However, we can minimize the chance of negative rates in simulation studies by choosing parameters appropriately.

### 2.1.1 SIMULATING PATHS OF THE VASICEK MODEL: EULER-MARUYAMA DISCRETIZATION

In this method we discretize the Vasicek model SDE in the following manner:

$$
\begin{aligned}
d r_{t} & =\gamma\left(\bar{r}-r_{t}\right) d t+\sigma d X_{t} \\
r_{t+\Delta}-r_{t} & =\gamma\left(\bar{r}-r_{t}\right) \Delta+\epsilon_{t+\Delta} \\
r_{t+\Delta} & =r_{t}+\gamma\left(\bar{r}-r_{t}\right) \Delta+\epsilon_{t+\Delta}
\end{aligned}
$$

where $\epsilon_{t+\Delta}$ is a normal random variable with mean 0 and variance $\sigma^{2} \Delta$. As $d X_{t}$ is a standard Brownian motion we can write from the above:

$$
r_{i \Delta}=r_{(i-1) \Delta}+\gamma\left(\bar{r}-r_{(i-1) \Delta}\right) \Delta+\epsilon_{i \Delta}, \quad i=1,2, \ldots
$$

From the properties of Brownian motion we know that $\epsilon_{i \Delta}, i=1,2, \ldots$ are independent identically distributed (i.i.d.) normal with mean zero and variance $\sigma^{2} \Delta$. For convenience let us write:

$$
\begin{aligned}
r(0) & =r_{0} \\
r(i) & =r_{i \Delta}, \quad i=1,2, \ldots \\
\alpha & =\gamma \bar{r} \Delta \\
\beta & =1-\gamma \Delta \\
\sigma^{*} & =\sigma \sqrt{\Delta} \\
\epsilon_{i} & =\epsilon_{i \Delta}
\end{aligned}
$$

Then:

$$
r(i)=\alpha+\beta r(i-1)+\epsilon_{i}, \quad i=1,2, \ldots
$$

with $\epsilon_{i}{ }^{\prime}$ s that are i.i.d. normal with mean 0 and standard deviation $\sigma^{*}$. The $\mathrm{R}$ function "Vasicek. Euler.sim" in the "InterestCalibration" library implements this method. The following code snippet demonstrates use of "Vasicek.Euler.sim."

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-13.jpg?height=297&width=1094&top_left_y=921&top_left_x=319)

## Simulated Vasicek paths (Euler Method)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-13.jpg?height=705&width=1070&top_left_y=1412&top_left_x=514)

### 2.1.2 SIMULATING PATHS OF THE VASICEK MODEL: TRANSITION DENSITY METHOD

The transition density method of simulating interest rate paths relies on the fact that the simulation can be carried out using the distribution of next observation $r_{t+s}$ at $t+s$ given observation $r_{t}$ at time $t$. This method is introduced by [11]. This is an exact method of simulation as opposed to the Euler-Maruyama scheme which relies on discretizing an SDE. Since $r_{t+s} \mid r_{t}$ is normal with mean and variance as given in (2) and (3) respectively, the realized value of $r_{t+s}$ is calculated from:

$$
r_{t+s}=\bar{r}+\left(r_{t}-\bar{r}\right) e^{-\gamma s}\left(\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma s}\right)\right)^{\frac{1}{2}} Z
$$

where $\mathrm{Z}$ is a standard normal random number. By writing:

$$
\begin{aligned}
r(0) & =r_{0} \\
r(i) & =r_{i \Delta}, \quad i=1,2, \ldots
\end{aligned}
$$

We can obtain:

$$
r(i)=\alpha^{*}+\beta^{*} r(i-1)+\epsilon_{i}, \quad i=1,2, \ldots
$$

where:

$$
\begin{aligned}
\alpha^{*} & =(1-\exp (-\gamma \Delta)) \bar{r} \\
\beta^{*} & =\exp (-\gamma \Delta) \\
\sigma^{* *} & =\sqrt{\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma \Delta}\right)}
\end{aligned}
$$

with $\epsilon_{i}{ }^{\prime}$ s that are i.i.d. normal with mean 0 and standard deviation $\sigma^{* *}$. The R function "Vasicek.Trans.sim" in the "InterestCalibration" library implements this method. The following code snippet demonstrates use of "Vasicek.Trans.sim."

## \#example3

rm(list=Is()) \# clear the workspace and functions

set.seed(123)

$\mathrm{X}$ =Vasicek.Trans. $\operatorname{sim}$ (Delta=1/252,M=10)

matplot(X,type="I",main="Simulated Vasicek paths (Transition Density Method)",

ylab="Short rate",xlab="Time Step in days")

## Simulated Vasicek paths (Transition Density Method)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-14.jpg?height=636&width=1068&top_left_y=1807&top_left_x=496)

### 2.2 COX-INGERSOLL-ROSS (CIR) MODEL

The SDE describing the CIR model is as follows:

$$
d r_{t}=\gamma\left(\bar{r}-r_{t}\right) d t+\sqrt{\alpha r_{t}} d X_{t}
$$

This model is also a mean reverting model and the parameters $\gamma$ and $\bar{r}$ have the same interpretation as in the Vasicek model. One advantage of this model over the Vasicek model is that when $\gamma \bar{r}>\frac{\alpha}{2}$ the rates are always non-negative. This model was introduced in [13] and [10] used it for modelling interest rates.

With some difficult mathematics one can show that the transition density function of $r_{t+s}$ conditioned on $r_{t}$ is given by:

$$
f\left(r_{t+s} \mid r_{t}\right)=c_{s} \chi^{2}\left(c_{s} r_{t+s}, v, \lambda_{t+s}\right)
$$

where $\chi^{2}\left(., v, \lambda_{t+s}\right)$ is a non-central $\chi^{2}$ density function with $v$ degrees of freedom and non-centrality parameter $\lambda_{t+s}$, with:

$$
\begin{aligned}
c_{s} & =\frac{4 \gamma}{\alpha(1-\exp (-\gamma s))} \\
\nu & =\frac{4 \gamma}{\alpha} \bar{r} \\
\lambda_{t+s} & =c_{s} r_{t} \exp (-\gamma s)
\end{aligned}
$$

A relatively easy way to visualize a characterization of the non-central $\chi^{2}$ random variable with an integervalued degrees of freedom parameter (i.e. $v$ is an integer) is that it can be obtained by summing up squares of $v$ independent normal random variables with non-zero means and unit variances. However, in our case $v$ may not be an integer.

Another characterization of the non-central $\chi^{2}$ distributions is that they can be represented as a mixture of Poisson and central $\chi^{2}$ distributions. As given on page 436 in [18], we can write the cdf, $F(x ; v, \lambda)$, of a non-central $\chi^{2}$ with degrees of freedom $v$ and non-central parameter $\lambda$ as:

$$
F(x ; \nu, \lambda)=\sum_{j=0}^{\infty}\left[\frac{\left(\frac{\lambda}{2}\right)^{j}}{j !} \exp (-\lambda / 2)\right] F(x ; \nu+2 j, 0)
$$

Although the above expression involves an infinite sum, it leads to easy generation of random numbers from a non-central $\chi^{2}$. It involves first generating a random number $J$ from a Poisson distribution with mean $\lambda / 2$ and then generating a random number from a central $\chi^{2}$ with degrees of freedom $v+2 J$; this random number will be from the non-central $\chi^{2}$.

### 2.2.1 SIMULATING PATHS OF THE CIR MODEL: EULER-MARUYAMA DISCRETIZATION

As in the Vasicek case we can discretize the SDE in the following manner:

$$
\begin{aligned}
d r_{t} & =\gamma\left(\bar{r}-r_{t}\right) d t+\sqrt{\alpha r_{t}} d X_{t} \\
r_{t+\Delta}-r_{t} & =\gamma\left(\bar{r}-r_{t}\right) \Delta+\sqrt{r_{t}} \epsilon_{t+\Delta}
\end{aligned}
$$

where $\epsilon_{t+\Delta}$ is a normal random variable with mean 0 and variance $\alpha \Delta$.

As in the Vasicek model we can further simplify and obtain:

$$
r(i)=\alpha_{1}+\beta_{1} r(i-1)+\sqrt{r(i-1)} \epsilon_{i}, i=1,2, \ldots
$$

where:

$$
\begin{aligned}
r(0) & =r_{0} \\
r(i) & =r_{i \Delta}, \quad \epsilon_{i}=\epsilon_{i \Delta}, \quad i=1,2, \ldots \\
\alpha_{1} & =\gamma \bar{r} \Delta \\
\beta_{1} & =1-\gamma \Delta \\
\sigma & =\sqrt{\alpha \Delta}
\end{aligned}
$$

with $\epsilon_{i}$ 's that are i.i.d. normal with mean 0 and standard deviation $\sigma$. The $\mathrm{R}$ function "CIR.Euler.sim" in the "InterestCalibration" library implements this method. The following R-code snippet illustrates the usage of "CIR.Euler.sim."

## \#example4

rm(list=Is()) \# clear the workspace and functions

set.seed(123)

$\mathrm{X}=\mathrm{CIR}$. Euler.sim(Delta=1/500, $\mathrm{M}=10$ )

matplot(X,type="I",main="Simulated CIR paths (Euler Method)",

ylab="Short rate",xlab="Time Step in days")

abline $(0,0)$

## Simulated CIR paths (Euler Method)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-16.jpg?height=577&width=984&top_left_y=1495&top_left_x=451)

As we can see from the graph, the Euler-Maruyama discretization method leads to negative values for $r_{t}$ which is theoretically impossible. Note that we can calculate the probability of $r(i)$ becoming negative conditioned on $r(i-1)$ for $i=1,2, \ldots$ as given below:

$$
\begin{aligned}
E[r(i) \mid r(i-1)] & =\alpha_{1}+\beta_{1} r(i-1) \\
\operatorname{Var}[r(i) \mid r(i-1)] & =\operatorname{Var}\left[\sqrt{r(i-1)} \epsilon_{i}\right] \\
& =r(i-1) \sigma^{2}=r(i-1) \alpha \Delta
\end{aligned}
$$

Under the Euler-Maryuma scheme the conditional distribution of $r(i)$ conditioned on $r(i-1)$ is normal with mean $E[r(i) \mid r(i-1)]$ and variance $\operatorname{Var}[r(i) \mid r(i-1)]$, the probability of $r(i)$ becoming negative conditioned on $r(i-1)$ is:

$$
\begin{aligned}
P[r(i)<0 \mid r(i-1)] & =\Phi\left(-\frac{E[r(i) \mid(r(i-1))]}{\sqrt{\operatorname{Var}[r(i) \mid(i-1)]}}\right) \\
& =\Phi\left(-\frac{\alpha_{1}+\beta_{1} r(i-1)}{\sqrt{r(i-1) \sigma^{2}}}\right)
\end{aligned}
$$

For example, the set of values $(r(i)=0.2 \%, \bar{r}=7 \%, \gamma=0.3262, \alpha=0.0221, \Delta=1 / 252$ ) will yield $P[r(i)<0 \mid r(i-1)]=0.00108$. Therefore, the Euler-Maruyama method should be used with caution, though it does have the appeal of simplicity.

### 2.2.2 SIMULATING PATHS OF THE CIR MODEL: TRANSITION DENSITY METHOD

From the discussion above the conditional distribution of $\frac{r_{t+s}}{c_{s}}$, conditioned on $r_{s}$, is distributed as a noncentral $\chi^{2}$ with degrees of freedom $v=\frac{4 \gamma}{\alpha} \bar{r}$ and non-centrality parameter $\lambda_{t+s}=c_{s} r_{t} \exp (-\gamma s)$. The algorithm uses $r_{t}$ 's value to generate $r_{t+s}$. Since we use $s=\Delta$, a constant value, at each step the noncentrality parameter $\lambda_{i \Delta}=c_{\Delta} r_{i \Delta} \exp (-\Delta)$ has to be evaluated using $r_{(i-1) \Delta}$ before calculating $r_{\mathrm{i} \Delta}$ for $i=$ $1,2, \ldots$.

The R function "CIR.Trans.sim" in the "InterestCalibration" library implements this method. The following Rcode snippet illustrates the usage of "CIR.Trans.sim."

## \#example5

rm(list=Is()) \# clear the workspace and functions

set.seed(123)

$\mathrm{X}=\mathrm{CIR}$.Trans.sim(Delta=1/252,M=10)

matplot(X,type="I",main="Simulated CIR paths (Transition Density Method)",

ylab="Short rate",xlab="Time Step in days")

abline $(0,0)$

## Simulated CIR paths (Transition Density Method)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-17.jpg?height=583&width=984&top_left_y=1858&top_left_x=554)

In the implementation we assumed that the non-central $\chi^{2}$ random number generation function " $r$ chisq" works perfectly. However, "rchisq" uses the mixture of Poisson and central $\chi^{2}$ characterization given in (6) to generate random numbers. The method is simple and straightforward but "Simulation of Square-root Processes" in [9] lists many drawbacks of this method and for practical applications one may use a method given in [12] and [2] to simulate non-central $\chi^{2}$ random numbers.

### 2.3 THE TWO-FACTOR VASICEK MODEL WITH CORRELATED FACTORS

This model can be written as the short rate process as of the sum of two factors, a short rate factor and a long rate factor:

$$
r_{t}=\phi_{1, t}+\phi_{2, t}
$$

Where each factor follows the following SDEs:

$$
\begin{aligned}
d \phi_{i, t} & =\gamma_{i}\left(\vec{\phi}_{i}-\phi_{i, t}\right) d t+\sigma_{i} d X_{i, t}, \quad i=1,2, \\
d X_{1, t} d X_{2, t} & =\rho d t
\end{aligned}
$$

With a few lines of algebra we can obtain the solution of these SDEs as follows:

$$
\phi_{i, t+s}=\phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right)+\sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}, \quad i=1,2
$$

The conditional means and variance of these two factors are given by:

$$
\begin{aligned}
E\left[\phi_{i, t+s} \mid \phi_{i, t}\right] & =\phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right), i=, 1,2 \\
\operatorname{Var}\left[\phi_{i, t+s} \mid \phi_{i, t}\right] & =\operatorname{Var}\left[\sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}\right] \\
& =\sigma_{i}^{2} \exp \left(-2 \gamma_{i} s\right) \operatorname{Var}\left[\int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}\right] \\
& =\sigma_{i}^{2} \exp \left(-2 \gamma_{i} s\right) \int_{0}^{s} \exp \left(2 \gamma_{i} v\right) d v \\
& =\frac{\sigma_{i}^{2}}{2 \gamma_{i}}\left(1-\exp \left(-2 \gamma_{i} s\right)\right), i=1,2
\end{aligned}
$$

Where the second to last equation follows from Itô's isometry. The conditional covariance between $\phi_{1, t+s}$ and $\phi_{2, t+s}$ conditioned on $\phi_{i, t}, i=1,2$ is given by:

$$
\begin{aligned}
\operatorname{Cov}\left[\phi_{1, t+s}, \phi_{2, t+s} \mid \phi_{1, t}, \phi_{1, t}\right] & =E\left[\sigma_{1} \exp \left(-\gamma_{1} s\right) \int_{0}^{s} \exp \left(\gamma_{1} v\right) d X_{1, v} \sigma_{2} \exp \left(-\gamma_{2} s\right) \int_{0}^{s} \exp \left(\gamma_{2} u\right) d X_{2, u}\right] \\
& =\rho \sigma_{1} \sigma_{2} \exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right) \int_{0}^{s} \exp \left(-\left(\gamma_{1}+\gamma_{2}\right) v\right) d v \\
& =\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)
\end{aligned}
$$

The conditional correlation coefficient between $\phi_{1, t+s}$ and $\phi_{2, t+s}$, which can be denoted as $\rho(s)$, is given by:

$$
\begin{aligned}
\operatorname{Corr}\left[\phi_{1, t+s}, \phi_{2, t+s} \mid \phi_{1, t}, \phi_{1, t}\right] & =\frac{\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)}{\sqrt{\frac{\sigma_{1}^{2}}{2 \gamma_{1}}\left(1-\exp \left(-2 \gamma_{1} s\right)\right) \frac{\sigma_{2}^{2}}{2 \gamma_{2}}\left(1-\exp \left(-2 \gamma_{2} s\right)\right)}} \\
\rho(s) & =\rho\left(\frac{4 \gamma_{1} \gamma_{2}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)^{2}}{\left(\gamma_{1}+\gamma_{2}\right)^{2}\left(1-\exp \left(-2 \gamma_{1} s\right)\right)\left(1-\exp \left(-2 \gamma_{2} s\right)\right)}\right)^{\frac{1}{2}}
\end{aligned}
$$

### 2.3.1 SIMULATING PATHS OF THE TWO-FACTOR VASICEK MODEL: TRANSITION DENSITY METHOD

When simulating paths we need to simulate each factor separately and add them together. We can use the transition density method for each factor. It works as follows:

- Choose initial short term rate $r_{0}$ and initial long term rate $r_{0}(\tau)$ for a suitable value of $\tau$.
- $\quad$ Solve the following two equations for $\phi_{1,0}$ and $\phi_{2,0}$ :

$$
\begin{aligned}
\phi_{1,0}+\phi_{2,0} & =r_{0} \\
A(\tau)-B_{1}(\tau) \phi_{1,0}-B_{2}(\tau) \phi_{2,0} & =-r_{0}(\tau) \tau
\end{aligned}
$$

The above two equations can be solved to obtain the following:

$$
\begin{aligned}
\phi_{1,0} & =\frac{B_{2}(\tau) r 0-\tau r_{0}(\tau)-A(\tau)}{B_{2}(\tau)-B_{1}(\tau)} \\
\phi_{2,0} & =\frac{\tau r_{0}(\tau)+A(\tau)-B_{1}(\tau) r_{0}}{B_{2}(\tau)-B_{1}(\tau)}
\end{aligned}
$$

- $\quad$ Simulate standard bivariate normal random number $\left(Z_{1}, Z_{2}\right)$ with correlation coefficient $\rho(s)$.

Note that this can be achieved by simulating two independent random numbers, $x_{1}$ and $x_{2}$, from a standard normal distribution and then setting:

$$
\begin{aligned}
Z_{1} & =x_{1} \\
Z_{2} & =\rho(s) x_{1}+\sqrt{1-\rho(s)^{2}} x_{2}
\end{aligned}
$$

- Set:

$$
\begin{aligned}
\phi_{i, t+s} & =\phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right)+\sqrt{\frac{\sigma_{i}^{2}}{2 \gamma_{i}}\left(1-\exp \left(-2 \gamma_{i} s\right)\right)} Z_{i}, i=1,2, \\
r_{t+s} & =\phi_{1, t+s}+\phi_{2, t+s}
\end{aligned}
$$

The R function "Two.factor.Vasicek.Trans.sim" in the "InterestCalibration" library implements this method. The following code snippet demonstrates use of "Two.factor.Vasicek.Trans.sim".

## \#example6

rm(list=Is()) \# clear the workspace and functions

set.seed(123)

X =Two.factor.Vasicek.Trans.sim(Delta=1/252,M=10)

matplot(X,type="I",main="Simulated two factor Vasicek paths", ylab="Short rate",xlab="Time Step in days")

## Simulated two factor Vasicek paths

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-20.jpg?height=591&width=987&top_left_y=347&top_left_x=428)

## 3 Calibration Techniques

In this section we provide calibrations of the Vasicek models and the CIR model. We look at real-world calibration for the Vasicek model and CIR model followed by risk-neutral calibration for the Vasicek model, the CIR model and for the two-factor Vasicek model. For real-world calibration the maximum likelihood estimation (MLE) technique is frequently used. MLE solves for parameters that maximize a likelihood function. This function is the probability distribution function of the parameters. MLE finds the parameters with the highest likelihood of generating the observed data from a statistical distribution assumed to fit the underlying data. However, as we shall see the parameter estimates have some bias.

Since the MLE parameters are estimates of the underlying data distribution's parameters, the parameters found by MLE are random variables with distributions and moments such as a mean. This means the accuracy of the estimated parameters may be estimated and evaluated for goodness of fit.

The MLE method has several drawbacks that limit its usefulness for interest rate models. First, it fits parameters to a data sample from a statistical distribution chosen by the modeler but provides no information on whether that model is a reasonable fit to the "true" underlying distribution. This means the assumed statistical distribution may be statistically biased, with a mean significantly different than the underlying "true" distribution of the data. MLE relies on asymptotic properties of large datasets which may not hold for interest rate models. A small sample of short rates may not produce convergent parameters, while extending the data farther back in time brings in interest rates from different economic and policy environments (say, pre-global financial crisis) that may not be applicable for models projecting into the future. MLE assumes the data is stationary. Short rates may appear stationary for a period of time due to government monetary policy, but may exhibit a drift or jump when such policies change. This drift could be due to a set of complex macroeconomic interactions of economic cycles, fiscal and monetary policy, or shocks due to extreme weather, climate, pandemic, or demographic changes.

### 3.1 THE VASICEK MODEL: REAL-WORLD CALIBRATION

In this section we look at calibrating a Vasicek model with real-world (equilibrium model) data. We assume that a random sample of short rate data $r_{0}, r_{\Delta}, r_{2 \Delta}, \ldots, r_{n \Delta}$, perhaps overnight rates observed over five years, is available to us. For simplicity we have assumed rates are observed at consecutive times with
equidistant periods. In this section we discuss two calibration techniques for the Vasicek model: maximum likelihood estimates and long-term quantile method.

### 3.1.1 MAXIMUM LIKELIHOOD ESTIMATOR METHOD

We have shown that the transition density function $f\left(r_{t+s} \mid r_{t}\right)$ is normal with the following means and variances:

$$
\begin{aligned}
E\left[r_{t+s} \mid r_{t}\right] & =\bar{r}+\left(r_{t}-\bar{r}\right) e^{-\gamma s} \\
\operatorname{Var}\left[r_{t+\mid s} \mid r_{t}\right] & =\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma s}\right)
\end{aligned}
$$

For notational simplicity let us define the following variables as defined in the introductory section:

$$
\begin{aligned}
\alpha^{*} & =(1-\exp (-\gamma \Delta)) \bar{r} \\
\beta^{*} & =\exp (-\gamma \Delta) \\
\sigma^{*} & =\sqrt{\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma \Delta}\right)}
\end{aligned}
$$

Then we can write:

$$
\begin{aligned}
E\left[r_{i \Delta} \mid r_{(i-1) \Delta}\right] & =\alpha^{*}+\beta^{*} r_{(i-1) \Delta}, \\
\operatorname{Var}\left[r_{i \Delta} \mid r_{(i-1) \Delta}\right] & =\sigma^{* 2}, \quad i=1,2, \ldots, n
\end{aligned}
$$

The density function, $f\left(r_{i \Delta} \mid r_{(i-1) \Delta}\right)$, of the conditional random variable $r_{i \Delta} \mid r_{(i-1) \Delta}$ for $i=1,2, \ldots, n$ can be written as:

$$
f\left(r_{i \Delta} \mid r_{(i-1) \Delta}\right)=\frac{1}{\sqrt{2 \pi} \sigma^{*}} \exp \left(-\frac{\left(r_{i \Delta}-\alpha^{*}-\beta^{*} r_{(i-1) \Delta}\right)^{2}}{2 \sigma^{* 2}}\right)
$$

Now it remains to specify the density function of the random variable $r_{0}$. The literature is not quite clear about how to specify it, therefore we denote it as $f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)$ without specifying its functional form. With this notation we can write the joint likelihood function of the random sample $r_{0}, r_{\Delta}, r_{2 \Delta}, \ldots, r_{n \Delta}$ as:

$$
\begin{aligned}
\mathscr{L} & =f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right) \prod_{i=1}^{n} f\left(r_{i \Delta} \mid r_{(i-1) \Delta}\right) \\
\mathscr{L} & =f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right) \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma^{*}} \exp \left(-\frac{\left(r_{i \Delta}-\alpha^{*}-\beta^{*} r_{(i-1) \Delta}\right)^{2}}{2 \sigma^{* 2}}\right) \\
& =f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right) \frac{1}{\sqrt{(2 \pi)^{n}} \sigma^{* n}} \exp \left(-\sum_{i=1}^{n} \frac{\left(r_{i \Delta}-\alpha^{*}-\beta^{*} r_{(i-1) \Delta}\right)^{2}}{2 \sigma^{* 2}}\right)
\end{aligned}
$$

Then the log-likelihood function becomes:

$$
\begin{aligned}
\ln (\mathscr{L})= & \ln \left(f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)\right)- \\
& \ln \left(\sqrt{(2 \pi)^{n}}\right)-n \ln \left(\sigma^{*}\right)-\sum_{i=1}^{n} \frac{\left(r_{i \Delta}-\alpha^{*}-\beta^{*} r_{(i-1) \Delta}\right)^{2}}{2 \sigma^{* 2}}
\end{aligned}
$$

Before we maximize $\ln (\mathcal{L})$, we need to specify the function $f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)$. If $\mathrm{n}$ is sufficiently large we could ignore the contribution of $f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)$ into the $\ln (\mathcal{L})$ and proceed. This method is called the quasi-maximum likelihood method. In this situation maximization is straightforward and we can obtain the following explicit expressions for estimates:

$$
\begin{aligned}
\hat{\beta}^{*} & =\frac{\sum_{i=1}^{n} r_{i \Delta} r_{(i-1) \Delta}-\frac{1}{n} \sum_{i=0}^{n-1} r_{i \Delta} \sum_{i=1}^{n} r_{i \Delta}}{\sum_{i=0}^{n-1} r_{i \Delta}^{2}-\frac{1}{n}\left(\sum_{i=0}^{n-1} r_{i \Delta}\right)^{2}} \\
\hat{\alpha}^{*} & =\frac{1}{n}\left(\sum_{i=1}^{n} r_{i \Delta}-\hat{\beta} \sum_{i=0}^{n-1} r_{i \Delta}\right) \\
\hat{\sigma}^{* 2} & =\frac{1}{n-2} \sum_{i=1}^{n}\left(r_{i \Delta}-\hat{\alpha}-\hat{\beta} r_{(i-1) \Delta}\right)^{2}
\end{aligned}
$$

Note that $\hat{\sigma}^{* 2}$ is the unbiased estimator for $\sigma^{* 2}$, not the MLE. Once we have these estimates we solve for $\gamma, \bar{r}$ and $\sigma$ using the following formulas:

$$
\begin{aligned}
\gamma & =-\frac{\ln \left(\hat{\beta}^{*}\right)}{\Delta} \\
\bar{r} & =\frac{\hat{\alpha}^{*}}{1-\hat{\beta}^{*}} \\
\sigma & =\sqrt{\frac{2 \hat{\gamma} \hat{\sigma}^{* 2}}{1-\hat{\beta}^{* 2}}}
\end{aligned}
$$

The implementation of this in R is straightforward as we can use R function "Im" for estimation. We illustrate the MLE calculation using the data in chapter 14, exercise Q5 of [24], as discussed in Section 5.2 and 5.3 below.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-22.jpg?height=756&width=946&top_left_y=1491&top_left_x=320)

The MLE's of $\gamma, \bar{r}$ and $\sigma$ are 3.64532, 0.30769 and 1.81376, respectively. The ANOVA table related to this calibration is:

|  | Df | Sum Sq | Mean Sq | F value | p-value |
| :--- | ---: | ---: | ---: | ---: | ---: |
| $\mathrm{x}$ | 1 | 376.303 | 376.303 | 29245 | 0 |
| Residuals | 541 | 6.961 | 0.013 | $\mathrm{NA}$ | $\mathrm{NA}$ |

To examine the performance of the MLE we carry out a simulation study using the R code snippet given below.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-23.jpg?height=1507&width=1003&top_left_y=646&top_left_x=319)

Simulation performance based on 1000 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\sigma$ |
| Bias | 0.50238 | -0.00267 | $1.58447 \times 10^{-5}$ |
| Standard <br> deviation | 0.50194 | 0.05453 | $3.03235 \times 10^{-4}$ |
| Root mean <br> square | 0.70999 | 0.05457 | $3.03497 \times 10^{-4}$ |

From the table we observe that MLE of $\sigma$ performs very well, $\bar{r}$ performs somewhat better, and $\gamma$ performs poorly. This is consistent with the results of [21] and readers are encouraged to explore this by changing the simulation specifications.

Instead of dropping the term $f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)$ from the likelihood function, we could assume that $r_{0}$ is normally distributed with:

$$
\begin{aligned}
E\left[r_{0}\right] & =\frac{\alpha^{*}}{1-\beta^{*}} \\
\operatorname{Var}\left[r_{0}\right] & =\frac{\sigma^{* 2}}{1-\beta^{* 2}}
\end{aligned}
$$

This choice seems reasonable and since $\gamma>0, \beta^{*}<1$ the pdf in this case becomes:

$$
f_{0}\left(r_{0} \mid \alpha^{*}, \beta^{*}, \sigma^{*}\right)=\frac{1}{\sqrt{2 \pi \sigma^{* 2} /\left(1-\beta^{* 2}\right)}} \exp \left[-\frac{\left(r_{0}-\left[\alpha^{*} /\left(1-\beta^{*}\right)\right]\right)^{2}}{2 \sigma^{* 2} /\left(1-\beta^{* 2}\right)}\right]
$$

Substituting this in (7) we obtain the following as the log-likelihood function:

$$
\begin{aligned}
\ln (\mathscr{L})= & -\frac{1}{2} \ln (2 \pi)-\frac{1}{2} \ln \left(2 \sigma^{* 2} /\left(1-\beta^{* 2}\right)\right)-\frac{\left(r_{0}-\left[\alpha^{*} /\left(1-\beta^{*}\right)\right]\right)^{2}}{2 \sigma^{* 2} /\left(1-\beta^{* 2}\right)} \\
& -\ln \left(\sqrt{(2 \pi)^{n}}\right)-n \ln \left(\sigma^{*}\right)-\sum_{i=1}^{n} \frac{\left(r_{i \Delta}-\alpha^{*}-\beta^{*} r_{(i-1) \Delta}\right)^{2}}{2 \sigma^{* 2}}
\end{aligned}
$$

When we compare this log-likelihood function with the log-likelihood function given in equation (5.2.9) on page 119 in [15], we see that (8) is in fact the log-likelihood function of an AR(1) model. Now it should become clear to the reader why this pdf for $r_{0}$ was chosen. For parameter estimation we could use $\mathrm{R}$ function ARIMA as illustrated in the code below.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-24.jpg?height=433&width=589&top_left_y=2059&top_left_x=320)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-25.jpg?height=1223&width=1068&top_left_y=262&top_left_x=319)

Simuation performance based on 1000 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\sigma$ |
| Bias | 0.49128 | -0.00672 | $8.54594 \times 10^{-6}$ |
| Standard <br> deviation | 0.47409 | 0.01674 | $3.03163 \times 10^{-4}$ |
| Root mean <br> square | 0.68256 | 0.01803 | $3.03132 \times 10^{-4}$ |

We observe that the performance of MLEs are quite similar to that of MLEs based on a quasi-likelihood function.

### 3.1.2 LONG TERM QUANTILE METHOD

This method is proposed in [5]. The major underlying assumption in this method is that sample quantiles are representative of the future observed quantiles. The second mathematically justifiable assumption is that theoretical quantiles are calculated based on the process behaviour when $t \rightarrow \infty$. The calculation of the longterm mean and variance of $r_{t}$ is as follows:

$$
\begin{aligned}
E\left[r_{t} \mid r_{0}\right] & =\bar{r}+\left(r_{0}-\bar{r}\right) e^{-\gamma t} \\
\lim _{t \rightarrow \infty} E\left[r_{t} \mid r_{0}\right] & =\bar{r} \\
\operatorname{Var}\left[r_{t} \mid r_{0}\right] & =\frac{\sigma^{2}}{2 \gamma}\left(1-e^{-2 \gamma t}\right) \\
\lim _{t \rightarrow \infty} \operatorname{Var}\left[r_{t} \mid r_{0}\right] & =\frac{\sigma^{2}}{2 \gamma}
\end{aligned}
$$

As $r_{t}$ 's are normally distributed random variables the $95 \%$ confidence interval for $\lim _{t \rightarrow \infty} r_{t}$ is given by:

$$
P\left[\bar{r}-\frac{1.96 \sigma}{\sqrt{2 \gamma}} \leq \lim _{t \rightarrow \infty} r_{t} \leq \bar{r}+\frac{1.96 \sigma}{\sqrt{2 \gamma}}\right]=0.95
$$

Let us denote $\hat{q}_{0.025}$ and $\hat{q}_{0.975}$ as the 2.5 th and the 97.5 th percentiles respectively, based on a sample of $r_{t}$ where preferably $t>10$. Then we have the following two equations:

$$
\begin{aligned}
& \hat{q}_{0.025}=\bar{r}-\frac{1.96 \sigma}{\sqrt{2 \gamma}} \\
& \hat{q}_{0.975}=\bar{r}+\frac{1.96 \sigma}{\sqrt{2 \gamma}}
\end{aligned}
$$

We can solve these two equations to obtain the following expressions for $\gamma$ and $\bar{r}$ :

$$
\begin{gathered}
\gamma=2\left(\frac{1.96 \sigma}{\hat{q}_{0.975}-\hat{q}_{0.025}}\right)^{2} \\
\bar{r}=\frac{\hat{q}_{0.025}+\hat{q}_{0.975}}{2}
\end{gathered}
$$

This procedure is easy to implement as given in the $\mathrm{R}$ code snippet below, but the drawback is obtaining a sample of $r_{t}$ for a large value of $t$.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-26.jpg?height=857&width=1135&top_left_y=1689&top_left_x=319)

The resulting estimates of $\gamma$ and $\bar{r}$ are 0.28199 and 0.05267 respectively.

### 3.2 THE VASICEK MODEL: RISK-NEUTRAL CALIBRATION

In this section we present calibration of a Vasicek model when we have a set of zero-coupon bond prices or a set of discount factors. The underlying assumption is that the real-world interest rate follows a Vasicek model and hence we can use a drift-adjusted Vasicek model that leads to the following closed-form formula for zero coupon bond prices.

$$
\begin{array}{ll}
{[24](15.28)} & Z(r, t ; T)=e^{A(t ; T)-B(t ; T) r} \\
{[24](15.29)} & B(t ; T)=\frac{1}{\gamma^{*}}\left(1-e^{-\gamma^{*}(T-t)}\right) \\
{[24](15.30)} & A(t ; T)=(B(t ; T)-(T-t))\left(\bar{r}^{*}-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\right)-\frac{\sigma^{2} B(t ; T)^{2}}{4 \gamma^{*}}
\end{array}
$$

Note that we are using parameters $\gamma^{*}$ and $\bar{r}^{*}$ to indicate the drift of the SDE for $r_{t}, \gamma^{*}\left(\bar{r}^{*}-r_{t}\right)$ in the riskneutral world, as opposed to parameters $\gamma$ and $\bar{r}$ with a drift of $\gamma\left(\bar{r}-r_{t}\right)$ in the real-world.

The calibration process involves minimizing the following quantity:

$$
J\left(\gamma^{*}, \bar{r}^{*}\right)=\sum_{i=1}^{n}\left(Z^{\text {Vasicek }}\left(r_{0}, 0 ; T_{i}\right)-Z^{\text {Data }}\left(0, T_{i}\right)\right)^{2}
$$

We can use either the "nlm" function or the "optim" function for this purpose. The following example first calculates a bond price vector for given maturities with known parameter values and then calculates parameters using the minimization. It is used as a verification of our code for the minimization.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-27.jpg?height=524&width=1145&top_left_y=1453&top_left_x=321)

Risk-neutral Parameter Estimates

| Method | Parameter |  |
| :--- | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ |
| nlm | 0.49999 | 0.07 |
| optim | 0.49951 | 0.07002 |

Readers are encouraged to try various values for parameters $\gamma^{*}$ and $\bar{r}^{*}$ and various reasonable guesses for initial values of those parameters to test the accuracy of the " $\mathrm{nlm}^{\mathrm{m}}$ and the "optim" routines.

Another option we may consider is if we do not have a reliable estimate for $\sigma$ we could also estimate it from observed bond price data as described in the following code snippets.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-28.jpg?height=569&width=1154&top_left_y=388&top_left_x=320)

Risk-neutral Parameter Estimates

| Method | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ | $\sigma$ |
| nlm | 0.43033 | 0.0802 | 0.06206 |
| optim | 0.41491 | 0.08264 | 0.06617 |

After trying out a few different initial values and increasing the maximum number of iterations in " $\mathrm{nlm}$ " we see that "nlm" produces values close to the actual values, but values produced by "optim" are not very close. This led to examination of other optimization methods available in R. Instead of writing our own function to minimize we can use the "nls" package for non-linear least squares minimization. Readers who may want to know more about non-linear regression with $\mathrm{R}$ may consult [22].

We realized using "nls" for yield rates instead of bond prices yields better results. The following code snippet illustrates usage of "nls" with bond yields.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-28.jpg?height=832&width=1027&top_left_y=1687&top_left_x=320)

The "nls" algorithm converged in 9 iterations and summary statistics are:

The Vasicek fit (simulated data):summary statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.5 | $3.53356 \times 10^{-10}$ | $1.41501 \times 10^{9}$ | $7.11346 \times 10^{-155}$ |
| $\bar{r}^{*}$ | 0.07 | $1.4747 \times 10^{-11}$ | $4.74673 \times 10^{9}$ | $2.45829 \times 10^{-164}$ |

We can also try to estimate $\sigma$ using bond yield data with "nls" as given below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-29.jpg?height=811&width=1026&top_left_y=666&top_left_x=322)

The "nls" algorithm converged in 35 iterations and summary statistics are:

The Vasicek fit (simulated data):summary statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.5 | $3.74357 \times 10^{-9}$ | $1.33562 \times 10^{8}$ | $4.00432 \times 10^{-129}$ |
| $\bar{r}^{*}$ | 0.07 | $4.70173 \times 10^{-10}$ | $1.48881 \times 10^{8}$ | $6.32221 \times 10^{-130}$ |
| $\sigma$ | 0.02 | $5.20598 \times 10^{-9}$ | $3.84174 \times 10^{6}$ | $6.34129 \times 10^{-103}$ |

We can also add a random error to simulated bond yields to evaluate the performance.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-29.jpg?height=574&width=1132&top_left_y=1968&top_left_x=319)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-30.jpg?height=291&width=986&top_left_y=263&top_left_x=324)

The "nls" algorithm converged in 10 iterations and summary statistics are:

The Vasicek fit (simulated data):summary statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.47522 | 0.02492 | 19.06995 | $2.18791 \times 10^{-13}$ |
| $\bar{r}^{*}$ | 0.07148 | 0.00116 | 61.55485 | $2.19487 \times 10^{-22}$ |

We can try estimating $\sigma$ from the same data set with a random error added to the yields:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-30.jpg?height=847&width=1011&top_left_y=972&top_left_x=320)

The "nls" algorithm converged in 44 iterations and summary statistics are:

The Vasicek fit (simulated data):summary statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.37994 | 2.10799 | 0.18024 | 0.8591 |
| $\bar{r}^{*}$ | 0.08849 | 0.37455 | 0.23625 | 0.81606 |
| $\sigma$ | 0.07293 | 0.31051 | 0.23488 | 0.81711 |

We see that when there is a random error, the estimate of $\sigma$ is not close to the actual value. Irrespective of what the results are, it is not a good practice to estimate $\sigma$ from the same data set; it has to be estimated from short rate volatility under a real life scenario.

We encourage readers to try different parameters and different initial values for all three methods using "optim", "nlm" and "nls". Based on our limited testing presented here for real applications, we recommend
using " $n \mid s$ " and trying out many different initial values and increasing number of iterations, before settling into one solution.

In the following code chunk we use data in Table 15.1 of [24].

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-31.jpg?height=1100&width=1211&top_left_y=457&top_left_x=319)

Risk-neutral Parameter Estimates

| Method | Parameter |  |
| :--- | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ |
| Text | 0.46530 | 0.06340 |
| nlm | 0.46509 | 0.06344 |
| optim | 0.40785 | 0.06615 |
| nls | 0.36455 | 0.06899 |

We see that values produced by " $\mathrm{nlm}$ " are close to the values given in Example 15.1 of [24]. The following is a summary statistics of the "nls" method, which converged after 7 iterations.

The Vasicek fit (simulated data):summary statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.36455 | 0.0406 | 8.97929 | $1.89865 \times 10^{-9}$ |
| $\bar{r}^{*}$ | 0.06899 | 0.00318 | 21.67434 | $3.60621 \times 10^{-18}$ |

To understand which optimization routine performs better we plot the fitted data along with market data and textbook estimates:

## \#example18

optim.yield $=$ Vasicek.yield $(\mathrm{r} 0=0.0168, \mathrm{t}=0, \mathrm{~T}=$ bond. . maturities,

gamma=model\$estimate[1],rbar=model\$estimate[2],

sigma $=0.0222$ )

nIm.yield $=$ Vasicek.yield( $\mathrm{r} 0=0.0168, \mathrm{t}=0, \mathrm{~T}=$ bond. maturities, gamma=model1\$par[1],rbar=model1\$par[2], sigma $=0.0222$ )

text.yield $=$ Vasicek.yield $(\mathrm{r} 0=0.0168, \mathrm{t}=0, \mathrm{~T}=$ bond. maturities, gamma $=0.4653$, rbar $=0.0634$, sigma $=0.0222$ )

plot(bond.maturities,bond.yields*100,xlab="Maturities",ylab="Yield(\%)", type="b",pch=10,lty="solid",col="red1")

lines(bond.maturities,fitted(Vasicek.fit)*100,type="b",pch=20,Ity="solid",

col="rosybrown")

lines(bond.maturities,optim.yield*100,type="b", pch=12,col="green4")

lines(bond.maturities,nlm.yield*100,type="b", pch=8,col="royalblue")

lines(bond.maturities,text.yield*100,type="b",pch=13,col="magenta")

legend("bottomright",legend=c("Market Yield(\%)","nls Yield(\%)",

"optim Yield(\%)","nlm Yield(\%)","Text Yield(\%)"),

col=c("red1","rosybrown","green4","royalblue","magenta"),

Ity $=c(1,1,1)$, pch $=c(10,20,12,8,13))$

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-32.jpg?height=1128&width=1244&top_left_y=1282&top_left_x=430)

### 3.3 THE CIR MODEL: REAL-WORLD CALIBRATION

In this section we consider three calibration methods: the Euler method, exact likelihood estimates and the generalized method of moments (GMM). The Euler discretization method leads to explicit expressions for estimates, while the exact maximum likelihood estimate method and GMM require using numerical routines to obtain solutions.

### 3.3.1 EULER METHOD

As we saw earlier the Euler discretization of the CIR model leads to:

$$
r(i)=\alpha_{1}+\beta_{1} r(i-1)+\sqrt{r(i-1)} \epsilon_{i}, \quad i=1,2, \ldots
$$

with $\epsilon_{i}$ 's that are i.i.d. normal with mean 0 standard deviation $\sigma$. We can rearrange this to get a linear regression as below:

$$
\begin{aligned}
r(i) & =\alpha_{1}+\beta_{1} r(i-1)+\sqrt{r(i-1)} \epsilon_{i}, \quad i=1,2, \ldots \\
\frac{r(i)}{\sqrt{r(i-1)}} & =\alpha_{1}\left(\frac{1}{\sqrt{r(i-1)}}\right)+\beta_{1} \sqrt{r(i-1)}+\epsilon_{i}
\end{aligned}
$$

Now write:

$$
\begin{aligned}
y_{i} & =\frac{r(i)}{\sqrt{r(i-1)}} \\
x_{1 i} & =\frac{1}{\sqrt{r(i-1)}} \\
x_{2 i} & =\sqrt{r(i-1)} \\
y_{i} & =\alpha_{1} x_{1 i}+\beta_{1} x_{2 i}+\epsilon_{i}, i=1,2, \ldots
\end{aligned}
$$

To obtain MLEs of $\alpha_{1}$ and $\beta_{1}$ we can use the "Im" function in R. Once we obtain least square estimates (or MLE) of $\alpha_{1}$ and $\beta_{1}$ we can obtain $\gamma, \bar{r}$ and $\alpha$ using:

$$
\begin{aligned}
\gamma & =\frac{1-\beta_{1}}{\Delta} \\
\bar{r} & =\frac{\alpha_{1}}{1-\beta_{1}} \\
\alpha & =\frac{\sigma^{2}}{\Delta}
\end{aligned}
$$

The following R code snippet illustrates this point along with a simple study of bias and mean square error of this estimate.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-33.jpg?height=390&width=1154&top_left_y=2078&top_left_x=320)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-34.jpg?height=1433&width=1075&top_left_y=315&top_left_x=320)

bias=rowMeans(euler.est-paras)

sd =rowSds(euler.est)

rmse $=\left(\text { rowMeans }\left((\text { euler.est-paras })^{\wedge} 2\right)\right)^{\wedge} 0.5$

Simulation performance based on 1000 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\alpha$ |
| Bias | 0.47566 | 0.02376 | $3.3307 \times 10^{-4}$ |
| Standard <br> deviation | 0.5895 | 0.71757 | 0.0018 |
| Root mean <br> square | 0.75724 | 0.7176 | 0.00183 |

### 3.3.2 MAXIMUM LIKELIHOOD ESTIMATE

As we saw earlier a short rate sample can be stated as $r(0), r(1), \ldots, r(n)$. Using (5) we can write the following expression for the full likelihood function:

$$
\begin{aligned}
\mathscr{L} & =f(r(0) \mid \gamma, \bar{r}, \alpha) \prod_{i=0}^{n-1} f(r(i+1) \mid r(i), \gamma, \bar{r}, \alpha) \\
& =f(r(0) \mid \gamma, \bar{r}, \alpha) \prod_{i=1}^{n} c_{\Delta} \chi^{2}\left(c_{\Delta} r_{i}, \nu, \lambda_{i}\right)
\end{aligned}
$$

where $f(r(0) \mid \gamma, \bar{r}, \alpha)$ is a pdf of $r(0), f(r(0) \mid \gamma, \bar{r}, \alpha)$ are the conditional pdfs of $r(i+1) \mid r(i)$ for $i=$ $0,1,2, \ldots, c_{\Delta}, \vartheta$ and $\lambda_{i}$ are as given below:

$$
\begin{aligned}
c_{\Delta} & =\frac{4 \gamma}{\alpha(1-\exp (-\gamma \Delta))} \\
\nu & =\frac{4 \gamma}{\alpha} \bar{r} \\
\lambda_{i} & =c_{\Delta} r(i-1) \exp (-\gamma \Delta)
\end{aligned}
$$

Since $f(r(i+1) \mid r(i), \gamma, \bar{r}, \alpha)$ is a function of a non-central $\chi^{2} \mathrm{pdf}$, we will have the full likelihood function if we specify the pdf, $f(r(0) \mid \gamma, \bar{r}, \alpha)$. However, in CIR calibration using MLE both [19] and [20] ignore the contribution of $f(r(0) \mid \gamma, \bar{r}, \alpha)$ and call them as MLEs, even though it is actually based on quasi-likelihood functions.

The maximization of the quasi-likelihood function can be easily implemented in $\mathrm{R}$ as given below; however numerical solutions mostly depend on the initial guess. There are some concerns with this method, which uses R function "dchisq" as it is based on evaluation of a truncated form of the infinite sum in (6).

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-35.jpg?height=1229&width=1161&top_left_y=1267&top_left_x=319)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-36.jpg?height=1025&width=1071&top_left_y=304&top_left_x=321)

bias.euler= rowMeans(euler.est-paras)

sd.euler= rowSds(euler.est)

rmse.euler $=\left(\text { rowMeans }\left((\text { euler.est-paras })^{\wedge} 2\right)\right)^{\wedge} 0.5$

bias.mle =rowMeans(mle.est-paras)

sd.mle= rowsds(mle.est)

rmse.mle $=\left(\text { rowMeans }\left((\text { mle.est-paras })^{\wedge} 2\right)\right)^{\wedge} 0.5$

Simulation performance based on 100 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\alpha$ |
| Bias (Euler method) | 0.48285 | -0.02065 | $9.20085 \times 10^{-5}$ |
| Bias (MLE) | 0.45736 | -0.02114 | $-2.0002 \times 10^{-4}$ |
| Standard <br> deviation (Euler) | 0.64624 | 0.21512 | 0.00156 |
| Standard <br> deviation (MLE) | 0.56166 | 0.21401 | 0.00147 |
| Root mean <br> square (Euler) | 0.80411 | 0.21504 | 0.00156 |
| Root mean <br> square (MLE) | 0.72214 | 0.21398 | 0.00148 |

As you see in each of the sample calculations, the estimate of $\alpha$ has relatively smaller bias and the estimates of $\gamma$ and $\bar{r}$ have a larger bias.

### 3.4 THE GENERALIZED METHOD OF MOMENTS

The idea of the generalized method of moments (GMM) first appeared in [16]. This method compares sample moments with their theoretical values. The parameters are estimated by minimizing the distance between sample moments and their theoretical values. Chan, Karolyi, Longstaff and Sanders (CKLS) [7] illustrate how to use GMM for the CKLS short rate model given by the following SDE:

$$
d r_{t}=\gamma\left(\bar{r}-r_{t}\right) d t+(\alpha)^{1 / 2} r_{t}^{\tau} d X_{t}
$$

Note that the above is a generalization of both the Vasicek and the CIR models as $\alpha=\sigma^{2}, \tau=0$ and $\tau=$ $1 / 2$ yields the Vasicek and the CIR models respectively. As CIR contains only three parameters we can adopt GMM as follows:

First define:

$$
\begin{aligned}
& f_{1}=\frac{1}{N} \sum_{i=1}^{N}\left(r(i)-\alpha_{1}-\beta_{1} r(i-1)\right) \\
& f_{2}=\frac{1}{N} \sum_{i=1}^{N}\left[\left(r(i)-\alpha_{1}-\beta_{1} r(i-1)\right)^{2}-r(i-1) \sigma^{2}\right] \\
& f_{3}=\frac{1}{N} \sum_{i=1}^{N}\left[r(i)-\alpha_{1}-\beta_{1} r(i-1)\right] r(i-1)
\end{aligned}
$$

We choose $\alpha_{1}, \beta_{1}$ and $\sigma$ to set $f_{1}, f_{2}$ and $f_{3}$ to zero, for instance by minimizing:

$$
J\left(\alpha_{1}, \beta_{1}, \sigma\right)=f_{1}^{2}+f_{2}^{2}+f_{3}^{2}
$$

The above equations are implemented in the code chunk:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-37.jpg?height=751&width=889&top_left_y=1115&top_left_x=324)

Once we obtain GMM estimates for $\alpha_{1}, \beta_{1}$ and $\sigma$ we obtain estimates for $\gamma, \bar{r}$ and $\alpha$ using the following as in the Euler method:

$$
\begin{aligned}
\gamma & =\frac{1-\beta_{1}}{\Delta} \\
\bar{r} & =\frac{\alpha_{1}}{1-\beta_{1}} \\
\alpha & =\frac{\sigma^{2}}{\Delta}
\end{aligned}
$$

The following R-code snippets implement this method:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-38.jpg?height=2266&width=1093&top_left_y=264&top_left_x=320)

Simulation Performance Based

On 10 Sample Paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\alpha$ |
| Bias (Euler method) | 0.38199 | -0.00882 | $-2.74156 \times 10^{-4}$ |
| Bias (GMM) | 0.38199 | -0.00887 | $-2.74157 \times 10^{-4}$ |
| Standard <br> deviation (Euler) | 0.34194 | 0.01973 | 0.00157 |
| Standard <br> deviation (GMM) | 0.34193 | 0.01971 | 0.00157 |
| Root mean <br> square (Euler) | 0.50114 | 0.02069 | 0.00152 |
| Root mean <br> square (GMM) | 0.50114 | 0.02069 | 0.00152 |

As we can see from the results, the difference between the Euler method and this method is minor.

Mathematically, we can prove that the Euler method and GMM would produce identical estimates in the CIR model.

### 3.5 THE CIR MODEL: RISK-NEUTRAL CALIBRATION

This section is very similar to the Section 3.2 "Vasicek model: risk-neutral calibration". The main difference is, in this section we use CIR model zero coupon bond pricing formulas (15.70) to (15.72) of [24] which are listed below, instead of the formulas in Section 3.2.

$$
Z(r, t ; T)=e^{A(t ; T)-B(t ; T) \times r}
$$

$$
\begin{aligned}
& B(t ; T)=\frac{2\left(e^{\psi_{1}(T-t)}-1\right)}{\left(\gamma^{*}+\psi_{1}\right)\left(e^{\psi_{1}(T-t)}-1\right)+2 \psi_{1}} \\
& A(t ; T)=2 \frac{\bar{r}^{*} \gamma^{*}}{\alpha} \log \left(\frac{2 \psi_{1} e^{\left(\psi_{1}+\gamma^{*}\right) \frac{(T-t)}{2}}}{\left(\gamma^{*}+\psi_{1}\right)\left(e^{\psi_{1}(T-t)}-1\right)+2 \psi_{1}}\right), \text { and } \psi_{1}=\sqrt{\left(\gamma^{*}\right)^{2}+2 \alpha}
\end{aligned}
$$

The calibration process involves minimizing the following quantity for a given value of $\alpha$ :

$$
J\left(\gamma^{*}, \bar{r}^{*}\right)=\sum_{i=1}^{n}\left(Z^{C I R}\left(r_{0}, 0 ; T_{i}\right)-Z^{\text {Data }}\left(0, T_{i}\right)\right)^{2}
$$

We can use either "nlm" or "optim" for this purpose as before. The following example first calculates a bond price vector for given maturities with known parameter values and then calculates parameters using the minimization. It is used as a verification of our code for the minimization as in the Vasicek case.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-39.jpg?height=565&width=1067&top_left_y=1967&top_left_x=323)

## CIR Risk-Neutral Parameter Estimates With $\boldsymbol{\alpha}=\mathbf{0 . 0 5}$

| Method | Parameter |  | Constraint |
| :--- | ---: | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ | $\gamma^{*} \times \bar{r}^{*}>\frac{1}{2} \alpha$ |
| nlm | 0.49999 | 0.07 | TRUE |
| optim | 0.49746 | 0.07011 | TRUE |

As in the Vasicek case we could try to estimate all three parameters from bond pricing data.

## \#example23

rm(list=Is()) \# clear the workspace and functions

bond. maturities $=\operatorname{seq}(0.5,10,0.5)$

bond.prices $=\mathrm{CIR} . \mathrm{zcbp}(\mathrm{r} 0=0.02, \mathrm{t}=0, \mathrm{~T}=$ bond.maturities,gamma $=0.5$,

rbar $=0.07$, alpha $=0.05$ )

model $=n \operatorname{lm}(f=\mathrm{CIR} . \mathrm{J}, \mathrm{p}=\mathrm{c}(0.3,0.05,0.02), \mathrm{r} 0=0.02$,

bond.prices=bond.prices,

bond.maturities=bond.maturities)

model1 $=\operatorname{optim}(c(0.3,0.05,0.02)$, lower $=c(0,0,0)$, CIR.J, method=("L-BFGS-B")

, $\mathrm{r} 0=0.02$, bond. prices=bond. prices,

bond.maturities=bond.maturities)

After a few initial guesses, we see that the results given in the table below are not satisfactory.

## CIR Risk-neutral Parameter Estimates

| Method | Parameter |  |  | Constraint |
| :--- | ---: | ---: | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ | $\alpha$ | $\gamma^{*} \times \bar{r}^{*}>\frac{1}{2} \alpha$ |
| nlm | 0.353 | 0.08847 | 0.13215 | FALSE |
| optim | 0.35041 | 0.08895 | 0.13359 | FALSE |

Therefore, we do not recommend using bond prices to estimate $\alpha$.

As in the Vasicek case, instead of writing our own function to minimize we can use the "nls" package for non-linear least squares minimization. The following code snippet illustrates usage of "nls" with bond yields.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-40.jpg?height=621&width=1262&top_left_y=1849&top_left_x=322)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-41.jpg?height=527&width=1003&top_left_y=261&top_left_x=322)

The "nls" algorithm converged in 9 iterations and summary statistics are:

The Vasicek Fit (Simulated Data): Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.5 | $2.80955 \times 10^{-12}$ | $1.77965 \times 10^{11}$ | $1.14742 \times 10^{-192}$ |
| $\bar{r}^{*}$ | 0.07 | $1.34795 \times 10^{-13}$ | $5.19307 \times 10^{11}$ | $4.87627 \times 10^{-201}$ |

This illustrates that as in the Vasicek case "nls" performs better than both "optim" and " $n I m$ " when the underlying distribution is CIR. As in the Vasicek case we may try to estimate the standard deviation parameter from the bond yield data as illustrated below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-41.jpg?height=1088&width=1262&top_left_y=1295&top_left_x=320)

The "nls" algorithm converged in 26 iterations and summary statistics are:

The Vasicek Fit (Simulated Data): Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.5 | $7.01055 \times 10^{-9}$ | $7.1321 \times 10^{7}$ | $1.71573 \times 10^{-124}$ |
| $\bar{r}^{*}$ | 0.07 | $6.39192 \times 10^{-10}$ | $1.09513 \times 10^{8}$ | $1.17007 \times 10^{-127}$ |
| $\sigma$ | 0.05 | $4.6444 \times 10^{-9}$ | $1.07657 \times 10^{7}$ | $1.56479 \times 10^{-110}$ |

For a practical example we could try using data from Table 15.1 of [24]:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-42.jpg?height=1411&width=1268&top_left_y=613&top_left_x=319)

CIR Risk-Neutral Parameter Estimates With $\boldsymbol{\alpha}=\mathbf{0 . 0 5 4 8}$

| Method | Parameter |  | Constraint |  |
| :--- | ---: | ---: | ---: | :---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ | $\gamma^{*} \times \bar{r}^{*}>\frac{1}{2} \alpha$ |  |
| nlm | 0.37982 | 0.07207 | FALSE |  |
| optim | 0.37876 | 0.07215 | FALSE |  |
| nls | 0.26401 | 0.08599 | FALSE |  |

We see that "optim" produced values that are close to the estimates of $\gamma^{*}=0.3807$ and $\bar{r}^{*}=7.2 \%$ in footnote 10 of page 552 of [24]. However, the resulting estimates do not satisfy the required constraint of $\gamma \times \bar{r}>\alpha / 2$.

The following are summary statistics of the "nls" method, which converged after 11 iterations:

The CIR Fit (Simulated Data): Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.26401 | 0.04652 | 5.67475 | $5.72022 \times 10^{-6}$ |
| $\bar{r}^{*}$ | 0.08599 | 0.00847 | 10.15586 | $1.53483 \times 10^{-10}$ |

If $\alpha$ is also unknown, we need to modify the code as given below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-43.jpg?height=1413&width=1262&top_left_y=819&top_left_x=319)

CIR Risk-Neutral Parameter Estimates

| Method | Parameter |  |  | Constraint |
| :--- | ---: | ---: | ---: | ---: |
|  | $\gamma^{*}$ | $\bar{r}^{*}$ | $\alpha$ | $\gamma^{*} \times \bar{r}^{*}>\frac{1}{2} \alpha$ |
| nlm | 0.02632 | 0.72611 | 0.18018 | FALSE |
| optim | 0.46538 | 0.06311 | 0.00727 | TRUE |
| nls | 0.1 | 0.19222 | 0.11924 | FALSE |

We see that only "optim" produces acceptable estimates but the resulting $\alpha$ value is not close to 0.0548 . The following is a summary statistics of "nls" method which converged after 55 iterations:

The CIR Fit (Simulated Data): Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.1 | 0.49444 | 0.20225 | 0.84136 |
| $\bar{r}^{*}$ | 0.19222 | 0.837 | 0.22965 | 0.82023 |
| $\alpha$ | 0.11924 | 0.13725 | 0.86881 | 0.39322 |

Based on the summary statistics we can conclude that CIR is not suitable model for the data set. To evaluate this issue further we can look at the fit of the model with the Vasicek model.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-44.jpg?height=1084&width=1265&top_left_y=1101&top_left_x=321)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-45.jpg?height=846&width=1326&top_left_y=267&top_left_x=323)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-45.jpg?height=1117&width=1242&top_left_y=1209&top_left_x=298)

From the plot we see that the CIR fit is marginally better than the Vasicek fit but the CIR fitted values may lead to negative interest rates; therefore we recommend using the Vasicek model for the given data.

### 3.6 THE TWO-FACTOR VASICEK MODEL CALIBRATION

The literature on real-world calibration of the two-factor Vasicek model is non-existent. Even the seminal text on interest rate models by Brigo (2009) focuses on calibrating in the risk-neutral environment. The difficulty in calibrating in the real world lies in selecting short term rates and then long term rates.

However, short and long term rates are extracted from bond prices which in turn use the risk-neutral world to model and calculate yields. Essentially, to calibrate in the real world we need the observed values of $\phi_{1, t}$ and $\phi_{2, t}$ individually but the market data (say overnight rates) are $r_{t}$ values. Therefore we have to use statistical mixture models to calibrate to real time data, but that is beyond the scope of this paper. As the appendix shows, zero-coupon bond prices under the two-factor Vasicek model are given by:

$$
Z\left(\phi_{1, t}, \phi_{2, t}, t ; T\right)=\exp \left(A(t ; T)-\phi_{1, t} B_{1}(t ; T)-\phi_{2, t} B_{2}(t ; T)\right)
$$

where:

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{1}\left(B_{1}(t ; T)-(T-t)\right)-\frac{\sigma_{1}^{2}}{2}\left[\frac{1}{\gamma_{1}^{2}}\left(B_{1}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{1}} B_{1}(t ; T)^{2}\right] \\
& +\vec{\phi}_{2}\left(B_{2}(t ; T)-(T-t)\right)-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t ; T)^{2}\right] \\
& -\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[B_{1}(t ; T)+B_{2}(t ; T)-B_{3}(t, T)-(T-t)\right]
\end{aligned}
$$

and

$$
B_{i}(t ; T)=\int_{0}^{T-t} \exp \left(-\gamma_{i} s\right) d s, i=1,2,3
$$

With $\gamma_{3}=\gamma_{1}+\gamma_{2}$. We write $B_{i}(t ; T)$ in an integral form as it is easy to evaluate it for $\gamma_{i}=0$ and $\gamma_{i} \neq 0$. The calibration process involves minimizing the following quantity:

$$
J\left(\gamma^{*}, \bar{r}^{*}\right)=\sum_{i=1}^{n}\left(Z^{\text {Two-factor-Vasicek }}\left(r_{0}, 0 ; T_{i}\right)-Z^{\text {Data }}\left(0, T_{i}\right)\right)^{2}
$$

where $Z^{T w o-f a c t o r-V a s i c e k}\left(r_{0}, 0 ; T_{i}\right)$ is as given in (9). As we need to estimate three parameters, we use a nonlinear least square minimization algorithm for this task. The R package "nls" is suitable for this task. In some cases $\gamma_{1}$ or $\gamma_{2}$ may turn out to be negative and in iterative computations the parameter values may go through zero; therefore it is important to know the behavior of $A(t ; T)$ and $B(t ; T)$ in the neighborhood of zero. As the appendix points out we can write:

- When $\gamma_{1}=0, \gamma_{2} \neq 0$

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{2}\left(B_{2}(t ; T)-(T-t)\right)+\sigma_{1}^{2} \frac{(T-t)^{3}}{6}-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t ; T)^{2}\right] \\
& +\rho \sigma_{1} \sigma_{2}\left[\frac{(T-t)^{2}}{2}+\frac{\exp \left(-\gamma_{2}(T-t)\right)\left(\gamma_{2}(T-t)+1\right)-1}{\gamma_{2}^{2}}\right]
\end{aligned}
$$

- When $\gamma_{1} \neq 0, \gamma_{2}=0$

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{1}\left(B_{1}(t ; T)-(T-t)\right)-\frac{\sigma_{1}^{2}}{2}\left[\frac{1}{\gamma_{1}^{2}}\left(B_{1}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{1}} B_{1}(t ; T)^{2}\right]+\sigma_{2}^{2} \frac{(T-t)^{3}}{6} \\
& +\rho \sigma_{1} \sigma_{2}\left[\frac{(T-t)^{2}}{2}+\frac{\exp \left(-\gamma_{1}(T-t)\right)\left(\gamma_{1}(T-t)+1\right)-1}{\gamma_{1}^{2}}\right]
\end{aligned}
$$

- When $\gamma_{1}=\gamma_{2}=0$

$$
A(t ; T)=\left(\sigma_{1}^{2}+\sigma_{2}^{2}+2 \rho \sigma_{1} \sigma_{2}\right) \frac{(T-t)^{3}}{6}
$$

The R function "Two.factor.Vasicek.A" implements these formulas. For the calibration we assume we have the following data after choosing a possible long-term rate (for example 5 years or 10 years):

- $\quad$ Volatility of short-term rate $d r_{t}, \sigma_{\tau}$
- Volatility of long-term rate $d r_{t}(\tau), \sigma(\tau)$
- $\quad$ Correlation between short-term rate $d r_{t}$ and long-term rate $d r_{t}(\tau), \rho(0, \tau)$
- Series of zero-coupon strip prices.

For each set of given values of $\gamma_{1}^{*}, \gamma_{2}^{*}, \vec{\phi}_{1}^{*}$ and $\vec{\phi}_{2}^{*}$ we solve following three simultaneous equations for $\sigma_{1}$, $\sigma_{2}$ and $\rho$ :

$$
\begin{aligned}
& \sigma_{\tau}=\sqrt{\sigma_{1}^{2}+\sigma_{2}^{2}+2 \sigma_{1} \sigma_{2} \rho} \\
& \sigma(\tau)=\sqrt{\sigma_{1}^{2}\left(\frac{B_{1}(\tau)}{\tau}\right)^{2}+\sigma_{2}^{2}\left(\frac{B_{2}(\tau)}{\tau}\right)^{2}+2\left(\frac{B_{1}(\tau)}{\tau}\right)\left(\frac{B_{2}(\tau)}{\tau}\right) \sigma_{1} \sigma_{2} \rho} \\
& \rho(0, \tau)=\frac{\sigma_{1}^{2}\left(\frac{B_{1}(\tau)}{\tau}\right)+\sigma_{2}^{2}\left(\frac{B_{2}(\tau)}{\tau}\right)+\left(\frac{B_{1}(\tau)}{\tau}+\frac{B_{2}(\tau)}{\tau}\right) \sigma_{1} \sigma_{2} \rho}{\sigma_{\tau} \sigma(\tau)}
\end{aligned}
$$

Although the above three equations appear to be non-linear, they can be converted into linear equations of $\sigma_{1}, \sigma_{2}$ and cova, where cova is defined as cova $=\rho \sigma_{1} \sigma_{2}$. The R function "Two.factor.Vasicek.Vols" given below implements this.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-47.jpg?height=660&width=1310&top_left_y=1492&top_left_x=319)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-48.jpg?height=377&width=1096&top_left_y=270&top_left_x=323)

Use these values of $\sigma_{1}, \sigma_{2}$ and $\rho$ in (9) along with strip prices to minimize (10) with respect to $\gamma_{1}^{*}, \gamma_{2}^{*}, \vec{\phi}_{1}^{*}$ and $\vec{\phi}_{2}^{*}$. In an iterative scheme with each set of new values of $\gamma_{1}^{*}, \gamma_{2}^{*}, \vec{\phi}_{1}^{*}$ and $\vec{\phi}_{2}^{*}$, the parameters $\sigma_{1}, \sigma_{2}$ and $\rho$ have to be calculated. Therefore, to feed to non-linear regression analysis we use the following routine for log bond yield calculation under the two-factor Vasicek model.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-48.jpg?height=792&width=1457&top_left_y=1052&top_left_x=325)

The final call for the minimization is carried out as given below:

## \#example29

\# Two factor Vasicek risk-neutral calibration with simulated data example rm(list=Is()) \# clear the workspace and functions

bond. maturities $=\operatorname{seq}(0.5,20,0.5)$

set.seed(12345)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-49.jpg?height=1541&width=1224&top_left_y=260&top_left_x=324)

The "nls" algorithm converged in 74 iterations and summary statistics are:

The Two-Factor Vasicek Fit (Simulated Data): Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\vec{\phi}_{1}^{*}$ | -0.0413 | $3.50551 \times 10^{-14}$ | $-1.17815 \times 10^{12}$ | 0 |
| $\gamma_{1}^{*}$ | 0.8269 | $4.62426 \times 10^{-14}$ | $1.78818 \times 10^{13}$ | 0 |
| $\gamma_{2}^{*}$ | -0.0288 | $1.09881 \times 10^{-14}$ | $-2.62101 \times 10^{12}$ | 0 |

The following values are obtained using the estimated values of $\vec{\phi}_{1}^{*}, \gamma_{1}^{*}$ and $\gamma_{2}^{*}$ :

| Parameter | Estimate |
| :--- | ---: |
| $\sigma_{1}$ | 0.02508 |
| $\sigma_{2}$ | 0.01318 |
| $\rho$ | -0.47532 |

From the summary statistics we see that the "nls" function converges to its true value quite easily. Now we can test the fit using an actual data set. For this purpose we use Table 15.1 of [24].

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-50.jpg?height=1412&width=1369&top_left_y=386&top_left_x=320)

The "nls" algorithm converged in 12 iterations and summary statistics are:

The Two-Factor Vasicek Fit: Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\vec{\phi}_{1}^{*}$ | -0.9 | 21.90681 | -0.04108 | 0.96756 |
| $\gamma_{1}^{*}$ | 0.34742 | 0.15571 | 2.23117 | 0.03487 |
| $\gamma_{2}^{*}$ | $1.45913 \times 10^{-4}$ | $3.27303 \times 10^{-7}$ | 445.80356 | $2.77736 \times 10^{-50}$ |

The following values are obtained using the estimated values of $\vec{\phi}_{1}^{*}, \gamma_{1}^{*}$ and $\gamma_{2}^{*}$ :

| Parameter | Estimate |
| :--- | ---: |
| $\sigma_{1}$ | 0.0373 |
| $\sigma_{2}$ | 0.02273 |
| $\rho$ | -0.83721 |

We tried many possible starting values but it converged only to these values. However the convergence was always accompanied a warning message "false convergence(8)". It may mean the yield rate function may not be continuous in the neighborhood of converging values. One may refer to [14] complete list of return codes ${ }^{2}$.

The summary statistics suggests that the model is not appropriate. To examine further we plot the fitted value based on the two-factor Vasicek model along with the Vasicek model:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-51.jpg?height=984&width=1468&top_left_y=813&top_left_x=314)

2 return code 8: false convergence: the gradient $\nabla f(x)$ may be computed incorrectly, the other stopping tolerances may be too tight, or either $f$ or $\nabla f$ may be discontinuous near the current iterate $x$.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-52.jpg?height=1127&width=1228&top_left_y=236&top_left_x=446)

The diagnostic p-values indicate that the two-factor Vasicek model is not an appropriate model for this data set. This agrees with the conclusion drawn in [24].

## 4 No-Arbitrage Models

When we fit risk-neutral versions of Vasicek and CIR models to a term structure extracted from Treasury bond prices we see that the resulting models are not exact fits, they just minimize the total error between market values and model values. To eliminate this mismatch, Hull-White $(1990,1993)$ extend Vasicek models by including a time dependent drift parameter. The two-factor Hull-White model and the LIBOR Market models are two more examples of no arbitrage models.

### 4.1 HULL-WHITE MODELS

In this section we describe the single factor Hull-White model and the two factor Hull-White model. In theory arbitrage-free models reproduce the yield curve and prices for a set of interest rate derivatives such as caps, floors or swaptions. In the calibration process that we outline, we see that they do not precisely reproduce the yield curve and derivative prices, but the error is minimal.

### 4.1.1 ONE FACTOR HULL-WHITE MODEL

The one factor Hull-White model is an extension of the Vasicek model with a time-varying drift coefficient given below:

$$
d r_{t}=\left(\theta_{t}-\gamma^{*} r_{t}\right) d t+\sigma d X_{t}
$$

The solution of this is:

$$
\begin{aligned}
r_{t+s} & =r_{t} \exp \left(-\gamma^{*} s\right)+\exp \left(-\gamma^{*}(t+s)\right) \int_{t}^{t+s} \theta_{u} \exp \left(\gamma^{*} u\right) d u+\sigma \exp \left(-\gamma^{*} s\right) \int_{0}^{s} \exp \left(\gamma^{*} u\right) d X_{u} \\
E\left[r_{t+s} \mid r_{t}\right] & =r_{t} \exp \left(-\gamma^{*} s\right)+\exp \left(-\gamma^{*}(t+s)\right) \int_{t}^{t+s} \theta_{u} \exp \left(\gamma^{*} u\right) d u \\
\operatorname{Var}\left[r_{t+s} \mid r_{t}\right] & =\left[\sigma \exp \left(-\gamma^{*} s\right)\right]^{2} \int_{0}^{s} \exp \left(2 \gamma^{*} u\right) d u=\frac{\sigma^{2}}{2 \gamma^{*}}\left(1-e^{-2 \gamma^{*} s}\right)
\end{aligned}
$$

As the Hull-White model is a Gaussian model (Ornstein-Uhlenbeck process ${ }^{3}$ ) the zero-coupon bond prices take the form:

[24] $(19.25$

$$
\begin{aligned}
& Z\left(r_{0}, 0 ; T\right)=e^{A(0 ; T)-B(0 ; T) r_{0}} \\
& B(0 ; T)=\frac{1}{\gamma^{*}}\left(1-e^{-\gamma^{*} T}\right) \\
& A(0 ; T)=-\int_{0}^{T} B(0 ; T-t) \theta_{t} d t+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(T+\frac{1-e^{-2 \gamma^{*} T}}{2 \gamma^{*}}-2 B(0 ; T)\right)
\end{aligned}
$$

$[24](19.27)$

When the Hull-White model is calibrated to be arbitrage-free, market discount factors should match the model price. We can solve for function $\theta_{t}$ as illustrated below:

$$
\begin{aligned}
Z\left(r_{0}, 0 ; T\right) & =e^{A(0 ; T)-B(0 ; T) r_{0}} \\
\ln \left(Z\left(r_{0}, 0 ; T\right)\right) & =A(0 ; T)-B(0 ; T) r_{0} \\
\frac{\partial \ln \left(Z\left(r_{0}, 0 ; T\right)\right)}{\partial T} & =\frac{\partial A(0 ; T)}{\partial T}-r_{0} \frac{\partial B(0 ; T)}{\partial T}
\end{aligned}
$$

But

$$
\begin{aligned}
f(0, T) & =-\frac{\partial \ln \left(Z\left(r_{0}, 0 ; T\right)\right)}{\partial T} \\
\frac{\partial B(0 ; T)}{\partial T} & =\exp \left(-\gamma^{*} T\right) \\
\frac{\partial A(0 ; T)}{\partial T} & =-B(0 ; T-T) \theta_{t}-\int_{0}^{T} \frac{\partial B(0 ; T-t)}{\partial T} \theta_{t} d t+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1+\exp \left(-2 \gamma^{*} T\right)-\frac{\partial B(0 ; T)}{\partial T}\right) \\
\frac{\partial B(0 ; T-t)}{\partial T} & =\exp \left(-\gamma^{*}(T-t)\right) \\
\frac{\partial A(0 ; T)}{\partial T \mid} & =-\int_{0}^{T} \exp \left(-\gamma^{*}(T-t)\right) \theta_{t} d t+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)+\exp \left(-2 \gamma^{*} T\right)\right) \\
f(0, T) & =\int_{0}^{T} \exp \left(-\gamma^{*}(T-t)\right) \theta_{t} d t-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)+\exp \left(-2 \gamma^{*} T\right)\right)+r_{0} \exp \left(-\gamma^{*} T\right) \\
f(0, T) & =\int_{0}^{T} \exp \left(-\gamma^{*}(T-t)\right) \theta_{t} d t-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)\right)^{2}+r_{0} \exp \left(-\gamma^{*} T\right) \\
f(0, T) \exp \left(\gamma^{*} T\right) & =\int_{0}^{T} \exp \left(\gamma^{*} t\right) \theta_{t} d t-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)\right)^{2} \exp \left(\gamma^{*} T\right)+r_{0}
\end{aligned}
$$

Differentiating both sides with respect to $T$ we can obtain an expression for $\theta_{T}$[^1]

$$
\begin{aligned}
& \frac{\partial f(0, T)}{\partial T} \exp \left(\gamma^{*} T\right)+f(0, T) \gamma^{*} \exp \left(\gamma^{*} T\right) \\
&= \exp \left(\gamma^{*} T\right) \theta_{T}-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}} 2\left(1-\exp \left(-\gamma^{*} T\right)\right) \exp \left(-\gamma^{*} T\right) \exp \left(\gamma^{*} T\right)- \\
& \frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)\right)^{2} \gamma^{*} \exp \left(\gamma^{*} T\right) \\
&= \exp \left(\gamma^{*} T\right) \theta_{T}-\frac{\sigma^{2}}{2 \gamma^{*}}\left(1-\exp \left(-2 \gamma^{*} T\right)\right) \exp \left(\gamma^{*} T\right) \\
& \theta_{T}= \frac{\partial f(0, T)}{\partial T}+\gamma^{*} f(0, T)+\frac{\sigma^{2}}{2 \gamma^{*}}\left(1-\exp \left(-2 \gamma^{*} T\right)\right)
\end{aligned}
$$

We notice that to evaluate $E\left[r_{s+t} \mid r_{t}\right]$, we need $\int_{t}^{s+t} \theta_{u} \exp \left(\gamma^{*} u\right) d u$. However, this integral can be simplified as illustrated below.

We already have the following from the derivation of $\theta_{t}$ :

$$
\int_{0}^{T} \exp \left(\gamma^{*} t\right) \theta_{t} d t=-r_{0}+f(0, T) \exp \left(\gamma^{*} T\right)+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} T\right)\right)^{2} \exp \left(\gamma^{*} T\right)
$$

From this we see:

$$
\begin{aligned}
\int_{t}^{t+s} \exp \left(\gamma^{*} u\right) \theta_{u} d u= & \int_{0}^{t+s} \exp \left(\gamma^{*} u\right) \theta_{u} d u-\int_{0}^{t} \exp \left(\gamma^{*} u\right) \theta_{u} d u \\
= & -r_{0}+f(0, t+s) \exp \left(\gamma^{*}(t+s)\right)+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*}(t+s)\right)\right)^{2} \exp \left(\gamma^{*}(t+s)\right) \\
& -\left[-r_{0}+f(0, t) \exp \left(\gamma^{*} t\right)+\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} t\right)\right)^{2} \exp \left(\gamma^{*} t\right)\right] \\
= & f(0, t+s) \exp \left(\gamma^{*}(t+s)\right)-f(0, t) \exp \left(\gamma^{*} t\right) \\
& +\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*}(t+s)\right)\right)^{2} \exp \left(\gamma^{*}(t+s)\right) \\
& -\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left(1-\exp \left(-\gamma^{*} t\right)\right)^{2} \exp \left(\gamma^{*} t\right) \\
= & f(0, t+s) \exp \left(\gamma^{*}(t+s)\right)-f(0, t) \exp \left(\gamma^{*} t\right)+ \\
& \frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left[\exp \left(\gamma^{*}(t+s)\right)-\exp \left(\gamma^{*} t\right)+\exp \left(-\gamma^{*}(t+s)\right)-\exp \left(-\gamma^{*} t\right)\right]
\end{aligned}
$$

Therefore, we have the following expression for $E\left[r_{s+t} \mid r_{t}\right]$ :

$$
\begin{aligned}
E\left[r_{t+s} \mid r_{t}\right]= & r_{t} \exp \left(-\gamma^{*} s\right)+f(0, s+t)-f(0, t) \exp \left(-\gamma^{*} s\right)+ \\
& \frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\left[1-\exp \left(-\gamma^{*} s\right)+\exp \left(-2 \gamma^{*}(t+s)\right)-\exp \left(-\gamma^{*}(2 t+s)\right)\right]
\end{aligned}
$$

This expression along with the expression for the $\operatorname{Var}\left[r_{s+t} \mid r_{t}\right]$ can be used to simulate interest rate paths from the Hull-White model.

### 4.1.2 THE TWO-FACTOR HULL-WHITE MODEL

The two-factor Hull-White model is a generalization of the two-factor Vasicek model. As in the two-factor Vasicek model, short rates are the sum of two factors,

$$
r_{t}=\phi_{1, t}+\phi_{2, t}
$$

Where each factor follows the following SDEs:

$$
\begin{aligned}
d \phi_{1, t} & =\left(\theta_{t}-\gamma_{1}^{*} \phi_{1, t}\right) d t+\sigma_{1} d X_{1, t} \\
d \phi_{2, t} & =-\gamma_{2}^{*} \phi_{2, t} d t+\sigma_{2} d X_{2, t} \\
d X_{1, t} d X_{2, t} & =\rho d t
\end{aligned}
$$

As given in ([24]) this is in fact the two-factor Vasicek model with $\gamma_{1}^{*} \vec{\phi}_{1}^{*}$ replaced by a time-varying function $\theta_{t}$ and setting $\vec{\phi}_{2}=0$. As in the two-factor Vasicek model, the SDE for each factor can be solved to obtain the following:

$$
\begin{aligned}
\phi_{1, t+s} & =\phi_{1, t} \exp \left(-\gamma_{1}^{*} s\right)+\exp \left(-\gamma_{1}^{*}(t+s)\right) \int_{t}^{t+s} \theta_{u} \exp \left(\gamma_{1}^{*} u\right) d u+\sigma_{1} \exp \left(-\gamma_{1}^{*} s\right) \int_{0}^{s} \exp \left(\gamma_{1}^{*} u\right) d X_{1, u} \\
\phi_{2, t+s} & =\phi_{2, t} \exp \left(-\gamma_{2}^{*} s\right)+\sigma_{2} \exp \left(-\gamma_{2} s\right) \int_{0}^{s} \exp \left(\gamma_{2} v\right) d X_{2, v}
\end{aligned}
$$

Hence we can obtain the following expressions for conditional expectations, variances and covariance:

$$
\begin{aligned}
\mathbb{E}\left[\phi_{1, t+s} \mid \phi_{1, t}\right] & =\phi_{1, t} \exp \left(-\gamma_{1}^{*} s\right)+\exp \left(-\gamma_{1}^{*}(t+s)\right) \int_{t}^{t+s} \theta_{u} \exp \left(\gamma_{1}^{*} u\right) d u \\
\mathbb{E}\left[\phi_{2, t+s} \mid \phi_{2, t}\right] & =\phi_{2, t} \exp \left(-\gamma_{2}^{*} s\right) \\
\mathbb{V} a r\left[\phi_{1, t+s} \mid \phi_{1, t}\right] & ==\sigma_{1}^{2} \frac{1-\exp \left(-2 \gamma_{1}^{*} s\right)}{2 \gamma_{1}} \\
\mathbb{V} a r\left[\phi_{2, t+s} \mid \phi_{2, t}\right] & ==\sigma_{2}^{2} \frac{1-\exp \left(-2 \gamma_{2}^{*} s\right)}{2 \gamma_{2}} \\
\operatorname{Cov}\left[\phi_{1, t+s}, \phi_{2, t+s} \mid \phi_{1, t}, \phi_{2, t}\right] & =\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)
\end{aligned}
$$

As we worked out for the one-factor Hull-White model we can obtain expressions for $\theta_{t}$ in terms of instantaneous forward rates, $f(0, t)$, and $\gamma_{1}^{*}, \gamma_{2}^{*}, \sigma_{1}^{*}$ and $\sigma_{2}^{*}$ and hence an expression for $E\left[r_{s+t} \mid r_{t}\right]$ but it is a quite long and involved expression, so we avoid reproducing it here.

### 4.1.3 HULL-WHITE MODEL CALIBRATION

Both one-factor and two-factor Hull-White model calibrations involve two steps. In the first step the yield curve will be interpolated to obtain values for chosen derivative cash flow timings. Then the time independent parameters of the Hull-White model are estimated using the interpolated yield curve, derivative prices, and non-linear least square methods. Least square methods can be used as long as the number of parameters is smaller than the available derivative prices. Then, using these estimated parameters, the time dependent parameter $\theta_{t}$ will be calculated.

The yield curve interpolation stage is the same for both one-factor and two-factor Hull-White models. For the yield curve interpolation one may use cubic splines, higher degree (degree of six or ten) polynomial fit, or Nelson-Siegel curve.

As it is difficult to cover all the possible option prices that can be used for calibration of time independent parameters in implementation, we concentrate on using cap prices. In the yield curve interpolation stage both one-factor and two-factor model use the following steps:

1. Obtain rates $r\left(0, t_{i}\right)$ using the discount factors $Z\left(r, t_{i}\right)$ from $r\left(0, t_{i}\right)=-\frac{1}{t_{i}} \ln \left(Z\left(0, t_{i}\right)\right), i=$ $1,2, \ldots, n$.
2. Fit a curve, $\hat{r}\left(0, t_{i}\right)$, for the points $\left(t_{i}, r\left(0, t_{i}\right)\right), i=1,2, \ldots, n$.
3. Use the fitted curve to get an estimate $\hat{f}(0, t)$ for $f(0, t)$ using $\hat{f}(0, t)=-\frac{\partial}{\partial t}[t \hat{r}(0, t)]$

### 4.2 YIELD CURVE INTERPOLATION: ONE-FACTOR MODEL

In fitting a curve for $r(0, t)$ we found that cubic-spline interpolation works poorly as the resulting $f(0, t)$ was an oscillating function. [24] suggests using a polynomial of degree 6 or degree 10 for $r(0, t)$. As an alternative we can fit using a Nelson-Siegel curve.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-56.jpg?height=999&width=1045&top_left_y=497&top_left_x=320)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-56.jpg?height=856&width=1109&top_left_y=1526&top_left_x=432)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-57.jpg?height=200&width=847&top_left_y=262&top_left_x=323)

The function $\theta$ (With Cubic Splines)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-57.jpg?height=837&width=1152&top_left_y=625&top_left_x=430)

### 4.2.1 FITTING AN $\boldsymbol{n}$ DEGREE POLYNOMIAL FOR $\boldsymbol{r}(\boldsymbol{0}, \boldsymbol{t})$

$R^{\prime}$ 's "poly" function fits the polynomial model:

$$
\begin{aligned}
r(0, t) & =\sum_{i=0}^{n} a_{i} t^{i} \\
f(0, t) & =\sum_{i=0}^{n} a_{i}(i+1) t^{i} \\
\frac{\partial f(0, t)}{\partial t} & =\sum_{i=1}^{n} a_{i} i(i+1) t^{i-1} \\
\theta_{t} & =\sum_{i=1}^{n} a_{i} i(i+1) t^{i-1}+\sum_{i=0}^{n} \gamma^{*} a_{i}(i+1) t^{i}+\frac{\sigma^{2}}{2 \gamma^{*}}\left(1-e^{-2 \gamma^{*} t}\right)
\end{aligned}
$$

## \#example33

TM = VeronesiTable15p1\$'Time to Maturity'

Yield = VeronesiTable15p1\$'Yield \% * *100

model1 = splinefun(TM,Yield,method="natural")

sigma $=0.0196$

gamma $=0.19$

model2 = Im(Yield poly(TM,6,raw=TRUE))

coefs = as.numeric( $\operatorname{coef}($ model2))

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-58.jpg?height=665&width=1159&top_left_y=270&top_left_x=319)

$6^{\text {th }}$ Degree Polynomial Fit

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-58.jpg?height=805&width=1116&top_left_y=1039&top_left_x=426)

plot(xvals, thetat,type="I",

main=expression(paste("The function ",

theta," (With 6 Degree Polynomial)")),

xlab="Time",ylab="Theta")

The function $\theta$ (With $6^{\text {th }}$ Degree Polynomial)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-59.jpg?height=816&width=1133&top_left_y=313&top_left_x=428)

### 4.2.2 FITTING A NELSON-SIEGEL CURVE TO $\boldsymbol{r}(\mathbf{0}, \boldsymbol{t})$

The Nelson-Siegel model specifies $f(0, t)$ in the following form:

$$
f(0, t)=\beta_{0}+\beta_{1} \exp \left(-\frac{t}{\tau}\right)+\frac{\beta_{2} t}{\tau} \exp \left(-\frac{t}{\tau}\right)
$$

However since we are fitting market yields we will get an expression for $r(0, t)$ :

$$
\begin{aligned}
r(0, t) & =\frac{1}{t} \int_{0}^{t} f(0, s) d s \\
& =\frac{1}{t} \int_{0}^{t}\left(\beta_{0}+\beta_{1} \exp \left(-\frac{s}{\tau}\right)+\frac{\beta_{2} s}{\tau} \exp \left(-\frac{s}{\tau}\right)\right) d s \\
& =\frac{1}{t}\left(\beta_{0} t+\beta_{1} \tau\left(1-\exp \left(-\frac{t}{\tau}\right)\right)+\beta_{2} \tau\left(1-\exp \left(-\frac{t}{\tau}\right)\right)-\beta_{2} t \exp \left(-\frac{t}{\tau}\right)\right) \\
& =\beta_{0}+\beta_{1} \frac{1-\exp \left(-\frac{t}{\tau}\right)}{\frac{t}{\tau}}+\beta_{2} \frac{1-\exp \left(-\frac{t}{\tau}\right)-\frac{t}{\tau} \exp \left(-\frac{t}{\tau}\right)}{\frac{t}{\tau}}
\end{aligned}
$$

Also we need:

$$
\frac{\partial}{\partial t} f(0, t)=-\frac{\beta_{1}}{\tau} \exp \left(-\frac{t}{\tau}\right)+\frac{\beta_{2}}{\tau} \exp \left(-\frac{t}{\tau}\right)-\frac{\beta_{2} t}{\tau^{2}} \exp \left(-\frac{t}{\tau}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-59.jpg?height=337&width=1066&top_left_y=2174&top_left_x=320)

\# The function "Nelson.Siegel" is from the Yield curve package.

NSP = Nelson.Siegel(Yield,TM)

\# The following three functions are developed with this paper.

rates $=$ NSRates(as.numeric(NSP),xvals)

fOt $=$ NSForwards(as.numeric(NSP),xvals)

thetat $=$ Theta(as.numeric(NSP), sigma $=0.0221$, gamma $=0.19$, xvals)

plot(xvals,fot,type="I",Ity=2,col="blue",main="Nelson-Siegel Fit",

xlab="Maturity",ylab="Rates(\%)" )

points(TM,Yield,type="b",|ty=1,col="red")

points(xvals, rates,type="I",Ity=1,col="green")

legend("bottomright",legend=c("Forward curve","Current yield",

"Fitted Yield"),col=c("blue", "red", "green"), lty=c( $2,1,1)$ )

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-60.jpg?height=1063&width=1098&top_left_y=973&top_left_x=424)

plot(xvals,thetat,type="I",

main=expression(paste("The function ", theta," (with Nelson-Siegel)")),

xlab="Time",ylab="Theta")

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-61.jpg?height=1082&width=1073&top_left_y=245&top_left_x=556)

### 4.3 CALIBRATION OF THE ONE-FACTOR HULL-WHITE MODEL

For both one-factor and two-factor Hull-White model calibration we assume that we have a data set similar to Table 19.4:

Swap Rates and Cap Prices on November 3, 2008

| Cap\# | Maturity (T) | Swap Rate | Price (x100) | Discount Factors |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.25 | 0.028588 | 0 | 0.9929037 |
| 2 | 0.50 | 0.026486 | 0.0528 | 0.9868908 |
| 3 | 0.75 | 0.024929 | 0.1313 | 0.9815442 |
| 4 | 1.00 | 0.024320 | 0.2401 | 0.9760606 |
| 5 | 1.25 | 0.024491 | 0.3826 | 0.9699535 |
| 6 | 1.50 | 0.024938 | 0.5405 | 0.9633988 |
| 7 | 1.75 | 0.025561 | 0.7106 | 0.9563730 |
| 8 | 2.00 | 0.026260 | 0.8932 | 0.9489501 |
| 9 | 2.25 | 0.027252 | 1.1095 | 0.9406132 |


| Cap\# | Maturity (T) | Swap Rate | Price (x100) | Discount Factors |
| :---: | :---: | :---: | :---: | :---: |
| 10 | 2.50 | 0.028630 | 1.3729 | 0.9309471 |
| 11 | 2.75 | 0.030108 | 1.6636 | 0.9204540 |
| 12 | 3.00 | 0.031400 | 1.9502 | 0.9098978 |
| 13 | 3.25 | 0.032471 | 2.2235 | 0.8995225 |
| 14 | 3.50 | 0.033474 | 2.4973 | 0.8889794 |
| 15 | 3.75 | 0.034408 | 2.7711 | 0.8783263 |
| 16 | 4.00 | 0.035270 | 3.0451 | 0.8676278 |
| 17 | 4.25 | 0.036076 | 3.3208 | 0.8568746 |
| 18 | 4.50 | 0.036835 | 3.5968 | 0.8460722 |
| 19 | 4.75 | 0.037531 | 3.8700 | 0.8353260 |
| 20 | 5.00 | 0.038150 | 4.1370 | 0.8247441 |

The above table contains one additional column, discount factors, which is derived from the Swap Rate column ([24]) of Table 19.4. The data set gives cap prices for 20 caps, each cap is quarterly spaced and the cap rate for each cap is the associated swap rate. For example, cap 12 is a 3-year cap with four payments per year and the cap rate is $3.14 \%$ with the first payment occurring at 0.5 years, if the observed rate is above the cap rate of $3.14 \%$. The value of a caplet is given by the following formulas from [24]: write $K=\frac{1}{1+r_{K} \Delta}$

$$
\begin{aligned}
& V\left(r_{0}, 0\right)=M \times\left(K Z\left(r_{0}, 0 ; T-\Delta\right) \mathcal{N}\left(-d_{2}\right)-Z\left(r_{0}, 0 ; T\right) \mathcal{N}\left(-d_{1}\right)\right) \\
& d_{1}=\frac{1}{S_{Z}(T-\Delta ; T)} \log \left(\frac{Z\left(r_{0}, 0 ; T\right)}{K Z\left(r_{0}, 0 ; T-\Delta\right)}\right)+\frac{S_{Z}(T-\Delta ; T)}{2} \\
& d_{2}=d_{1}-S_{Z}(T-\Delta ; T)
\end{aligned}
$$

while $B(t ; T)$ remains as:

$$
B(t ; T)=\frac{1}{\gamma^{*}}\left(1-e^{-\gamma^{*}(T-t)}\right)
$$

A careful observation reveals that this is the put option formula under the Vasicek model with modeled bond prices replaced by market observed bond prices. The cap prices are obtained by adding all the prices of corresponding caplets together. We first implement a caplet formula in the code block given below.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-63.jpg?height=565&width=1003&top_left_y=271&top_left_x=324)

Note that the R function Vasicek.B is implemented as:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-63.jpg?height=425&width=612&top_left_y=992&top_left_x=320)

Once the caplet prices are calculated the cap price is calculated as the sum of these caplets as given below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-63.jpg?height=427&width=1132&top_left_y=1564&top_left_x=323)

Now to calculate a cap price vector as given in Table 19.4 of ([24]) we can use the following $R$ function:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-64.jpg?height=563&width=1184&top_left_y=346&top_left_x=323)

Now we can estimate $\gamma^{*}$ and $\sigma^{*}$ using the non-linear least squares function "nls" which can be downloaded from R's CRAN archive. To verify the nls function we first use a simulated data set assuming the prices are from a Hull-White model.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-64.jpg?height=424&width=949&top_left_y=1160&top_left_x=321)

The "nls" algorithm converged in 4 iterations and summary statistics are:

The Hull-White Model Fit: Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.09707 | 0.00531 | 18.28544 | $4.49888 \times 10^{-13}$ |
| $\sigma$ | 0.01496 | $9.61873 \times 10^{-5}$ | 155.50562 | $1.29281 \times 10^{-29}$ |

From the output it is clear that "nls" function estimates are very close to the actual values. Now we can do the analysis for the data in Table 19.4 of [24]. The code snippet for the analysis is:

## \#example36

Data_set =VeronesiTable19p4

Data_set\$'Cap Price $(x 100)^{\prime}=$ VeronesiTable19p4\$'Cap Price $(x 100)^{\prime} / 100$

Data_set\$'Cap Price (x100)'[1]=0

Hull.White. fit =

nls(Data_set\$'Cap Price (x100)' Hull.White.cap. price.vector(

Maturity=Data_set\$Maturity, cap_rates=Data_set\$'Swap Rate', discount_factors=

Data_set\$discount_factors, gamma=gamma, sigma=sigma),

data=Data_set ,start=list(gamma=.1,sigma=0.1),

nls. control(maxiter $=100$, tol $=1$ e-05,

minFactor $=1 / 10240$,

printEval $=$ FALSE, warnOnly $=$ FALSE,

scaleOffset $=0$, nDcentral $=$ FALSE))

sum_mod = summary(Hull.White.fit)

The "nls" algorithm converged in 5 iterations and summary statistics are:

The Hull-White Model Fit: Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.06712 | 0.00376 | 17.84779 | $6.80885 \times 10^{-13}$ |
| $\sigma$ | 0.01454 | $6.87588 \times 10^{-5}$ | 211.40969 | $5.1521 \times 10^{-32}$ |

From the summary statistics we see that the fit is very good. As further evidence of the appropriateness of the fit we consider some graphical analysis with code snippets:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-65.jpg?height=244&width=840&top_left_y=1778&top_left_x=320)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-66.jpg?height=892&width=984&top_left_y=237&top_left_x=495)

plot('Cap Price (x100)' 'Maturity', data =Data_set, xlab = "Maturity", ylab = "Cap Price")

lines(Data_set\$'Maturity', fitted(Hull.White.fit))

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-66.jpg?height=935&width=1027&top_left_y=1408&top_left_x=473)

plot(fitted(Hull. White.fit), residuals(Hull.White.fit),xlab="Fitted Values", ylab="Residuals")

abline $(a=0, b=0)$

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-67.jpg?height=845&width=941&top_left_y=369&top_left_x=500)

As the graphs indicate the fitted model is an ideal one.

### 4.4 CALIBRATION OF THE TWO-FACTOR HULL-WHITE MODEL

The calibration of time-independent parameters will work as follows:

- First calculate the value of a caplet using the following formulas:

$$
\text { [23] (22.57) } \begin{aligned}
S_{Z}\left(T_{O} ; T_{B}\right)^{2}= & B_{1}^{2}(T O ; T B) \frac{\sigma_{1}^{2}}{2 \gamma_{1}^{*}}\left(1-\exp \left(-2 \gamma_{1}^{*} T_{O}\right)\right. \\
& +B_{2}^{2}\left(T_{O} ; T_{B}\right) \frac{\sigma_{2}^{2}}{2 \gamma_{2}^{*}}\left(1-\exp \left(-2 \gamma_{2}^{*} T_{O}\right)\right. \\
& +B_{1}\left(T_{O} ; T_{B}\right) B_{2}\left(T_{O} ; T_{B}\right) \sigma_{1} \sigma_{2} \rho \frac{1-\exp \left(-\left(\gamma_{1}^{*}+\gamma_{2}^{*}\right) T_{O}\right)}{\gamma_{1}^{*}+\gamma_{2}^{*}} \\
K= & \frac{1}{1+r_{K} \Delta} \\
V\left(r_{0}, 0\right)= & M \times\left(K Z\left(r_{0}, 0 ; T-\Delta\right) \mathcal{N}\left(-d_{2}\right)-Z\left(r_{0}, 0 ; T\right) \mathcal{N}\left(-d_{1}\right)\right) \\
d_{1}= & \frac{1}{S_{Z}(T-\Delta ; T)} \log \left(\frac{Z\left(r_{0}, 0 ; T\right)}{K Z\left(r_{0}, 0 ; T-\Delta\right)}\right)+\frac{S_{Z}(T-\Delta ; T)}{2} \\
d_{2}= & d_{1}-S_{Z}(T-\Delta ; T)
\end{aligned}
$$

In the above formula bond prices are market or interpolated bond prices. The above formulas are implemented in the following code chunk:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-68.jpg?height=801&width=1251&top_left_y=263&top_left_x=324)

- In the R functions for cap price, the cap price vector is similar to functions in the one-factor Vasicek model.

The following example illustrates calibration using a simulated data set.

## \#example 38

\# Hull-White fit with simulated data example

Testdata2 $=$ VeronesiTable19p4

Testdata2\$'Cap Price $(x 100)^{\prime}=$

Two.factor.Hull.White.cap.price.vector(cap_rates=VeronesiTable19p4\$'Swap Rate', Maturity=VeronesiTable19p4\$Maturity, discount_factors=VeronesiTable19p4\$discount_factors, gamma1=0.1,gamma2=-0.2,sigma1=0.2, sigma2=0.3,rho=0.5)

Testdata2\$'Cap Price $(x 100)^{\prime}[1]=0$

Two.factor.Hull.White.fit =nls('Cap Price (x100)'

Two.factor.Hull.White.cap.price.vector(cap_rates=Testdata2\$'Swap Rate', Maturity=Testdata2\$Maturity, discount_factors=Testdata2\$discount_factors, gamma1=gamma1,gamma2=gamma2,sigma1=sigma1,sigma2=sigma2,rho=rho), data= Testdata2, start=list(gamma1=.3,gamma2=-0.3,sigma1=0.1,sigma2=0.4,rho=0.6),

nls. control(maxiter $=100$, tol $=1 \mathrm{e}-05$, minFactor $=1 / 1024$,

printEval $=$ FALSE, warnOnly $=$ FALSE, scaleOffset $=0$,

nDcentral $=$ FALSE))

\#\# Error in nls('Cap Price (x100) ' Two.factor. Hull. White.cap.price.vector(cap rates

$=$ Testdata2\$ 'Swap Rate', : step factor 0.000488281 reduced below 'minFactor'

of 0.000976562

summary(Two.factor.Hull.White.fit)

\#\# Error in summary(Two.factor.Hull.White.fit): object 'Two.factor.Hull.White.fit' not found

After trying out several initial values we failed to find results. If we look at the cap price vector formula closely we see that each element is a function similar to $\sum_{i} a_{i} \Phi\left(x_{i}, \underline{\mu_{i}}, \underline{\sigma}_{i}\right)$ where $a_{i}, i=1,2, \ldots$ are known constants and $\Phi\left(x_{i}, \underline{\mu_{i}}, \underline{\sigma}_{i}\right)$, cdf of a normal distribution, is as given below:

$$
\Phi\left(x_{i}, \underline{\mu}_{i}, \underline{\sigma}_{i}\right)=\frac{1}{2 \pi \underline{\sigma}_{i}} \int_{-\infty}^{x_{i}} \exp \left(-\frac{\left(t-\underline{\mu}_{i}\right)}{\underline{\sigma}_{i}^{2}}\right) d t
$$

In the above expression, $\underline{\mu}_{i}$ and $\underline{\sigma}_{i}$ are functions of the five parameters $\gamma_{1}, \gamma_{2}, \sigma_{1}, \sigma_{2}$, and $\rho$. In the non-

linear least squares minimization, we minimize the distance between $\sum_{i} a_{i} \Phi\left(x_{i}, \underline{\mu_{i}}, \underline{\sigma_{i}}\right)$ and its observed values. It may be very sensitive to initial guesses and it may also have local values that minimize the objective function. So, we need an alternative method to compute parameters.

When we look at (22.57) of [24] carefully we see that caplet with a pay-off at time $T$ is a function of $S_{Z}(T-\Delta ; T)$, where it is given by:

$$
\begin{aligned}
S_{Z}(T-\Delta ; T)^{2}= & B_{1}(T-\Delta ; T)^{2} \frac{\sigma_{1}^{2}}{2 \gamma_{1}^{*}}\left(1-\exp \left(-2 \gamma_{1}^{*}(T-\Delta)\right)\right. \\
& +B_{2}(T-\Delta ; T)^{2} \frac{\sigma_{2}^{2}}{2 \gamma_{2}^{*}}\left(1-\exp \left(-2 \gamma_{2}^{*}(T-\Delta)\right)\right. \\
& +B_{1}(T-\Delta ; T) B_{2}(T-\Delta ; T) \sigma_{1} \sigma_{2} \rho \frac{1-\exp \left(-\left(\gamma_{1}^{*}+\gamma_{2}^{*}\right)(T-\Delta)\right)}{\gamma_{1}^{*}+\gamma_{2}^{*}} \\
= & B_{1}(0 ; \Delta)^{2} \frac{\sigma_{1}^{2}}{2 \gamma_{1}^{*}}\left(1-\exp \left(-2 \gamma_{1}^{*}(T-\Delta)\right.\right. \\
& +B_{2}(0 ; \Delta)^{2} \frac{\sigma_{2}^{2}}{2 \gamma_{2}^{*}}\left(1-\exp \left(-2 \gamma_{2}^{*}(T-\Delta)\right.\right. \\
& +B_{1}(0 ; \Delta) B_{2}(0 ; \Delta) \sigma_{1} \sigma_{2} \rho \frac{1-\exp \left(-\left(\gamma_{1}^{*}+\gamma_{2}^{*}\right)(T-\Delta)\right)}{\gamma_{1}^{*}+\gamma_{2}^{*}}
\end{aligned}
$$

The above formula can be coded as:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-69.jpg?height=407&width=1397&top_left_y=2053&top_left_x=340)

We see that $S_{Z}(T-\Delta ; T)$ characterizes the particular caplet, independent of which caplet it belongs to. We can exploit this fact first to obtain $S_{Z}((i-1) \Delta ; i \Delta)$ for $i=1,2, \ldots$ and then applying the nonlinear least squares method to estimate parameters $\gamma_{1}^{*}, \gamma_{2}^{*}, \sigma_{1}$ and $\sigma 2$. Extracting $S_{Z}((i-1) \Delta ; i \Delta) \mathrm{i}=1,2, \ldots$ is similar to extracting forward volatilities from flat volatilities as given in section 20.1.2 of [24]. It works as follows:

- Use the caplet with payment at time 0.5 to obtain $S_{z}(0 ; 0.5)$ This is similar to computing Black implied volatility.
- Calculate the price of a caplet with a payout at time 0.5 with cap rate applicable to a cap maturing at time 0.75 . Subtract this caplet value from the cap maturing at time 0.75 to obtain caplet with a payoff at time 0.75 . Use this to compute $S_{Z}(0.5 ; 0.75)$.
- $\quad$ Proceed similarly to calculate caplet prices and then compute $S_{Z}(0.25(i-1), 0.25 i), i=4,5, \ldots$

Note that the above procedure of extracting $S_{Z}((i-1) \Delta ; i \Delta)$ for $i=1,2, \ldots$ values are identical for both one factor and two factor Hull-White model, except for the one factor model $S_{Z}(T-\Delta, ; T)$ given as:

$$
S_{Z}(T-\Delta ; T)^{2}=B(0 ; \Delta)^{2} \frac{\sigma^{2}}{2 \gamma^{*}}\left(1-\exp \left(-2 \gamma^{*}(T-\Delta)\right)\right.
$$

The above formula can be coded as:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-70.jpg?height=244&width=1181&top_left_y=1129&top_left_x=304)

We can implement the above algorithm as given below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-70.jpg?height=710&width=1219&top_left_y=1550&top_left_x=323)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-71.jpg?height=481&width=695&top_left_y=258&top_left_x=324)

The auxiliary functions needed for the above functions are given below:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-71.jpg?height=430&width=1001&top_left_y=906&top_left_x=320)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-72.jpg?height=522&width=1033&top_left_y=263&top_left_x=321)

Even though the Hull-White model performance with cap prices and "nls" was excellent, we can try it with the method proposed in this section. The following code block illustrates this method with a simulated data set.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-72.jpg?height=1556&width=1158&top_left_y=993&top_left_x=320)

We see that in this case also the "nls" algorithm converged in 6 iterations. Summary statistics are:

The Hull-White Model Fit: Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.10091 | 0.0049 | 20.61337 | $1.82562 \times 10^{-13}$ |
| $\sigma$ | 0.01502 | $1.15879 \times 10^{-4}$ | 129.59386 | $6.63247 \times 10^{-27}$ |

Now we can attempt the same analysis with the data set in Table 19.4 of [24]:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-73.jpg?height=1088&width=1316&top_left_y=641&top_left_x=321)

We see that in this case the "nls" algorithm converged in 7 iterations and summary statistics are:

The Hull-White Model Fit: Summary Statistics

| Parameter | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: |
| $\gamma^{*}$ | 0.07803 | 0.01253 | 6.22849 | $9.17305 \times 10^{-6}$ |
| $\sigma$ | 0.01474 | $3.01536 \times 10^{-4}$ | 48.87517 | $9.9965 \times 10^{-20}$ |

From the summary statistics we see that the estimate of $\gamma^{*}$ is a little different but the estimate of $\sigma$ is quite close to that in example 36.

Since we were successful with the new method in the Hull-White case, we try the calibration of the twofactor Hull-White model with the new method:

\# example41

\# Two factor Hull-White fit with simulated data example

rm(list=Is()) \# clear the workspace and functions

Testdata =subset(VeronesiTable19p4,select=-c('Cap Price (x100)'))

Testdata\$'Cap Prices' =

Two.factor.Hull.White.cap.price.vector(cap_rates=Testdata\$'Swap Rate',

Maturity=Testdata\$Maturity,

discount_factors=Testdata\$discount_factors,

gamma1=0.1,gamma2=-0.2,sigma1=0.02, sigma2 $=0.03$, rho $=-0.4$ )

Testdata\$'Cap Prices'[1]=0

fvol.dat = HW.forward.vol(Maturity=Testdata\$Maturity, discount_factors =Testdata $\$$ discount_factors, cap_rates=Testdata\$'Swap Rate', cap_prices =Testdata\$'Cap Prices')+

rnorm(length(Testdata\$Maturity),0,0.001)

$\operatorname{sim} . S Z=$ Two.factor.Vasicek.SZ(TB=fvol.dat\$Maturity,

TO = fvol.dat\$Maturity-0.25,

gamma1 $=0.1$, gamma $2=-0.2$,

sigma $1=0.02$, sigma $2=0.03$,

rho=-0.4)

fvol.dat\$sim.SZ = sim.SZ

Two.factor.Hull. White.fit =nls('Forward Vol.'

Two.factor.Vasicek.SZ(TB=Maturity,

TO = Maturity-0.25,

gamma1=gamma1,

gamma2=gamma2,

sigma1=sigma1, sigma2=sigma2,

rho=rho),

data= fvol.dat,

start=list(gamma1=.3,gamma2=-0.3, sigma1=0.1,

sigma2 $=0.4$, rho $=0.6$ ),

algorithm = "port",

upper=list(gamma1=1,gamma2=1,sigma1=1,

sigma2 $2=1$, rho $=0.9$ ),

lower=list(gamma1=-1,gamma2=-1,sigma1=0.001,

sigma $2=0.001$, rho $=-0.9$ ),

nls.control(maxiter $=1000$,

tol $=1 \mathrm{e}-05$,

minFactor $=1 / 10240$,

printEval $=$ FALSE,

warnOnly $=$ FALSE,

scaleOffset $=0$,

nDcentral $=$ FALSE))

\#\# Error in nls('Forward Vol.' Two.factor.Vasicek.SZ(TB = Maturity, TO = Maturity

- : Convergence failure: singular convergence (7)

sum_mod = summary(Two.factor.Hull.White.fit)

\#\# Error in eval(expr, envir, enclos): object 'Two.factor.Hull.White.fit' not found

With many different initial values for the parameters, this method did not converge to a value close to the true value. Therefore we decided to use a nonlinear least squares estimation package "nlrs" which has been developed recently. In the package "nIrs" the function "nlfb" performs very well. However, the input for " $n \mid f b$ " is different from that of "nls". We need to input the residual function and the gradient of the residual function.

The following code chunk implements the residual function to be used with "nflb":

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-75.jpg?height=853&width=970&top_left_y=1014&top_left_x=320)

We also developed a function that calculates the Jacobian of the residual function with respect to parameters that need to be estimated; it is given in the following code chunk:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-76.jpg?height=1456&width=1183&top_left_y=264&top_left_x=321)

The function "Two.factor.Vasicek.SZ.gradient" calls another function, "Vasicek.DB", which calculates the derivative of $B(t ; T)$ with respect to $\gamma$ and it is:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-76.jpg?height=379&width=1121&top_left_y=1926&top_left_x=321)

We illustrate the use of these functions in the following code chunk:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-77.jpg?height=1183&width=1463&top_left_y=339&top_left_x=319)

fvol.dat\$'Forward Vol.sq' = fvol.dat\$'Forward Vol.'^2/(fvol.dat\$Maturity-0.25)

We see that in this case the "nlfb" algorithm converged in 22 iterations and summary statistics are:

## The Hull-White Model Fit: Summary Statistics

| Parameter | Exact value | Estimate | Std. Error | t-value | $\operatorname{Pr}[>\|t\|]$ |
| :--- | ---: | ---: | ---: | ---: | ---: |
| $\gamma_{1}^{*}$ | 0.1 | 0.10762 | 0.00221 | 48.72325 | $4.99986 \times 10^{-17}$ |
| $\gamma_{2}^{*}$ | -0.2 | -0.20095 | $2.64635 \times 10^{-4}$ | -759.33669 | $1.04201 \times 10^{-33}$ |
| $\sigma_{1}^{*}$ | 0.2 | 0.1934 | 0.00187 | 103.5146 | $1.34983 \times 10^{-21}$ |
| $\sigma_{2}^{*}$ | 0.3 | 0.2974 | $7.092 \times 10^{-4}$ | 419.34879 | $4.24367 \times 10^{-30}$ |
| $\rho$ | -0.2 | -0.13636 | 0.01829 | -7.45701 | $3.07326 \times 10^{-6}$ |

We tried many different starting values and the values presented here were the best. We see that estimates of $\gamma_{1}^{*}, \gamma_{2}^{*}, \sigma_{1}$ and $\sigma_{2}$ are very close to the actual values and the estimate of $\rho$ is a little away from the actual value. To evaluate the performance of the function " $\mathrm{nlfb}$ " for our situation, we need to carry out an extensive Monte Carlo simulation study which is beyond the scope of this paper. We would like to conclude this section by stating that non-linear least square minimization to estimate the five parameters in the two-factor Hull White model is a challenging problem even with most recently developed $R$ functions.

## 5 Model Validation

At a high level, model validation is about the process around actual modeling work. It specifies the business purposes for using the model and assesses and confirms whether:

- The model is "fit for purpose"
- The methods used are accepted practice and compliant with standards and regulation.

In the U.S. applicable guidance is in Actuarial Standard of Practice 56, Modeling, and American Academy of Actuaries Model Governance Practice Note, April 2017, pages 11-14.

Canadian practice is evolving from CALM to IFRS. CALM guidance is in "Calibration of Stochastic Risk-Free Interest Rate Models for Use in CALM Valuation", from the Canadian Institute of Actuaries' Committee for Life Insurance Financial Reporting (CIA, CLIFR), June 2021.

ASOP 56 Section 3.6 covers model risk, and outlines the process of model validation as a means of dealing with model risk. Section 3.6 breaks model validation into model testing (3.6.1) and model output validation (3.6.2).

The AAA practice note lays out review and model testing procedures. It begins with Design Use/Fit, about the business uses for the model and whether it is appropriate to use the particular model in those situations - whether it is "fit for purpose". Next is Design Methods/Processing - whether the methods used are accepted practice and compliant with standards and regulation. Explicitly stating the modeling work's purposes - stress testing, or setting prices as of a specific date, or showing realistic balance sheets and income statements into the future - will clarify certain design decisions. These issues were discussed in Sections 1.4 and 1.5 .

### 5.1 DATA AND ASSUMPTIONS

Whether input data is accurate, consistent, complete, and correctly loaded is a simple matter for the initial yield curve. In contrast, the mean reversion strength and target are assumptions that must be developed. There isn't one right answer; we will have to experiment, use judgement, and document our reasoning.

In Section 2.1.1 the Vasicek model was run. Opening the R function we see time and time step parameters (daily), plus the starting value, mean reversion speed, long term mean reversion target, and instantaneous volatility.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-78.jpg?height=287&width=1369&top_left_y=1861&top_left_x=321)

Above these were given, but in practice they must be estimated. This is done in section 3.1.1, where Example 6 works [24] Chapter 14 Question 5:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-79.jpg?height=786&width=950&top_left_y=263&top_left_x=319)

Notice how the gamma, rbar, and sigma code directly implement the formulas immediately preceding Example 6 in 3.1.1 above.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-79.jpg?height=1085&width=1166&top_left_y=1273&top_left_x=319)
model $=\operatorname{Im}\left(y^{\sim} x\right)$

mle.gamma= -log(as.numeric(model\$coefficients)[2])/Delta

mle.gamma

\#\# [1] 3.6453

mle.rbar = as.numeric(model\$coefficients)[1]/

(1-as.numeric(model\$coefficients)[2])

mle.rbar

\#\# [1] 0.30769

mle.sigma $=\operatorname{sigma}($ model $) *(2 *$ mle.gamma/

$(1$-as.numeric(model\$coefficients)[2]^2))^. 5

mle.sigma

\#\# [1] 1.8138

The practice notes advise us that the values of these parameters need to be accurate, consistent, in line with accepted practice and compliant with standards and regulation.

The short rate $\mathrm{r} 0$ will most likely be taken from the model start date's actual yield curve, with the same tenor (time to maturity) as the short rate used in calibration. The data used here is the one-month U.S. Treasury Bill rate.

The other parameters - short rate volatility (sigma), mean reversion strength (gamma), and long term mean reversion target (rbar) - are typically estimated from historical data. Rbar is estimated at $0.31 \%$ (rounded), which is low because the data is from the global financial crisis (GFC) period.

This model can be tested by using these values of gamma, rbar, and sigma to generate scenarios:

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-80.jpg?height=755&width=1010&top_left_y=1665&top_left_x=319)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-81.jpg?height=828&width=1013&top_left_y=261&top_left_x=320)

## Simulation performance based on 1000 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\sigma$ |
| Bias | 0.44992 | -0.00406 | 0.00138 |
| Standard <br> deviation | 0.98044 | 0.15718 | 0.02501 |
| Root mean <br> square | 1.0783 | 0.15715 | 0.02503 |
| Relative <br> Root mean <br> square | 0.2958 | 0.51074 | 0.0138 |

In the code, the matrix "mle" is the gamma, rbar, and sigma of each scenario. "bias" is the difference between the average gamma, rbar, and sigma, versus the gamma, rbar, and sigma estimated in Example 6, meaning this set of scenarios is "off" by that much. A bias very close to zero is desired. rbar and sigma appear to satisfy that, while gamma's bias is about 0.45 . Is that tolerable?

To assess this we consider the root mean squared error (RMSE), which is the average residual, or the average across all scenarios of how far the three parameters are from the line of best fit. If we found another model or another calibration with a lower RMSE it would be a better fit to the underlying data.

The RMSE for gamma also looks large at 1.078. However, RMSE scales with the data so again it is hard to know. Relative RMSE (RRMSE) normalizes RMSE against the actual value. An RRMSE above $30 \%$ is considered a poor fit. The value for gamma is borderline, but now rbar is assessed as a very poor fit. We need to adjust the model calibration.

### 5.2 INVESTIGATE THE DATA

The example being studied here is from Veronesi [24]. We see the data is a daily short rate series from January 2, 2008 to March 5, 2010. This is through the beginning of the GFC. The series begins with the rate drifting down from $3.09 \%$ to $1.56 \%$. On March 14, 2008, the rate jumps to $1.20 \%$, on March 18 to $0.71 \%$,
and on March 19 to $0.26 \%$. This is when Bear Stearns collapsed and was taken over by J.P. Morgan. On March 25 the rate jumped $+0.80 \%$ to $1.47 \%$. Later, on September 15, 2008, the rate jumps down from $1.37 \%$ to $0.36 \%$ when Lehman Brothers collapsed.

The Vasicek model is not designed to handle jumps like this. We will need to try fitting a different model, such as a regime switching model or a jump-diffusion version of CIR.

Continuing with this example and the Vasicek model for a moment, the data series ends on March 5, 2010, with a short rate of $0.11 \%$. The modeled interest rates are then projected forward from that point in time (cell J9 references cell C552, the continuously compounded version of the observed "nominal" short rate in B552). However, the data used to calibrate the model include $3 \%+$ rates from before the two major financial system shocks.

The modeler may make some design choices here. If a local model of very low rates is desired, the Vasicek model could be recalibrated using data beginning September 15, 2008. However, this series is unlikely to generate scenarios with rates in the $3 \%$ to $6 \%$ range that were the norm before the GFC.

Instead of daily data the modeler could choose to use monthly data from a much longer time span, say 1980 to present. This could be desirable if the model for which the scenarios are being generated will run with a monthly time step. However, that time span had generally declining rates, so the long-run mean reversion target $\bar{r}$ is unclear.

There is no one clear correct choice. This is the art of modeling.

### 5.3 RECALIBRATE

Download the rate data from the US Treasury Department's website ${ }^{4}$. Open it in Excel. Filter the data to eliminate rows with a blank or an ND in the one-month column. Convert semi-annual rates to effective annual rates. Create a new tab and copy the date and one-month rate column for the dates needed into it. Insert a simple header row, say Date and OneMonthTBill. Save as a .xlsx file.

In RStudio's top right window, Environment tab, select Import Dataset. R may want to install an updated readxl package. Browse for and select the downloaded rate data file. In Import Options (lower left), select the new sheet. Import.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-82.jpg?height=385&width=1157&top_left_y=1767&top_left_x=320)

${ }^{4}$ Market yield on U.S. Treasury securities at 1-month constant maturity, quoted on investment basis, series H15/H15/RIFLGFCM01_N.B can be selected from www.federalreserve.gov/DataDownload. Filtered data can be obtained directly at https://home.treasury.gov/resourcecenter/data-chart-center/interest-rates/TextView?type=daily treasury yield curve\&field tdr date value=all\&data=yieldAll.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-83.jpg?height=1954&width=1007&top_left_y=261&top_left_x=319)

We now have 1000 scenarios and want to evaluate whether they are a good fit relative to our calibrated parameters. To do this we'll calculate the CIR parameters implied by each scenario, and see whether on average they are close to our calibrated parameters. If so, then the set is valid and the calibration "worked".

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-84.jpg?height=974&width=960&top_left_y=263&top_left_x=319)

bias=rowMeans(euler.est-paras)

sd $=$ rowSds(euler.est)

rmse $=\left(\right.$ rowMeans $\left(\left(\text { euler.est-paras) }{ }^{\wedge} 2\right)\right)^{\wedge} 0.5$

rrmse $=\left(\left(\text { rowMeans }\left((\text { euler.est-paras })^{\wedge} 2\right)\right) /(\text { paras })\right)^{\wedge} 0.5$

The code above was adapted from Example 13 code. We started with r0 set to 2.741129, the first value in the data series, so we produce a set of scenarios "around" the historical data used for calibration. Across the 1000 scenarios, the gamma, rbar, and alpha compare to the calibration gamma, rbar, and alpha as follows:

## Simulation performance based on 1000 sample paths

|  | Parameter |  |  |
| :--- | ---: | ---: | ---: |
|  | $\gamma$ | $\bar{r}$ | $\alpha$ |
| Bias | 0.65112 | 0.00504 | -0.76063 |
| Standard <br> deviation | 2.36859 | 0.19081 | 0.48787 |
| Root mean <br> square | 2.45531 | 0.19078 | 0.90352 |
| Relative <br> Root mean <br> square | 1.16059 | 0.31244 | 0.32637 |

All three parameters show little bias, with rbar very close. The standard deviation across the 1000 scenarios is broader, which also shows up in the RMSE and relative RMSE metrics. Indeed, gamma and rbar have RRMSEs greater than 30\%, indicating a poor fit. Looking at the scenarios produced,

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-84.jpg?height=243&width=1391&top_left_y=2238&top_left_x=321)

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-85.jpg?height=932&width=957&top_left_y=255&top_left_x=516)

The scenarios show material dispersion during the first year, but they then settle down to extended low rates clustered in the $0 \%$ to $1.5 \%$ range. This is roughly the pattern of the historical data used for calibration, so the CIR model appears to produce scenarios in line with the calibration data, in this case. Calibrating to a historical dataset with higher or more variable rates might produce more dispersion in the scenario set. Alternatively, we notice the mean reversion strength gamma produced by our calibration is greater than 1.0. Reviewing the CIR model in equation (4), this could amplify volatility, which could be offset by the $\sqrt{\alpha r_{t}}$ volatility term. This emphasizes the need for assessing the scenario set produced by the model. Alternatively it is usable with the caveat that the scenario set only spans scenarios in a regime like 2017 to 2019 U.S. rates, but not scenarios from a different regime.

### 5.4 VALIDATE

Assuming that the scenario set is appropriate for the modeling work to be undertaken, we proceed to complete the validation process.

The Practical Guide [1] Section 6.3 explores desirable properties for a set of economic scenarios. Focusing on government yield curve projections, we assess the properties of our scenario set:

1. Yields for longer maturities are usually greater than yields for shorter maturities, i.e. the yield curve is "upward sloping".
2. The volatility of short maturity yields tends to be greater than long maturity yields - but not during periods of central bank intervention.
3. Short and long maturity yields are highly correlated.
4. When short rates are low, long rates tend to be greater than short rates.
5. When short rates are high, long rates tend to be lower than short rates (i.e., the yield curve is said to be "inverted"). The above properties are not applicable for a one-factor short rate model, and point to the need to consider two-factor and other models.
6. Negative short rates are possible. The scenarios generated here do not span negative rates but they do produce many scenarios with rates close to zero.
7. Higher rates occur but do not persist for long. The scenarios generated here do not probe higher rates. The highest rate scenario at the one year point gets to about $6 \%$ and then reverts toward the mean reversion target of $0.37 \%$.

Further stylized facts can be considered for corporate bond yields or spreads, equity market scenarios, and inflation and other economic variables. These are beyond the scope of models considered in this paper.

The following considerations may also apply:

1. Actual Results - is this model similar to others? We know that Vasicek and CIR scenario sets don't model long rates, inverted yield curves, or very low or high rate paths.
2. Evaluate with benchmarking and replication (static validation, parallel testing, spreadsheet replica). The Veronesi spreadsheet plots a zero-volatility trend developed in column J.
3. Evaluate with outcome analysis (dynamic replication, back-testing, out-of-sample testing). By about day 80 of the historical data, actual short rates went to zero as the central bank responded to the COVID-19 pandemic. The Vasicek scenarios did not encompass such an outcome, while the CIR scenarios seem to do so.
4. Sound/Stable Results - are results sound and stable across a range of use and scenarios? The scenarios are quite stable.
5. Stress, sensitivity, or extreme value testing. A test scenario set with gamma reduced or alpha increased may conform better to stylized facts, and would be worth exploring.
6. Dependencies and correlations - how is inflation correlated with the short rate? Should the inflation assumption in the broader model be linked to the interest rate scenario set, perhaps with a lag?

### 5.5 MODEL GOVERNANCE

As of this writing, standard practice is to submit model assumptions and design choices to a Model Governance Committee. The choices of model, data series, time steps, and the implications should be listed and described in accordance with applicable standards of practice. They then are submitted to the Model Governance Committee or the Principal sponsoring the work assignment for discussion and acceptance or further investigation. This aligns with standards of practice that a) results should be communicated in a useful and understandable way, and b) the model is appropriately documented and governed. Generally the interest rate or economic scenario model would be run as part of a larger modeling process, so documentation and review and acceptance may be part of the larger modeling effort.

A word of encouragement on documentation. We know we should do it, and standards of practice such as ASOP 56 Modeling, section 3.7 in the U.S. recommend it. Yet as a new procedure is developed it is unclear what to write, and as deadlines approach documentation falls by the wayside. Don't let the perfect be the enemy of the good. As the work progresses write down the project objectives, then the data sources, then the data transforms and loads, then the run procedure and results interpretation, then why the model is plausible. Do this as work proceeds. You will have a solid start at documentation! Then the next time the process is run, refine the documentation. Last, check back to the standards of practice and add an item or two to ensure compliance.

## 6 Conclusion

Each model has issues which become apparent when fit to an actual historical data series or a specific yield curve. In Section 5 we saw that the one-factor models have difficulty fitting historical data where exogenous shocks caused discontinuities, or "jumps", in the data series. Adding a random jump term can be done, at the cost of additional complexity. The practitioner can also test the two-factor Vasicek model with correlated factors and the two-factor Hull-White model, as explored in Section 4. Both of these models are in the class of G2++ models, which can be explored further in [6] section 4.2. Ultimately the choice of model and calibration data comes down to art and professional judgement. Real world data is messy, with exogenous shocks from political shifts, central bank intervention, geopolitical events, and more. There's no one right answer, but rather informed choices and trade-offs. That's what makes it interesting. Best wishes.

![](https://cdn.mathpix.com/cropped/2024_04_15_1550fc49de49f4302507g-87.jpg?height=252&width=1523&top_left_y=2254&top_left_x=301)

## 7 Acknowledgments

The researchers' deepest gratitude goes to those without whose efforts this project could not have come to fruition: the Project Oversight Group and others for their diligent work in reviewing and editing this report for accuracy and relevance. Project Oversight Group members:

Ted Chang, FSA, MAAA, PhD

Gary Hatfield, FSA, MAAA, CFA, PhD

Jason Kehrberg, FSA, MAAA, PhD

Paul Ngai, FSA, FCIA

At the Society of Actuaries:

Doug Chandler, FSA FCIA

The volunteers who generously shared their wisdom, insights, advice, guidance, and arm's-length review of this study prior to publication. Any opinions expressed may not reflect their opinions nor those of their employers. Any errors belong to the authors alone.

Steve Strommen, FSA, MAAA

## References

[1] Economic Scenario Generators: A Practical Guide. Society of Actuaries, 2016.

[2] Leif BG Andersen. Efficient simulation of the Heston stochastic volatility model. Available at SSRN 946405, 2007.

[3] David F Babbel and Frank J Fabozzi. Investment management for insurers, volume 43. John Wiley \& Sons, 1999.

[4] Jean-François Bégin. Economic scenario generator and parameter uncertainty: A Bayesian approach. ASTIN Bulletin: The Journal of the IAA, 49(2):335-372, 2019.

[5] Victor Bernal. Calibration of the Vasicek model: a step by step guide. 2016.

[6] Damiano Brigo and Fabio Mercurio. Interest rate models - theory and practice. Springer Finance. Springer, Berlin, Germany, 2 edition, Aug 2007.

[7] Kalok C Chan, G Andrew Karolyi, Francis A Longstaff, and Anthony B Sanders. An empirical comparison of alternative models of the short-term interest rate. The Journal of Finance, 47(3):1209-1227, 1992.

[8] Eric Chin, Sverrir Olafsson, and Dian Nel. Problems and Solutions in Mathematical Finance, Volume 1: Stochastic Calculus. John Wiley \& Sons, 2014.

[9] Rama Cont. Encyclopedia of quantitative finance. Wiley, 2010.

[10] John Cox, Jonathan Ingersoll, and Stephen Ross. A theory of the term structure of interest rates. Econometrica, 53:385-407, 021985.

[11] J. L. Doob. The Brownian Movement and Stochastic Equations, volume 43. Annals of Mathematics, 1942.

[12] Daniel Dufresne, Felisa Vázquez-Abad, and Stephen Chin. Change of measure for the square-root process. In Proceedings of the Winter Simulation Conference 2014, pages 465-475, 2014.

[13] William Feller. Two singular diffusion problems. Annals of Mathematics, 54(1):173-182, 1951.

[14] David M Gay. Usage summary for selected optimization routines. Computing Science Technical Report 153, AT\&T Bell Laboratories, Murray Hill, NJ 07974, October 1990.

[15] James Douglas Hamilton. Time Series analysis. Princeton University Press, 1994.

[16] Lars Peter Hansen. Large sample properties of generalized method of moments estimators. Econometrica: Journal of the econometric society, pages 1029-1054, 1982.

[17] Stefano M lacus. Simulation and inference for stochastic differential equations: with $R$ examples, volume 486. Springer, 2008.

[18] Norman L Johnson, Samuel Kotz, and Narayanaswamy Balakrishnan. Continuous univariate distributions, volume 2, volume 289. John Wiley \& Sons, 1995.

[19] Giuseppe Orlando, Rosa Mininni, and Michele Bufalo. Interest rates calibration with a CIR model. The Journal of Risk Finance, 20(4):370-387, 2019.

[20] Giuseppe Orlando, Rosa Maria Mininni, and Michele Bufalo. Forecasting interest rates through Vasicek and CIR models: A partitioning approach. Journal of Forecasting, 39(4):569-579, July 2020.

[21] Hansen Pei. Mean-Reverting Spread Modeling: Caveats in Calibrating the OU Process. Hudson and Thames Research, August 2021.

[22] Christian Ritz and Jens Carl Streibig. Nonlinear regression with R. Springer, 2008.

[23] Stephen J. Strommen. Understanding the Connection Between Real-World and Risk-Neutral Scenario Generators. Society of Actuaries, 2022.

[24] Pietro Veronesi. Fixed income securities: Valuation, risk, and risk management. John Wiley \& Sons, 2010.

## Appendix A: Zero coupon bond prices under one-factor Vasicek model

Under one factor Vasicek model zero-coupon bond prices are given by:

$$
\begin{aligned}
& Z(r, t ; T)=e^{A(t ; T)-B(t ; T) r} \\
& B(t ; T)=\frac{1}{\gamma^{*}}\left(1-e^{-\gamma^{*}(T-t)}\right) \\
& A(t ; T)=(B(t ; T)-(T-t))\left(\bar{r}^{*}-\frac{\sigma^{2}}{2\left(\gamma^{*}\right)^{2}}\right)-\frac{\sigma^{2} B(t ; T)^{2}}{4 \gamma^{*}}
\end{aligned}
$$

Note that we are using parameters $\gamma^{*}$ and $\bar{r}^{*}$ to indicate the drift of the SDE for $r_{t}, \gamma^{*}\left(\bar{r}^{*}-r_{t}\right)$ in the riskneutral world, as opposed to parameters $\gamma$ and $\bar{r}$ with the drift of $\gamma\left(\bar{r}-r_{t}\right)$ in the real world.

When we fit these to market bond prices we need to use a numerical search algorithm. As [24] points out in many places it is possible to get negative values for the parameter $\gamma^{*}$ so we must look at the behaviour of the bond price function in the neighbourhood of $\gamma^{*}=0$. We see that $B(t ; T)$ is a continuous function with the limit of $\gamma \rightarrow 0$ being $(T-t)$. However, we see that calculating the limiting value of $A(t ; T)$ as $\gamma^{*} \rightarrow 0$ is zero is not an easy task based on [24] (15.30), but with some calculus we can prove that $A(t ; T)$ is discontinuous at $\gamma^{*}=0$. So if we do not address this properly in the implementation of numerical optimizations, we may end up getting wrong values. To calculate the bond price formula when $\gamma^{*}=0$ takes some effort. For this we can either use the fact that when $\gamma^{*}=0$ the Vasicek model reduces to a zero-drift Ho-Lee model and then using [24] (19.8)-(19.9), or we can use the following approach.

First notice that bond prices are given by:

$$
Z\left(r_{t}, t ; T\right)=E^{\mathbb{Q}}\left[\exp \left(-\int_{t}^{T} r_{s} d s\right) \mid r_{t}\right]
$$

In the risk-neutral world the SDE of $r_{t}$ is given as:

$$
d r_{t}=\gamma^{*}\left(\bar{r}^{*}-r_{t}\right) d t+\sigma d X_{t}
$$

The solution of the above SDE takes the following form:

$$
r_{t+s}=r_{t} \exp \left(-\gamma^{*} s\right)+\bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right)+\sigma \exp \left(-\gamma^{*} s\right) \int_{0}^{s} \exp \left(\gamma^{*} u\right) d X_{u}
$$

From this we can obtain:

$$
\begin{aligned}
\int_{0}^{T-t} r_{t+s} d s= & r_{t} \int_{0}^{T-t} \exp \left(-\gamma^{*} s\right) d s+\int_{0}^{T-t} \bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right) d s+ \\
& \int_{0}^{T-t} \sigma \exp \left(-\gamma^{*} s\right)\left(\int_{u=0}^{s} \exp \left(\gamma^{*} u\right) d X_{u}\right) d s
\end{aligned}
$$

Using Stochastic Fubini's theorem,

$$
\begin{aligned}
\int_{0}^{T-t} r_{t+s} d s= & r_{t} \int_{0}^{T-t} \exp \left(-\gamma^{*} s\right) d s+\int_{0}^{T-t} \bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right) d s+ \\
& \int_{u=0}^{T-t} \sigma \exp \left(\gamma^{*} u\right)\left(\int_{s=u}^{T-t} \exp \left(-\gamma^{*} s\right) d s\right) d X_{u}, \\
\int_{t}^{T} r_{s} d s= & r_{t} \int_{0}^{T-t} \exp \left(-\gamma^{*} s\right) d s+\int_{0}^{T-t} \bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right) d s+ \\
& \int_{u=0}^{T-t} \sigma \exp \left(\gamma^{*} u\right)\left(\int_{s=u}^{T-t} \exp \left(-\gamma^{*} s\right) d s\right) d X_{u},
\end{aligned}
$$

Since $\int_{t}^{T} r_{s} d s \mid r_{t}$ is a normal random variable the bond pricing formula reduces to:

$$
Z\left(r_{t}, t ; T\right)=\exp \left[\mathbb{E}^{\mathbb{Q}}\left(-\int_{t}^{T} r_{s} d s \mid r_{t}\right)+\frac{1}{2} \mathbb{V} a r^{\mathbb{Q}}\left(-\int_{t}^{T} r_{s} d s \mid r_{t}\right)\right]
$$

But:

$$
\begin{aligned}
& \mathbb{E}^{\mathbb{Q}}\left(-\int_{t}^{T} r_{s} d s \mid r_{t}\right)=-r_{t} \int_{0}^{T-t} \exp \left(-\gamma^{*} s\right) d s-\int_{0}^{T-t} \bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right) d s \\
& \mathbb{V a r} \\
& \mathbb{Q}\left(-\int_{t}^{T} r_{s} d s \mid r_{t}\right)=\sigma^{2} \int_{u=0}^{T-t} \exp \left(2 \gamma^{*} u\right)\left(\int_{s=u}^{T-t} \exp \left(-\gamma^{*} s\right) d s\right)^{2} d u,
\end{aligned}
$$

where the first equation follows from the fact that expectation of the Itô integral is zero and the second equation follows from Itô isometry. By comparing (12) with the [24] (15.28)-(15.30) we see that:

$$
\begin{aligned}
B(t ; T) & =\int_{0}^{T-t} \exp \left(-\gamma^{*} s\right) d s \\
A(t ; T) & =-\int_{0}^{T-t} \bar{r}^{*}\left(1-\exp \left(-\gamma^{*} s\right)\right) d s+\frac{\sigma^{2}}{2} \int_{u=0}^{T-t} \exp \left(2 \gamma^{*} u\right)\left(\int_{s=u}^{T-t} \exp \left(-\gamma^{*} s\right) d s\right)^{2} d u
\end{aligned}
$$

Readers are encouraged to verify that when $\gamma^{*} \neq 0$ the above integrals simplify to [24] (15.29) and (15.30). Now we can easily calculate values of $B(t ; T)$ and $A(t ; T)$ when $\gamma^{*}=0$ by substituting $\gamma^{*}=0$ in the above:

$$
\begin{aligned}
B(t ; T) & =\int_{0}^{T-t} d s \\
& =(T-t) \\
A(t ; T) & =\frac{\sigma^{2}}{2} \int_{u=0}^{T-t}\left(\int_{s=u}^{T-t} d s\right)^{2} d u \\
& =\frac{\sigma^{2}(T-t)^{3}}{6}
\end{aligned}
$$

Note that when $\gamma^{*}=0$ the model is a Ho-Lee model with zero drift and our result agrees with [24] (19.9).

## Appendix B: Zero coupon bond prices under the two-factor Vasicek model

This model can be written as the short rate process written as the sum of two factors, a short rate factor and a long rate factor:

$$
r_{t}=\phi_{1, t}+\phi_{2, t}
$$

where each factor follows the following SDEs:

$$
d \phi_{i, t}=\gamma_{i}\left(\vec{\phi}_{i}-\phi_{i, t}\right) d t+\sigma_{i} d X_{i, t}, \quad i=1,2
$$

With a few lines of algebra we can obtain the solution to these SDEs as follows:

$$
\phi_{i, t+s}=\phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right)+\sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}, \quad i=1,2
$$

The conditional means and variance of these two factors are given by:

$$
\begin{aligned}
E\left[\phi_{i, t+s} \mid \phi_{i, t}\right] & =\phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right) \\
\operatorname{Var}\left[\phi_{i, t+s} \mid \phi_{i, t}\right] & =\operatorname{Var}\left[\sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}, i=1,2\right. \\
& =\sigma_{i}^{2} \exp \left(-2 \gamma_{i} s\right) \int_{0}^{s} \exp \left(2 \gamma_{i} v\right) d v \\
& =\frac{\sigma_{i}^{2}}{2 \gamma_{i}}\left(1-\exp \left(-2 \gamma_{i} s\right)\right)
\end{aligned}
$$

where the second to last equation follows from the Itô isometry. The conditional covariance between $\phi_{1, t+s}$ and $\phi_{2, t+s}$ conditioned on $\phi_{i, t}, i=1,2$ is given by:

$$
\begin{aligned}
\operatorname{Cov}\left[\phi_{1, t+s}, \phi_{2, t+s} \mid \phi_{1, t}, \phi_{1, t}\right] & =E\left[\sigma_{1} \exp \left(-\gamma_{1} s\right) \int_{0}^{s} \exp \left(\gamma_{1} v\right) d X_{1, v} \sigma_{2} \exp \left(-\gamma_{2} s\right) \int_{0}^{s} \exp \left(\gamma_{2} u\right) d X_{2, u}\right] \\
& =\rho \sigma_{1} \sigma_{2} \exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right) \int_{0}^{s} \exp \left(-\left(\gamma_{1}+\gamma_{2}\right) v\right) d v \\
& =\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)
\end{aligned}
$$

The conditional correlation coefficient between $\phi_{1, t+s}$ and $\phi_{2, t+s}$, which can be denoted as $\rho(s)$, is given by:

$$
\begin{aligned}
\operatorname{Corr}\left[\phi_{1, t+s}, \phi_{2, t+s} \mid \phi_{1, t}, \phi_{1, t}\right] & =\frac{\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)}{\sqrt{\frac{\sigma_{1}^{2}}{2 \gamma_{1}}\left(1-\exp \left(-2 \gamma_{1} s\right)\right) \frac{\sigma_{2}^{2}}{2 \gamma_{2}}\left(1-\exp \left(-2 \gamma_{2} s\right)\right)}} \\
\rho(s) & =\rho\left(\frac{4 \gamma_{1} \gamma_{2}}{\left(\gamma_{1}+\gamma_{2}\right)^{2}} \frac{\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)^{2}}{\left(1-\exp \left(-2 \gamma_{1} s\right)\right)\left(1-\exp \left(-2 \gamma_{2} s\right)\right)}\right) \\
& =\rho\left(\frac{4 \gamma_{1} \gamma_{2}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right) s\right)\right)^{2}}{\left(\gamma_{1}+\gamma_{2}\right)^{2}\left(1-\exp \left(-2 \gamma_{1} s\right)\right)\left(1-\exp \left(-2 \gamma_{2} s\right)\right)}\right)
\end{aligned}
$$

The zero-coupon bond prices can be calculated by evaluating:

$$
Z\left(r_{t}, t ; T\right)=E^{\mathbb{Q}}\left[\exp \left(-\int_{t}^{T} r_{s} d s\right) \mid r_{t}\right]
$$

Since $r_{t}=\phi_{1, t}+\phi_{2, t}$ let us look at obtaining $\int_{t}^{s} \phi_{i, u} d u$ first:

$$
\begin{aligned}
\phi_{i, t+s}= & \phi_{i, t} \exp \left(-\gamma_{i} s\right)+\vec{\phi}_{i}\left(1-\exp \left(-\gamma_{i} s\right)\right)+\sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}, \quad i=1,2 . \\
\int_{0}^{T-t} \phi_{i, t+s} d s= & \phi_{i, t} \int_{0}^{T-t} \exp \left(-\gamma_{i} s\right) d s+\vec{\phi}_{i} \int_{0}^{T-t}\left(1-\exp \left(-\gamma_{i} s\right)\right) d s \\
& +\int_{0}^{T-t} \sigma_{i} \exp \left(-\gamma_{i} s\right) \int_{0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v} d s
\end{aligned}
$$

Using the stochastic Fubini's lemma we can exchange the order of the last integral:

$$
\int_{s=0}^{T-t} \sigma_{i} \exp \left(-\gamma_{i} s\right)\left(\int_{v=0}^{s} \exp \left(\gamma_{i} v\right) d X_{i, v}\right) d s=\sigma_{i} \int_{v=0}^{T-t} \exp \left(\gamma_{i} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{i} s\right) d s\right) d X_{i, v}
$$

Now we see that all three integrals can be simplified when $\gamma_{i} \neq 0$ and when $\gamma_{i}=0$. However we leave them as it is for now and observe the following. Each integral is a normally distributed random variable and the means, variances and covariances are given as below:

$$
\begin{aligned}
E\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =\phi_{i, t} \int_{0}^{T-t} \exp \left(-\gamma_{i} s\right) d s+\vec{\phi}_{i} \int_{0}^{T-t}\left(1-\exp \left(-\gamma_{i} s\right)\right) d s, \quad i=1,2, \\
\operatorname{Var}\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =\sigma_{i}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{i} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{i} s\right) d s\right)^{2} d v, \quad i=1,2,
\end{aligned}
$$

When $\gamma_{i} \neq 0$ the above integrals simplify to:

$$
\begin{aligned}
E\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =\phi_{i, t} \frac{1}{\gamma_{i}}\left(1-\exp \left(-\gamma_{i}(T-t)\right)\right)-\vec{\phi}_{i}\left(\frac{1-\exp \left(-\gamma_{i}(T-t)\right)}{\gamma_{i}}-(T-t)\right) \\
\operatorname{Var}\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =\sigma_{i}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{i} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{i} s\right) d s\right)^{2} d v \\
& =\sigma_{i}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{i} v\right)\left(\frac{\exp \left(-\gamma_{i} v\right)-\exp \left(-\gamma_{i}(T-t)\right)}{\gamma_{i}}\right)^{2} d v \\
& =-\sigma_{i}^{2}\left[\frac{1}{\gamma_{i}^{2}}\left(\frac{1-\exp \left(-\gamma_{i}(T-t)\right)}{\gamma_{i}}-(T-t)\right)+\frac{1}{2 \gamma_{i}}\left(\frac{1-\exp \left(-\gamma_{i}(T-t)\right)}{\gamma_{i}}\right)^{2}\right]
\end{aligned}
$$

By defining $B_{i}(t ; T)$ as in [24],

$$
B_{i}(t ; T)=\frac{1}{\gamma_{i}}\left(1-\exp \left(-\gamma_{i}(T-t)\right)\right), \quad i=1,2
$$

we can write:

$$
\begin{aligned}
E\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =\phi_{i, t} B_{i}(t, T)-\vec{\phi}_{i}\left(B_{i}(t, T)-(T-t)\right) \\
\operatorname{Var}\left[\int_{t}^{T} \phi_{i, s} d s \mid r_{t}\right] & =-\sigma_{i}^{2}\left[\frac{1}{\gamma_{i}^{2}}\left(B_{i}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{i}} B_{i}(t, T)^{2}\right]
\end{aligned}
$$

Let us simplify the conditional covariance between $\int_{t}^{T} \phi_{1, s} d s$ and $\int_{t}^{T} \phi_{2, s} d s$ conditioned on $r_{t}$.

$$
\begin{aligned}
& \operatorname{Cov}\left[\int_{t}^{T} \phi_{1, s} d s, \int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right] \\
& \quad=\rho \sigma_{1} \sigma_{2} \int_{v=0}^{T-t} \exp \left(\left(\gamma_{1}+\gamma_{2}\right) v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{1} s\right) d s\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{2} s\right) d s\right) d v
\end{aligned}
$$

when $\gamma_{i} \neq 0$ for $i=1,2$ the above integral can be evaluated as:

$$
\begin{aligned}
\operatorname{Cov} & {\left[\int_{t}^{T} \phi_{1, s} d s, \int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right] } \\
= & \rho \sigma_{1} \sigma_{2} \int_{v=0}^{T-t} \exp \left(\left(\gamma_{1}+\gamma_{2}\right) v\right)\left(\frac{\exp \left(-\gamma_{1} v\right)-\exp \left(-\gamma_{1}(T-t)\right)}{\gamma_{1}}\right)\left(\frac{\exp \left(-\gamma_{2} v\right)-\exp \left(-\gamma_{2}(T-t)\right)}{\gamma_{2}}\right) d v \\
= & -\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[\left(\frac{1-\exp \left(-\gamma_{1}(T-t)\right)}{\gamma_{1}}-(T-t)\right)+\left(\frac{1-\exp \left(-\gamma_{2}(T-t)\right)}{\gamma_{2}}-(T-t)\right)\right. \\
& \left.-\left(\frac{1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right)(T-t)\right)}{\gamma_{1}+\gamma_{2}}-(T-t)\right)\right]
\end{aligned}
$$

By writing:

$$
B_{3}(t ; T)=\frac{1}{\gamma_{1}+\gamma_{2}}\left(1-\exp \left(-\left(\gamma_{1}+\gamma_{2}\right)(T-t)\right)\right)
$$

we can rewrite the above expression for covariance as below:

$$
\begin{aligned}
& \operatorname{Cov}\left[\int_{t}^{T} \phi_{1, s} d s, \int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right] \\
& =-\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[B_{1}(t, T)+B_{2}(t, T)-B_{3}(t, T)-(T-t)\right]
\end{aligned}
$$

As [6] explains the

$$
Z\left(r_{t}, t ; T\right)=\exp \left(E^{\mathbb{Q}}\left[-\int_{t}^{T} r_{s} d s \mid r_{t}\right]+\frac{1}{2} V A R^{\mathbb{Q}}\left[-\int_{t}^{T} r_{s} d s \mid r_{t}\right]\right)
$$

But

$$
\begin{aligned}
\mathbb{E}^{\mathbb{Q}}\left[-\int_{t}^{T} r_{s} d s \mid r_{t}\right]= & \mathbb{E}^{\mathbb{Q}}\left[-\int_{t}^{T}\left(\phi_{1, s}+\phi_{2, s}\right) d s \mid r_{t}\right] \\
= & \mathbb{E}^{\mathbb{Q}}\left[-\int_{t}^{T}\left(\phi_{1, s}+\phi_{2, s}\right) d s \mid r_{t}\right] \\
= & -\mathbb{E}^{\mathbb{Q}}\left[\int_{t}^{T} \phi_{1, s} d s \mid r_{t}\right]-\mathbb{E}^{\mathbb{Q}}\left[\int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right] \\
= & -\phi_{1, t} B_{1}(t, T)-\vec{\phi}_{1}\left(B_{1}(t, T)-(T-t)\right) \\
\operatorname{Var}^{\mathbb{Q}}\left[-\int_{t}^{T}{ }^{\left.r_{s} d s \mid r_{t}\right]}=\right. & \operatorname{Var}^{\mathbb{Q}}\left[-\int_{t, t}\left(\phi_{1, s}+\phi_{2, s}\right) d s \mid r_{t}\right] \\
= & \operatorname{Var}^{\mathbb{Q}}\left[\int_{t}^{T} \phi_{1, s} d s \mid r_{t}\right]+\operatorname{Var}{ }^{\mathbb{Q}}\left[\int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right]+2 C o v\left[\int_{t}^{T} \phi_{1, s} d s, \int_{t}^{T} \phi_{2, s} d s \mid r_{t}\right] \\
= & -\sigma_{1}^{2}\left[\frac{1}{\gamma_{1}^{2}}\left(B_{1}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{1}} B_{1}(t, T)^{2}\right] \\
& -\sigma_{2}^{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t, T)^{2}\right] \\
& -\frac{2 \rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[B_{1}(t, T)+B_{2}(t, T)-B_{3}(t, T)-(T-t)\right]
\end{aligned}
$$

Therefore:

$$
\begin{aligned}
\mathbb{E}^{\mathbb{Q}}[ & \left.-\int_{t}^{T} r_{s} d s \mid r_{t}\right]+\frac{1}{2} V a r^{\mathbb{Q}}\left[-\int_{t}^{T} r_{s} d s \mid r_{t}\right] \\
= & -\phi_{1, t} B_{1}(t, T)-\phi_{2, t} B_{2}(t, T) \\
& +\vec{\phi}_{1}\left(B_{1}(t, T)-(T-t)\right)-\frac{\sigma_{1}^{2}}{2}\left[\frac{1}{\gamma_{1}^{2}}\left(B_{1}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{1}} B_{1}(t, T)^{2}\right] \\
& +\vec{\phi}_{2}\left(B_{2}(t, T)-(T-t)\right)-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t, T)^{2}\right] \\
& -\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[B_{1}(t, T)+B_{2}(t, T)-B_{3}(t, T)-(T-t)\right]
\end{aligned}
$$

However [24] writes zero-coupon bond prices as:

$$
Z\left(\phi_{1, t}, \phi_{2, t}, t ; T\right)=\exp \left(A(t, T)-\phi_{1, t} B_{1}(t, T)-\phi_{2, t} B_{2}(t, T)\right)
$$

Therefore:

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{1}\left(B_{1}(t, T)-(T-t)\right)-\frac{\sigma_{1}^{2}}{2}\left[\frac{1}{\gamma_{1}^{2}}\left(B_{1}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{1}} B_{1}(t, T)^{2}\right] \\
& +\vec{\phi}_{2}\left(B_{2}(t, T)-(T-t)\right)-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t, T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t, T)^{2}\right] \\
& -\frac{\rho \sigma_{1} \sigma_{2}}{\gamma_{1} \gamma_{2}}\left[B_{1}(t, T)+B_{2}(t, T)-B_{3}(t, T)-(T-t)\right]
\end{aligned}
$$

Since:

$$
B_{i}(t ; T)=\int_{0}^{T-t} \exp \left(-\gamma_{i} s\right) d s, \quad i=1,2,3
$$

it is obvious that $B_{i}(t ; T), i=1,2,3$ are continuous in the neighbourhood of $\gamma_{i}=0$ and its value at $\gamma_{i}=0$ is $T-t$. However, $A(t ; T)$ is not continuous around $\gamma_{i}=0$ for $i=1$ or $i=2$ and the function has to be evaluated using its integral expression.

$$
\begin{aligned}
A(t ; T)= & -\vec{\phi}_{1} \int_{0}^{T-t}\left(1-\exp \left(-\gamma_{1} s\right)\right) d s-\vec{\phi}_{2} \int_{0}^{T-t}\left(1-\exp \left(-\gamma_{2} s\right)\right) d s \\
& +\frac{1}{2}\left[\sigma_{1}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{1} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{1} s\right) d s\right)^{2} d v\right] \\
& +\frac{1}{2}\left[\sigma_{2}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{2} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{2} s\right) d s\right)^{2} d v\right] \\
& +\rho \sigma_{1} \sigma_{2} \int_{v=0}^{T-t} \exp \left(\left(\gamma_{1}+\gamma_{2}\right) v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{1} s\right) d s\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{2} s\right) d s\right) d v
\end{aligned}
$$

Therefore if $\gamma_{1}=0$ and $\gamma_{2} \neq 0 A(t ; T)$ becomes:

$$
\begin{aligned}
A(t ; T)= & -\vec{\phi}_{2} \int_{0}^{T-t}\left(1-\exp \left(-\gamma_{2} s\right)\right) d s \\
& +\frac{1}{2}\left[\sigma_{1}^{2} \int_{v=0}^{T-t}\left(\int_{s=v}^{T-t} d s\right)^{2} d v\right] \\
& +\frac{1}{2}\left[\sigma_{2}^{2} \int_{v=0}^{T-t} \exp \left(2 \gamma_{2} v\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{2} s\right) d s\right)^{2} d v\right] \\
& +\rho \sigma_{1} \sigma_{2} \int_{v=0}^{T-t} \exp \left(\gamma_{2} v\right)\left(\int_{s=v}^{T-t} d s\right)\left(\int_{s=v}^{T-t} \exp \left(-\gamma_{2} s\right) d s\right) d v
\end{aligned}
$$

Upon simplification we obtain:

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{2}\left(B_{2}(t ; T)-(T-t)\right)+\sigma_{1}^{2} \frac{(T-t)^{3}}{6}-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t ; T)^{2}\right] \\
& +\rho \sigma_{1} \sigma_{2}\left[\frac{(T-t)^{2}}{2}+\frac{\exp \left(-\gamma_{2}(T-t)\right)\left(\gamma_{2}(T-t)+1\right)-1}{\gamma_{2}^{2}}\right]
\end{aligned}
$$

By symmetry when $\gamma_{1} \neq 0$ and $\gamma_{2}=0$, the expression for $A(t ; T)$ simplifies to:

$$
\begin{aligned}
A(t ; T)= & \vec{\phi}_{2}\left(B_{2}(t ; T)-(T-t)\right)+\sigma_{1}^{2} \frac{(T-t)^{3}}{6}-\frac{\sigma_{2}^{2}}{2}\left[\frac{1}{\gamma_{2}^{2}}\left(B_{2}(t ; T)-(T-t)\right)+\frac{1}{2 \gamma_{2}} B_{2}(t ; T)^{2}\right] \\
& +\rho \sigma_{1} \sigma_{2}\left[\frac{(T-t)^{2}}{2}+\frac{\exp \left(-\gamma_{2}(T-t)\right)\left(\gamma_{2}(T-t)+1\right)-1}{\gamma_{2}^{2}}\right]
\end{aligned}
$$

When both $\gamma_{1}=0$ and $\gamma_{2}=0$ the integral for $A(t ; T)$ becomes:

$$
\begin{aligned}
A(t ; T)= & \frac{1}{2}\left[\sigma_{1}^{2} \int_{v=0}^{T-t}\left(\int_{s=v}^{T-t} d s\right)^{2} d v\right]+\frac{1}{2}\left[\sigma_{2}^{2} \int_{v=0}^{T-t}\left(\int_{s=v}^{T-t} d s\right)^{2} d v\right] \\
& +\rho \sigma_{1} \sigma_{2} \int_{v=0}^{T-t}\left(\int_{s=v}^{T-t} d s\right)\left(\int_{s=v}^{T-t} d s\right) d v
\end{aligned}
$$

Which simplifies to:

$$
A(t ; T)=\left(\sigma_{1}^{2}+\sigma_{2}^{2}+2 \rho \sigma_{1} \sigma_{2}\right) \frac{(T-t)^{3}}{6}
$$

## About The Society of Actuaries Research Institute

Serving as the research arm of the Society of Actuaries (SOA), the SOA Research Institute provides objective, datadriven research bringing together tried and true practices and future-focused approaches to address societal challenges and your business needs. The Institute provides trusted knowledge, extensive experience and new technologies to help effectively identify, predict and manage risks.

Representing the thousands of actuaries who help conduct critical research, the SOA Research Institute provides clarity and solutions on risks and societal challenges. The Institute connects actuaries, academics, employers, the insurance industry, regulators, research partners, foundations and research institutions, sponsors and nongovernmental organizations, building an effective network which provides support, knowledge and expertise regarding the management of risk to benefit the industry and the public.

Managed by experienced actuaries and research experts from a broad range of industries, the SOA Research Institute creates, funds, develops and distributes research to elevate actuaries as leaders in measuring and managing risk. These efforts include studies, essay collections, webcasts, research papers, survey reports, and original research on topics impacting society.

Harnessing its peer-reviewed research, leading-edge technologies, new data tools and innovative practices, the Institute seeks to understand the underlying causes of risk and the possible outcomes. The Institute develops objective research spanning a variety of topics with its strategic research programs: aging and retirement; actuarial innovation and technology; mortality and longevity; diversity, equity and inclusion; health care cost trends; and catastrophe and climate risk. The Institute has a large volume of topical research available, including an expanding collection of international and market-specific research, experience studies, models and timely research.


[^0]:    ${ }^{1}$ https://home.treasury.gov/policy-issues/_nancing-the-government/interest-rate-statistics/interest-ratesfrequently-asked-questions

[^1]:    ${ }^{3}$ An Ornstein-Uhlenbeck process is a Weiner process (random walk) modified so that it mean-reverts.

