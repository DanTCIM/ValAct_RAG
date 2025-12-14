# NAIC GOES - Interest Rate Model

Author: ©2025 Conning, Inc. Conning, Inc

## NAIC Basic Data Set

The Basic Data Set provided free of charge to insurers is the standard scenario file set delivered as part of the NAIC scenario service. Users can access the scenarios online by downloading a file containing stochastic scenarios from the Generator of Economic Scenarios (GOES) for real-world interest rates, equity, and bond fund returns. The typical application for these scenarios is in calculations of life and annuity statutory reserves according to the Valuation Manual (e.g., VM-20, VM-21) and capital under the NAIC RBC requirements (e.g., C3 Phase 1, C3 Phase 2).

In this document, the technical specification of the underlying stochastic model of the ESG used for producing government bond yields and returns on bond funds for the Basic Data Set are described.

## Interest Rate Model

Scenarios for the non-defaultable term structure of interest rates (i.e., Treasury yields) as well as bond fund returns are simulated using a multi-factor affine short rate model. Some of the reasons that this model has been selected are:

- Realistic yield curve dynamics with a small number of parameters
- Arbitrage free dynamics making the model applicable to risk-neutral and real-world applications
- Closed-form bond and semi-closed form derivative price formulas
- Well-understood estimation and calibration procedures
- Production of parallel shifts, twists or steeping and curvature in simulated yield curves


### 3-Factor Model Specification

The underpinnings of the model are a 3 -factor extension to the well-known Cox-Ingersoll-Ross (CIR) modeling framework. In this model the dynamics of yield curves are governed by three independent stochastic processes referred to as state variables. These state variables are labeled $X_{i}(t)$, where $i=1,2,3$ and $t$ is time, indicating that the value of these variables change through time.

Three factors are chosen because they allow for the modeling of the three predominant types of yield curve movement observed in real market data; parallel shifts, steepening and curvature (sometimes referred to as shift, twist and butterfly/smile).

The 3 state variables $X_{i}(t)$ are governed by an extended version of the standard CIR stochastic differential equation (SDE):

$$
d X_{i}(t)=\left(\theta_{i}+\lambda_{i}^{0}+\left(\lambda_{i}^{1}-\kappa_{i}\right) X_{i}(t)\right) d t+\sigma_{i} \sqrt{X_{i}(t)} d W_{i}(t)
$$

where

- $K_{i}$ controls the mean reversion speed and level
- $\theta_{i}$ controls the mean reversion level
- $\lambda_{i}^{0}$ and $\lambda_{i}^{1}$ are risk premia
- $\sigma_{i}$ controls the volatility
- $d W_{i}(t)$ is the change in the Wiener process.

The formulation of the model implemented in GOES also allows for the simulation of negative interest rates, in line with what has been observed in market data in many geographies in the last 20 years.

In the real-world formulation of this model used to produce the Basic Data Set, risk premia are included in the above formula. These risk premia allow the model to better capture the dynamics of real government bond markets as well as defining the change of measure between real world and risk neutral. The three-factor formulation of the model can produce kurtose and skewed distributions which match historically observed distributions well. The mean reverting properties of the model produce stable long-term simulations with well constrained tails. This is in contrast to the commonly used log normal models, such as Libor market models (LMM) and Black Karasinski models, which tend to produce unrealistic or explosive interest rates, especially over long simulation horizons, making them less suitable for real-world applications.

### Yield Curve Simulation and Construction

The interest rate model falls into a class of models called affine short rate models. In these models a stochastic short rate (in the 1 -factor case) or a set of stochastic state variables (in the multi factor case) are simulated. The price of a zero-coupon bond at time t maturing at time $T, P(t, T)$ has the form:

$$
P(t, \tau)=e^{\sum_{i=1}^{3}\left(A_{i}(\tau)+B_{i}(\tau) X_{i}(t)\right)}
$$

Where in the case of the model described here, $X_{i}(t)$ are the three state variables of the interest rate model described in the previous section, and $A_{i}(T)$ and $B_{i}(T)$ are so call auxiliary functions of the model. The auxiliary functions for the CIR model are given by:

