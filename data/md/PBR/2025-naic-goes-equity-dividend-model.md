# 2025 NAIC GOES - Equity and Dividend Model

Author: ©2025 Conning, Inc. Conning, Inc

## NAIC Basic Data Set

The Basic Data Set provided free of charge to insurers is the standard scenario file set delivered as part of the NAIC scenario service. Users can access the scenarios online by downloading a file containing stochastic scenarios from the GEMS ${ }^{\text {® }}$ Economic Scenario Generator (ESG) for real-world interest rates, equity and bond fund returns. The typical application for these scenarios is in calculations of life and annuity Statutory reserves according to the Valuation Manual (e.g., VM-20, VM-21) and capital under the NAIC RBC requirements (e.g., C3 Phase 1, C3 Phase 2).

In this document the technical specification of the underlying stochastic model of the ESG used for producing Equity fund returns for the Basic Data Set is described.

## Equity Prices and Dividend Yields

The equity markets of different economies exhibit a wide range of characteristics which must be incorporated into a model for it to be useful for pricing, risk management and other common applications. The equity market consists of multiple interconnected components namely price, dividend, and volatility dynamics, which must be properly modeled in order for the model to be considered realistic.

Figure 1 shows the daily equity price returns for the S\&P 500. We observe some interesting features which we might like to include in any modeling approach. These include:

- A degree of randomness or stochasticity in the price returns
- Periods of high and low volatility, which have a tendency to cluster
- Extreme events, with the price return suddenly spiking to high positive or negative values
- A higher frequency and a larger magnitude of extreme events during periods of high volatility
- A higher frequency of extreme negative returns as compared to extreme positive returns

<img src="https://cdn.mathpix.com/cropped/c16a0786-cf3c-4b56-821b-a04fa0e24a53-1.jpg?height=529&width=1032&top_left_y=1931&top_left_x=554" alt="image" style="width:100%;height:auto;">
Figure 1. Daily equity price returns for the S\&P 500. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

Another important dynamic to capture in equity markets is the income cash flows received from dividends. In particular, it is observed across multiple equity markets that dividend yields are negatively correlated with price returns and that when jumps are observed in equity prices the dividend yield tends to jump in the oppositive direction. Figure 2 shows this behavior in the historical data. We observe that the rolling 12 -month equity price returns and the 12 -month dividend yield on United States Large Cap equity are negatively correlated and during the 2008 crisis moved rapidly apart.

<img src="https://cdn.mathpix.com/cropped/c16a0786-cf3c-4b56-821b-a04fa0e24a53-2.jpg?height=777&width=1480&top_left_y=646&top_left_x=317" alt="image" style="width:100%;height:auto;">
Figure 2 Historical relationship between large cap price returns in a rolling twelve-month window and dividend yields. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

The market data looked at here shows the extent to which equity markets exhibit dynamics with particular structural features. Modeling all these features is key to properly managing the risk on equity investments.

## Equity Model Specification

In the last section we saw that equity market returns exhibit a high degree of volatility with specific features. The GOES stochastic volatility with jumps (SVJ) model is a highly realistic cutting-edge model which was chosen in part for the following reasons:

- The model produces realistic behavior under the Real-World measure. For instance:
- fat tails in the return distribution
- volatility clustering
- jumps in returns which are more prevalent in time of high volatility
- price decreases coupled with volatility increases
- dividend cash flows negatively correlated with price returns
- Accurate semi-closed option pricing formulas and the ability to reproduce the volatility smile observed in traded equity derivatives.
- Model can be used for both real-world modeling and risk-neutral valuation purposes.
- The model has a built-in correlation structure among the price, variance and dividend processes and allows for realistic interactions among multiple stock indices within and across economies.
- Estimation and calibration procedures and methods are well defined.

It helps to understand the GOES SVJ equity model by first considering the simplest reasonable model of equity returns, Geometric Brownian Motion (GBM). GBM models the change in the price of an equity index, $d S(t)$, according to the stochastic differential equation (SDE):

$$
d S(t)=\mu S(t) d t+\sigma S(t) d W(t)
$$

Where, $\mathrm{S}(\mathrm{t})$ is the equity index value at time $\mathrm{t}, \mu$ is the drift which controls the rate of growth of the index, $\sigma$ is the variance parameter and $d W(t)$ is an independent random process or Wiener process.

