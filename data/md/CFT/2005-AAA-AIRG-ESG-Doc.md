AMERICAN ACADEMY of ACTUARIES

C3 Phase II Risk-Based Capital for Variable Annuities: Pre-Packaged Scenarios

Presented by the American Academy of Actuaries' Life Capital Adequacy Subcommittees'<br>C-3 Phase 2 Work Group to the National Association of Insurance Commissioners'<br>Capital Adequacy Task Force

March 2005

The American Academy of Actuaries is the public policy organization for actuaries practicing in all specialties within the United States. A major purpose of the Academy is to act as the public information organization for the profession. The Academy is non-partisan and assists the public policy process through the presentation of clear and objective actuarial analysis. The Academy regularly prepares testimony for Congress, provides information to federal elected officials, comments on proposed federal regulations, and works closely with state officials on issues related to insurance. The Academy also develops and upholds actuarial standards of conduct, qualification and practice and the Code of Professional Conduct for all actuaries practicing in the United States.

Larry M. Gorski, F.S.A., M.A.A.A., Chair

Robert A. Brown, F.S.A., M.A.A.A., Vice-Chair

Gerald A. Anderson, F.S.A., M.A.A.A.

Jeffrey M. Brown, F.S.A., M.A.A.A.

Martin R. Claire, F.S.A., M.A.A.A.

Todd H. Erkis, F.S.A., M.A.A.A.

Luke N. Girard, F.S.A., M.A.A.A.

Arnold N. Greenspoon, F.S.A., M.A.A.A.

Ann L Kallus, F.S.A., M.A.A.A.

Robert G. Meilander, F.S.A., M.A.A.A.

Hubert B. Mueller, F.S.A., M.A.A.A.
Keith D. Osinski, F.S.A., M.A.A.A.

Jan L. Pollnow, F.S.A., M.A.A.A.

Craig R. Raymond, F.S.A., M.A.A.A

Mark C. Rowley, F.S.A., M.A.A.A.

Max J. Rudolph, F.S.A., M.A.A.A.

George M. Wahle, F.S.A., M.A.A.A.

William H. Wilton, F.S.A., M.A.A.A.

Michael L. Zurcher, F.S.A., M.A.A.A.

The following report is a follow up to a proposal from March 2002 and was prepared by the Life Capital Adequacy Subcommittee's C-3 Phase 2 Work Group* (chaired by Bob Brown). The work group is made up of several members of the subcommittee as well as Mike Akers, Frederick Andersen, Robert Berendsen, Tom Campbell, Andrew Eastman, Jack Gies, Geoff Hancock, Jeff Krygiel, Jim Lamson, Jeffrey Leitz, Craig Morrow, John O'Sullivan, Link Richardson, Jim Reiskytl, Dave Sandberg, Van Villaruz, and Albert Zlogar. The work group would also like to thank Philip Barlow, Jan Brown, Bill Carmello, Michael Cebula, Allen Elstein, Mark Evans, Dennis Lauzon, and Mark Tenney for their helpful suggestions and feedback.

(*It should also be noted, that since this project has been on-going for several years, many other individuals contributed to the work that paved the way for this report.)

## Background

Over the past two years, the AAA Life Capital Adequacy Subcommittee ("LCAS") has issued several versions of a report entitled "Recommended Approach for Setting Regulatory Risk-Based Capital Requirements for Variable Annuities and Similar Products"1 that recommends implementing "C3 Phase II RBC" to address both the interest rate and equity risk associated with variable annuity products with guaranteed benefits.

The LCAS recommendation indicates that the American Academy of Actuaries will provide 10,000 "prepackaged" scenarios for the common asset classes typically needed in the stochastic cashflow projections of variable annuities. This report documents the models and parameters used to develop the "pre-packaged" scenarios ${ }^{2}$. Guidance is also provided on the use of the pre-packaged scenarios, including a utility that allows companies to select ("pick") a subset of representative scenarios from the full sample of 10,000 .

While the LCAS proposal encourages companies to develop their own stochastic models for scenario testing, companies may choose to use the pre-packaged scenarios as an alternative. Also, the "Alternative Method" factors and formulas for GMDB risks have been developed from stochastic testing using these scenarios. More information on the scenario files is provided later in this document under "Pre-packaged Scenario Files".[^0]

## Scenario Files