$$
A_{i}(\tau)=\frac{2 \theta_{i}}{\sigma_{i}^{2}} \ln \left(\frac{2 \gamma_{i} e^{\left(\gamma_{i}+\kappa_{i}\right) \tau / 2}}{\left(\gamma_{i}+\kappa_{i}\right)\left(e^{\gamma_{i} \tau}-1\right)+2 \gamma_{i}}\right)
$$

and

$$
B_{i}(\tau)=\frac{-2\left(e^{\gamma_{i} \tau}-1\right)}{\left(\gamma_{i}+\kappa_{i}\right)\left(e^{\gamma_{i} \tau}-1\right)+2 \gamma_{i}}
$$

where

$$
\gamma_{i}=\sqrt{\kappa_{i}^{2}+2 \sigma_{i}^{2}}
$$

By extension the continuously compounded yield curve can be constructed by rearranging the pricing formula to give:

$$
y(t, \tau)=\frac{-1}{\tau}\left(\sum_{i=1}^{3} A_{i}(\tau)+\sum_{i=1}^{3} B_{i}(\tau) X_{i}(t)\right)
$$

Figure 1 shows the dependencies of the two auxiliary functions $A$ and $B$ on the model parameters, and the bond maturity given fixed values for the other parameters. Observing how the value changes
for different points on the yield curve as we change the model parameters gives a visual representation of how different model parameters enable different yield curve shapes to emerge in a multi-factor model with this structure.

<img src="https://cdn.mathpix.com/cropped/938b3b20-c492-4275-b78b-3598013d92f2-3.jpg?height=1926&width=1286&top_left_y=449&top_left_x=418" alt="image" style="width:100%;height:auto;">
Figure 1: The parameterand maturity dependencies of the auxiliary functions of the Cox Ingersoll Ross interest rate model. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

Note that the auxiliary functions are only dependent on the risk neutral model parameters (i.e. the parameters $\lambda$ do not enter the functions) and the time to maturity of the bond under consideration. Therefore, given the simulated state variables at any point in time and the parameters of the model, the yield curve can be constructed from the given pricing formula.

An important aspect of any yield curve model is its ability to produce a wide range of simulated yield curve shapes. Figure 2 shows four selected simulated yield curves from the GOES model. This demonstrates the extent to which the model is able to produce quite flat yield curves(e.g. path 8201), steep as well as flatter yield curves with negative rates (e.g. paths 3665 and 3262) and even inverted yield curves (e.g. path 9713). The curves shown also demonstrate different degrees of curvature.

<img src="https://cdn.mathpix.com/cropped/938b3b20-c492-4275-b78b-3598013d92f2-4.jpg?height=816&width=1273&top_left_y=779&top_left_x=416" alt="image" style="width:100%;height:auto;">
Figure 2: Simulated yield curves from the GEMS ${ }^{®}$ Economic Scenario Generator. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

### Initial Yield Curve Fitting

In its standard form as described the multifactor CIR model is only able to approximately fit the initial market yield curve. For most practical applications it is a requirement that the initial yield curve and sometimes yields for extrapolated maturities must be fit to a high degree of accuracy. To enable such fitting the GOES model employs a deterministic shift function exogenously from the stochastic differential equation used to drive the state variables. Under this scheme the formula for the initial or $\mathrm{t}=0$ continuously compounded yield of a bond of maturity T is modified by a shift function $\mathrm{l}(\mathrm{t})$ such that:

$$
y(t=0, \tau)=\frac{-1}{\tau}\left(\left(-\int_{0}^{\tau} l(s) d s\right)+\sum_{i=1}^{3} A_{i}(\tau)+\sum_{i=1}^{3} B_{i}(\tau) X_{i}(t=0)\right)
$$

Given that at time zero the auxiliary functions $A$ and $B$ and the state variables $X_{i}(t=0)$ are fixed for all paths, the function $I(t)$ can be found which recovers any given market curve. Since the values of the function $I(t)$ can take negative values, this mechanism also allows the model to produce negative
simulated yields while maintaining strictly positive state variables $X_{i}(t)$, which is a requirement under the CIR process due to the square root in the diffusion term.

Figure 3 shows a fit to an initial yield curve for United States Treasuries and demonstrates the extent to which the market yield curve is accurately fit. The model can also fit initial yield curves with significantly negative starting values, including when longer tenors are negative.

