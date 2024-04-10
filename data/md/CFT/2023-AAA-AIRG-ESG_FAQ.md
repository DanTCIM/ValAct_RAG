![](https://cdn.mathpix.com/cropped/2024_04_10_32a86db207c052644d1fg-1.jpg?height=323&width=1542&top_left_y=191&top_left_x=232)

# Academy Interest Rate Generator: Frequently Asked Questions (FAQ) 

MAY 2023

This frequently asked questions (FAQ) document has been developed by the Joint Economic Scenario Generator Project Oversight Group of the American Academy of Actuaries (Academy) and the Society of Actuaries (SOA) to provide information relevant to the Academy Interest Rate Generator (AIRG). ${ }^{1}$

The Academy's Economic Scenario Work Group (ESWG) originally released an interest rate generator, calibration criteria, and a scenario picking tool in December 2008. The ESWG developed Version 7 of the AIRG in 2010; the enhancements to Version 7 are summarized in Question 4 below. Subsequent updates to Version 7 are summarized in Question 7.

The latest version of the AIRG is available on the SOA's website at: www.soa.org/resources/tablescalcs-tools/research-scenario/ and can also be accessed from the Academy's website at: https://www.actuary.org/content/economic-scenario-generators.

## 1. What is the status of the AIRG? Has it been approved for use in VM-20 reserves and C3P3?

VM-20

In August 2010, the National Association of Insurance Commissioners (NAIC) adopted the Standard Valuation Law. The NAIC adopted the Valuation Manual (VM) on Dec. 2, 2012. The VM-20 section of the revised Valuation Manual prescribes the calculation of life reserves and includes a description of the scenario requirements. The NAIC Life Actuarial (A) Task Force (LATF) has designated the AIRG as the prescribed generator for VM-20. LATF did not allow the use of proprietary generators for stochastic life reserve calculations in VM-20.

The 2010 release of the AIRG was used to develop scenarios for the NAIC study of the impact of the VM-20 on reserves for life insurance products.

## C3P3

The NAIC Life Risk-Based Capital Working Group (LRBCWG) has exposed the Academy's C3 Life and Annuity Capital Work Group's recommendation titled "RBC C3 Requirements for[^0]

Life Products,” which includes the recommendation to use either the AIRG or proprietary generators whose scenarios satisfy the required calibration criteria. The NAIC has not taken any formal action on the exposure.

## 2. Is the AIRG approved for use in C3P1, C3P2, and AG43?

The ESWG, along with the Academy's Life Capital Adequacy Subcommittee (LCAS), recommended that the AIRG replace the Enhanced C3 Phase I Interest Rate Generator. Some specific elements of the C3P1 calculation and/or instructions will need to be modified before the NAIC can prescribe the use of this new AIRG in regulatory capital calculations.

## C3P1

The AIRG has not yet been approved by the NAIC for use in C3P1 capital calculations. Until further action by the NAIC, C3P1 requires the use of the Enhanced C3 Phase I Interest Rate Generator.

The Enhanced C3 Phase I Interest Rate Generator is available at:

www.naic.org/documents/committees_e_capad_lrbc_RbcC3Scn.xls.

## C3P2 and AG43

Both C3P2 and Actuarial Guideline XLIV (AG43) allow companies to generate and use their own scenarios, provided those scenarios meet the calibration criteria. Therefore, equity and interest rate scenarios (including fixed-income equity scenarios) can be generated using the AIRG for use in C3P2 and AG43 calculations, as long as the scenarios satisfy the approved calibration criteria. The AIRG fixed-income return scenarios will differ from the pre-packaged scenarios previously generated and available on the Academy's website.

- For AG43, a company can generate scenarios or use the approved pre-packaged scenarios. A company can use any tool to generate scenarios, including the new AIRG. Regardless of the generator used, the equity scenarios must meet the prescribed calibration criteria.

The pre-packaged scenarios can be found at: www.actuary.org/content/c3-phase-ii-pre-packaged-asset-scenarios.

They are fully documented at: www.actuary.org/pdf/life/c3supp_march05.pdf.

- For C3P2, the pre-packaged equity scenarios are the same as those approved for AG43, and can also be found at: www.actuary.org/content/c3-phase-ii-pre-packaged-asset-scenarios.

If generating scenarios, the equity scenarios need to meet the calibration methodology and requirements outlined in Appendix 2 of the Life Capital Adequacy Subcommittees' June 2005 report, Recommended Approach for Setting Regulatory Risk-Based Capital Requirements for Variable Annuities and Similar Products.

## 3. Are proprietary generators allowed in regulatory calculations?

As described above, the NAIC allows the use of proprietary generators for AG43 and C3P2 calculations, as long as the generated scenarios satisfy the calibration criteria adopted by the NAIC.

While the Academy's Life Reserves Work Group recommended the use of proprietary generators for life reserve calculations subject to calibration criteria, LATF did not include the use of proprietary generators for stochastic life reserve calculations in the exposed version of VM-20. The Academy's Life Capital Work Group also recommended the use of proprietary generators for C3P3 capital calculations. While the Academy's Life Capital Work Group's recommendation on C3P3 capital requirements was exposed for comment, the LRBCWG has not yet voted on any aspect of the C3P3 recommendations, including the use of proprietary generators for C3P3.

## 4. What enhancements were included in the 2010 release of the AIRG?

The AIRG released in 2010 is based on the same methodology as the 2008 release and was updated to be more user-friendly. In particular, the 2010 release:

- Allows the generator to be run with different starting dates.
- Calculates the mean reversion point reflecting the formula approved by LATF for use in VM-20 calculations. The mean reversion calculation has been programmed, so that it will automatically update based on future changes in interest rates. The mean reversion point is held constant during a calendar year based on January values.
- Produces Stochastic Exclusion Test (SET) scenarios as of a specified date.
- Includes ability to generate spot rates. The generator can save results as either coupon yield curves or as spot rate yield curves, based on user selection. The coupon yield curves are expressed as bond-equivalent yields (i.e., a rate to be compounded every six months) while the spot rates are expressed as annual-effective yields. Because derivation of a spot curve from a bond curve requires values for the coupon bond curve at six-month maturity intervals, the derivation used here is based on linear interpolation between the 10 points on the bond curve that are output from the generator.
- Includes the scenario picker tool developed by the ESWG with the generator and is automatically run whenever 10,000 scenarios are generated. The results are used to pick subsets of less than 10,000 upon request. This scenario picking tool has been provided as a convenience to users, and its inclusion with the AIRG should not be construed as the preferred scenario reduction technique; many scenario reduction techniques or other modeling efficiency techniques can be used. If the ESWG scenario picker is used for regulatory calculations (e.g., VM-20 or AG43), the actuary must confirm that any scenario subsets satisfy the calibration criteria, no matter how the scenarios were selected.
- Incorporates the ability to generate either interest rate or equity scenarios within the same workbook. The generator for fixed-income fund returns has been integrated with the generator for interest rate scenarios so that fund returns depend on the change in interest rates in the same scenario.
- Includes additional functionality, such as the ability to:
- More easily view the generated scenarios;
- Generate a user-specified number of scenarios; and
- Output results to a new file format called EconSML (format developed by the Technology Section of the SOA as a proposed standard for exchange of scenario files between modeling systems).


## 5. Were there any technical changes to the 2010 release of the AIRG?

The ESWG made a technical modification to the AIRG. The method of yield curve interpolation was changed from an approach based on historical curves to one using the Nelson-Siegel formula. The impetus for this change was the occurrence of anomalous results when generated yield curves went outside the range of historical observations.

Nelson-Siegel parameters were chosen so as to produce results similar to the historical method across a broad range of observed yield curves. Results outside observed ranges were deemed to be reasonable.

The floor on generated interest rates has been changed to 0.01 percent. The previous floor was formulaic.

## 6. Will the ESWG or other Academy/SOA work groups continue to provide prepackaged scenarios?

Pre-packaged scenarios have been generated by Academy work groups at various times in the past and will remain available on the Academy website. However, going forward, neither the Academy nor the SOA will publish updated pre-packaged scenarios.

## 7. What information on the AIRG is available on the Academy and the SOA websites?

Information on the AIRG can be found at:

- actuary.org/content/economic-scenario-generators, and
- $\quad$ www.soa.org/tables-calcs-tools/research-scenario/.

Since early 2009, the Academy website has included the following information relating to the initial release of the AIRG:

- December 2008 report from the ESWG that describes the development of the generator and the calibration criteria.
- Interest rate generator with parameters set to develop interest scenarios based on the Sept. 30, 2008, Treasury curve.
- 10,000 pre-packaged interest scenarios developed as of Sept. 30, 2008, and a subset of 1,000 scenarios that meet the calibration criteria.
- Scenario picking tool that can be used to pick a subset of scenarios from the 10,000 pre-packaged interest scenarios using a significance measure method (see additional
details below). The actuary will need to confirm that subsets produced from the tool satisfy the calibration criteria.
- Sixteen Stochastic Exclusion Test scenarios (including both interest and equity rates for these scenarios) developed as of Sept. 30, 2008.

In late 2009, the ESWG updated the AIRG parameters to develop interest scenarios based on the Sept. 30, 2009, U.S. Treasury curve. The following information was posted on the Academy website in February 2010:

- 10,000 pre-packaged interest scenarios developed as of Sept. 30, 2009, and a subset of 1,000 scenarios that meet the calibration criteria.
- Scenario picking tool that can be used to pick a subset of scenarios from the 10,000 pre-packaged interest scenarios using a significance measure method (see additional details below). If used for regulatory calculations (e.g., VM-20, AG43), the actuary will need to confirm that subsets produced from the tool satisfy the calibration criteria.
- Sixteen Stochastic Exclusion Test scenarios (including both interest and equity rates for these scenarios) developed as of Sept. 30, 2009.

In November 2010, the ESWG revised the AIRG and posted the following information to the Academy website:

- 2010 release of the AIRG
- Release notes for 2010 release

In December 2011, the Academy and the SOA joined forces to provide user support to members on the generators. The SOA offers front-line support on the generators, with a Project Oversight Group (POG) providing overall strategic direction and backup technical support. Members of the POG have been involved with the development of generators, including the generator approved by the NAIC. Updates to the generator published before November 2010 are only available on the Academy website. Updates published after November 2010 are available on both the Academy and SOA websites.

In April 2012, the POG updated the AIRG with historical yield curves through December 2011. In addition, the scenario numbers of scenario subsets generated by the internal scenario picking tool assumed a Sept. 30, 2011, start date.

In September 2013, the POG updated the AIRG with historical yield curves through December 2012. In addition, the scenario numbers of scenario subsets generated by the internal scenario picking tool assumed a Sept. 30, 2012, start date. In addition, the descriptions of parameters $\beta_{1}$, $\beta_{3}$, and $\tau_{3}$ on the parameters tab have been clarified. Finally, a change to the scenario generator code was made to prevent an error if the user overrides the default parameters of the generator to introduce a non-zero correlation between shocks to volatility and shocks to interest rate levels. This change in coding had no effect on scenarios generated using the default parameters.

In June 2014, the POG updated the AIRG with historical yield curves through March 2014. In addition, the scenario numbers of scenario subsets generated by the internal scenario picking tool assumed a March 31, 2014, start date. The NAIC Mean Reversion Point (MRP) changes only once per year, in January. This version of the AIRG reflected the updated MRP.

In March 2015, the POG updated the AIRG with historical yield curves through December 2014. The scenario numbers of scenario subsets generated by the internal scenario picking tool assumed a Dec. 31, 2014, start date, and the MRP was updated.

In April 2016, the POG updated the AIRG with historical yield curves through December 2015. The scenario numbers of scenario subsets generated by the internal scenario picking tool assumed a Dec. 31, 2015, start date, and the MRP was updated. In addition, the POG corrected visual basic for applications (VBA) code to match the formula in $\mathrm{P}$ of the tab "Single Scenarios." This moved the application of soft cap, moved from before this calculation, to just before adding the random shock. This change had an effect on scenarios where maximums or minimums were reached. Most scenarios were not affected.

In March 2017, the POG updated the AIRG with historical yield curves through December 2016. The scenario numbers of subsets generated by the internal picking tool assumed a Dec. 31, 2016, start date, and the MRP was updated. In addition, another check was added to the VBA code generator to be sure the intended MRP is always used after the user makes updates to historical data.

In May 2018, the POG updated the AIRG with historical yield curves through December 2017. The subsets generated by the internal picking tool assumed a Dec. 31, 2017, start date, and an updated MRP.

In May 2019, the POG updated the AIRG with historical yield curves through December 2018. The subsets generated by the internal picking tool assumed a Dec. 31, 2018, start date, and an updated MRP.

In May 2020, the POG updated the AIRG with historical yield curves through December 2019. The subsets generated by the internal picking tool assume a Dec. 31, 2019, start date, and an updated MRP.

In May 2021, the POG updated the AIRG with historical yield curves through December 2020. The subsets generated by the internal picking tool assume a Dec. 31, 2020, start date, and an updated MRP.

In May 2022, the POG updated the AIRG with historical yield curves through December 2021. The subsets generated by the internal picking tool assume a Dec. 31, 2021, start date, and an updated MRP.

In May 2023, the POG updated the AIRG with historical yield curves through December 2022. The subsets generated by the internal picking tool assume a Dec. 31, 2022, start date, and an updated MRP.

For VM-20, the actuary must use scenarios developed from the approved AIRG. VM-20 does not specify calibration criteria for the scenarios, but the actuary is responsible for determining and justifying the appropriate number of scenarios.

## 8. What documentation is available on the equity scenario generator?

Information on the Academy's equity scenario generator is on the Academy's website:
www.actuary.org/content/c3-phase-ii-rbc-and-reserves-project.

## 9. Is the NAIC requiring use of the Academy's scenario picking tool?

In certain circumstances.

VM-21 permits the use of scenario reduction techniques but is not requiring the use of any specific techniques or tools for selecting a subset of scenarios to be used in the calculations. A user would typically select a scenario reduction technique, or other modeling efficiency approaches, appropriate for their use. The actuary would need to confirm that any scenario subsets satisfy the criteria for acceptable scenarios.

VM-20 requires the use of the Academy scenario picking tool that is embedded in the Academy economic scenario generator, including limiting the choice of the number of scenarios to the pre-populated choices of $50,200,500$, or 1,000 . At this time, the embedded tool only offers stratification based on the 20-year Treasury rates. The actuary will need to confirm that any scenario subsets satisfy the relevant criteria, which differ slightly from those in VM-21.

In the scenario picking tool, what methods were used to pick the 1,000-scenario subset from the 10,000 -scenario set?

- The significance measure algorithm is described in the following article:

Chueh, Yvonne C.M. "Efficient Stochastic Modeling for Large and Consolidated Insurance Business: Interest Rate Sampling Algorithms,” NAAJ, Vol. 6, No. 3, July 2002, pages 88103. www.tandfonline.com/doi/abs/10.1080/10920277.2002.10596058.

- The algorithm used, called the Significance Method, is described on pages 92-93 of the article. The measure used was:

$$
s=\sqrt{\sum_{t=1}^{T}\left[\prod_{m=0}^{t-1}\left(1+\frac{i_{m}}{2}\right)^{-\frac{2}{12}}\right]^{2}}=\sqrt{\sum_{t=1}^{T}\left[\prod_{m=0}^{t-1}\left(1+\frac{i_{m}}{2}\right)^{-\frac{1}{3}}\right]}
$$

- Where $i_{m}$ is the monthly long rate (i.e., 20-year rate), and the measure is calculated over the entire time period of the scenario.

10. Will the scenario picker integrated into the generator work properly if a user changes the projection start date or other parameters?

The integrated tool will produce the correct stratified scenarios if the start date, projection length, and other parameters are unchanged. In the case of version 7.1.201604, this would be a start date of December 2014 and a projection length of 30 years. In order to stratify correctly for other choices, the user will need to select the desired start date, projection length, and other parameters and generate a full set of 10,000 scenarios before generating a subset.


[^0]:    ${ }^{1}$ For purposes of this FAQ document, the December 2008 interest rate generator along with any subsequent technical modifications developed by the ESWG is referred to as the Academy Interest Rate Generator (AIRG).