While this model has many strong features, its limitations restrict its applicability to only the simplest of applications. In particular, if we look at Figure 3, which shows simulated daily returns using the GBM model, we see that it is not capable of producing many of the features that we observed in the real data shown in the last section. For instance, the probability of producing a 2008 or March-2020 type loss is effectively zero in such model. The model also produces none of the volatility clustering that we see in real data. Finally, the model is not able to produce the smile effect when pricing derivatives away from money.

<img src="https://cdn.mathpix.com/cropped/c16a0786-cf3c-4b56-821b-a04fa0e24a53-3.jpg?height=611&width=1182&top_left_y=1256&top_left_x=466" alt="image" style="width:100%;height:auto;">
Figure 3: Simulated daily equity returns using a GBM model. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{\text {® }}$ Economic Scenario Generator.

The next major development was that of Heston (1993) with the introduction of a stochastic volatility process to the modeling of equities. The precise formulation of the model may differ, but a general form of the model which naturally extends the GBM process is given by the coupled two-dimensional stochastic differential equations.

$$
\begin{aligned}
& d S(t)=\mu S(t) d t+V(t) S(t) d W_{1}(t) \\
& d V(t)=(\alpha-\beta V(t)) d t+\sigma \sqrt{V(t)} d W_{2}(t)
\end{aligned}
$$

Where we note the addition of a stochastic volatility process with mean reversion parameters $\alpha$ and $\beta$ which control the mean reversion level and speed of the variance process. The model also allows
for the correlation of the two Wiener processes $d W_{1}(t)$ and $d W_{2}(t)$ via a parameter $\rho$. The value of $\rho$ is usually set to be negative such that falling equity markets are coupled with higher volatility.

The Heston model was highly successful in explaining the volatility smile effect in equity derivatives prices. The model was also significantly better at recreating the volatility clustering effects that we have previously noted. However, the model has no mechanism for producing the most severe types of drawdown that have been observed historically and as such is not likely to be suitable for typical insurance applications which require robust modeling of the tail.

The SVJ model used in GOES further extends the Heston stochastic volatility model. The general form of the model expands the Heston price process for $S(t)$ with the addition of a jump process. A third SDE is added which allows for the modeling of the dividend yields. The coupled three-dimension stochastic differential equations governing the equity dynamics is given by:

$$
\begin{aligned}
\frac{d S(t)}{S(t)} & =\left[-D(t)+\mu_{0}+\mu_{1} V(t)-\lambda m V(t)\right] d t+\sqrt{V(t)} d W_{1}(t)+\gamma d N(t) \\
d V(t) & =(\alpha-\beta V(t)) d t+\sigma \sqrt{V(t)} d W_{2}(t) \\
d D(t) & =\kappa\left(\alpha_{D}+\theta z(t)-D(t)\right) d t+\sigma_{D} \sqrt{D(t)} d W_{3}(t)+D(t) \gamma_{D} d N(t)
\end{aligned}
$$

Where:

- $D(t)$ is the stochastic dividend yield,
- $\mu_{0}$ and $\mu_{1}$ are risk premia,
- $\quad V(t)$ is the stochastic variance,
- $N(t)$ is a Poisson counting process with intensity $\lambda \mathrm{V}(\mathrm{t})$ which is shared by the price and dividend processes,
- $\lambda$ controls the jump intensity
- $y$ is a variable jump size
- $m$ is the average of the variable jump size $\gamma$,
- $\beta$ is a parameter controlling the mean reversion speed of the variance process,
- $\alpha$ controls the mean reversion level where $\alpha / \beta$ is the mean reversion level of $V(t)$,
- $\sigma$ is the instantaneous variance of the variance process,
- $\kappa$ is a parameter controlling the mean reversion speed of the dividend process,
- $\alpha_{D}$ is a parameter controlling the mean reversion level of the dividend process,
- $z(t)$ is a government bond yield scaled by parameter $\theta$,
- $\sigma_{D}$ is the instantaneous variance of the dividend process,
- $y_{D}$ is the variable jump size of the dividend process,
- $d W 1, d W 2$ and $d W 3$ are correlated wiener processes.

Figure 4 shows an example path for the simulated daily returns of large cap equities using a stochastic volatility with jumps model. The addition of the jump process enables the model to more faithfully reproduce the kinds of return dynamics that we observed in the real data. These dynamics include volatility and jump clustering, and a higher frequency of more severe jumps than is possible in simpler models. The addition of the jump process allows for the frequency of these jumps as well as the distribution of the jump sizes to be precisely controlled.