<img src="https://cdn.mathpix.com/cropped/938b3b20-c492-4275-b78b-3598013d92f2-5.jpg?height=691&width=1019&top_left_y=575&top_left_x=550" alt="image" style="width:100%;height:auto;">
Figure 3: 3-Factormodel fit to initial yield curve for United States Treasuries. Prepared by Conning, Inc.
©2025 Conning, Inc. Source: GEMS ${ }^{\text {® }}$ Economic Scenario Generator.

## Mean Reversion

The GOES three-factor model of interest rates is a mean reverting model. The model has a welldefined mean reversion level for the state variables $X_{i}(t)$ defined by the parameters $\theta_{i}$ and $K_{i}$, and the speed of mean reversion is controlled through the parameter $K_{\text {i. }}$.

More explicitly we can see that for a process with a drift term of the form:

$$
d X_{i}(t)=\left(\theta_{i}-\kappa_{i} X_{i}(t)\right) d t
$$

such as the square root process used in the GOES three-factor model, that the (mean) value of the process at time $t=1$ will be given by;

$$
\begin{aligned}
& X_{i}(t=1)=X_{i}(t=0)+d X_{i}(t=1) \\
& =X_{i}(t=0)+\left(\theta_{i}-\kappa_{i} X_{i}(t=0)\right) \\
& =\left(1-\kappa_{i}\right) X_{i}(t=0)+\theta_{i}
\end{aligned}
$$

Following the same logic the value of the process at $t=2$ will be:

$$
X_{i}(t=2)=\left(1-\kappa_{i}\right)^{2} X_{i}(t=0)+\left(1-\kappa_{i}\right) \theta_{i}+\theta_{i}
$$

and at $t=3$

$$
X_{i}(t=3)=\left(1-\kappa_{i}\right)^{3} X_{i}(t=0)+\left(1-\kappa_{i}\right)^{2} \theta_{i}+\left(1-\kappa_{i}\right) \theta_{i}+\theta_{i}
$$

And more generally:

$$
X_{i}(t)=\left(1-\kappa_{i}\right)^{t} X_{i}(t=0)+\theta_{i} \sum_{j=0}^{t-1}\left(1-\kappa_{i}\right)^{j}
$$

And from this we can see that the mean reversion property of the process is that the first summand converges to 0 and the second summand converges to $\theta_{i} / k_{i}$ as $t \rightarrow \infty$.

The mean reversion parameters of the model are usually estimated either from data or based on a set of calibration criteria for the long term mean reversion level of interest rates.

## Flooring Mechanism

The NAIC desires a scenario set that contains both a reasonable frequency of low-for-long treasury curves and a reasonable range of short-term movements of the treasury curves. When we calibrate GOES to these targets, the resulting Treasury Yields have a very wide steady state distribution. In particular, the short end of the curve produces a high frequency of negative Yields. In order to control this frequency, a soft-flooring mechanism, referred to as the Dynamic Generalized Fractional Floor (Dynamic GFF) was added to the native GOES model.

The original GFF had three main components:

- $\mathbf{s}$ - the GOES simulated spot rate
- $\mathbf{k}$ - the spot rate threshold below which the flooring is applied
- $\mathbf{m}$ - the fractional adjustment to s when $\mathrm{s}<k$
and the simulated spot rate is adjusted upward to a floored spot rate equal to

$$
m^{*} s+(1-m) * k
$$

With the Dynamic GFF, $m$ becomes a dynamic component. When $s$ is at the threshold $k, m$ starts with its maximum value. As s decreases, $m$ will also gradually decrease down to a calculated minimum. As s continues to decrease, $m$ gradually increases back to its maximum value.

Before we can determine the value of this now variable $m$, we need two other assumptions.

- $\quad \mathbf{s}_{0}$ - the value of $s$ where $m$ will have its minimum value
- $\mathbf{s}_{\text {min }}$ - the value of $s$ where $m$ returns to its maximum value

This leads to the following function for $m$ as a function of $s$ :

$$
m(s)=m_{0}+\max \left(\min (s, k)-s_{0}, 0\right) * R_{0}-\max \left(s_{0}-\max \left(s, s_{\min }\right), 0\right) * R_{\min }
$$

where
$\bar{m}$ is the terminal fraction level that applies when $s=k$
$m_{0}=\frac{k}{k-s_{0}}$ is the fraction that ensures rate ( $\mathrm{s}_{0}=0$ )
$R_{0}=\frac{\bar{m}-m_{0}}{k-s_{0}}$
$m_{\text {min }}=\frac{k-r_{\text {ate }} e_{\text {min }}}{k-s_{\text {min }}}$ is the fraction that ensures rate $\left(s_{\text {min }}\right)=r a t e_{\text {min }}$