Scenario files are provided for the economic variables ("asset classes”) shown in Table 1.

Table 1: Scenario Files

| Economic Variable / Asset Class | Short Name | Scenario File |
| :---: | :---: | :---: |
| 3-month U.S. Treasury yields | UST_3m | UST_3m.csv |
| 6-month U.S. Treasury yields | UST_6m | UST_6m.csv |
| 1-year U.S. Treasury yields | UST_1y | UST_1y.csv |
| 2-year U.S. Treasury yields | UST_2y | UST_2y.cSv |
| 3-year U.S. Treasury yields | UST_3y | UST_3y.cSv |
| 5-year U.S. Treasury yields | UST_5y | UST_5y.cSv |
| 7-year U.S. Treasury yields | UST_7y | UST_7y.cSv |
| 10-year U.S. Treasury yields | UST_10y | UST_10y.cSV |
| 20-year U.S. Treasury yields | UST_20y | UST_20y.csv |
| 30-year U.S. Treasury yields | UST_30y | UST_30y.csv |
| Money Market / Short-Term | MONEY | MONEY.CSV |
| U.S. Intermediate Term Government Bonds | U.S. ITGVT | ITGVT.csV |
| U.S. Long Term Corporate Bonds | U.S. LTCORP | LTCORP.csV |
| Diversified Fixed I ncome | FIXED | FIXED.cSV |
| Diversified Balanced Allocation | BALANCED | BALANCED.CSV |
| Diversified Large Capitalized U.S. Equity | US | US.cSV |
| Diversified International Equity | INTL | INTL.cSV |
| Intermediate Risk Equity | SMALL | SMALL.CSV |
| Aggressive or Specialized Equity | AGGR | AGGR.csV |

## Market Data

Table 2 indicates the source data or composition of each asset class. Parameters are determined by fitting the models to data over the specified historic periods.

Table 2: Asset Classes for Scenario Modeling

| Asset Class | Market Proxies | Historic Period |
| :--- | :--- | :---: |
| U.S. Treasury Yields | U.S. Treasury Yield Curves | $1951.01-1995.12$ |
| Money Market | 3 Month Treasury returns | $1955.12-2003.12$ |
| U.S. ITGVT | U.S. Intermediate Term Government Bonds | $1955.12-2003.12$ |
| U.S. LTCORP | U.S. Long Term Corporate Bonds | $1955.12-2003.12$ |
| Fixed Income | $65 \%$ ITGVT + 35\% LTCORP | $\mathrm{n} / \mathrm{a}$ |
| Balanced Allocation | $60 \%$ Diversified Equity + 40\% Fixed Income | $\mathrm{n} / \mathrm{a}$ |
| Diversified Large Cap U.S. Equity | S\&P500 Total Return Index | $1955.12-2003.12$ |
| Diversified International Equity | MSCI-EAFE \$USD Total Return Index | $1969.12-2003.12$ |
| Intermediate Risk Equity | U.S. Small Capitalization Index | $1955.12-2003.12$ |
| Aggressive Equity | Emerging Markets, NASDAQ, Hang Seng | $1984.12-2003.12$ |

## Model Descriptions and Notes

- Pseudo-random numbers are generated using the Mersenne Twister algorithm ${ }^{3}$. Variance reduction techniques were not used.
- All models use a one-month interval as the time increment (i.e., 12 periods per year).
- For simplicity, the correlation matrix is constant.
- The random "shocks" that drive changes in interest rates are independent (i.e., zero correlation) of all other model factors, including equity and bond returns.
- Additional scenarios may be created by blending the accumulation factors for the market proxies.
- The Treasury yields can be used to project credited rates on fixed accounts and annuity purchase rates under GMIB options. The Treasury yields are also suitable for testing C-3 Phase I RBC ("interest rate risk") on the assets and liabilities underlying the fixed account. See the section entitled "U.S. Treasury Yields" for further information.
- Bond index returns ("Money Market", "U.S. ITGVT" and "U.S. LTCORP") are modeled as a function of interest rates. See later under "Bond Index Returns”.
- Equity returns are generated from a monthly stochastic log volatility model ("SLV”). Additional details are given in the section "Equity Market Returns”. The S\&P500 TR scenarios (Diversified Equity) satisfy the calibration criteria within sampling error.[^1]- Parameters for "Diversified International Equity" are estimated from data denominated in \$US currency.
- The hypothetical 'Aggressive/Exotic Equity' index was constructed by blending returns for the NASDAQ, Emerging Markets and Hang Seng indices. This proxy has an unconditional annualized volatility of approximately $25 \%$. This market mix is not meant to suggest a representative asset profile for this class, but used merely to build an historic index with high volatility and sufficient history.
- The estimation of the SLV model parameters for "U.S. Diversified Equity" imposed some subjective restrictions to ensure an unconditional expected total annualized return of $8.75 \%$ effective. Appendix 2 of the LCAS report includes complete details on the development of the SLV model and associated calibration criteria.
- Parameters for the other equity markets were determined by 'constrained' maximum likelihood estimation whereby the Sharpe ratio $\psi$ must satisfy the following relationship:

$$
\psi^{*} \leq \psi \leq 1.05 \times \psi^{*}, \quad \text { where } \psi=\frac{E[R]-r}{\sigma}
$$

$E[R]$ and $\sigma$ are respectively the annualized unconditional expected return (effective) and standard deviation (volatility) of market returns. For simplicity, we assume that the risk-free rate $r=5.25 \%$ (annual effective) for all markets, roughly equal to the average 3-month U.S. Treasury yield over the past 50 years. $\psi^{*}=0.232$ is the Sharpe ratio for the S\&P500 Total Return index (1955.12 - 2003.12).

## U.S. Treasury Yields

The U.S. Treasury yields are generated using the "C-3 Phase I" interest rate model designed by the American Academy of Actuaries' C-3 Subgroup of the Life Risk Based Capital Task Force. The model simulates Treasury bond yields according to a stochastic variance process with mean reversion under the real-world ${ }^{4}$ probability measure. For full details, please see "Appendix III - Technical Aspects of the Scenario Generator and the Scenario Selection Process” in the October 1999 report to the NAIC Life RBC Working Group.

The starting yield curve ${ }^{5}$ (December 2004) for the interest rate model is given in Table 3. All rates are expressed as semi-annual bond equivalent yields.

Interest rate movements are uncorrelated ${ }^{6}$ with other model factors. Before using the integrated set of prepackaged scenarios, the actuary should be confident that an assumption of independence is reasonable and does not lead to a material understatement of the risk exposure.

Table 3: Starting U.S. Treasury Yield Curve - December 2004 Semi-Annual Bond Equivalent Yields

| Maturity <br> (in years) | $\mathbf{0 . 2 5}$ | $\mathbf{0 . 5}$ | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{5}$ | $\mathbf{7}$ | $\mathbf{1 0}$ | $\mathbf{2 0}$ | $\mathbf{3 0}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| S/A Yield | $2.22 \%$ | $2.50 \%$ | $2.67 \%$ | $3.01 \%$ | $3.21 \%$ | $3.60 \%$ | $3.93 \%$ | $4.23 \%$ | $4.88 \%$ | $5.00 \%$ |

[^2]
## Bond Index Returns

The monthly returns on money market and fixed income (e.g., bond) investments are generated according to:

$$
r_{t}=\beta_{0} \times\left(i_{t}^{m}+\kappa\right)-\beta_{1} \times\left(i_{t}^{m}-i_{t-1}^{m}\right)+\sigma \cdot \sqrt{i_{t-1}} \cdot Z_{t}
$$

where $Z_{t}$ is a standard normal variate and $i_{t}^{m}$ is the $m$-year Treasury yield in period $t$. The money market process is a function of the 3-month yield, while the ITGVT and LTCORP bond index returns are respectively modeled from the 7-year and 10-year maturities. The model parameters are provided in Table 4.

The Fixed Income scenarios ("FIXED.csv") assume a constant asset mix of 65\% ITGVT and 35\% LTCORP. U.S. ITGVT and U.S. LTCORP are published indices (not managed funds) which respectively represent diversified portfolios of intermediate-term government bonds and long-term investment grade corporate bonds.

Table 4: Model Parameters for Bond Index Returns

|  | $m$ | $\beta_{0}$ | $\kappa$ | $\beta_{1}$ | $\sigma$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Money Market | 0.25 | 0.083333 | -0.00445 | -0.07148 | 0.00370 |
| U.S. ITGVT | 7 | 0.083333 | -0.00153 | 3.65043 | 0.05239 |
| U.S. LTCORP | 10 | 0.083333 | 0.00704 | 5.81293 | 0.08282 |

Although this is a simple empirical model, it has a plausible (and intuitive) interpretation and fits the observed data extremely well. Consistent with our expectations, the monthly return is composed of three elements:

- An income component, equal to one-twelfth of the reference yield rate plus a "credit/liquidity spread".
- A price movement term, equal to the duration of the index multiplied by the net increase in interest rates.
- A random shock, which reflects the relative level of interest rates and other extraneous factors.


## Equity Market Returns

The equity return scenarios are generated from a monthly SLV model wherein the natural logarithm of the annualized volatility follows a strong mean-reverting stochastic process and the annualized drift ${ }^{7}$ is a deterministic quadratic function of volatility. This model is not prescribed or 'preferred' above others, but was chosen because it captures many of the dynamics observed in the equity market data, including:

- Negative skewness and positive kurtosis ("fat tails") over short holding periods;
- Time-varying volatility and volatility clustering; and
- Increased volatility in bear markets.

The monthly SLV model is governed by the equations shown in Table 5. The model parameters (including descriptions) for each equity market are given in Table 6.

Table 5: SLV Model Processes

$$
\begin{aligned}
\tilde{v}(t) & =\operatorname{Min}\left[v^{+},(1-\phi) \times v(t-1)+\phi \times \ln (\tau)\right]+\sigma_{v} \times{ }_{v} Z_{t} \\
v(t) & =\operatorname{Max}\left\{v^{-}, \operatorname{Min}\left[v^{*}, \tilde{v}(t)\right]\right\} \\
\mu(t) & =A+B \times \sigma(t)+C \times \sigma^{2}(t) \\
\ln \left[\frac{S(t)}{S(t-1)}\right] & =\frac{\mu(t)}{12}+\frac{\sigma(t)}{\sqrt{12}} \times{ }_{s} Z_{t} \\
S(t) & =\text { stock index level at time } t \\
v(t) & =\text { natural logarithm of annualized volatility in month } t \\
\sigma(t) & =\text { annualized volatility of stock return process in month } t=\exp [v(t)] \\
\mu(t) & =\text { mean annualized log return ("drift") in month } t \\
v^{-} & =\text {lower bound for log volatility = } \ln \sigma^{-} \\
v^{+} & =\text {upper bound for log volatility (before random component) }=\ln \sigma^{+} \\
v^{*} & =\text { absolute upper bound for log volatility }=\ln \sigma^{*}
\end{aligned}
$$

${ }_{v} Z_{t}$ and ${ }_{s} Z_{t}$ are correlated standard normal random samples, where ${ }_{v} Z_{t}$ is the random "shock" to the $\log$ volatility process and ${ }_{s} Z_{t}$ is the random component for the stock index return. As noted previously, the drift term $\mu(t)$ is a deterministic quadratic function of $\sigma(t)$. In Table $6, v^{-}=\ln \sigma^{-}, v^{+}=\ln \sigma^{+}$and $v^{*}=\ln \sigma^{*}$. From the foregoing, it should be clear that given $\sigma(t)$, the log (i.e., continuous) returns in any month are normally distributed with mean $\frac{\mu(t)}{12}$ and standard deviation $\frac{\sigma(t)}{\sqrt{12}}$.[^3]

Table 6: Stochastic Log Volatility Model Parameters (Monthly) - Equity Markets

|  | Description | U.S. | INTL | SMALL | AGGR |
| :---: | :--- | ---: | ---: | ---: | ---: |
| $\tau$ | Long-run target volatility (annualized) | 0.12515 | 0.14506 | 0.16341 | 0.20201 |
| $\phi$ | Strength of mean reversion | 0.35229 | 0.41676 | 0.3632 | 0.35277 |
| $\sigma_{v}$ | Standard deviation of the log volatility process (monthly) | 0.32645 | 0.32634 | 0.35789 | 0.34302 |
| $\rho$ | Correlation co-efficient between ${ }_{v} Z_{t},{ }_{s} Z_{t}$ | -0.2488 | -0.1572 | -0.2756 | -0.2843 |
| $A$ | Drift of stock return process as $\sigma(t) \rightarrow 0$ (i.e., intercept) | 0.055 | 0.055 | 0.055 | 0.055 |
| $B$ | Co-efficient of quadratic function for $\mu(t)$ | 0.56 | 0.466 | 0.67 | 0.715 |
| $C$ | Co-efficient of quadratic function for $\mu(t)$ | -0.9 | -0.9 | -0.95 | -1 |
| $\sigma(0)$ | Starting volatility (annualized) | 0.1476 | 0.1688 | 0.2049 | 0.2496 |
| $\sigma^{-}$ | Minimum volatility (annualized) | 0.0305 | 0.0354 | 0.0403 | 0.0492 |
| $\sigma^{+}$ | Maximum volatility (annualized), before random component | 0.3 | 0.3 | 0.4 | 0.55 |
| $\sigma^{*}$ | Maximum volatility (annualized), after random component | 0.7988 | 0.4519 | 0.9463 | 1.1387 |

Table 7 provides some statistics for the simulated ("model") annualized volatilities compared to the historic data. For each market, an historic "volatility series" was constructed by calculating the 6-month rolling standard deviations of the monthly log returns. Table 8 shows statistics for the monthly log returns ${ }^{8}$.

Table 7: Statistics for Annualized Volatility

|  | U.S. Diversified <br> Equity |  | International <br> Diversified Equity |  | Intermediate Risk <br> Equity |  | Aggressive $/$ Exotic <br> Equity |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | History | Model | History | Model | History | Model | History | Model |
| Minimum | 0.014 | 0.031 | 0.042 | 0.035 | 0.041 | 0.040 | 0.071 | 0.049 |
| $10^{\mathbf{1 H}}$ Percentile | 0.068 | 0.072 | 0.080 | 0.087 | 0.088 | 0.090 | 0.113 | 0.114 |
| $\mathbf{2 5}^{\mathrm{TH}}$ Percentile | 0.093 | 0.094 | 0.103 | 0.111 | 0.117 | 0.120 | 0.136 | 0.150 |
| Median | 0.122 | 0.125 | 0.146 | 0.145 | 0.162 | 0.164 | 0.177 | 0.202 |
| $75^{\mathrm{TH}}$ Percentile | 0.164 | 0.167 | 0.194 | 0.190 | 0.213 | 0.224 | 0.280 | 0.274 |
| $\mathbf{9 0}^{\mathrm{TH}}$ Percentile | 0.200 | 0.217 | 0.237 | 0.243 | 0.292 | 0.296 | 0.360 | 0.360 |
| Maximum | 0.408 | 0.799 | 0.398 | 0.452 | 0.584 | 0.946 | 0.748 | 1.139 |
| Average | 0.133 | 0.137 | 0.153 | 0.157 | 0.181 | 0.182 | 0.221 | 0.224 |
| Standard Deviation | 0.062 | 0.062 | 0.064 | 0.065 | 0.094 | 0.089 | 0.125 | 0.106 |
| Skewness | 1.436 | 1.426 | 0.694 | 1.175 | 1.672 | 1.544 | 1.999 | 1.505 |
| Kurtosis | 3.810 | 3.756 | 0.496 | 1.980 | 3.902 | 4.242 | 5.161 | 4.090 |

Table 8: Statistics for Monthly Log Returns

|  | U.S. Diversified <br> Equity |  | International <br> Diversified Equity |  | Intermediate Risk <br> Equity |  | Aggressive I Exotic <br> Equity |  |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|  | History | Model | History | Model | History | Model | History | Model |
| $\mathbf{0 . 1}^{\mathbf{T H}}$ Percentile | -0.2423 | -0.2199 | -0.1553 | -0.2268 | -0.3452 | -0.3219 | -0.4541 | -0.3944 |
| $\mathbf{1 0}^{\mathbf{T H}}$ Percentile | -0.0451 | -0.0447 | -0.0519 | -0.0518 | -0.0577 | -0.0612 | -0.0662 | -0.0769 |
| $\mathbf{2 5}^{\mathbf{T H}}$ Percentile | -0.0155 | -0.0156 | -0.0176 | -0.0197 | -0.0212 | -0.0211 | -0.0190 | -0.0275 |
| Median | 0.0110 | 0.0086 | 0.0103 | 0.0081 | 0.0148 | 0.0105 | 0.0164 | 0.0119 |
| $\mathbf{7 5}^{\mathbf{T H}}$ Percentile | 0.0374 | 0.0309 | 0.0385 | 0.0345 | 0.0452 | 0.0391 | 0.0575 | 0.0473 |
| $\mathbf{9 0}^{\mathbf{T H}}$ Percentile | 0.0549 | 0.0540 | 0.0637 | 0.0619 | 0.0783 | 0.0694 | 0.0899 | 0.0842 |
| $\mathbf{9 9 . 9}^{\mathrm{TH}}$ Percentile | 0.1533 | 0.1691 | 0.1644 | 0.1953 | 0.2443 | 0.2258 | 0.2112 | 0.2707 |
| Average | 0.0084 | 0.0060 | 0.0086 | 0.0062 | 0.0112 | 0.0063 | 0.0120 | 0.0065 |
| Standard Deviation | 0.0426 | 0.0436 | 0.0487 | 0.0492 | 0.0598 | 0.0590 | 0.0721 | 0.0724 |
| Skewness | -0.59 | -0.67 | -0.33 | -0.40 | -0.72 | -0.89 | -1.47 | -0.91 |
| Kurtosis | 2.42 | 4.02 | 0.78 | 2.69 | 4.16 | 5.33 | 7.84 | 5.20 |

[^4]
## Correlations

The correlation matrix governing the stochastic processes is given in Table 9. The matrix is decomposed using the standard technique of Cholesky ${ }^{9}$ factorization in order to generate correlated normal samples.

Table 9: Correlation Matrix for Integrated Scenario Model

|  | $\underset{\text { LogVol }}{\text { US }}$ | US <br> LogRet | INTL <br> LogVol | INTL <br> LogRet | SMALL <br> LogVol | SMALL <br> LogRet | AGGR <br> LogVol | AGGR <br> LogRet | MONEY <br> Return | ITGVT <br> Return | LTCORP <br> Return |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| US <br> LogVol | 1 | -0.249 | 0.318 | -0.082 | 0.625 | -0.169 | 0.309 | -0.183 | 0.023 | 0.075 | 0.080 |
| US <br> LogRet | -0.249 | 1 | -0.046 | 0.630 | -0.123 | 0.829 | -0.136 | 0.665 | -0.120 | 0.192 | 0.393 |
| INTL <br> LogVol | 0.318 | -0.046 | 1 | -0.157 | 0.259 | -0.050 | 0.236 | -0.074 | -0.066 | 0.034 | 0.044 |
| INTL <br> LogRet | -0.082 | 0.630 | -0.157 | 1 | -0.063 | 0.515 | -0.098 | 0.558 | -0.105 | 0.130 | 0.234 |
| SMALL <br> LogVol | 0.625 | -0.123 | 0.259 | -0.063 | 1 | -0.276 | 0.377 | -0.180 | 0.034 | 0.028 | 0.054 |
| SMALL <br> LogRet | -0.169 | 0.829 | -0.050 | 0.515 | -0.276 | 1 | -0.142 | 0.649 | -0.106 | 0.067 | 0.267 |
| AGGR <br> LogVol | 0.309 | -0.136 | 0.236 | -0.098 | 0.377 | -0.142 | 1 | -0.284 | 0.026 | 0.006 | 0.045 |
| AGGR <br> LogRet | -0.183 | 0.665 | -0.074 | 0.558 | -0.180 | 0.649 | -0.284 | 1 | 0.034 | -0.091 | -0.002 |
| MONEY <br> Return | 0.023 | -0.120 | -0.066 | -0.105 | 0.034 | -0.106 | 0.026 | 0.034 | 1 | 0.047 | -0.028 |
| ITGVT <br> Return | 0.075 | 0.192 | 0.034 | 0.130 | 0.028 | 0.067 | 0.006 | -0.091 | 0.047 | 1 | 0.697 |
| LTCORP <br> Return | 0.080 | 0.393 | 0.044 | 0.234 | 0.054 | 0.267 | 0.045 | -0.002 | -0.028 | 0.697 | 1 |

[^5]Tables 10 and 11 respectively show the historic ("observed") and sample (from the 10,000 prepackaged scenarios) correlations for the monthly log returns.

Table 10: Historic Correlations for Monthly Log Returns

|  | S\&P500 | MSCI-EAFE <br> \$USD | U.S. <br> SmallCap | Aggressive <br> Equity | Money <br> Market | U.S. <br> ITGVT | U.S. <br> LTCORP |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| S\&P500 | $\mathbf{1}$ |  |  |  |  |  |  |
| MSCI-EAFE <br> \$USD | 0.560 | $\mathbf{1}$ | 0.447 | $\mathbf{1}$ | $\mathbf{1}$ |  |  |
| U.S. <br> SmallCap | 0.759 | 0.488 | 0.579 | $\mathbf{1}$ |  |  |  |
| Aggressive <br> Equity | 0.595 | -0.059 | -0.053 | 0.002 | $\mathbf{1}$ | 1 |  |
| Money <br> Market | -0.046 | 0.091 | 0.042 | -0.064 | 0.113 | $\mathbf{1}$ |  |
| U.S. <br> ITGVT | 0.137 | 0.171 | 0.184 | -0.005 | 0.026 | 1 |  |
| U.S. <br> LTCORP | 0.280 |  |  |  |  |  |  |

Table 11: Model Correlations (10,000 Scenarios) for Monthly Log Returns

|  | U.S. | INTL | SMALL | AGGR | MONEY | ITGVT | LTCORP |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| U.S. | 1 |  |  |  |  |  |  |
| INTL | 0.558 | 1 |  |  |  |  |  |
| SMALL | 0.762 | 0.445 | 1 |  |  |  |  |
| AGGR | 0.577 | 0.481 | 0.565 | 1 |  |  |  |
| MONEY | -0.036 | -0.031 | -0.030 | 0.009 | 1 |  |  |
| ITGVT | 0.143 | 0.099 | 0.048 | -0.067 | 0.084 | 1 |  |
| LTCORP | 0.303 | 0.184 | 0.201 | -0.002 | 0.015 | 0.775 | 1 |

## Scenario Statistics - Accumulation Factors

Tables 12 through 15 provide sample statistics for the accumulation factors (gross wealth ratios) over various holding periods. For reference, the calibration points ${ }^{10}$ (applicable to U.S. Diversified Equity) are also shown. Within sampling error, the statistics for the U.S. Equity scenarios satisfy these criteria.

Table 12: Statistics for 1-Year Accumulation Factors

|  | Calibration <br> Point | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathbf{0 . 5 \%}$ |  | 1.003 | 0.909 | 0.848 | 0.658 | 0.649 | 0.549 | 0.470 |
| $\mathbf{1 . 0 \%}$ |  | 1.004 | 0.921 | 0.865 | 0.700 | 0.694 | 0.603 | 0.531 |
| $\mathbf{2 . 5 \%}$ | $\mathbf{0 . 7 8}$ | 1.006 | 0.937 | 0.893 | 0.756 | 0.760 | 0.679 | 0.612 |
| $\mathbf{5 . 0 \%}$ | $\mathbf{0 . 8 4}$ | 1.008 | 0.953 | 0.915 | 0.818 | 0.810 | 0.748 | 0.695 |
| $\mathbf{1 0 . 0 \%}$ | $\mathbf{0 . 9 0}$ | 1.011 | 0.970 | 0.941 | 0.886 | 0.872 | 0.827 | 0.787 |
| $\mathbf{5 0 . 0 \%}$ |  | 1.022 | 1.027 | 1.033 | 1.089 | 1.083 | 1.096 | 1.102 |
| $\mathbf{9 0 . 0 \%}$ | $\mathbf{1 . 2 8}$ | 1.034 | 1.085 | 1.130 | 1.297 | 1.330 | 1.382 | 1.461 |
| $\mathbf{9 5 . 0 \%}$ | $\mathbf{1 . 3 5}$ | 1.038 | 1.101 | 1.156 | 1.370 | 1.408 | 1.485 | 1.584 |
| $\mathbf{9 7 . 5 \%}$ | $\mathbf{1 . 4 2}$ | 1.041 | 1.115 | 1.177 | 1.437 | 1.494 | 1.572 | 1.711 |
| $\mathbf{9 9 . 0 \%}$ |  | 1.044 | 1.132 | 1.205 | 1.518 | 1.596 | 1.707 | 1.880 |
| $\mathbf{9 9 . 5 \%}$ |  | 1.046 | 1.144 | 1.226 | 1.590 | 1.658 | 1.827 | 2.016 |
| Mean |  | 1.022 | 1.027 | 1.034 | 1.089 | 1.095 | 1.103 | 1.117 |
| Stdev |  | 0.009 | 0.045 | 0.073 | 0.166 | 0.185 | 0.226 | 0.275 |

Table 13: Statistics for 5-Year Accumulation Factors

|  | Calibration <br> Point | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathbf{0 . 5 \%}$ |  | 1.019 | 0.938 | 0.812 | 0.537 | 0.495 | 0.380 | 0.287 |
| $\mathbf{1 . 0 \%}$ |  | 1.025 | 0.961 | 0.848 | 0.620 | 0.568 | 0.441 | 0.348 |
| $\mathbf{2 . 5 \%}$ | $\mathbf{0 . 7 2}$ | 1.037 | 0.995 | 0.908 | 0.722 | 0.681 | 0.545 | 0.455 |
| $\mathbf{5 . 0 \%}$ | $\mathbf{0 . 8 1}$ | 1.052 | 1.024 | 0.955 | 0.807 | 0.772 | 0.664 | 0.565 |
| $\mathbf{1 0 . 0 \%}$ | $\mathbf{0 . 9 4}$ | 1.072 | 1.060 | 1.015 | 0.933 | 0.891 | 0.804 | 0.718 |
| $\mathbf{5 0 . 0 \%}$ |  | 1.160 | 1.194 | 1.234 | 1.452 | 1.464 | 1.491 | 1.525 |
| $\mathbf{9 0 . 0 \%}$ | $\mathbf{2 . 1 7}$ | 1.267 | 1.341 | 1.490 | 2.222 | 2.358 | 2.597 | 2.995 |
| $\mathbf{9 5 . 0 \%}$ | $\mathbf{2 . 4 5}$ | 1.305 | 1.389 | 1.569 | 2.481 | 2.677 | 3.038 | 3.619 |
| $\mathbf{9 7 . 5 \%}$ | $\mathbf{2 . 7 2}$ | 1.337 | 1.439 | 1.637 | 2.731 | 3.022 | 3.485 | 4.329 |
| $\mathbf{9 9 . 0 \%}$ |  | 1.381 | 1.485 | 1.731 | 3.063 | 3.417 | 4.084 | 5.116 |
| $\mathbf{9 9 . 5 \%}$ |  | 1.413 | 1.515 | 1.804 | 3.315 | 3.746 | 4.520 | 5.938 |
| Mean |  | 1.166 | 1.198 | 1.245 | 1.525 | 1.563 | 1.626 | 1.737 |
| Stdev |  | 0.077 | 0.111 | 0.188 | 0.520 | 0.606 | 0.760 | 1.005 |

[^6]Table 14: Statistics for 10-Year Accumulation Factors

|  | Calibration <br> Point | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathbf{0 . 5 \%}$ |  | 1.064 | 1.055 | 0.905 | 0.572 | 0.501 | 0.345 | 0.236 |
| $\mathbf{1 . 0 \%}$ |  | 1.081 | 1.087 | 0.956 | 0.653 | 0.573 | 0.429 | 0.302 |
| $\mathbf{2 . 5 \%}$ | $\mathbf{0 . 7 9}$ | 1.112 | 1.139 | 1.041 | 0.771 | 0.730 | 0.557 | 0.412 |
| $\mathbf{5 . 0 \%}$ | $\mathbf{0 . 9 4}$ | 1.146 | 1.190 | 1.118 | 0.923 | 0.865 | 0.718 | 0.561 |
| $\mathbf{1 0 . 0 \%}$ | $\mathbf{1 . 1 6}$ | 1.194 | 1.250 | 1.213 | 1.124 | 1.048 | 0.932 | 0.780 |
| $\mathbf{5 0 . 0 \%}$ |  | 1.409 | 1.487 | 1.596 | 2.089 | 2.120 | 2.191 | 2.219 |
| $\mathbf{9 0 . 0 \%}$ | $\mathbf{3 . 6 3}$ | 1.714 | 1.823 | 2.115 | 3.805 | 4.223 | 4.851 | 6.059 |
| $\mathbf{9 5 . 0 \%}$ | $\mathbf{4 . 3 6}$ | 1.834 | 1.941 | 2.297 | 4.441 | 5.077 | 6.042 | 7.851 |
| $\mathbf{9 7 . 5 \%}$ | $\mathbf{5 . 1 2}$ | 1.954 | 2.062 | 2.464 | 5.173 | 6.085 | 7.301 | 9.603 |
| $\mathbf{9 9 . 0 \%}$ |  | 2.097 | 2.233 | 2.694 | 6.182 | 7.316 | 9.472 | 12.633 |
| $\mathbf{9 9 . 5 \%}$ |  | 2.203 | 2.339 | 2.856 | 6.993 | 8.404 | 10.992 | 15.376 |
| Mean |  | 1.437 | 1.517 | 1.637 | 2.321 | 2.445 | 2.634 | 2.958 |
| Stdev |  | 0.214 | 0.235 | 0.364 | 1.147 | 1.401 | 1.823 | 2.599 |

Table 15: Statistics for 20-Year Accumulation Factors

|  | Calibration <br> Point | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| :---: | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $\mathbf{0 . 5 \%}$ |  | 1.230 | 1.383 | 1.229 | 0.706 | 0.596 | 0.393 | 0.211 |
| $\mathbf{1 . 0 \%}$ |  | 1.270 | 1.446 | 1.348 | 0.830 | 0.732 | 0.491 | 0.298 |
| $\mathbf{2 . 5 \%}$ |  | 1.357 | 1.544 | 1.526 | 1.101 | 0.995 | 0.688 | 0.474 |
| $\mathbf{5 . 0 \%}$ | $\mathbf{1 . 5 1}$ | 1.441 | 1.646 | 1.672 | 1.411 | 1.251 | 0.953 | 0.730 |
| $\mathbf{1 0 . 0 \%}$ | $\mathbf{2 . 1 0}$ | 1.559 | 1.782 | 1.868 | 1.832 | 1.696 | 1.380 | 1.095 |
| $\mathbf{5 0 . 0 \%}$ |  | 2.165 | 2.473 | 2.841 | 4.274 | 4.442 | 4.618 | 4.851 |
| $\mathbf{9 0 . 0 \%}$ | $\mathbf{9 . 0 2}$ | 3.350 | 3.779 | 4.636 | 10.153 | 11.816 | 14.736 | 19.775 |
| $\mathbf{9 5 . 0 \%}$ | $\mathbf{1 1 . 7 0}$ | 3.939 | 4.385 | 5.459 | 12.926 | 15.475 | 19.866 | 29.577 |
| $\mathbf{9 7 . 5 \%}$ |  | 4.508 | 5.090 | 6.488 | 15.653 | 20.040 | 26.467 | 41.019 |
| $\mathbf{9 9 . 0 \%}$ |  | 5.402 | 6.264 | 7.922 | 20.586 | 26.076 | 37.184 | 62.771 |
| $\mathbf{9 9 . 5 \%}$ |  | 6.240 | 7.662 | 9.011 | 24.523 | 32.851 | 49.303 | 80.079 |
| Mean |  | 2.363 | 2.689 | 3.123 | 5.385 | 5.946 | 6.933 | 8.782 |
| Stdev |  | 0.881 | 0.995 | 1.317 | 4.065 | 5.301 | 7.687 | 12.479 |

## Scenario Statistics - Returns

Tables 16 through 18 show statistics for the gross returns on each asset class over various holding periods (i.e., years $1-10,11-20$, etc.). As expected, the returns (and volatilities) on the fixed income funds rise over time, consistent with the parameterization of the interest rate model. The returns and volatilities on the equity funds are relatively constant (within sampling error) since the starting volatility (at "time zero" - see Table 6) for each market is set roughly equal to the long-term average.

Table 16: Average Annualized Holding Period Return (Annual Effective)

|  | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $\mathbf{1 - 1 0}$ | $3.69 \%$ | $4.25 \%$ | $5.05 \%$ | $8.79 \%$ | $9.35 \%$ | $10.17 \%$ | $11.45 \%$ |
| $\mathbf{1 1 - 2 0}$ | $4.92 \%$ | $5.85 \%$ | $6.74 \%$ | $8.76 \%$ | $9.26 \%$ | $10.09 \%$ | $11.45 \%$ |
| $\mathbf{2 1 - 3 0}$ | $5.36 \%$ | $6.58 \%$ | $7.60 \%$ | $8.63 \%$ | $9.16 \%$ | $9.96 \%$ | $11.31 \%$ |
| $\mathbf{3 0}$ Years | $4.87 \%$ | $5.69 \%$ | $6.49 \%$ | $8.73 \%$ | $9.26 \%$ | $10.11 \%$ | $11.37 \%$ |

Table 17: Median Annualized Holding Period Return (Annual Effective)

|  | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $\mathbf{1 - 1 0}$ | $3.49 \%$ | $4.05 \%$ | $4.79 \%$ | $7.65 \%$ | $7.81 \%$ | $8.16 \%$ | $8.30 \%$ |
| $\mathbf{1 1 - \mathbf { 2 0 }}$ | $4.38 \%$ | $5.11 \%$ | $5.89 \%$ | $7.69 \%$ | $7.80 \%$ | $8.07 \%$ | $8.44 \%$ |
| $\mathbf{2 1 - 3 0}$ | $4.68 \%$ | $5.65 \%$ | $6.49 \%$ | $7.55 \%$ | $7.76 \%$ | $7.97 \%$ | $8.39 \%$ |
| $\mathbf{3 0}$ Years | $4.21 \%$ | $5.03 \%$ | $5.79 \%$ | $7.53 \%$ | $7.73 \%$ | $7.89 \%$ | $8.18 \%$ |

Table 18: Annualized Volatility

|  | MONEY | ITGVT | LTCORP | U.S. | INTL | SMALL | AGGR |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $\mathbf{1 - 1 0}$ | $0.67 \%$ | $4.66 \%$ | $7.31 \%$ | $15.15 \%$ | $17.06 \%$ | $20.48 \%$ | $25.18 \%$ |
| $\mathbf{1 1 - \mathbf { 2 0 }}$ | $0.84 \%$ | $5.19 \%$ | $8.09 \%$ | $15.11 \%$ | $17.04 \%$ | $20.44 \%$ | $25.10 \%$ |
| $\mathbf{2 1 - 3 0}$ | $0.90 \%$ | $5.42 \%$ | $8.44 \%$ | $15.05 \%$ | $16.99 \%$ | $20.40 \%$ | $24.98 \%$ |
| $\mathbf{3 0}$ Years | $0.83 \%$ | $5.10 \%$ | $7.96 \%$ | $15.10 \%$ | $17.03 \%$ | $20.44 \%$ | $25.08 \%$ |

Pre-packaged Scenario Files

The pre-packaged scenarios are available for download from the American Academy of Actuaries ("AAA") website http://www.actuary.org. The following files are provided in comma-separated value (*.csv) text format (i.e., each scenario is terminated with a new line and line feed character).

It is important to note that the scenarios have been constructed so that the $K^{\text {th }}$ scenario (path) for each asset class must be used together and considered one "future investment return environment". It is inappropriate to misalign the ordering of scenarios (e.g., scenario $J$ for "Diversified U.S. Equity" cannot be combined with scenario $K$ for "Diversified International Equity”, $J \neq K$ ).

The scenario files provide monthly values for 30 years. The first column applies at "time zero". For interest rates, the first column in the scenario matrix is the yield at the start of the test. For all other files, the first column is composed entirely of ones (certain software programs may require this column to be removed before use). Hence, the size of the 'scenario matrix' in each file is $10,000 \times(1+12 \times 30)=10,000 \times 361$.

The U.S. Treasury yields are expressed as nominal semi-annual bond equivalent yields in decimal format. All other returns are expressed as periodic (not cumulative) market accumulation factors (i.e., monthly "gross wealth ratios”). Interest rates are assumed to change at the start of each month, hence the value in column T applies for month $\mathrm{T}-1$. The market accumulation factor in column $\mathrm{T}$ represents the growth in month $\mathrm{T}-1$.

Durations 0 through 9 (inclusive) for the first ten (10) scenarios in the Diversified U.S. Equity file are shown below in Table 19. Table 20 gives the first ten scenarios for the 10-year U.S. Treasury yields. Using scenario 6 as an example, the yield in month 3 is $4.5164 \%$ and the monthly U.S. equity growth factor is 1.006528 .

Table 19: First 10 Scenarios for Diversified U.S. Equity (US.csv) - Monthly Accumulation Factors

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1.092469 | 1.083986 | 1.006021 | 1.015863 | 1.020886 | 1.017517 | 1.033370 | 1.065896 | 1.014492 |
| 2 | 1 | 0.919721 | 0.974064 | 1.004553 | 1.010235 | 1.013128 | 0.996171 | 1.008690 | 0.979059 | 1.001054 |
| 3 | 1 | 1.017425 | 1.019115 | 1.026518 | 0.975530 | 1.006764 | 1.020923 | 0.956538 | 0.963677 | 0.985936 |
| 4 | 1 | 1.050778 | 1.009128 | 1.083217 | 0.956835 | 0.968311 | 1.042744 | 0.983705 | 1.045328 | 1.049569 |
| 5 | 1 | 0.980780 | 0.994217 | 1.019358 | 0.991551 | 1.120387 | 0.877891 | 1.049358 | 0.950271 | 1.005277 |
| 6 | 1 | 0.971779 | 0.978151 | 1.006528 | 1.005762 | 1.060561 | 1.058023 | 1.014724 | 0.972309 | 0.993515 |
| 7 | 1 | 0.925176 | 1.009579 | 1.062304 | 1.019200 | 1.050946 | 1.045153 | 1.015894 | 1.001342 | 1.000698 |
| 8 | 1 | 1.050359 | 0.995239 | 0.990647 | 1.013092 | 1.000848 | 1.004970 | 0.974614 | 1.024655 | 0.991690 |
| 9 | 1 | 1.035438 | 1.010034 | 1.009361 | 1.013842 | 1.022945 | 1.015931 | 1.020676 | 0.920945 | 1.063518 |
| 10 | 1 | 1.018519 | 1.162125 | 1.030109 | 1.052653 | 1.070173 | 1.025596 | 1.010738 | 0.958566 | 0.978353 |

Table 20: First 10 Scenarios for 10-year U.S. Treasury yield (UST_10y.csv) - Nominal SIA BEY

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.0423 | 0.042787 | 0.043649 | 0.043802 | 0.044557 | 0.046567 | 0.044913 | 0.044837 | 0.048417 | 0.049807 |
| 2 | 0.0423 | 0.043597 | 0.043754 | 0.045324 | 0.047070 | 0.048851 | 0.048940 | 0.047389 | 0.046302 | 0.046620 |
| 3 | 0.0423 | 0.042218 | 0.041209 | 0.042634 | 0.042988 | 0.041944 | 0.040294 | 0.038418 | 0.037532 | 0.038767 |
| 4 | 0.0423 | 0.043108 | 0.041918 | 0.042406 | 0.042604 | 0.041861 | 0.042539 | 0.044035 | 0.044223 | 0.042515 |
| 5 | 0.0423 | 0.043627 | 0.043071 | 0.041678 | 0.039150 | 0.035005 | 0.032911 | 0.033751 | 0.034600 | 0.034904 |
| 6 | 0.0423 | 0.043018 | 0.043928 | 0.045164 | 0.045187 | 0.043728 | 0.042704 | 0.044122 | 0.043114 | 0.041484 |
| 7 | 0.0423 | 0.044257 | 0.045586 | 0.046619 | 0.046970 | 0.044459 | 0.042934 | 0.044681 | 0.046048 | 0.046603 |
| 8 | 0.0423 | 0.042637 | 0.040846 | 0.040029 | 0.038512 | 0.037170 | 0.035555 | 0.035722 | 0.038985 | 0.040438 |
| 9 | 0.0423 | 0.042294 | 0.043150 | 0.045104 | 0.046244 | 0.048910 | 0.049638 | 0.050845 | 0.053803 | 0.054804 |
| 10 | 0.0423 | 0.042397 | 0.041191 | 0.042953 | 0.043788 | 0.043130 | 0.042707 | 0.042405 | 0.043704 | 0.044746 |

## Scenario Conversion

If a company chooses to make use of the scenarios, it will be the company's responsibility to translate the scenarios into the format required by its projection software. This could require a change to the periodicity (i.e., timestep) and/or type of return. This conversion will normally be straightforward, but is clearly a critical step in the scenario testing. The actuary will usually conduct or oversee the successful conversionof the scenarios. For conversion purposes, the company should assume geometric averaging to transform the interest rates.

Tables 21 and 22 show the conversion to a quarterly timestep for a variety of return types for scenario 6.

Table 21: Conversion of Diversified U.S. Equity Accumulation Factors to Quarterly Periodicity

| Month | Accumulation <br> Factor | Quarter | Accumulation <br> Factor (1) | Log Return <br> (2) | Nominal <br> Return (3) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.971779 |  |  |  |  |
| 2 | 0.978151 | 1 | 0.956752 | -0.044211 | -0.043248 |
| 3 | 1.006528 |  |  |  |  |
| 4 | 1.005762 |  |  |  |  |
| 5 | 1.060561 |  |  |  | 0.1285636 |
| 6 | 1.058023 |  |  |  |  |

(1) Product of the monthly accumulation factors.

(2) Natural logarithm of the quarterly accumulation factor = sum of monthly log returns.

(3) Quarterly accumulation factor - 1.

Table 22: Conversion of 10-year U.S. Treasury Yields to Quarterly Periodicity

| Month | Semi-Annual <br> Bond Yield | Quarter | Semi-Annual <br> Bond Yield (4) | Effective Rate <br> $(5)$ | Continuous <br> Return (6) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.043018 | 1 | 0.0440365 | 0.0445213 | 0.0435587 |
| 2 | 0.043928 |  |  |  |  |
| 3 | 0.045164 |  |  |  |  |
| 4 | 0.045187 | 2 | 0.0438727 | 0.0443540 | 0.0433985 |
| 5 | 0.043728 |  |  |  |  |
| 6 | 0.042704 |  |  |  |  |

(4) For the $k^{\text {th }}$ quarter, $i_{k}^{*}=2 \times\left[\left(\prod_{t=1}^{3}\left(1+\frac{i_{3(k-1)+t}}{2}\right)\right)^{\frac{1}{3}}-1\right]$.

(5) $i_{k}^{\prime}=\left(1+\frac{i_{k}^{*}}{2}\right)^{2}-1$.

(6) Natural logarithm of $\left(1+i_{k}^{\prime}\right)$.

## Representative Scenarios

Recognizing that the company may wish to run fewer than 10,000 scenarios, we have created a utility in Microsoft ${ }^{\circledR}$ Excel 2002 which selects a representative subset of size $N$ (user-specified). The workbook "Scenario Picking Tool (AAA LCAS C3 Phase II RBC) v6 Locked.xls" is available for download from the AAA website.

A significance measure $S$ (defined below) has been calculated for each scenario. The selection process ranks (orders) the significance values and stratifies the sample, picking the mid-point of each stratum as the representative. The selection process has been designed so that the representative scenarios are equally likely.

The significance $S$ of an investment return path is defined as:

$$
S=\sqrt{\sum_{t=1}^{H}\left(\prod_{k=1}^{t} \frac{1}{A F_{k}}\right)^{2}}
$$

where time is measured in months and $A F_{k}$ is the accumulation factor in month $k$. We have selected a horizon $H=180$ months (i.e., 15 years) in the calculations.

The workbook is fully documented and easy to use. Only a handful of fields (cells) are accessible; the rest of the workbook is locked for protection. Input fields are identified by light yellow or ivory background shading and blue font for text. The actuary simply selects an asset class for the scenario selection using the drop-down list and inputs the desired number of scenarios (minimum 200). The selected asset class should closely approximate the investment option (fund category) to which the company is most exposed. For most companies, this would be the "Diversified U.S. Equity" class.

The representative scenarios are identified by scenario number. The significance measures are also provided. This output is located in the cells with light green shading and may be copied and pasted into other applications.

## Sampling Error

Statistical measures estimated by simulation are always subject to sampling error. For tail measures (e.g., quantiles, CTE, etc.) the mis-estimation due to sampling error can be significant, especially when there are fewer than 1000 scenarios. As such, the selection method to obtain representative scenarios should be used with caution. As a general rule, the company should attempt to process as many scenarios as possible. If fewer than 1000 scenarios are used, it is strongly advised that the company investigate the potential sampling error and adjust the results according to prior sensitivity testing. Such analysis could include testing the variability in results for a small, suitably chosen 'representative portfolio',11.[^7]


[^0]:    ${ }^{1}$ Variations on this title include "Recommended Approach for Setting Regulatory Risk-Based Capital Requirements for Variable Products with Guarantees (Excluding Index Guarantees)"

    ${ }^{2}$ Note: This document and the accompanying "pre-packaged" scenarios replace those provided in 2004.

[^1]:    ${ }^{3}$ The Mersenne Twister is a well documented and robust algorithm with extremely high periodicity.

[^2]:    ${ }^{4}$ The interest rate model is designed for cash flow projections only. It is not arbitrage-free and could give inappropriate values if used to price options and other derivatives as part of an asset/liability management strategy.

    ${ }^{5}$ The 30 -year maturity was estimated by fitting the rest of the curve to a power function. It is not used in the modeling.

    ${ }^{6}$ The historic data tend to suggest a weak negative correlation between interest rate movements and equity returns.

[^3]:    ${ }^{7}$ In this document, the term "drift" refers to the expected instantaneous return.

[^4]:    ${ }^{8}$ In Table 8, the $0.1 \%$ and $99.9 \%$ values for history are respectively the minimum and maximum monthly returns over the observation period

[^5]:    ${ }^{9}$ The Cholesky decomposition method works when the matrix is positive semi-definite (i.e., has non-negative eigenvalues). The correlation matrix in Table 9 satisfies this property.

[^6]:    ${ }^{10}$ The calibration points are taken from Table 1 in Appendix 2 of the March 2005 LCAS Report.

[^7]:    ${ }^{11}$ Suppose the company wishes to use $N$ scenarios $(N<10,000)$. It could adjust the total portfolio CTE $(X)$ based on the difference in $\operatorname{CTE}(X)$ results for a representative portfolio run over (1) all 10,000 pre-packaged scenarios and (2) the selected subset of $N$ paths.