<img src="https://cdn.mathpix.com/cropped/c16a0786-cf3c-4b56-821b-a04fa0e24a53-5.jpg?height=647&width=1253&top_left_y=277&top_left_x=421" alt="image" style="width:100%;height:auto;">
Figure 3: Simulated daily equity returns from a stochastic volatility with jumps model. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

Dividends are modeled as a separate stochastic process where the Wiener process of the model is correlated with that of the price process. This enables the model to achieve simulated dynamics similar to those observed in Figure 2. Figure 5 shows the evolution of the price return and dividend yield on a single simulated path from the GOES SVJ model. As in the market data, the dividends have a tendency to increase when price returns are falling. This feature is an important one to capture, because it has a significant impact on the total return distributions of equity holdings.

<img src="https://cdn.mathpix.com/cropped/c16a0786-cf3c-4b56-821b-a04fa0e24a53-5.jpg?height=622&width=1223&top_left_y=1383&top_left_x=451" alt="image" style="width:100%;height:auto;">
Figure 5: Simulated dividend yield and equity price returns from the GOES SVJ model. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

## Summary

Equity markets exhibit features which include stochastic volatility of returns, rapid and severe jumps in returns, volatility and jump clustering and a dividend process which is negatively correlated with the long-term return process. Equity derivatives also exhibit significant nonlinearity in the relationship between price and strike value.

Attempts to model these markets using stochastic processes have been evolutionary, and a number of different models have been discussed here. The GOES Stochastic Volatility with Jumps Model (SVJ)
can simulate paths with highly realistic return dynamics relative to those observed in the market data. This realism extends to the modeling of extreme tail events which are the key to effective risk management.

The ability of the GEMS implementation of the model to capture the interplay between returns and dividend yields is another key feature of the model. It should be noted that for risk neutral applications such as the market consistent valuation of liabilities, the model is able to efficiently and accurately calibrate to a large number of points on the option implied volatility surface. These considerations together make the GOES SVJ model a highly robust and widely applicable choice for equity modeling tasks.

## Additional Reading

Heston, S., (1993), A Closed-Form Solution of Options with Stochastic Volatility with Applications to Bond and Currency Options, The Review of Financial Studies, Vol.6, No.2, 327-343.

Bates, D., (1996), Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutsche Mark Options, Review of Financial Studies, Vol.9, 69-107.

Bates, D., 2000, Post-87 crash fears in S\&P 500 futures option, Journal of Econometrics, 94, 181238.

Oksendal, Bernt K. (2002), Stochastic Differential Equations: An Introduction with Applications, Springer, pp. 326, ISBN 3540637206.

## Disclosures/Confidentiality Notice

©2025 Conning, Inc. Conning, Inc., Goodwin Capital Advisers, Inc., Conning Investment Products, Inc., a FINRAregistered broker-dealer, Conning Asset Management Limited, and Conning Asia Pacific Limited (collectively "Conning") and Octagon Credit Investors, LLC, Global Evolution Holding ApS and its subsidiaries, and Pearlmark Real Estate, L.L.C. and its subsidiaries (collectively "Affiliates" and together with Conning, "Conning \& Affiliates") are all direct or indirect subsidiaries of Conning Holdings Limited which is one of the family of companies whose controlling shareholder is Generali Investments Holding S.p.A. ("GIH") a company headquartered in Italy. Assicurazioni Generali S.p.A. is the ultimate controlling parent of all GIH subsidiaries. This document and the software described within are copyrighted with all rights reserved. No part of this document may be distributed, reproduced, transcribed, transmitted, stored in an electronic retrieval system, or translated into any language in any form by any means without the prior written permission of Conning \& Affiliates. Conning \& Affiliates do not make any warranties, express or implied, in this document. In no event shall any Conning \& Affiliates company be liable for damages of any kind arising out of the use of this document or the information contained within it. This document is not intended to be complete, and we do not guarantee its accuracy. Any opinion expressed in this document is subject to change at any time without notice.

ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{®}$ and CONNING ALLOCATION OPTIMIZER ${ }^{®}$ are registered trademarks of Conning, Inc. in the U.S. ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{®}$ and CONNING ALLOCATION OPTIMIZER ${ }^{®}$ are proprietary software published and owned by Conning, Inc. Copyright 1990-2025 Conning, Inc. All rights reserved.

This document is for informational purposes only and should not be interpreted as an offer to sell, or a solicitation or recommendation of an offer to buy any security, product or service, or retain Conning \& Affiliates for investment advisory services. The information in this document is not intended to be nor should it be used as investment advice. COD00001153