$$
R_{\min }=\frac{m_{0}-m_{\min }}{s_{0}-s_{\min }}
$$

As an example, with the initial proposed parameters of:

- $\mathrm{k}=0.4 \%$
- $\mathrm{m}=20 \%$
- $\mathrm{s}_{0}=-2.4 \%$
- $\mathrm{S}_{\min }=-6.55 \%$
the resulting Dynamic slope versus simulated GOES Spot Rate shown in Figure 4. Finally, when these slopes get applied, it produces the simulated Floored Spot Rates shown in Error! Reference source not found..

<img src="https://cdn.mathpix.com/cropped/938b3b20-c492-4275-b78b-3598013d92f2-7.jpg?height=658&width=1232&top_left_y=861&top_left_x=446" alt="image" style="width:100%;height:auto;">
Figure 4: Dynamic Slope based on initial proposed parameters. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

<img src="https://cdn.mathpix.com/cropped/938b3b20-c492-4275-b78b-3598013d92f2-7.jpg?height=849&width=1168&top_left_y=1652&top_left_x=476" alt="image" style="width:100%;height:auto;">

Figure 5: Impact of Dynamic GFF on Simulated 1-Year Spot Rate. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{®}$ Economic Scenario Generator.

## Summary

In this document, the technical specification and the properties of the interest rate model used for the production of the NAIC Basic Data Set has been described. The GOES three factor model of interest rates described represents a highly parsimonious and highly tractable structure with which to generate stochastic term structures and bond returns. The model is efficient to estimate and produces output which is consistent with the dynamics observed in real market data. Prior to scenario production the model is fit to the initial market yield curve. The statistical properties of the simulated model can also be customized to take account of specified or changing calibration criteria.

## Additional Reading

Cox, J.C., J.E. Ingersoll and S.A. Ross (1985). A Theory of the Term Structure of Interest Rates. Econometrica 53: 385407.

Brigo, Damiano and Fabio Mercurio (2001b). A deterministic shift extension of analytically tractable and time-homogeneous short rate models. Finance \& Stochastics 5 (3): 369388

## Disclosures/Confidentiality Notice

©2025 Conning, Inc. Conning, Inc., Goodwin Capital Advisers, Inc., Conning Investment Products, Inc., a FINRAregistered broker-dealer, Conning Asset Management Limited, and Conning Asia Pacific Limited (collectively "Conning") and Octagon Credit Investors, LLC, Global Evolution Holding ApS and its subsidiaries, and Pearlmark Real Estate, L.L.C. and its subsidiaries (collectively "Affiliates" and together with Conning, "Conning \& Affiliates") are all direct or indirect subsidiaries of Conning Holdings Limited which is one of the family of companies whose controlling shareholder is Generali Investments Holding S.p.A. ("GIH") a company headquartered in Italy. Assicurazioni Generali S.p.A. is the ultimate controlling parent of all GIH subsidiaries. This document and the software described within are copyrighted with all rights reserved. No part of this document may be distributed, reproduced, transcribed, transmitted, stored in an electronic retrieval system, or translated into any language in any form by any means without the prior written permission of Conning \& Affiliates. Conning \& Affiliates do not make any warranties, express or implied, in this document. In no event shall any Conning \& Affiliates company be liable for damages of any kind arising out of the use of this document or the information contained within it. This document is not intended to be complete, and we do not guarantee its accuracy. Any opinion expressed in this document is subject to change at any time without notice.

ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{®}$ and CONNING ALLOCATION OPTIMIZER ${ }^{®}$ are registered trademarks of Conning, Inc. in the U.S. ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{\text {® }}$ and CONNING ALLOCATION OPTIMIZER ${ }^{\text {® }}$ are proprietary software published and owned by Conning, Inc. Copyright 1990-2025 Conning, Inc. All rights reserved.

This document is for informational purposes only and should not be interpreted as an offer to sell, or a solicitation or recommendation of an offer to buy any security, product or service, or retain Conning \& Affiliates for investment advisory services. The information in this document is not intended to be nor should it be used as investment advice. COD00001233

