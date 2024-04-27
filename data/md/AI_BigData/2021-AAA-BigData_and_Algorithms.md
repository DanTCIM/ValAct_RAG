## BIG DATA AND ALGORITHMS IN ACTUARIAL MODELING AND CONSUMER IMPACTS

American Academy of Actuaries

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-01.jpg?height=111&width=155&top_left_y=1891&top_left_x=1603)

(C) 2021 American Academy of Actuaries. All rights reserved.

# Big Data and Algorithms in Actuarial Modeling and Consumer Impacts 

## Data Science and Analytics Committee-2021

Dorothy Andrews MAAA, ASA-<br>Chairperson<br>Charles Letourneau MAAA, FCAS<br>Xin Liu MAAA, FSA<br>Seong-min Eom MAAA, FSA-<br>Vice Chairperson<br>Shawna Ackerman MAAA, FCAS<br>Mary Bahna-Nolan MAAA, FSA<br>Jennifer Balester MAAA, FCAS<br>Emily Bartel MAAA, ASA<br>Robert Beuerlein MAAA, FSA<br>Elena Black MAAA, EA, FCA, FSA<br>Elizabeth Brill MAAA, FSA<br>Scott Brown MAAA, ACAS<br>Mary Pat Campbell MAAA, FSA<br>Boon-Yi Cheah MAAA, ASA<br>Aron Chun MAAA, FCIA, FSA<br>Richard Daillak MAAA, FSA<br>Joseph Dorocak MAAA, ASA<br>Ian Duncan MAAA, FCA, FCIA, FIA, FSA<br>Alexander Esche MAAA, ASA<br>Michael Lundquist FSA<br>Sonya Mbatchou MAAA, ASA<br>Paul Meixler MAAA, EA, FCA<br>Robert Miccolis MAAA, FCA, FCAS<br>Roosevelt Mosley MAAA, FCAS<br>Reese Mularz MAAA, ACAS<br>Belinda Nguyen MAAA, ACAS<br>Michael Payan MAAA, ASA<br>Kirsten Pedersen MAAA, FSA<br>Andrew Provines MAAA, FCAS<br>Marianne Purushotham MAAA, FSA<br>Andrea Rome MAAA, FSA<br>Julia Romero MAAA, FSA<br>Sougata Roy MAAA, FSA<br>Frederick Ryan MAAA, FCAS<br>Spencer Sadkin MAAA, FCAS<br>David Sandberg MAAA, FSA<br>Andy Ferris MAAA, FCA, FSA<br>Greg Frankowiak MAAA, FCAS<br>Andreea Savu MAAA, FSA<br>Richard Gibson MAAA, FCAS<br>Paula Schwinn MAAA, FSA<br>Lijia Guo MAAA, ASA<br>Yi Fan He MAAA, FSA<br>Brad Herman MAAA, ACAS<br>William Hines MAAA, FSA<br>Liaw Huang MAAA, EA, FCA, FSA<br>Bobby Jaegers MAAA, ACAS<br>Dzianis Kapylou MAAA, FSA<br>Laurel Kastrup MAAA, FSA<br>Gareth Kennedy MAAA, ACAS<br>Martin Snow MAAA, FSA<br>Daniel Stevens MAAA, FSA<br>Michelle Sun MAAA, FSA<br>Leslie Vernon MAAA, FCAS<br>Miles Williams MAAA, FSA<br>Matthew Wolf MAAA, FSA<br>Scott Wright MAAA, FSA<br>Eric Xu MAAA, FCAS<br>Jingjing Xu MAAA, FCIA, FSA<br>Rostislav Zilber MAAA, FSA The committee would like to specifically acknowledge the contributions of the core drafting group of this issue paper: Dorothy Andrews Mary Bahna-Nolan Seong-min Eom Brad Herman Liaw Huang Julia Romero Dave Sandberg Ross Zilber<br>Mengting Kim MAAA, FSA

## Purpose of the Issue Paper

It has been nearly three years since the publication of the American Academy of Actuaries' Big Data Task Force monograph, Big Data and the Role of the Actuary, and even in that short time the use of big data and algorithms in insurance has evolved significantly.

The monograph used the definition of big data as, "the collection of extremely large data sets that may be analyzed using advanced computational methods to reveal trends, patterns, and associations," and discussed big data in terms of the 5 V's: Volume, Velocity, Variety, Veracity, and Value. Some sources cite as many as 42 V's of big data, ${ }^{1}$ - among them is virality, denoting the speed with which big data can spread around the world. The monograph provides a solid foundation for discussing the use of big data and algorithms in insurance. It explored early uses of big data and algorithms in all practice areas and the regulatory framework governing their applications. The knowledge gap of advanced statistical modeling techniques between insurers and regulators has been closing over that period, aiding regulators to better investigate and articulate concerns with big data applications. In addition, in the last few years, the Actuarial Standards Board (ASB) has finalized actuarial standards of practice (ASOPs) on the use of data and the building and validation of models. Data scientists have gained prominence working in the insurance sector building models previously thought to be under the sole purview of actuaries because of their deep machine learning (ML) skills. As will be discussed in this paper, the advent of data scientists in this space has not taken place without circumspection by regulators to evaluate their ability to navigate the landscape of insurance regulations.

The purpose of this paper is to provide:

1. A framing for understanding how developments in big data and artificial intelligence (AI) may impact insurance offerings and their oversight;
2. Education for actuaries, regulators, legislators, and other interested stakeholders on the evolving impacts of big data and AI technologies on the oversight, accessibility, and sustainability of insurance since the publication of the Big Data and the Role of the Actuary monograph; and
3. Education for a framework on algorithmic accountability and specific considerations across different lines of insurance.

## Introduction

Big data and artificial intelligence (AI) are having a tremendous impact on the business model of insurance with respect to the design, marketing, regulation, and servicing of insurance products. Some impacts are relatively minor and incremental in nature, while other impacts are transformational with major implications. Insurance serves many societal functions; however, it may not be able to address all socially desirable outcomes and remain both sustainable and accessible. The following framework and key concepts lay the foundation for understanding the limits of insurance systems to be both sustainable and accessible. A 2019 report by the U.S. Government Accountability Office (GAO), ${ }^{2}$ which is discussed in more detail in a later section of this paper, highlights the role actuaries need to play to facilitate a positive transformation of the insurance industry. Those observations are consistent with the insights in this paper. Insurance promotes commerce, economic growth, investment in innovations, and social well-being. It is in the best interest of insurers and regulators to work together to ensure a healthy and viable marketplace. This includes sufficient comprehension of the need to construct and deploy insurance models to enable sound decision making and help legislators and regulators determine appropriate public policy.

## Traditional Framework of Insurance

The framework for traditional insurance is based on the need to manage the volatility of risk. Insurance covers varying exposures to loss which necessarily follow risk-based pricing. This can create differences at an individual and a group level. Premium and product structures have traditionally had to account for the following costs before they can generate a profit for shareholders who provide the capital for insurance:

- Mean Cost of Risk-The amount of expected claims.
- Cost of Volatility of Expected Claims-An additional cost for an insurance provider to have the necessary funds on hand for fluctuations from expected claims in order to assure both supervisors and shareholders that the company will survive adverse developments through holding additional capital. This is in addition to the expected claim amounts. Since these funds are typically "borrowed" in order to sell a policy, they represent the additional costs needed to pay back those who contributed the capital needed to back the product.
- Cost of Uncertainty About the Mean and the Volatility-When this cost is hard to quantify or estimates are subject to significant uncertainty, it is often addressed through product designs via limits on coverage, the use of dividends or nonguaranteed elements, or the use of premiums that reset each year.
- Costs to Market, Sell, Build and Service Product, Fund Payments (Including Investment Risk) and Monitor Emerging Risk Expenses and Disclose Performance of OperationsThese costs are added to the average expected claims when setting the premiums for the coverage and may also be included in additional required capital.

FIGURE 1: DRIVERS OF VALUE FOR INSURANCE PRODUCTS

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-07.jpg?height=813&width=1393&top_left_y=949&top_left_x=491)

Reducing the cost of any of these four major elements drives the "value chain" of insurance. ${ }^{3}$ The relative importance of each of these elements differs by product across life, health, and property and casualty (P\&C) coverages. Moreover, the relative importance of the four elements drives specific product design and regulatory oversight. The impact of specific AI and big data applications and innovations can be better understood by seeing which elements they might impact in the value chain of insurance. If any of these costs are not reflected in the premiums or product design, then the insurer will not be sustainable in the long run. In the U.S., insurance regulators (typically through state statute) ensure that insurance is accessible, sustainable, and meets reasonable policyholder expectations. This introduction provides a road map for discerning how and whether AI and big data will impact the insurance market.

## Key Concepts

1. The business model of insurance encompasses certain services to be provided. It is helpful to assess which element of the value chain is being targeted by the use of big data and AI. Below is a listing of some of their most common areas of application:

- Distribution-Does AI or big data help identify the people and/or methods most able to effectively represent and carry out the insurer's marketing efforts?
- Customer Satisfaction-Do big data and AI provide a more satisfying customer experience, either at the time of the sale or throughout the servicing of the policy or both?
- Selling-Do big data and AI streamline the sales process or help the distribution channel(s) identify and sell to customers who would benefit from the insurance product(s)?
- Maintenance and Servicing (Claims, Underwriting, Reserving)-Do big data and AI allow the insurer to provide these needed services in a more efficient manner?
- Fraud detection-Do big data and AI ensure better identification of insurance fraud?
- Risk Management by the Customer-Do big data and AI allow or incentivize behavior or actions by the insured to reduce the level and volatility of their risk exposure (such as through wellness programs)?
- Price Prediction-Because setting the price is a "prediction" exercise based on data, can the use of big data and AI provide better estimates of the mean and volatility of the riskand thus allow for lower or less volatile premiums?
- Regulatory Oversight-Do big data and AI allow the supervision of insurance to be more effective and efficient?

In addition, each of the above items will be of more or less importance based on the specific line of business under consideration.

FIGURE 2: $\quad$ COMMON AREAS OF FOCUS FOR DIVERSE STAKEHOLDERS \& PRODUCT LINES

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-09.jpg?height=838&width=835&top_left_y=611&top_left_x=778)

2. Understanding Risk versus Uncertainty-Frank Knight, a 20th century economist, is recognized as the first person to draw a distinction between risk and uncertainty. ${ }^{4}$ Risk applies to situations where one does not know the outcomes of a given situation but can measure the probability of each outcome, i.e., measurable uncertainty. Uncertainty applies to situations where one does not know the outcomes of a given situation and cannot measure the probability of each outcome, i.e., unmeasurable uncertainty. All insurance lies on a spectrum bounded by measurable risk and complete uncertainty. Depending where on the spectrum a specific kind of insurance risk lies, the tools used to price and structure the insurance offering will shift and differ. For instance, life insurance offers longer term premium guarantees to accommodate long-duration risks. Auto insurance rates are more predictably steady as the risk is measurable and typically a shorter-duration kind of event. In contrast, consider an example with some catastrophic coverages where due to the lack of experience and data this may be a situation more in line with uncertainty.
3. Efficiency vs. Transformation-Does a big data analytic solution focus more on cost savings or speed? Or does it transform the way a service is provided-whether it be a transformation of the sales, underwriting, pricing or administration policies and procedures (as occurred with Uber \& Lyft for taxi services)?

## 4. Better Prediction vs. Better Judgment

- Does big data replace people or become a tool to enhance their judgment, creativity, and behaviors? According to some, AI tools can produce more consistent decisions than people. $^{5}$
- Machine learning may approximate functions and analysis performed by an actuary, underwriter, or claims manager, or it may learn on its own. What is the end result of these processes? Does it replace individuals or augment and accelerate their capabilities?

5. Evaluating the Data Asset-There is a vast difference in the quality of data that can be applied. Risk managers routinely assess the quality of traditional assets like bonds, real estate, etc. Critical considerations in the applications of AI are a uniform understanding of the quality of the existing data assets, their requirements for sufficient data remediation and enrichment, and any needed investments to improve data quality.
6. Regulation and Oversight-What is an appropriate role for regulation to foster innovation, access, sustainability and to safeguard consumer privacy and other consumer protections?

Another way to summarize the various differing ways that the service model can be impacted is shown in the following image:

### FIGURE 3: $\quad$ OPPORTUNITIES FOR INNOVATION

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-10.jpg?height=574&width=1342&top_left_y=1838&top_left_x=478)

The role of the actuary continues to evolve along with the tools used to perform actuarial work. There have been many developments in actuarial practice since the days where assumption setting relied solely on data from a company's policy master files. Using big data, we can explore and investigate additional patterns of behavior that can drive the risk being insured and the manner of its delivery and servicing.

The Academy's Big Data and the Role of the Actuary monograph provided a detailed examination of how big data and insurance technology (insurtech) have changed the landscape of insurance and some of their implications for the role of the actuary and the regulation and supervision of insurance. This paper updates the evolution of the technology and emerging issues since the publication of that monograph.

The remaining sections of this paper include:

Terms and Their Usage in the Issue Paper 11

Guiding Actuarial Standards, Practices, and Other Considerations 16

$\begin{array}{ll}\text { Ethics and AI } & 19\end{array}$

Actuarial Risk Classification \& Pricing 23

Validation \& Veracity Modeling That Changes the Application Process 26

Power of Big Data and Algorithms to Identify \& Influence Risk Profiles 32

Assessing Sources of Nontraditional Data to Improve Consumer Experience 40

Controlling for Systemic Influences and Socioeconomics 43

Evaluating Nontraditional Data 49

Regulatory Concerns Impacting the Work of the Actuary 52

Transformational Impacts of Big Data and AI on the 54 Future of Insurance and Society

Appendix A: Recommended Reading 65

# Terms and Their Usage in the Issue Paper

This section of the paper will provide definitions to terms to ensure a consistent understanding of the ensuing discussion.

Algorithm-A set of instructions to describe how to implement a process.

Anti-Selection-A phenomenon in insurance where those who have higher risks buy insurance based on asymmetric information that benefits their purchase of the product to the disadvantage of the insurer. This is also referred to as adverse selection. ${ }^{6}$ Anti-selective behavior could also include making premium payments, lapses, fund selections, exercising dividend options, and utilizing other policy benefits based on asymmetric information.

Artificial Intelligence-A program that performs a task that one would normally think of as being calculated or determined by humans. ${ }^{7}$ It is discussed in the context of automation and human augmentation. ${ }^{8}$ It can also be a group of algorithms that can modify and create new algorithms as it processes data. ${ }^{9}$

Accessibility-The timely use of personal health services to achieve the best possible health outcomes. Importantly, this definition relies on both the use of health services and on health outcomes to provide yardsticks for judging whether access has been achieved. The test of equity of access involves determining whether there are systematic differences in use and outcome among groups in society and whether these differences are the result of financial or other barriers to care. ${ }^{10}$

Conditional Statistical Parity (CSP)—CSP is closely related to the idea of fairness through blindness, in which one attempts to create fair algorithms by prohibiting the use of protected attributes, such as race. However, as frequently noted, traditional approaches to achieve fairness find it difficult to restrict to legitimate features that do not at least partially correlate with race and other protected attributes, and so one cannot be completely "blind" to the sensitive information and so do not necessarily reduce racial disparities. Conditional statistical parity mitigates these limitations of the blindness approach. ${ }^{11}$ CSP is discussed in further detail in a later section of this paper.[^0]

Data Veracity-Data veracity refers to, in general, how accurate or truthful a data set may be. In the context of big data, however, it takes on additional meaning. More specifically, when it comes to the accuracy of big data, it is not just the quality of the data itself but how trustworthy the data source, type, and processing of it is. Removing things like bias, abnormalities or inconsistencies, duplication, and volatility are just a few aspects that factor in improving the veracity of big data.

Disparate Impact-The U.S. Department of Housing and Urban Development (HUD) published a final rule regarding the HUD implementation of the Fair Housing Act's disparate impact standard in 2020. The final rule as amended would provide more appropriate guidance on what constitutes unlawful disparate impact to better reflect the U.S. Supreme Court's 2015 ruling in Texas Department of Housing and Community Affairs v. Inclusive Communities Project, Inc. The HUD disparate impact prohibits facially neutral practices that have unintended discriminatory effects on classes of persons protected under the Fair Housing Act. The rule has no impact on determinations of intentional discrimination. In its 2015 decision, the Supreme Court upheld the use of a "disparate impact" theory to establish liability under the Fair Housing Act for business policies and local ordinances even if the policy or ordinance is neutral-in intent and application-if it disproportionately affects a protected class without a legally sufficient justification. ${ }^{12}$

Disparate Treatment-Per the Supreme Court, even benignly motivated policies that appear neutral on their face but are traceable to the nation's long history of invidious race discrimination in employment, education, housing, and many other areas constitute disparate impact. ${ }^{13}$

False Negative Error Rate-The proportion of positives that yield negative test outcomes with the test, i.e., the conditional probability of a negative test result given that the condition being looked for is actually present.

False Positive Error Rate-The proportion of all negatives that still yield positive test outcomes, i.e., the conditional probability of a positive test result given an event that was not present.

Fast Data-Data that is processed in real time and analyzed to make rapid decisions. Streaming data is considered fast data. ${ }^{14}$

Feature Engineering-The process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data. ${ }^{15}$

Ground Truth Data—Data collected through direct observation. It may include images and image labels for object recognition such as the count, location, and relationships of key features. ${ }^{16}$

Group Fairness-A classifier satisfies this definition if the subjects in the protected and unprotected groups have equal probability of being assigned to the positive predicted class. Also referred to as statistical parity, demographic parity, acceptance rate, and benchmarking. ${ }^{17}$ An example of statistical parity of an algorithmic classifier would be an algorithm that equally rates men and woman as qualified for a technical position.

Human-Centered AI-Defined by systems that are continuously improving because of human input while providing an effective experience between humans and robots. It learns from human input and collaboration, focusing on algorithms that exist among a larger, human-based system. ${ }^{18}$

Insurance-As used in this paper, an economic device transferring risk from an individual (or groups of individuals) to a company (or government body) to reduce the uncertainty of risk via pooling. Thus, in a more general sense, risk in general is transferred to another entity that can be a private commercial company or a state-run program.

Insurtechs-Insurance technology (insurtech) companies are regarded here as companies that develop technology-enabled innovations used by the insurance industry to increase sales, offer simpler products or a streamlined customer experience, or enhance the pricing and management of insurance risk through big data and/or AI applications.

Lift Curve-A graphical visualization of the performance gains that result from a classification model. Lift curves are discussed in further in a later section of this paper.

Machine Learning-An evolving branch of computational algorithms that are designed to emulate human intelligence by learning from the surrounding environment. They are considered the workhorse in the new era of big data. ${ }^{19}$

Negative Predictive Value (or Accuracy)-The proportion of negative results in statistical and diagnostic tests that are true negative results.

NTSB-The National Transportation and Safety Board is an independent U.S. government investigative agency responsible for civil transportation accident investigation.

Noisy Data-Noise (in the data science space) is unwanted data items, features, or records that don't help in explaining the feature itself, or the relationship between feature and target. Noise often causes algorithms to miss patterns in the data. ${ }^{20}$

NOAA-The National Oceanic and Atmospheric Administration is a scientific agency within the United States Department of Commerce that focuses on the conditions of the oceans, major waterways, and the atmosphere.

Pipeline Problem-A term used to reference the absence of diverse candidates in the hiring pool, and often used to justify the inability of large firms to achieve diversity due to scarcity. ${ }^{21}$

Positive Predictive Value (or Accuracy)-The proportion of positive results in statistical and diagnostic tests that are true positive results.

Price Optimization-The process of maximizing or minimizing a business metric using sophisticated tools and models to quantify business considerations. Examples of business metrics include marketing goals, profitability, and policyholder retention. ${ }^{22}$

Rules-Based Decision Making (Machine Learning)-A type of classifier which makes the class decision depending on using various "if ... else" rules. These rules are easily interpretable and thus these classifiers are generally used to generate descriptive models. The condition used with "if" is called the antecedent and the predicted class of each rule is called the consequent. ${ }^{23}$

Sensitivity-The ability of a test to correctly identify those with a condition.

Social Determinants of Health-The attributes associated with where people are born, grow, live, work, and their age, which then shape their health. They include attributes like socioeconomic status, education, neighborhood and physical environment, employment, and social support networks, as well as access to health care.

# Specificity-The ability of a test to correctly identify those without a condition.

Structured Data-Data that conforms to a tabular format with relationships between the rows, columns, and tables. It is easy to access with programming code because of this organization. Relational databases and flat files are common examples of structured data.

Supervised Learning-Learning done using a ground truth, i.e., prior knowledge of what the output values are, and then building a model to reproduce those output values to give the best approximation of the relationship between input and output values observable in the data. ${ }^{24}$

Sustainability in Health Care-The integration of a healthy ecological system, viable economy, and social equity such that unfair or disproportionate impacts on contributory elements of the health care system are minimized. ${ }^{25}$

Systemic Societal Issues-A focus on the outcomes of public policies that have a disparate impact on marginalized groups that prevent access and opportunity to better jobs, neighborhoods, education and financial security or which preclude access to health care.

Test Data-A data set that is used to test the veracity of the model. It is not used to train the model.

Training Data-A data set that is used to build a model and coerce its parameter estimates.

Type I Error-The error of rejecting a true hypothesis associated with the alpha ( $\alpha$ ) level of statistical significance.

Type II Error-The error of accepting a false hypothesis associated with the beta ( $\beta$ ) probability of this error. It is related to the power of the test $(1-\beta)$.

Unstructured Data-Data that lacks the row, column, and table structure of structured data. It is most often stored as text and requires specialized text processing software to extract information and meaning from it.

Unsupervised Learning-Learning that is not supervised to reproduce known values (or labels). Unsupervised learning can infer the natural structure or patterns present within a dataset. For example, a cluster analysis finds groups in data such that within group differences are small but between groups differences are great.

# Guiding Actuarial Standards, Practices, and Other Considerations

To ensure that professions meet their obligations to the public, some are regulated and licensed by government entities. Alternatively, governments may rely on a profession to regulate itself because of its specialized knowledge and understanding of standard practices, provided that the self-regulation assures competent and ethical services. The actuarial profession is a self-regulated profession that generally sets its own rules for admission, education, standards of practice, and disciplinary processes to best serve the needs of the public.

Applicability guidelines ${ }^{26}$ provide actuaries with a nonauthoritative reference to standards that usually apply to various actuarial assignments, but do not apply to actuaries in their roles as general managers, investment advisers, etc. The guidelines are published by the Council on Professionalism of the American Academy of Actuaries.

Consider how the U.S. actuarial profession meets some general characteristics of a profession and the steps the U.S. actuarial profession takes to regulate its members:

- Specialized Knowledge-Actuaries must complete a rigorous and specialized course of study. Actuaries gain actuarial experience primarily working for insurance companies and consulting firms, although increasing numbers are working in banking, government, financial institutions, information technology companies and insurtechs, innovating technology for the insurance industry. Actuaries are required to meet certain continuing education (CE) requirements annually to ensure that their training is up to date.
- Responsibility to the Public-The profession recognizes that the work of actuaries affects the financial well-being of individuals and companies, and that the public depends on this work. Actuaries fulfill their responsibility to the public by adhering to the high standards of conduct, practice, and qualifications of the actuarial profession.
- Accepted Practice-Actuarial standards of practice (ASOPs) define appropriate actuarial practice and serve as guidance for the competent and ethical work of actuaries. The Actuarial Standards Board (ASB) continually reviews existing ASOPs to ensure standards continue to be relevant and create new ASOPs if necessary, in response to emerging issues and the evolution of actuarial practice. The ASOPs are principlebased, rather than narrowly prescriptive, meaning that the standards leave room for professional judgment. Practice notes are intended to provide information to actuaries on current or emerging practices in which their peers are engaged. They are not interpretations of actuarial standards of practice, nor are they meant to be a codification of generally accepted actuarial practice.
- Code of Conduct-The Code of Professional Conduct, developed under the auspices of the American Academy of Actuaries, has been independently and uniformly adopted by each of the five U.S.-based actuarial organizations. Members of any of these organizations are required to comply with the Code of Professional Conduct.
- Discipline Process-The discipline process for the U.S. actuarial profession begins with the Actuarial Board for Counseling and Discipline (ABCD). The ABCD receives and reviews complaints against actuaries, investigates complaints that indicate the possibility of a material violation of the Code of Professional Conduct, and recommends discipline, when indicated, to any of the five national U.S. actuarial membership organizations, ranging from admonishing members of the profession for unacceptable behavior or practice to expelling them from the profession. Each organization then makes an independent decision on discipline for each specific case.

Requests for Guidance-The $\mathrm{ABCD}$ also serves the profession as a resource by responding to requests for guidance (RFGs) from individual actuaries. Through this process, an actuary may confidentially discuss with a member of the $\mathrm{ABCD}$ a situation in which the actuary is uncertain of the appropriate action. The guidance provided may reduce the likelihood of the actuary taking actions that might violate the Code of Professional Conduct. In recent years, the $\mathrm{ABCD}$ has responded to over 100 RFGs annually. Actuaries may also receive counseling after a complaint has been made against them. In these cases, a member of the $\mathrm{ABCD}$ will discuss with the subject actuary potential improvements to the subject actuary's processes that will make it less likely for the subject actuary to be in violation of the Code of Professional Conduct. Counseling may occur even when the ABCD recommends discipline.

- Membership-Actuaries are considered part of the U.S. actuarial profession if they belong to one of the five U.S.-based actuarial organizations. Members of these organizations must meet the qualification standards and comply with the requirements established by the Code of Professional Conduct.

There are myriad regulations which govern insurance and retirement systems and the work of actuaries in particular in the U.S. It has often been the case that statutes and rules with the added rigor of actuarial standards has enhanced the sustainability of insurance and retirement systems through the application of the expertise of the U.S. actuarial profession. Even in areas where there may not be a specific regulation, the standards and Code of Professional Conduct still apply.

The following lists of ASOPs may be applicable to actuaries working with big data and AI algorithms:

- ASOP No. 1, Introductory Actuarial Standard of Practice
- ASOP No. 2, Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts. Applicable if AI or other data used in determination of nonguaranteed elements.
- ASOP No. 7, Analysis of Life, Health, or Property/Casualty Insurer Cash Flows. Applicable in cases where actuarial assumptions are influenced by advanced analytics techniques.
- ASOP No. 12, Risk Classification (for All Practice Areas). Applies to selection of risk classes resulting in equitable and fair rates.
- ASOP No. 15, Dividends for Individual Participating Life Insurance, Annuities, and Disability Insurance. Applies when advanced analytics techniques are used in setting assumptions or dividend determinations.
- ASOP No. 23, Data Quality. Provides guidance when selecting data, performing a review of data, using data, or relying on data supplied by others in performing actuarial services.
- ASOP No. 41, Actuarial Communications. Critical standard applied to the actuary's communication within any practice area.
- ASOP No. 54, Pricing of Life Insurance and Annuity Products. Applies to actuaries performing actuarial services with respect to pricing, that is, setting rates, charges, and benefits.
- ASOP No. 56, Modeling. Provides guidance when performing actuarial services with respect to designing, developing, selecting, modifying, using, reviewing, or evaluating models.


# Ethics and AI

The need for model builders to be ethical in the design and use of big data and algorithms deployed in the heavily regulated field of insurance

Insurance carriers are increasingly using AI across various functions and aspects of the business including research, marketing, risk classification, pricing, in-force management, and claims adjudication to estimate sales, risk premium, claim frequency and severity. AI models are complex, often "black box" in design, where results may be difficult to explain or interpret. Although consumers may have an implicit expectation that insurers use AI ethically, as is true for many current applications of AI, there is not strong consensus around sound ethical AI principles, universal definitions, or ethical standards by which to judge algorithms or their usage.

As the insurance industry becomes more reliant on AI and big data to replace or supplement human decision processes, in evaluating the risk of unintended bias and discriminatory impacts to protected and marginalized groups, it may be necessary to consider:

1. The quantity and quality of underlying modeling data as a core reason for unintended consequences. The data may be unrepresentative, unbalanced, non-credible, and poorly constructed to address the modeling question.
2. The selection of the appropriate machine learning algorithm and ensuring the data satisfies the underlying statistical assumptions of the algorithm.
3. The model risk posed by the technique and the continued fit of the model. Even a good model degrades over time and failure to properly monitor the continued fit of a model can result in its inapplicability and its potential harm to insureds. ${ }^{27}$
4. How well the model validates to address the question (e.g., how well it identifies fraud, or how well does it identify differences in expected claim cost).

The following are additional key areas of consideration for the use of big data and AI algorithms in insurance decision-making to guard against unintended bias and disparate impacts:

- Data Quality-It is important that data sources are:
- Objective in its collection. It is critical to ask questions regarding why specific data was collected and for what purpose.
- Applicable to the modeling question and is current. It important to examine whether the design and construction of the data set fits the intended purpose of the model.

27 "Model Risk"; Goldman Sachs Quantitative Strategies Research Notes; 1996.

- Reconciled to auditable sources and expert judgment.
- Tested for credibility, representativeness, balance, and accuracy to mitigate bias in the results.

Regulators may be particularly interested in audits of data proxies for regulatory disallowed variables.

- Data Transparency and Privacy-Data is often modified from its original source through feature engineering, which can make it unrecognizable and difficult to validate by consumers. While feature engineering is a standard process with a long history of use in analytics outside of insurance, it can obscure the role of traditional insurance data elements by transforming them into variables that are difficult to understand. The transformed variables can be problematic as insureds may not understand how to recognize when their values are erroneous and know when to request an insurer to correct them. Insurers may be challenged to provide transparency into the determinants of a rate if the model input data has been transformed and feature engineered, so that the data no longer resembles its preprocessed version. Using third-party data in actuarial models presents challenges to consumers as well, as consumers may have to engage those parties to have any errors in their data corrected. As more data is provided by third parties, there is also an increased potential of exchanging personal data among the customer, third-party vendors and the insurance carrier. Controls need to be in place to ensure data privacy is preserved.
- Model Purpose and Limitations-A model should clearly identify its purpose, appropriate usage, and limitations. This includes the relevancy of the model inputs, the applicable cohorts to which it applies, the conditions under which it applies, and metrics signaling when it is no longer applicable. Models need appropriate human oversight to monitor when calibrations are needed to correct for model "drift" that compromises model fit.
- Responsible Research-It is important that research supporting the development of $\mathrm{AI}$ is based on credible scientific principles and practices and clearly references the modeling question. It should be well documented with tractable findings that have been tested for unintended consequences and biases and rigorously reviewed by qualified peers.
- Correlation, Causation, and Consistency-Care should be taken to understand and communicate the model decisioning path and distinguish whether the patterns detected by models are causal versus associative in nature. Correlations must be assessed for the strength and quality of their associations. Spurious correlations can be statistically significant but are of poor quality and irrelevant in explaining patterns identified by models. Correlations should be evaluated for their potential to explain and quantify causal relationships which are further validated by research, experience, and observable behaviors. The "gold standard" for assessing causation, the randomized control trial (RCT), is often used in evidence-based medical research to prove a certain treatment is a cure for a disease. ${ }^{28}$ Most actuarial models do not meet this standard, as RCTs are experiments run over long periods with many study subjects. Rather, predictive models look for patterns of association or correlation in models but cannot be relied upon to assess causation. Correlations can be informative but can also have adverse impact on model parameters depending on the statistical technique being deployed. For example, under a linear modeling framework, model parameters can become unstable in the presence of correlated variables. Special consideration must be afforded in cases where variables within the training dataset are highly correlated. Failing to address these correlations can result in model results that are uninterpretable, biased, and unreliable. On the other hand, Principal Component Analysis ${ }^{29}$ leverages correlations to reduce the dimensionality of a dataset to a set of uncorrelated principal components that can be modeled as variables in a linear model, alleviating concerns correlated variables pose for parameter estimates.
- Proxies for Disallowed Variables-Proxy variables are concerning when they mimic disallowed variables, because of their adverse impacts to protected classes. It is also important to recognize that a disallowed variable under one state's regulatory regime may be allowed under another. Regulatory differences are a prime reason a company's model in one state might differ in form in another state. Proxies in a model are not necessarily utilized with ill intent, however. Proxy variables that do pose risks of adverse impacts may be useful modeling variables for attributes that are not readily accessible through internal company sources or third-party sources. For example, body mass index (BMI) might serve as a proxy for the health status of an individual; education might serve as a proxy for income and aptitude; and per capita GDP might be a proxy for standard of living.
- Interpretability and Explainability-While there are many definitions, it is generally agreed that interpretability refers to a level of transparency where users of all experience levels can understand a model, while explainability holds the modeler responsible for decloaking "black box" models to explain how they behave to users. ${ }^{30}$ Interpretability can be accomplished with just the human mind without the use of external support, other than model parameters and summary output. ${ }^{31}$ An interpretable model explains itself, while an "explainable" model does not. It requires an explanation with support material because it is too complicated to explain itself. For example, decision trees and simple linear regression models are considered interpretable because they can be visualized using diagrams. Decision trees have a tree structure with branching based on rules which trace input data to its eventual terminal node. Simple linear regression model solutions can be easily visualized in two-dimensional space using a slope and intercept term. A neural network model which attempts to mirror the structure and function of neural pathways in the brain would be considered an "explainable" model. Like the human brain, these models are complicated, and the hidden layers of mathematical functions are not easily perceptible, requiring external techniques to decompose a solution into its predictive elements.

Both interpretability and explainability are essential to allow consumers the ability to challenge outcomes of algorithms. Models should have effective challenge procedures and documented audits of fit for purpose, dependencies, data quality, decisioning, and the controls and governance of outputs and decisions.

- Diversity in Model Development and Review-Those working with models find that to protect against unintended biases and model drift over time, it is good practice to have a diverse set of reviewers (e.g., by gender, ethnicity, race, age, technical training, and experience) of the various AI inputs, decisioning, and outputs relevant to the targeted purpose, as part of a well-defined monitoring plan. This provides greater perspective regarding potential biases and unintended consequences.


# Actuarial Risk Classification \& Pricing

## Background

The key concepts regarding insurance and insurance underwriting and pricing are moral hazard, the pooling of risks, the law of large numbers and the degree of risk vs. uncertainty of the risk coverage. Insurance providers rely on these fundamental concepts to determine an actuarially justified design and pricing of a product. Carriers apply underwriting guidelines to risk characteristics to determine the insurability of an individual or business relative to the type of insurance being offered.

Insurance pricing varies by type of insurance. Some insurance is annually renewable, whereby the premiums can be reset by the insurance carrier each year based on various factors such as changes in expectations of future performance or profitability. Some forms of annually renewable insurance require underwriting or eligibility qualification each year (e.g., personal auto). Other forms, such as with term life insurance, only underwrite a policy at issuance but may have pricing elements which can be reset each year. There are unique considerations related to each line of insurance.

Other types of insurance have prices that are locked in at issue for a long period of time and in many cases guaranteed for periods of 5 or 10 years, or for a lifetime to age 120. For these types of products, the underwriting performed prior to policy issue and the risk classification set at the time of initial underwriting is often more extensive than for policies where the premiums and insurability standards are reestablished on a more frequent basis.

For insurance coverages where eligibility and insurability are established at issue only, any future changes to the premiums or charges required or other nonguaranteed charges within a policy that could impact future policy cost and performance, may not be applied at an individual level based on that individual's prior poor experience. Changes must be forward-looking (not recouping past losses) based on future expectations as well as applied consistently to an entire risk cohort of similarly situated policies.

The underwriting process applies rules and algorithms (whether rule-based with human judgment or more automated, model-based) to project or estimate the level of risk of an individual or business and then assigns it to a risk pool or risk classification. Actuaries are involved in assigning the appropriate risk charge for each classification offered by the insurance carrier whereas the underwriter, who may or may not be an actuary, assigns the risk classification based on risk factors. The premium charged to the insured is a function
of the risk charge as well as other expense recovery, reserve and capital requirements, and profit expectations. The longer the risks are eligible for coverage without a risk-rated review and adjustment, the greater the margin for uncertainty included in the price. Long-duration contracts subject to guarantees over an extended time frame are especially affected by greater uncertainty margins.

Some states require insurance companies to file their policy rates and/or nonguaranteed elements prior to their use, while others do not. Most states require filing of the insurance policy application questions but do not require submission and approval of the underwriting algorithms and rules for some types of insurance products. This practice is coming under greater scrutiny by state and federal regulators to assess whether any algorithms used in the eligibility determination, risk selection, and risk classification process have unintentionally introduced bias toward protected classes, regardless of the type of insurance.

## Al Implications on Traditional Risk Classification \& Pricing

As the use of AI becomes more prevalent in insurance underwriting and pricing, the use of more timely data to replace slower data continues to evolve. It is important for model developers and users to understand the biases inherent in high-velocity data and its impacts on risk classification. Even models based on internal experience data may have inherent biases based on how the data was initially collected (e.g., with human judgment) and to which pool or cohort the data applies. Data that fits the purpose for one cohort or risk characteristic and profile may not fit the purpose for another. While this is not a new challenge for actuaries and insurance underwriting and algorithm development, it is heightened with the acceleration of automated decisioning algorithms and high-speed, nontraditional data sources.

While AI models can finely segment risks, resulting in granular risk classifications thereby reducing dispersion around mean losses for pricing cohorts, highly granular models suffer from weaknesses as well. They may result in risk classifications that differ from more traditional models for identical cohorts, with some individuals or businesses paying higher costs than others. Misclassification risk can be easily visualized using a simple confusion matrix which is an $\mathrm{N} \mathrm{x} \mathrm{N}$ matrix that classifies prediction error. Diagonal elements represent model predictions that exactly replicate observed values and off-diagonal elements represent prediction errors. The smaller the prediction errors, the greater the confidence in the model to predict actual outcomes, while the greater the misclassification, the greater the costs associated with risk charges, premiums and expected claims. Figure 4 illustrates these concepts for a $4 \mathrm{x} 4$ confusion matrix.

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-27.jpg?height=708&width=1116&top_left_y=459&top_left_x=583)

The use of AI in underwriting algorithms and pricing is transforming the business of insurance from initial risk selection, risk pool assignment, and claim management to claim fraud prevention. These advanced tools and analytics are improving the identification of significant drivers of claims and the extricating of volatility from trend to enable fine-tuning in the rate setting. It is expected that insurance will develop advanced AI applications to improve customer engagement and interactions and improve bottom-line company performance. Given the velocity of big data and sophisticated machine learning algorithms, continuous underwriting is emerging as a viable technology, allowing for a more dynamic and responsive relationship between risk selection and pricing.

# Validation \& Veracity Modeling That Changes the Application Process

The insurance application is often the most relevant and important source of data about the insured in the insurance underwriting and risk classification process. ${ }^{32}$ Innovations in technology are now allowing insurers to better process insurance policy applications online and evaluate them for accuracy before the policy is issued. However, application data can be subject to manipulation, fraud, or misrepresentation that could be uncovered by AI tools and third-party data for verification. There are several ways AI is being deployed to test the accuracy of traditional data supplied by the insurance application, such as:

- AI technology can verify applicant identities and properties for insurance and detect fraudulent claim activity using natural language processing ${ }^{33}$ and sentiment analysis ${ }^{34}$ within minutes of claim submission.
- Pattern detection can identify inconsistencies between answers as well as inconsistencies with instantly available third-party data in real time.
- Reflexive questions to gather additional information to evaluate inaccuracies can be identified and additional data needed for a prediction can be determined in moments rather than days.

This development and advancement of technology has enabled insurance companies to capture and utilize broader types of big data from different sources. This includes internal company data, such as adjuster notes, and new external sources from third-party data brokers. While structured insurance data is easier to process with most programming languages, it accounts for a relatively smaller percentage of all available data, most of which is unstructured. Both types of data can be noisy, containing less meaningful data than desired and both must be cleansed and analyzed to reveal predictive signals for a desired purpose. It is noteworthy that:
- Nontraditional data sources tend to be noisier than traditional data sources as they were not designed to answer insurance questions but may contain unexpected and unanticipated behavioral information. Noise and uncertainty in data can be reduced by collecting and assessing data from a variety of data sources, i.e., a consensus approach. The process of interrogating data from different sources can also reveal interconnections that may strengthen the quality of the modeling data, increase its trustworthiness for the purpose of the model, and identify how to integrate it with internal company data[^1]sources, increasing the predictive power of the model data and the machine learning algorithm.
- Validating unstructured data for accuracy can be more difficult than assessing structured data for accuracy because unstructured data requires more consensus for it to be deemed credible and it is often not subject to controls that are easy to audit. ${ }^{35}$ For example, two claims adjusters might view and document the same claim using the unstructured adjuster notes field with varying levels of details, which could lead an algorithm to reach contradictory assessments of fraud with respect to the claim. If insurance companies do not have established guidelines for how claims adjusters use the notes sections of the claims system, adjuster notes may be difficult to mine for nuggets of information. Claims adjusters generally have discretion over how they document this field during their claim reviews.

Both structured and unstructured data are subject to errors and missing data. The company should consider reviewing the quality of the data source and interrogate the data for inaccuracies, missing data, completeness, bias, internal consistency, and controls against which it can be validated. Financial controls are basic validation measures against which model data can be assessed. For example, a financial control for premiums can validate the insurance premiums represented in a model by fiscal year. Companies may want to investigate sampling techniques if the distribution of premiums in the modeling data is sharply dissimilar to company level financial results by year. ASOP No. 23 may provide guidance to actuaries for such a review. Another emerging issue with data sources is its lack of independent validation. There are no regulatory agencies that regulate, validate, and certify nontraditional data sources, raising questions such as:

1. How much can the company or the model owner trust the source of the data?
2. Is the data source appropriate for the risk classification and pricing exercise?
3. Is all the data relevant, compatible, and current for the rating and pricing exercise?
4. Are there any external events that would have an undue influence on the outcome variable?
5. Whose responsibility is it to validate external data used in risk classification and pricing?
6. Is it sufficient to rely on vendor certifications that external data meets a high-quality standard?
7. How do consumers gain access to their data to inspect and correct erroneous data from external sources?
8. Should insurance companies provide insureds with the rating data used to determine their insurance rates?

35 "Unstructured Data: an overview of the data of Big Data." International Journal of Computer Trends and Technology; 2016.

Understanding the lineage and provenance of the data becomes a critical activity for the company and model owner. Before adopting a new data set, the company and model owner should demonstrate, at a minimum, that

1. the data source can be trusted,
2. the data is appropriate to the model and its underlying assumptions,
3. noise and uncertainty in the data have been statistically resolved without overfitting, and
4. the data has a reasonable relationship to the outcome variable being modeled.

Additionally, regulators may be interested in distinguishing relationships between input variables and outcomes as either causal or associative, and having overall results examined for soundness from a diversity of perspectives and expertise.

One area of challenge is that the company may not have access to or can adequately explain the data processes and algorithms used by third parties to create data. This is a challenge that must be overcome if company risk classification and pricing models are to meet regulator, independent validation, and public expectations. It may not be sufficient to rely on the reputation, references, experience, or expert judgment of third parties in support of the merits of an algorithm developed for insurance purposes. To build confidence with regulators and consumers, insurers may need to validate third-party data sources and algorithms before incorporating them into internal pricing and risk classification models. Guidance is provided in ASOP No. 56.

Regulatory filing reviews are increasingly interrogating filings that contain advanced statistical models for post-implementation model monitoring processes. Models may start to degrade once they are installed in a production environment for a variety of reasons. The chief reasons for machine learning model degradation fall into three broad categories. ${ }^{36}$ They are:

1. Relevancy of Model Data

a. The period of time over which independent variables continue to provide accurate predictions.

i. Consistency of definitions. Data sources may change how data elements are defined and calculated.
ii. Collection methods may also change, affecting variable meaning. The original meaning and construction of a data variable might change affecting its use in a model.

iii. There may be a decay in the relationship between independent and dependent variables for known or unknown reasons.

b. Model drift occurs when the statistical properties of the dependent variable change in unexpected and unforeseen ways, compromising prediction accuracy.

c. Human behavior may change from what the model has been trained to expect, adversely impacting the dependent variable.

d. Modeling data may reflect extreme, one-time events or other natural anomalies in the external environment unrepresentative of the future.

2. Age and Stability of the Model

a. The model may lack sufficient generalization to withstand subtle changes in variables, environment, and human behavior, because of overfitting.

b. Model parameters may be unstable due to training models with highly correlated variables. Some modeling techniques can eliminate or reduce the impact of correlated variables on parameter stability, while others cannot.

3. Model Risks

a. The model may lack sufficient generalization to withstand subtle changes in variables, environment, and human behavior, because of overfitting.

b. Changes in business processes, regulations, product offerings, industry, distribution channel, competitors, and economic indicators. ${ }^{37}$

c. A model may pose risks ${ }^{38}$ because it may:

i. Become inapplicable to the problem

ii. Use faulty assumptions or may be missing needed assumptions

iii. Produce a solution that is badly approximated

iv. Have been produced using faulty software

v. Contain an inherent mistake

vi. Be used inappropriately

37 "When Machine Learning Goes Off the Rails"; Harvard Business Review; January-February 2021.

38 "Model Risk"; op. cit.

It is important to not take a "set it and forget it" approach to models after they are put in production. Models degrade over time for a variety of reasons as previously discussed and they must be monitored with regular frequency for continued fit. A prevalent tool for assessing model fit is the lift curve.

FIGURE 5: $\quad$ MODEL DEGRADATION LIFT CHART

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-32.jpg?height=821&width=1135&top_left_y=706&top_left_x=625)

A lift curve is a graphical visualization of the performance gains that result from a classification model. The lift curve achieved at initial implementation of the model, the top curve, sets the standard against which to measure model degradation. To measure the continued fit of the model, new data is introduced into the model and a new lift curve is constructed and plotted alongside the prior lift curve, as depicted in Figure 5. The cumulative difference between the area under the two curves represents a measure of degradation in fit. ${ }^{39}$ The company needs to incorporate a decision rule to alert when the degradation is outside the tolerance set for the model. Another method to assess model degradation is recreating models on fresh data at a desired frequency and measuring changes in parameter estimates. ${ }^{40}$[^2]

Once the model has degraded beyond its tolerance, the company must decide whether a refresh or rebuild of the model is justified. A model refresh employs the same variables as the old model but uses fresh data to update the model parameters. A model rebuild may introduce completely new variables or use a combination of new and old variables. A model rebuild may have many implications for other dependent company systems and procedures and may not be an optimal choice for company expense reasons. For example, banks rely on loan scorecards, which are based on predictive models, to score loans for risk. If a new scoring variable is discovered, it may not make its way into the scorecard unless the benefit significantly outweighs the cost to retrain loan underwriters and upgrade banking systems to accommodate the new variable. There are similar issues in underwriting insurance policies along with the hurdle of getting underwriters to trust algorithms that are often viewed as threats to their job security. Actuaries often take the role of exponent for the benefits of the algorithm and work with management to build trust in the results of the algorithm among underwriters and other stakeholders throughout the model lifecycle, from initial deployment through model rebuilds and even model depreciation.

# Power of Big Data and Algorithms to Identify \& Influence Risk Profiles

Sherry Turkle of the Massachusetts Institute of Technology (MIT) says, "Technology does not just change what we do, it changes who we are."41 This statement reminds us that we have to be mindful and watchful of the behavioral effects of technology to shape the data we study and the models built upon that data. Technology is increasing connectedness through media and decreasing connectedness through interpersonal contact, with consequences not yet fully understood. A prime example of this is the use of self-quantification devices like the Fitbit, which has driven psychological imperatives to achieve 10,000 steps before bedtime, taking those last few needed laps around the dining room table to do so. An arbitrary benchmark of 10,000 steps-while considered an admirable goal-has become a powerful fitness norm because of such wearable devices. Reportedly this benchmark has its roots more in marketing than in science, with its significance stemming from a Japanese pedometer with a name that means " 10,000 step meter" and the character for 10,000 in Japanese looks like a running man. ${ }^{42}$ While there is a positive health benefit with increased activity, a daily 10,000-step goal illustrates the powerful psychological effects of technologydriven algorithms to change behavior, and with it the potential to generate new data, and the utility of that new data for insurance applications.

The John Hancock Vitality Program has transformed the life insurance experience through innovation. Traditional life insurance policyholder experience had very few touchpoints with insurance companies limited to paying premiums and receiving benefits. Vitality transformed this experience to an on-going continuous interactive relationship, mostly through wearable devices. Policyholders receive financial rewards for physical activity, nutrition, preventive care, smoking sessions, meditation and sleep, diabetes management, and other steps to improve their health. These behaviors improve policyholder health resulting in improved longevity.

Health data is just one type of data more and more insurance companies are collecting. Companies are finding these kinds of behavioral data can reveal traits that are desirable to have in policyholders, such as honesty, resiliency, self-efficacy, positive psychology, and self-regulation. Self-efficacy, for example, refers to one's belief in his or her capacity to execute behaviors necessary to achieve a goal. ${ }^{43}$ People of high self-efficacy are drawn to self-imposed challenges, such as achieving 10,000 steps per day, and need very little external "nudging"44 to complete tasks.

An impetus to use external data sources to link health outcomes to behavioral traits of potential insureds was the Affordable Care Act (ACA), with its requirement that all Americans purchase "qualified" plans of insurance and government subsidies for those with household incomes below $400 \%$ of the Federal Poverty Level. ${ }^{45}$ This policy change presented challenges to the insurance industry because now companies were required by federal law to offer plans of insurance on a "guaranteed issue" basis to individuals for whom there was little or no information on how they would consume health care. There is an ample history of plan performance to reasonably predict future health care costs for midsize and large insurers. Prior to ACA, many who previously went uninsured had little credible claims history that could be used to predict their health care costs. These new entrants to the health market raised many questions regarding how to predict their future medical expenses and raised concerns regarding pricing and underwriting risks.

A study with a health insurer led to insights for understanding the health behaviors of broader populations including those uninsured by identifying data beyond age, location, and tobacco use with predictive power as a proof of concept. ${ }^{46}$ The researchers (data analysts, financial and actuarial experts) hypothesized that consumer data enhances the predictive value of risk cost models and can classify insureds with no known historical claims and utilization data. The data considered for participants who remained in the study for 12 months entails the following:

- Demographic Data (age, gender, race, etc.) $\cdot$ household information (household size, children, length of residence, etc.) - financial stability (net worth, rent/own a home, invest in stocks, etc.) $\cdot$ behavioral (book reader, travel interests, hobbies, community involvement, etc.) - propensity (media channel, vehicle brands, telecommunication trends, etc.) - census
- Featured Engineered Variables

$\cdot$ average number of claims
- average number of claims for different claims types (inpatient, outpatient, professional, and office)
- average costs for different claim types (two months, quarterly, six months) for different age and gender groups at a postal code level[^3]- Potential Variables
- dental claims
- inpatient claims
- outpatient claims
- total amount from ancillary claims
- total amount from inpatient claims
- total amount from office professional claims
- total amount from outpatient professional claims

The target variable was engineered based on total health care costs for the 12-month period coded as a dichotomous variable where 0 indicated a "low-cost" insured (claims less than \$20,000) and 1 a "high-cost" insured (claims greater than $\$ 20,000$ ). The model was a neural network classifier model validated on 100,000 insureds. The full model with all the consumer data was compared to a baseline model based only on age and gender. The performance metrics included sensitivity, specificity, and positive predictive value. The chart below summarizes the results.

FIGURE 6: $\quad$ MODEL PERFORMANCE METRICS
![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-36.jpg?height=496&width=1392&top_left_y=1384&top_left_x=454)

The age \& gender model is the baseline model that serves as the reference model for the performance of the consumer data model. The consumer data model includes age and gender plus the consumer variables discussed above. If the consumer model performs better than the baseline model, then it can be concluded the consumer variables improve the differentiation of risks into "high-cost" versus "low-cost." The performance metrics for the comparison are Sensitivity (the true positive rate), 1-Specificity (the false positive rate), and the Positive Predictive Value (the proportion of positive results in statistical and diagnostic tests that are true positive results). To be considered better than the reference model, the sensitivity of the consumer model will increase over that of the reference model, the false positive rate will decrease, and the positive predictive power will increase. The comparison in Figure 6 reflects this directionality, implying the addition of consumer data improves the segmentation of health care risks.

More recently, an analysis ${ }^{47}$ was done on the potential of data from wearable devices to predict health insurance cost and found it of limited utility. The researchers found wearable devices provide the minimal data necessary for Health Risk Assessments (HRAs) and the step data produced insignificant positive health benefits with increasing steps but significant negative benefits when step levels are decreased.

Health insurers are finding value in data elements related to what you buy and eat, television consumption patterns, race, education level, marital status, net worth, social media posts, online buying habits, clothing size, ZIP code, and bill paying behavior, as predictors of health insurance costs. ${ }^{48}$ While these data are valuable for gaining insights into many aspects of health care, they are not allowed to be used to set health insurance premiums for individuals. Nonetheless, companies like Lexis Nexis, Optum, IBM Watson, and Acxiom warehouse "oceans" of public domain data primed to feed predictive algorithms that can preemptively identify health risks that will require immediate case management to mitigate huge healthcare expenditures if the risks are not addressed. For example, it has been reported Optum has collected medical diagnoses, tests, prescriptions, costs and socioeconomic data of 150 million Americans going back to 1993, and the company says it uses the information to link patients' medical outcomes and costs to details like their level of education, net worth, family structure and race. ${ }^{49}$ Lexis Nexis uses 442 nonmedical personal attributes to predict a person's medical costs, which includes more than 78 billion records from more than 10,000 public and proprietary sources, including people's cellphone numbers, criminal records, bankruptcies, property records, neighborhood safety and more, to predict ER visits, pharmacy costs, motivation to stay healthy, and stress levels. ${ }^{50}$ These millions of data points help paint a picture of insureds for an insurance company that is never likely to meet them in person or interact with directly. The mediation of the insurerinsured relationship through big data and algorithms has replaced interpersonal contact in understanding policyholder behavior.

Social media platforms are providing further avenues for identifying and targeting populations with specific personality and character traits. Facebook, for example, has filed for patents that detect 1) the emotional context of text messages from the speed and pressure at which they are being typed, 2) phone camera "fingerprints" through its metadata and other features (such as, broken pixels and lens scratches) that are embedded in photographs to match photos to social media users, 3) emotions through emotion-reading technology, and 4) scrolling activity to determine content of most interest to users, aided by the phone's[^4]"image capture technology" to determine what part of the screen a user is looking at. ${ }^{51}$ Facebook has also filed patents to 1) understand the romantic status of your relationships and the genders of relationship partners, 2) classify personalities by type, 3) predict major life events using user posts, text messages, and credit card transactions and their transaction locations, 4) listen to your environment, 5) track your routines, and 6) infer your habits. Technology patents of this type are not just limited to Facebook. Amazon, Google, Spotify, and Airbnb—all have filed patents to detect personality traits, and even LinkedIn has filed customer profiling and customer segmentation by lifetime value patents. ${ }^{52}$ In 2016, a health insurer filed a patent application to gather what people share on platforms like Facebook and Twitter to link this material to personal clinical and payment information. ${ }^{53}$ In 2017, patents among insurance companies jumped $40 \%$ with more than half in the area of telematics, artificial technology, and machine learning, with most focused on risk pricing algorithms based on personal characteristics, gleaned from lifestyle data. ${ }^{54}$ Beyond patents for behavioral traits inventions are patents for physiological data. A leading automobile insurer was granted a patent to detect heart rate, blood pressure, and electrocardiogram signals from steering wheel sensors, believing there is a market for this type data among health insurers. ${ }^{55}$ It is notable the patent application referred to the invention as "predictive modeling for future behavior."56 This notion aligns with research at the Massachusetts Institute of Technology (MIT) purporting that machines are better at understanding human behavior than humans are. ${ }^{57}$

Facial recognition software has been touted by some as having the potential to become the new polygraph test, to the extent it is utilized in the application process and claims filing processes for the insurance industry to detect when consumers are being dishonest, ${ }^{58}$ and enhancing security measures. The technology is being used to access patient records, streamline patient registration, detect emotion and pain in patients, identify certain genetic diseases, price insurance premiums ${ }^{59}$ and detect mental disorders, such as depression. The World Health Organization (WHO) predicts that by 2030 depression will be the leading cause of disease, ${ }^{60}$ which is significant because of its impact on overall health. Early detection of depression is important because of its ramifications for acute care, stress to ER systems, and impacts on mortality. ${ }^{61}$ Social media data can be predictive of depression

51 " 4 Creepy Facebook Patents That Are Actually Real"; IPVision Blog.

53 "Health Insurers Are Vacuuming Up Details About You-And It Could Raise Your Rates"; op. cit.

54 "Insurtech patent filing increased 40\% in 2017"; Managing IP; Nov. 6, 2018.

55 "Insurer monitoring your heart rate? Allstate's patent makes it possible"; Chicago Tribune; June 18, 2015.

56 United States Patent Application Publication; March 20, 2014.

57 "An algorithm can predict human behavior better than humans"; Quartz; Oct. 18, 2015.

58 "Facial recognition is the new polygraph test for insurers"; The Sociable; June 13, 2019.

59 "Facial Recognition Is Already Here: These Are The 30+ US Companies Testing The Technology"; CB Insights; June 5, 2019.

60 Depression: A Global Crisis; World Federation for Mental Health; Oct. 10, 2012.

61 "Facebook language predicts depression in medical records"; Proceedings of the National Academy of Sciences of the United States of America; 2018
and researchers contend the platform is a valuable digital solution (office space alternative) for its clinical detection and treatment. However, many of the algorithms used suffer from racial and gender biases. Software engineers find it difficult to detect these biases until an independent analysis finds a pattern of discrimination. An infamous example involves a study conducted at Shanghai Jiao Tong University to predict whether someone would be a criminal based on their facial features. ${ }^{62}$ This algorithm was swiftly and widely debunked because the researchers used mugshots to train the model for criminality and Chinese state ID photos to train the model for non-criminal faces. The researchers based their findings on the long considered pseudoscience of physiognomy, the practice of judging a person's character by their facial features, contending non-criminal faces have similar features and criminal faces tend to have eyes that are close together, where the inner corners as slightly narrower (5.6\%) than non-criminal faces. ${ }^{63}$ Attempts at detecting criminality using facial recognition software continues to be met with heavy criticism and charges of racial bias. ${ }^{64}$

Facial recognition software also has high misclassification rates for African Americans, Asians, and women. Amazon's Rekognition software failed to match African Americans and Asians photos between 10 and 100 times more often than Caucasian photos. ${ }^{65}$ This is a perpetual problem for many facial recognition algorithms. In a National Institute of Standards and Technology (NIST) study, facial recognition algorithms were found to have more trouble recognizing females than males, and an MIT and Microsoft algorithm with a $1 \%$ error rate identifying white male faces had an error rate of almost $35 \%$ recognizing darkskinned women. ${ }^{66}$ Demographic factors accounted for more false positive rates than false negative rates, with the former of greater concerns for most classification problems. There were higher false positive error rates for Asians, African Americans, and American Indians than for white individuals, women had higher false positive rates than men, and children and the elderly had higher false positive rates than middle-aged adults. ${ }^{67}$ Subsequently, researchers have found ways to lessen demographic errors. The predominant reason for bias reduction was the diversity of the training data to ensure ample representation of different demographic groups. Regulators in the European Union (EU) pay close attention to the representativeness of training data and soon it may garner more attention from U.S. regulators as the relationship between algorithmic bias and training data nonrepresentativeness becomes better understood.

The biases of facial recognition software have implications for disease diagnosis. It is important to understand how the algorithms perform in different demographic groups. What is the error rate in diagnosing the same condition in whites versus Asians, African Americans, and American Indians, for example? Failure rates of the technology have the potential to disparately increase medical costs in non-white groups, leading to higher premium rates because an algorithm failed at early disease detection.

Despite the ongoing challenges to improve facial recognition software, it has proven to be an essential tool being utilized by providers in managing patient care and improving health outcomes. The use cases include: 68,69

- Patient check-in process-Simplifying the admission process with reduced paperwork.
- Patient tracking-Determining where patients are and should be in a facility.
- Managing chronic pain and medication usage-Matching medications to pain levels.
- Diagnosis of certain diseases or conditions-Facial monitoring and eye-tracking combined with artificial intelligence to recognize and diagnose diseases.
- Staff identification-Ensuring only authorized individuals enter patient rooms.
- Securing facilities-Ensuring individuals that may pose harm to patients and staff are not allowed to enter medical facilities.
- Real-time emotion detection-Determining the emotional states of patients to detect collateral conditions and respond quickly with the correct medical treatment.

The benefits of algorithms extend to all practice areas in insurance, improving risk selection and classification, managing benefits and claim costs, marketing, and improving customer engagement. Therefore, it is important to focus on the benefits of algorithms while at the same time recognizing there are defects in programming and bad actors that should be addressed. We are witnessing steady technological improvements to address biases and defects in algorithms and improving security measures to thwart bad actors. According to Sendhil Mullainathan, professor of behavioral and computational science at the University of Chicago, "Changing algorithms is easier than changing people: software on computers can be updated; the 'wetware' in our brains has so far proven much less pliable." ${ }^{70}$ While in substance this is a true statement, we must remember that algorithms are programmed by people who are innately biased. An effective way to mitigate the risk of algorithmic bias is to ensure diversity on modeling teams. A team of researchers from Columbia University found algorithmic bias can be attributable to two primary sources: biased training data and biased programmers. ${ }^{71}$ There are simple remedies for both sources of bias.

The Brookings Institution published public policy recommendations, self-regulatory best practices, and consumer-focused strategies intended to mitigate algorithmic bias and reduce harm to consumers. ${ }^{72}$ The recommendations include:

## Public Policy

- Updating of nondiscrimination and civil rights laws to apply to digital practices. The intent is to understand how algorithms trigger discrimination and update existing civil rights laws to reflect contributory digital parameters and thresholds.
- Implementation of regulatory sandboxes to foster anti-bias experimentation and safe harbors to curb online biases.


## Self-Regulatory

- Acknowledgement of the possibility and causes of bias.
- Ask the question: Will the algorithm leave some groups of people worse off because of its design or unintended consequences?
- Operators of algorithms must develop a bias impact statement through the development of interrogatories that vet the algorithm against standards set in the initial design phase. New York University's AI Now Institute has developed such a framework that includes external, independent algorithmic impact assessments.
- Operators of algorithms should regularly audit algorithms for bias. Third-party auditors may provide the greatest insights.
- Operators of algorithms must rely upon cross-functional diverse work teams and expertise. A diversity of backgrounds, experience, and expertise can mitigate cultural and ethnic blind spots in algorithms before rollout that might otherwise go undetected.
- Increase human involvement in the design and monitoring of algorithms. It is important not to take a "set it and forget it" ${ }^{\text {"73 }}$ approach to algorithms in production. Human oversight will always be needed to ensure algorithms remain effective for their intended use. On this point, Alex Peysakhovich, a senior research scientist from Facebook, shared, "[W]e don't need to eliminate human moderators. We need to hire more and get them to focus on edge cases." ${ }^{74}$


## Consumer-Focused

1. Consumer algorithmic literacy programs are needed to ensure consumers understand how they are impacted by an algorithm's use of their data.
2. Formal feedback mechanisms between consumers and civil society groups can further improve the detection of algorithmic bias.

These best practices and suggested policies as set forth by the Brookings Institution may be worth considering by actuaries attempting to understand human behavior using algorithms. It is important to make sure inferences are not adversely affected by algorithmic bias, especially when they can be effectively mitigated as suggested above.

# Assessing Sources of Nontraditional Data to Improve Consumer Experience

Insurance companies are increasingly using nontraditional data and machine learning to streamline insurance operations and processes to develop efficient delivery systems and products customized to target markets and consumers. Prior to the emergence of big data, the collection of underwriting data was mostly limited to traditional sources such as the insurance applications, medical records and lab results, home and building inspections records, credit reports, and publicly available data. It still remains true that the underwriting data are primarily collected from the consumer through the insurance policy application and underwriting process, and if the consumer consents, the insurance company can collect data on medical records, property records, and motor vehicle records. Today, a variety of nontraditional data sources-such as social media, smartphones, activity trackers, and thirdparty sources that are easy to access-are used to augment traditional data sets, yielding richer behavioral insights. These new data sources have been used to increase the predictive power of risk classification models and improve the alignment of risk to price. Life and health insurance underwriting processes are leveraging activity and biometric tracking data with medical electronic health record (EHR) data, as illustrated in Figure $7 .{ }^{75}$ Electronic health records are static, capturing key health indicators at discrete points in time. Tracking data is more continuous in its velocity and more predictive of an imminent health event, an important distinction over EHR data. Continuous data can prevent a health event from becoming catastrophic by signaling health professionals of needed care. Insurers use activity data to identify long periods of inactivity so they can "nudge" insureds to get moving to improve their health. ${ }^{76}$

75 "Speed the development of wearable devices with a solid, targeted platform"; Electronic Products \& Technology. 76 "Insurers want to nudge you to better health. So they're data mining your shopping lists"; Stat; Dec. 15, 2015.

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-43.jpg?height=832&width=943&top_left_y=451&top_left_x=488)

While insurance companies can collect directly from these nontraditional data sources, they more often rely on third-party vendors to collect and provide data from nontraditional data sources. Insurers merge nontraditional data with traditional data sources to identify patterns of risk that can inform the underwriting process. The patterns may also point to demographic and lifestyle indications to better engage customers to manage their health and environmental risks. These new data sources may lead to different risk pooling than that based on more traditional data and underwriting approaches alone, for better or worse. Big data analytics can save life insurers the expense of time-consuming, invasive, and costly medical tests and procedures in underwriting, benefitting both the insured and the insurer. A major concern with nontraditional data is the risk it may drive unfair discriminatory underwriting consequences. Nontraditional data may have been collected in a biased manner and not be representative of the cohorts to which it is applied, further biasing any analysis that uses it. When biased underwriting is applied to insurance consumers, risks may be inappropriately priced with financially adverse impacts to both insureds and insurers. Underwriting with nontraditional data can result in unfair and disparate treatment of consumers and unintended discrimination, when

1. there are data quality issues, or
2. the implicit data contains limited exposures, or
3. where the data is not fit for the purpose or intended application, or
4. the risks identified during the analysis are not appropriate due to a lack of ground truth data.

Actuaries would generally review guidance provided by ASOP No. 23 and ASOP No. 56 to investigate data quality issues when building a predictive model.

Nontraditional data is also subject to errors that can be difficult to correct by consumers, even when it is disclosed at the request of consumers through an adverse underwriting decision. If the data is not released to the consumer, the consumer does not have an opportunity to review and correct incorrect data and may purchase an insurance product that is not appropriately priced based on their risk classification. When carriers use federal Fair Credit Reporting Act (FCRA)-compliant third-party data, adverse underwriting decisions come with reason codes $^{77}$ to support the decision. Reason codes, such as placement in a higher-cost risk class, may signal an insured to contest the accuracy of the data used to drive the underwriting decision and demand that inaccuracies be corrected. This is not the case with non-FCRA-compliant data, such as social media or purchaserelated data, and poses risks to risk classification and pricing algorithms.

Collecting data continuously and in real time is another benefit of the velocity of big data and the technology to analyze it synchronously. For example, cars are equipped with sensors, also referred to as telematics devices, that track everything from speed, acceleration, and braking frequency to gas consumption and engine performance. Activity trackers measure and collect physical activities and basic body vital measurements, and cell phones have GPS technology that can track where, when, and how often consumers visit certain physical locations. The benefits of analyzing continuous data in real time enables insurers to immediately identify the needs of insureds, respond quickly to market changes that may affect product demand, and communicate with insureds more responsively using mobile devices. Continuous, real-time data also helps insurers identify and analyze policyholder behaviors relevant to the insurance policy that require immediate attention and intervention to avert costly policy outcomes. This suggests some insurers may adopt continuous underwriting systems where risk premiums are continuously adjusted. Many property and casualty lines of insurance, such as private passenger auto, adjust premiums only at renewal points which may be as frequently as twice yearly. Notably, with the rise of digital insurance platforms along with new innovative product structures, carriers have been able to support higher-frequency premium adjustments powered by tools like continuous underwriting. Continuous underwriting can result in better measurement of risks with the continuous transfer of data, but insurers may have to incentivize insureds to participate in the collection frequency. It should be noted that some lines of insurance may be restricted differentially by the states on the frequency of rate changes which may prohibit premium adjustments more

77 Reason codes are descriptors that explain favorable or adverse credit-score-related decisions.
frequently than annually. Individual underwriting may not be allowed in some states and for some products and real-time data collection is not included in the insurance contract by default. This feature is only added with the consent of consumer telematics. Drivers with "safe" telematics metrics can earn as much as a $30 \%$ premium discount or more. ${ }^{78}$ Life insurance companies are collecting data from wearable devices to make coverages for those with health conditions, such as diabetes, more affordable. The inherent risk of this data is that it is collected from the insured on a voluntary basis, and therefore any analysis done on this data may not be wholly generalizable. The other risk is that consumers may not use data collection devices continuously which may impair any analysis done using this data, compromising the generalizability of any modeling results.

The wider the range of data insurance companies have access to, the better they can identify appropriate markets and their understanding of consumers; this can benefit both insurers and insureds. Smart technology, social media, and internet technologies constantly produce new information about consumers that insurers can harness to better understand consumer needs and predict behavior. The result may be a better alignment of product needs and risk profiles, and more direct engagement with consumers, accelerating policy issue.

# Controlling for Systemic Influences and Socioeconomics

Practitioners and policymakers alike know algorithmic decision-making-based data analytics can have biased and discriminatory effects if, for example, the data or algorithmic process are not carefully constructed and evaluated. While human biases based on preferences and socioeconomics have always existed, it is hoped that by replacing human judgment with technology, the decision-making process can be more neutral to systemic influences and socioeconomics. Indeed, studies have shown that machine-learning-based algorithms can outperform humans in making unbiased and discrimination-free decisions in various applications. One such area is bank lending decisions, where it has been shown machine-learning-based algorithms can lead to higher profits for the lender and at the same time reduce biases with respect to minority borrowers. ${ }^{79}$ Yet many experts continue to be concerned that replacing human decision-making with algorithms may actually perpetuate the biases that currently exist in society in hiring, retail, and the criminal justice system. ${ }^{80}$[^5]

To utilize indirect data sources for correlations and risk exposures, it is important that the underlying data have sufficient ground truth data underlying the data training set. A wellknown example is in facial recognition or analytical systems. If more photos of lighterskinned faces are used to train a model than photos of darker-skinned faces, then the system would naturally be inferior at recognizing darker-skinned faces. This is the problem of a biased training dataset. The dataset is either not representative of reality or it reflects existing biases structured in the data by modelers. Furthermore, if a model is trained on historical human decisions, then it would tend to perpetuate existing human biases and systemic influences.

Biases and systemic influences cannot be blamed on biased training datasets alone. At each stage of the model building process, biases can creep into the framing of the problem or in data collection and preparation, or in the parameterizing of the data. Modeling decisions made early in the process may have undesirable downstream impacts. ${ }^{81}$ For example, in selecting features to use in a predictive model, variables such as education level, income, and ZIP code may turn out to be very predictive. But would the use of such variables produce undesirable systemic influences? The impact of feature selection on predictive accuracy is easy to measure, but its impact on model bias is not.

A 2020 paper, "Technological Innovation and Discrimination in Household Finance," prepared for the Federal Reserve System Finance and Economics Discussion Series, summarizes five areas of discrimination in the financial services industry that those working in data analytics and modeling should be aware of. They are:

1. Human involvement in designing and coding algorithms, where there is a lack of diversity among coders.
2. Biases embedded in training datasets, where, for example, a few states represent a majority of the exposures or policy counts in a countrywide model.
3. Use of variables that proxy for membership in a protected class, such as ZIP code, income, and occupation as a proxy for race.
4. Statistical discrimination profiling shopping behavior, such as price optimization, which might be implemented using retention modeling. It is worth noting that some states have issued guidance against using this practice for property and casualty insurance ratemaking.
5. Technology-facilitated advertising algorithms used in ad targeting and ad delivery, such as, for example, targeting only protected classes with certain financial offers or delivering ads to purchase household goods rather than technical material. ${ }^{82}$

Actuaries may want to consider thinking about their models in the five areas above in the context of the regulatory framework. Actuaries may also want to consider determining how to effectively detect unwanted biases and systemic influences in their models, especially when underlying attribute data attributable to protected classes is not directly available. It turns out that there are no easy approaches to resolving these issues without universally understood notions of bias and fairness.

A case that illustrates this point is an algorithm called COMPAS, designed to assign a risk score of recidivism used by judges to decide whether defendants awaiting trial should be released on bail. If the algorithm is assessed based on its positive predictive accuracy-i.e., the proportion of defendants that are assigned a medium- or high-risk score that actually reoffend - then the algorithm does not seem to have biases because Black defendants and white defendants have similar positive predictive accuracy. However, if the algorithm is assessed based on its false positive error rate-i.e., the proportion of defendants that ultimately do not reoffend but are misclassified as median or high risk-then Black defendants are twice as likely to be misclassified as white defendants ( $42 \%$ vs. $22 \%$ ). ${ }^{83}$

Because the algorithm has similar positive predictive accuracy for Black and white defendants, it can be argued that the algorithm is race-agnostic, and the judge using it does not need to consider the race of the defendant. However, it can also be argued that misclassifying defendants results in more harm, and therefore a fair algorithm should not misclassify more Black defendants than white defendants. The problem is that in this situation it is mathematically impossible to achieve a positive predictive accuracy value and a false positive error rate that results in the equal treatment of defendants at the same time. It is often difficult for an algorithm to have a zero false positive rate and a zero false negative rate, as depicted in Figure 10. ${ }^{84}$ If that were the case, the graphs of innocent people and guilty people would not overlap and there would be no false positives or false negatives as depicted in Figure 8. In criminal justice cases, setting the standard of proof makes the difference between sending innocent people to jail (sensitivity) and letting guilty people go free (specificity), and where the standard of proof line is drawn is critical to jury outcomes, as depicted in Figure 10. ${ }^{85}$[^6]

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-48.jpg?height=534&width=1068&top_left_y=405&top_left_x=493)

Therefore, whether an algorithm appears to be biased may depend on the metric that is used to measure such bias.

It is important to note the difference between figures 8 and 10 is the certainty of guilt or innocence. Figure 8 is the case when police only arrest guilty people, making it a certainty that juries only send guilty people to jail if a high standard of proof is set. However, law enforcement and the justice system are not perfect, and people make mistakes. In this case, where the standard of proof is set can have dire consequences for those who are innocent and found guilty.

Researchers have developed methods to remove biases in AI algorithms. One approach is to pre-process the data to maintain as much accuracy as possible while reducing any relationship between outcomes and protected characteristics or sensitive attributes.

Techniques such as sampling and reweighing can reduce the bias by adjusting the balance of the different groups present in the data and therefore increasing the learning opportunity for the models. ${ }^{86}$

FIGURE 9: $\quad$ APPEARANCE vs. GUILT

Null Hypothsis $(\mathrm{H} 0)$ :

Alternative Hypotheses $(\mathrm{H} 1)$ :

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-49.jpg?height=399&width=740&top_left_y=500&top_left_x=714)

FIGURE 10: APPEARANCE OF GUILT

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-49.jpg?height=630&width=775&top_left_y=1035&top_left_x=770)

Another approach is to set up a "fairness constraint" that either transforms some of the model's predictions to satisfy the fairness constraint or imposes the constraint during the model's optimization process. It is also possible to add more data points to improve performance for protected classes; ${ }^{87}$ however, this may not always be possible. Mitigating biases is an area of active and ongoing research in building AI models. Thus, actuaries may look at a variety of measures to assess biases and systemic influences, and the measures chosen should reflect the social and the business context in which the model is to be used. It is also important to consider the potential trade-offs in predictive accuracy of any such model and the resulting negative impact on outcomes such as cost-based prices.

One measure of fairness looks at predicted outcomes only, such as group fairness, which is defined as having an equal probability of assigning a favorable class to a protected class and an unprotected class. A more refined concept is conditional statistical parity, which considers group fairness conditioned on certain attributes. For example, an algorithm might assign a higher proportion of male applicants to a favorable class than female applicants, but adjusting for age and income, the algorithm may assign the same proportion of male and female applicants to a favorable class. Thus, the algorithm may satisfy conditional statistical parity but fail group fairness. Another class of fairness measures looks at both predicted outcomes and actual outcomes. The positive predictive value and false positive error rate are two such measures. Similarly, one can also calculate the negative predictive value and false negative error rate. It is important to consider how similarly situated subjects are treated by a predictive algorithm. If two subjects have the same attributes, except that one is in a protected class and the other is not, then the predictive algorithm should produce the same outcome for both subjects. ${ }^{88}$

There is no automatic means for detecting unwanted systemic influences and biases, and human judgment is still needed. It is important to consider the social context in which models are deployed and use a variety of measures to assess them for unwanted systemic influences and biases. Some ways actuaries might control systemic influences, biases, and socioeconomic impacts include being aware of the complexity of this issue as a first step and enlisting a diverse project team as a second. The diversity is beneficial for understanding model results from different perspectives of fairness and biases. Finally, developing an explainable and transparent model allows actuaries to better access and communicate any model effects of systemic influences, biases and socioeconomic impacts to users, regulators, and the public.

# Evaluating Nontraditional Data

Insurance companies are finding great value in the variety and velocity of nontraditional data sources for product development and pricing, underwriting, and marketing purposes. Emerging technology allows consumers of data to directly access social media and publicly available data and purchase lifestyle, demographic, environmental, sociographic, socioeconomic, and catastrophic data from third parties. Many insurance companies are building in-house centers specializing in data acquisition and machine learning technologies to support AI driven insurance innovations. Internal analytics teams may or may not include actuaries, but the preferred choice of regulators is for oversight and team integration with actuaries. The United States Government Accountability Office (GAO) released a report in 2019 on the benefits and challenges of the innovative uses of big data and machine learning that address this wish. ${ }^{89}$ The GAO concluded:

- Models are being developed by data scientists who, unlike actuaries, may not fully understand insurance-specific requirements, such as setting premium rates that are not unfairly discriminatory, and may struggle to measure the impact of new variables used in the models.
- Data scientists may be unfamiliar with insurance rules and regulations and may not understand how to communicate their work to state insurance regulators.

The observations of the GAO have strong implications for the role of actuaries to facilitate a positive transformation of the insurance industry as it becomes more reliant on big data and AI models to increase the predictive value of insurance models to identify policyholder behaviors indicative of risk. Data scientists may not adhere to a set of professional standards equivalent in scope to the standards of the actuarial profession.

The work of the GAO suggests a strong need for actuaries to collaborate with regulators to assist them in developing effective ways to evaluate data sources and AI models appropriate for insurance. Insurance promotes commerce, economic growth, investment in innovations, and social well-being. ${ }^{90}$ Actuaries because of their unique role working with and for insurers are well positioned to work with regulators to help develop regulation and oversight of the technical aspects of insurance including complex models.

Communication and collaboration between actuaries and regulators are critical in the following areas:

- Sourcing, defining, and social implications of model variables. It is important to identify any correlations with disallowed variables and their relationships to the risk being insured where possible.
- Continuous data feeds. Continuous data from sources such as social media, smart phones, and telematics can create challenges in continuous underwriting. Some of the issues needing resolution are how often to sample from data streams, how to detect artifacts in data caused by faulty mobile applications (apps), and how to empower consumers to inspect and refute erroneous data used to price their coverages.
- Data sampling. Two major concerns with sampling are the population from which data is sampled and the sampling methodology. There are companies that, for example, might sample from their employee population in a local region to build a countrywide model. This may result in a model that is untenable for application in diverse geographic populations. It is also important to consider the merits of sampling methods such as simple random sampling or stratified random sampling.
- The need for actuaries and regulators to coordinate on data reliability standards. External data sources such as census data (which may be limited), geological data from NOAA, and transportation data from the NTSB raise fewer concerns among regulators than data from social media, tracking devices, and third-party vendors. The use of credit scores, long scrutinized by regulators, has been receiving attention because of renewed concern over racial bias leading to recent efforts over their restriction or prohibition. ${ }^{91}$
- Data verification processes are needed to qualify the veracity and freshness of data for the time frame of the model. It is important to assess the appropriateness of the age of the data to predict future behavior and to make sure it is not unduly influenced by extreme events during the epoch of the data which may limit its utility and bias model results
- The model risk management and model governance of insurance companies may need to be reviewed and their scope may need to be expanded to include the use of big data, data analytics, and predictive models. Expanding risk management and governance policies to include best practices around data and model building can improve risk mitigation.
- Metrics-Insurers may wish to partner with regulators to develop easy-to-understand metrics by which models can be assessed for accuracy, reliability, compliance with regulatory standards, and model fit.
- Causality vs. correlation. Under ASOP No. 12, Risk Classification, actuaries are not required to identify causation in predictive models. Distinguishing correlation from causation analysis can aid a more complete understanding of the concerns and limitations of a model. This could involve identifying valid rationales for model variables and methods. Regulators may also require valid rationales before approving a rating plan based on external data and advanced modeling techniques for use in their states.
- Actuarial communications. There is a tendency to assume algorithms beyond a Generalized Linear Model (GLM) are difficult to explain. However, in an actuarial communication, it is the responsibility of the modeler to be able to explain their work products per Actuarial Standard of Practice No. 41, Actuarial Communications.

New York State Insurance Circular Letter No. $1^{92}$ issued in 2019 can be a useful reference and is an important regulatory requirement for insurance companies. This circular letter covers the use of external data and certain approaches in data analytics and predictive models. Though this circular letter applies to life insurance companies and their use of external data and information sources in underwriting, the guidelines can provide useful elements for other insurance practice areas. The guidance recognizes the use of external data from nontraditional data sources and potential benefits of simplified underwriting and sales processes for life insurance policies with more accurate underwriting results. However, the concern raised in the circular letter is that external data, algorithms, or predictive modeling results can have a negative impact on the availability and affordability of life insurance for protected classes of consumers. The guidance requires insurance companies to disclose the sources of information used for underwriting and reasons for adverse decisions. Additionally, the circular letter requires insurance companies to verify the data and model comply with the laws and regulations of the state and to provide rationales for data variables and the choice of algorithms. The guidelines from New York state can be intricately linked to ASOP No. 23, Data Quality, and ASOP No. 56, Modeling. It is worth noting that since the increased usage of data and modeling, which has facilitated insurers to underwrite and price a wider range of risks, policy counts in automobile residual markets have dropped dramatically as more consumers have been able to find coverage in the voluntary market. The National Flood Insurance Program (NFIP) is another good example-increased modeling has provided for a more robust private company participation in that market, which can ease the burden on the government.

National Association of Insurance Commissioners (NAIC) groups are engaged in issues emerging in the use of nontraditional data and data technology and artificial intelligence. The Innovation and Technology (EX) Task Force and its subcommittee, the Big Data and Artificial Intelligence (EX) Working Group, coordinate the NAIC'S efforts on these topics and consider the need for overall regulatory guidance on insurer's use of consumer data and industry practices around data technologies. ${ }^{93}$

# Regulatory Concerns Impacting the Work of the Actuary

Actuaries working as regulators and for insurance companies each have a unique mission to bring innovative solutions to consumers without compromising consumer protections. The industry recognizes the need for effective regulation overseeing an environment of robust innovation and has indicated it wants to work with regulators to identify and institute mechanisms that will satisfy regulatory concerns and continue to encourage innovations in the field.

To illustrate the regulatory perspective, a comprehensive white paper addressing regulatory review of property and casualty insurance predictive modeling was recently produced by the NAIC in which the regulatory concerns in that white paper and others include: ${ }^{94}$

- The use of third-party datasets not verified for the purpose they are being used for and their completeness for that purpose.
- Reliance on third-party, nontransparent algorithms that may use regulatory disallowed variables. Some algorithms are not transparent but are accepted for use. Questions to address include:
- What is acceptable in terms of transparency?
- Should transparency be limited to the data the consumer sees and how it is used in models as applied to the individual consumer? There is a need to work with regulators in defining the criteria for transparency.
- What are alternatives for dealing with a lack of transparency?
- Safeguards to maintain trade-secret protection.
- Are there third-party organizations regulators would accept as validators of external data and models?
- Models that are difficult to explain and interpret undermine public trust. The use of advanced statistical algorithms that are difficult to explain are challenging regulators to assess whether they are unfairly discriminatory. Regulators need to develop expertise and metrics for evaluating models that do not produce the standard (GLM) output and to rank feature importance. Regulators need to increase their education of these advanced models.

There is a lack of professional standards of data scientists involved in actuarial model building and a lack of actuarial responsibility for and reliance on their work products. The ASB circulated a request for input concerning the possible development of a standard on P\&C rate filings. The NAIC's Casualty Actuarial and Statistical (C) Task Force raised concerns over the development of such an ASOP for actuaries to sign off on rate filings because of concerns that actuaries have not been trained in advanced modeling techniques, although this is changing. Actuaries might assume responsibility for reviewing complicated models because rate filings are actuarial work products. ASOP No. 56 can provide guidance here.

- Insurers need to work with regulators to clarify terms such as causation, correlation, and their justifications with respect to model variables and model outcomes. Predictive models are only structured to address correlation not causation because they do not meet the standards of a randomized control trial. However, justifications for model assumptions, design, and model variables can be subject to review.
- The inability of modelers to communicate advanced statistical techniques and modeling results to regulators to enable regulators to ensure that rates are not excessive, not inadequate, and do not unfairly discriminate.
- A lack of reconciliation of differences in model factors produced by different software packages. What is an acceptable tolerance level for the differences?
- Ensuring data is protected and how data breaches will be handled. What processes are in place to allow consumers to inspect and correct, if necessary, errors and omissions in insurance company modeling data? How will insurance companies make corrections on the impacted policies including coverages or premiums due to incorrect or incomplete data?95

There is a lot of work to do on the part of insurers and regulators to find common ground to ensure consumers are protected while balancing the utility and innovations advanced modeling techniques can bring to a positive transformation of insurance.

95 Cyber Risk Insurance-A Resource Guide for Actuaries; American Academy of Actuaries; May 2019.

# Transformational Impacts of Big Data and Al on the Future of Insurance and Society

Compared to other sectors, the insurance industry is relatively in its infancy in the use of big data and algorithms to develop insurance applications, with property and casualty insurance beginning to apply advanced modeling techniques toward the end of the $20^{\text {th }}$ century. ${ }^{96}$ It was not long before health and life insurers followed suit. There is much to learn from other fields, including the health care sector, of the pitfalls and benefits of applying big data and algorithms to human-centered problems. Precision medicine applies big data and algorithms to diagnose and manage diseases while tackling complex ethical issues related to biased training data and faulty modeling approaches. The high-tech/information technology industry similarly has come under immense criticism for algorithms biased by nonrepresentative training data and a nondiverse workforce of data modelers. This section of the paper explores the lessons learned that the actuarial profession might find instructive when building predictive models in the insurance sector.

## Precision Medicine

According to the White House-sponsored Precision Medicine Initiative, precision medicine is "an emerging approach for disease treatment and prevention that takes into account individual variability in genes, environment, and lifestyle for each person, ${ }^{, 97}$ using an increased reliance on big data and algorithms. ${ }^{98}$ One group of researchers posit machine learning algorithms used in the medical profession should also follow the Hippocratic oath: "First do no harm."99 At a minimum:

1. Data must be checked for biases, balance, misrepresentation, and completeness and issues must be resolved to ensure models appropriately distinguish signal from noise, especially for algorithms used to remove artifacts from brain imaging readouts, for example. ${ }^{100}$
2. Training, validation, and test datasets should all be of equal quality, representative of the condition under study, and thoroughly vetted to prevent automation bias "the human tendency to accept a computer-generated solution without searching for contradictory information." ${ }^{101}$[^7]
3. Models should be validated for internal mathematical consistency and against the knowledge of subject-matter experts for credibility to ensure improved patient outcomes.
4. It is important that machine learning results are interpretable, which is not often an easy task because of their "black box" nature. Without interpretability, using model results to automate diagnoses may pose harm to patients and betray the trust of clinicians.
5. Finally, machine learning models need to be assessed against standards for fairness (they should not unfairly discriminate), privacy (data protection), reliability (robustness), causality (are associations reasonable or spurious?), and trust (are the results correct for the right reasons or just by chance?).

Insurers can apply these measures for data and algorithms in precision medicine to data and algorithms used in risk classification and pricing. The actuarial profession can benefit by examining how big data and algorithms have influenced the transformations of other professions to see what may apply. The health care industry has used algorithms without an understanding of their potential to create disparities and has also learned from these past negative experiences to overcome many of the challenges. ${ }^{102}$ Researchers have demonstrated a deep understanding of how to apply big data and algorithms to medical problems, measure and validate their efficacy, understand how to harness the disruption they present for medicine, and have realistic expectations regarding winners and losers as the technology becomes more pervasive. In this view, patients will come out on top if they generously donate their data to algorithms. ${ }^{103}$

## Addressing Both Accessibility and Sustainability.

Two key factors that impact insurance product designs and pricing include:

1. If an individual cannot impact/prevent a future possible risk, then insurance is a privatized or public solution to aid those who have future unfortunate events resulting in losses.
2. If individuals can control or mitigate their risk exposure, then insurance can incentivize that behavior through lower premiums.

In addition, the rising use of big data is also intersecting with the accelerating desire to address issues of systemic inequality. Access to insurance provides an option to reduce the volatility of one's current wealth/assets, but it is not an avenue to increase one's current level of wealth. In fact, it requires a very slight reduction in one's mean level of wealth to reduce its future volatility.

For those with limited means, there are two options beyond the traditional private insurance markets-microinsurance and public programs (e.g., Social Security). Microinsurance has played an important role in developing countries and economies, such as in India and Africa. It encompasses simple products and a strong element of trust/social cohesion for it to succeed. It has also been piloted in some areas of the U.S. Could the use of AI and big data, supported by regulatory policies, assist in both identifying those who would benefit from microinsurance and to reduce its costs? Microinsurance needs low expense and profit margins to make it more accessible—both possible outcomes of big data and AI innovations.

The ability of big data and AI to better identify and signal the factors that lead to increased risk will, for many, lead to less expensive insurance. As insurance evolves to become a greater a collaboration between a "provider of risk-relevant data" via an insurance organization to the individual(s) or company responsible to manage the risk-as is occurring with precision medicine. However, there will also be those individuals who, for a variety of reasons, either cannot or will not change behaviors that reduce their risks. And thus, will end up with no insurance or assigned to a high-risk pool. The application of insurtechs may well lead to a sizeable segment of the population willing to share their personal data on diet, sleep, health, movements, and activities to reduce their risks and the costs of insuring that risk. But there may still be a group of individuals unwilling to act or change or that will not be able to afford any kind of insurance as they are grouped with other high-risk individuals. Past examples of ways to address risk pool participation include:

1. Mandates to purchase insurance with fines or imprisonment for failure to purchase auto insurance.
2. Creation of a high-risk pool, as done in many states, for individuals who cannot qualify for private health insurance. The cost may be borne through either taxpayer and/or charges to the private insurance providers and their customers.

If the desire to increase accessibility to sustainable insurance is to be met, private insurance solutions may well need to rely on public policy solutions to ensure insurance is sustainable as well as create incentives to lower the overall risk exposures.

## Leverage Diversity in Al

There is ample evidence that diverse teams outperform homogenous teams. Companies with diverse management teams are $35 \%$ more likely to outperform their industry financial averages, and gender diversity in the top quartile further improves the likelihood of outperformance by $15 \% .{ }^{104}$ Analogous improvements have been observed with respect to diversity of modelers building predictive models, ${ }^{105}$ but instead of focusing on financial metrics as the standard of performance, fairness (they should not unfairly discriminate) and unbiasedness are the metrics. While the insurance industry lags other industries in the deployment of AI technologies, it is in prime position to improve its deployment by observing lessons learned in other sectors. Even within the insurance industry, the missteps experienced have resulted in backlash that was swift and sharp. One health algorithm indicated Black individuals were less of a health risk than white clients and referred Black patients for improvement programs less often than white clients. ${ }^{106}$ Critics of the algorithm say the bias is due in part to "a lack of diversity among algorithm designers, and a lack of training about the social and historical context of their work.".107

FIGURE 11: $\quad$ RACIAL DIVERSITY IN SILICON VALLEY

How major tech companies stack up against each other

![](https://cdn.mathpix.com/cropped/2024_04_10_e7bd1ea6c348174c8d4eg-59.jpg?height=591&width=1244&top_left_y=1382&top_left_x=489)

The AI industry is transforming the insurance industry, while at the same time it needs transformation in the very area that would aid in mitigating algorithmic bias-diversity among programmers. Figure 11 depicts the ethnic mix of the top tech companies of Silicon Valley as reported in 2019. For many of these companies, the mix had not changed much over the five years prior. For example, in 2014 Google was $61.3 \%$ white and $69.4 \%$ male
and in 2019 , the numbers were $54.4 \%$ and $68.4 \%$, respectively, ${ }^{108}$ and similar patterns hold for the other firms. It is notable the numbers for Apple and Amazon are inflated by their warehouse staff. Similar trends exist in data scientist roles. Less than $20 \%$ of the roles are filled by women, $55 \%$ are filled by whites, $27 \%$ by Asians, $8 \%$ by Hispanics, $6.9 \%$ by Blacks, 0.3\% American Indian and Alaska Native, and 2.6\% unknown. ${ }^{109}$ These numbers do not bode well for preventing biases due to a lack of programmer diversity. One study ${ }^{110}$ suggests that bias due to a lack of programmer diversity is more than just a "pipeline" problem. When there is a lack of programmer diversity, other measures to mitigate bias become even more important to build trust between insurers, the public and regulators. They include:

1. Greater transparency of algorithm methodology-Greater transparency converts "black box" algorithms into "glass box" algorithms which can be evaluated for their strengths and weaknesses. With greater transparency comes greater understanding and more enabled decision-making.
2. Composition of training data-It is important to make sure the training data is representative of the population any model built on it will be applied to.
3. Independent audit results-It is important to have independent audits of modeling data and models by agents who did not play a role in building the model to minimize biasing of results.
4. Target variable analysis-It is important to analyze the target variable to ensure it is a reasonable and unbiased representation of the risk being modeled.
5. Validation metrics to relieve concerns of algorithmic bias-Metrics are a good place to start understanding the extent to which biases are embedded in the underlying data and mechanics of a model. It is also important to validate model results against intuition, expert judgment, and systemic social patterns of bias as well.

These efforts will aid a positive transformation of the insurance industry as the uses of big data and algorithms continue to evolve and find more applications.

# Conclusion

The analysis presented in this paper strongly underscores the future of insurance will be grounded in predictive analytics, ${ }^{111}$ with all the promise and potential hazards big data and algorithms present for insurance practitioners and regulators. There is consensus on the importance and necessity of innovation for the positive transformation of the insurance industry not only to facilitate its vibrancy and efficiency, but also to benefit consumers while ensuring consumer protections.

But navigating the negative effects posed by big data and algorithm is not without challenges. As big data and algorithms mediate the relationship between insurers and consumers, will they enhance, diminish, or obfuscate the impact of human judgment, bias, or possible unfair decision-making? Algorithms can process larger volumes of data per unit time than human capacity is capable of, making algorithms logical choices for sifting through large data sets to find predictive patterns to leverage in decision-making. But delegating decision-making to algorithms requires imposing high rigor to ensure modeling outcomes promote a system of insurance that is accessible, transparent, and sustainable. While algorithms can be an important tool to promote social equity, they may not be perfect in doing so, as achieving zero false positives and zero false negatives is nearly impossible. However, actuaries and regulators can work together to minimize the adverse effects of algorithms:

1. By ensuring representativeness, balance, and unbiasedness in training data. Most sources of adverse impacts can be traced to poorly designed training data and the process used to train from it. The work of the Federal Reserve in identifying discrimination in the financial services sector found concentrating exposures in a few states biased a countrywide model.
2. By measuring the veracity of data. Data has become a valuable asset, and rating methods analogous to those used by Moody's, S\&P, and the National Aeronautics and Space Administration (NASA) are coming under consideration to assess the accuracy, reliability, and value of the data and the algorithms that are applied to the data. These methods offer promising opportunities to help insurers and regulators assess the merit of third-party data assets deployed in advanced statistical models and AI processes.
3. By promoting diversity among modeling teams in terms of gender, ethnicity, race, age, technical training, experience, and discipline. Diverse teams should reflect a balance across the technical and social sciences to detect and mitigate cultural and ethnic blind spots in model results before model implementation. Monitoring model implementation is also important in preventing biases due to misuses of models.
4. By ensuring model fit is continuously monitored by human oversight. It is important not to take a "set it and forget it" approach after implementation. There are many reasons a model will degrade due to model drift, data changes, changes in consumer behavior, product design changes, etc. Knowing when to refresh or rebuild a model is necessary for ensuring model fit.
5. By striving for transparency, interpretability, and explainability in communicating the composition of the data and algorithms deployed in advanced modeling techniques for risk classification and pricing. This includes analyzing data variables as proxies for regulatory disallowed variables. These efforts are important for establishing trust with the public.
6. By holding algorithms accountable. Algorithmic accountability can be addressed through "holistic" audits that are performed on advanced modeling techniques and the underlying data. ${ }^{112}$ Including protected class attributes, rather than excluding them in modeling is gaining attention from social scientists and practitioners as a method of identifying, isolating, and removing the disparate effects of race on model results, in hopes of prompting algorithmic fairness. ${ }^{113}$ Implementing such a solution can be challenging and will require an interdisciplinary approach to measure its effectiveness.
7. Professional standards can keep pace with the evolution of big data and algorithms by developing appropriate ASOPs in conjunction with practice and adherence to regulatory requirements. Recommendations by the Brookings Institution focus on updating civil rights laws so that they apply to digital practices and the establishment of algorithmic triggers of discrimination. Public policy efforts in this area could impact the actuarial profession, requiring responsiveness in developing appropriate professional standards.

While insurance serves many socially useful functions, it may not be able to address all socially desirable outcomes while remaining sustainable and accessible. It may be necessary to look to other solutions if the use of big data and algorithms cannot completely remove or neutralize the biases from risk classification and pricing models. Microinsurance and public programs are promising options to address systemic inequality issues to keep insurance systems accessible and sustainable. Insurers and regulators will need to work to find solutions that promote the continued positive transformation of the insurance industry while keeping consumers safe from the potential harms posed by big data and algorithms.

This paper has summarized key developments in the use of big data and algorithms in insurance modeling since the publication of the American Academy of Actuaries' Big Data Task Force monograph, Big Data and the Role of the Actuary. Continued education and awareness of these issues is foundational, and the pivotal role of actuaries and regulators in supporting the public's trust and contributing to sound public policy decision making is essential.

# References

American Academy of Actuaries (Academy). (2020). Self-Regulation and the Actuarial Profession. Committee of Professional Responsibility. American Academy of Actuaries. Washington, D.C.

Andrews, D.L. (2017). Predictive Model Building 101. SOA Predictive Analytics and Futurism Newsletter, (15). Retrieved from https://www.soa.org/globalassets/assets/Library/Newsletters/ Predictive-Analytics-and-Futurism/2017/june/2017-predictive-analytics-iss15-andrews.pdf

Artiga, S., Hinton, E. (2018, May 10). Beyond Health Care: The Role of Social Determinants in Promoting Health and Health Equity. KFF. Retrieved from https://www.kff.org/disparities-policy/ issue-brief/beyond-health-care-the-role-of-social-determinants-in-promoting-health-and-healthequity/

British Broadcasting Corporation (BBC). (2019a). Facial recognition to 'predict criminals' sparks row over AI bias. Retrieved from https://www.bbc.com/news/technology-53165286\#: :text=A\%20US\%20 university's\%20claim $\% 20$ it, a $\% 20$ picture $\% 20$ of $\% 20$ their $\% 20$ face $\% 22$

British Broadcasting Corporation (BBC). (2019b). Facial recognition fails on race, government study says. Retrieved from https://www.bbc.com/news/technology-50865437

Buckle, J., Hayward, T., Singhai, N., Desai, K. (2020). The Role of Wearables in Private Medical Insurance. Milliman. Retrieved from https://milliman-cdn.azureedge.net///media/milliman/pdfs/ articles/the role of wearables in private medical insurance.ashx

Buolamwini, J. (2019, May 22). Facial Recognition Technology (Part 1): Its Impact on our Civil Rights and Liberties. United States House Committee on Oversight and Government Reform Hearing. Retrieved from https://docs.house.gov/meetings/GO/GO00/20190522/109521/HHRG-116-GO00Wstate-BuolamwiniJ-20190522.pdf

Cahan, E.M., Hernandez-Boussard, T., Thadaney-Israni, S. et al. Putting the data before the algorithm in big data addressing personalized healthcare. npj Digit. Med. 2, 78 (2019).

Chu, R., Duling, D., Thompson, W. (2007). Best Practices for Managing Predictive Models in a Production Environment. SAS Institute Inc. Retrieved from https://support.sas.com/resources/ papers/proceedings/proceedings/forum2007/076-2007.pdf

Cowgill, B., Dell'Acqua, F., Deng, S., Hsu, D., Verma, N., \& Chaintreau, A. (2020). Biased Programmers? Or Biased Data? A Field Experiment in Operationalizing AI Ethics. Proceedings of the 21st ACM Conference on Economics and Computation.

Crumpler, W. (2020, May 1). The Problem of Bias in Facial Recognition. Center for Strategic \& International Studies. Retrieved from https://www.csis.org/blogs/technology-policy-blog/problembias-facial-recognition

Derman, E. (1996). Model Risk. Goldman Sachs Quantitative Strategies Research Notes, United Kingdom. Retrieved from http://pricing.online.fr/docs/model risk.pdf

Dickey, M. R. (2019, June 17). The future of diversity and inclusion in tech: Where the industry needs to go from here. Retrieved from https://techcrunch.com/2019/06/17/the-future-of-diversity-andinclusion-in-tech/

Garla, S., Hopping, A., Monaco, R, Rittman, S. (2013). What Do Your Consumer Habits Say About Your Health? Using Third-Party Data to Predict Individual Health Risk and Costs. SAS Institute. Retrieved from https://support.sas.com/resources/papers/proceedings13/170-2013.pdf

Eichstaedt, J.C., Smith, R.J., Merchant, R.M., Ungar, L.H., Crutchley, P., Preotiuc-Pietro, D., Asch, D.A., \& Schwartz, H.A. (2018). Facebook language predicts depression in medical records. Proceedings of the National Academy of Sciences of the United States of America, 115, 11203 - 11208.

Hanks, A., Solomon, D., Weller, C. (2018, February 18). Systematic Inequality. Center for American Progress. Retrieved from https://www.americanprogress.org/issues/race/reports/2018/02/21/447051/ systematic-inequality/

Housing and Urban Development (HUD). (2019, August 16). HUD Proposes Revised Disparate Impact Rule. https://www.federalregister.gov/documents/2020/09/24/2020-19887/hudsimplementation-of-the-fair-housing-acts-disparate-impact-standard

Kuhlman, C., Jackson, L., \& Chunara, R. (2020). No Computation without Representation: Avoiding Data and Algorithm Biases through Diversity. Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining.

Lee, I. M., Shiroma, E. J., Kamada, M., Bassett, D. R., Matthews, C. E., \& Buring, J. E. (2019). Association of Step Volume and Intensity With All-Cause Mortality in Older Women. JAMA internal medicine, 179(8), 1105-1112.Advance online publication. https://doi.org/10.1001/ jamainternmed.2019.0899

Li, M. (2020, October 26). To Build Less-Biased AI, Hire a More-Diverse Team. Harvard Business Review. Retrieved from https://hbr.org/2020/10/to-build-less-biased-ai-hire-a-more-diverse-team

Morse, A., Pence, K. (2020). Technological Innovation and Discrimination in Household Finance. https://www.federalreserve.gov/econres/feds/files/2020018pap.pdf

National Association of Insurance Commissioners (NAIC). (Retrieved 2020, May 14). Consumer Glossary. Retrieved from https://content.naic.org/consumer glossary\#I

Nickson, C. (2019, April 9). Randomised Control Trials. Retrieved from https://litfl.com/randomisedcontrol-trials/

Obermeyer, Z., \& Emanuel, E. J. (2016). Predicting the Future - Big Data, Machine Learning, and Clinical Medicine. The New England journal of medicine, 375(13), 1216-1219. https://doi. org/10.1056/NEJMp1606181

O’Sullivan, C. (2020). Interpretable vs Explainable Machine Learning. Retrieved from https:// towardsdatascience.com/interperable-vs-explainable-machine-learning-1fa525e12f48

Repovš, G. (2010). Dealing with Noise in EEG Recording and Data Analysis. Informatica Medica Slovenica, 15(1), 18-25.

Rock, D. \& Grant, H. (2016, November 4). Why Diverse Teams Are Smarter. Harvard Business Review. Retrieved from https://hbr.org/2016/11/why-diverse-teams-are-smarter

Sanchez-Martinez, S., Camara, O., Piella, G., Cikes, M., Ballester, M.A., Miron, M., Vellido, A., Gomez, E., Fraser, A., \& Bijnens, B. (2019). Machine Learning for Clinical Decision-Making: Challenges and Opportunities. Retrieved from https://europepmc.org/article/ppr/ppr 103512

Shmueli, G. (2016). Analyzing Behavioral Big Data: Methodological, Practical, Ethical, and Moral Issues. SSRN, Retrieved from https://ssrn.com/abstract=2736189

Suhara, Y., Xu, Y., \& Pentland, A.S. (2017). DeepMood: Forecasting Depressed Mood Based on SelfReported Histories via Recurrent Neural Networks. Proceedings of the 26th International Conference on World Wide Web. 715-724.

The Info Underground (TIU). (2008, August 7). Type I and Type II Errors - Making Mistakes in the Justice System. Retrieved from http://theinfounderground.com/smf/index.php?topic=1649.0;wap2

Turner Lee, N., Resnick, P., \&Barton, G. (2019, May 22). Algorithmic bias detection and mitigation: Best practices and policies to reduce consumer harms. Brookings Institution, Retrieved from https:// www.brookings.edu/research/algorithmic-bias-detection-and-mitigation-best-practices-and-policiesto-reduce-consumer-harms/

Verma, S. \& Rubin, J. (2018). Fairness Definitions Explained. 2018 ACM/IEEE International Workshop on Software Fairness. Retrieved from http://fairware.cs.umass.edu/papers/Verma.pdf

Wu, X., \& Zhang, X. (2016). Automated Inference on Criminality using Face Images. Retrieved from https://arxiv.org/pdf/1611.04135v1.pdf

Wu, X., \& Zhang, X. (2016). Responses to Critiques on Machine Learning of Criminality Perceptions (Addendum of arXiv:1611.04135). arXiv: Computer Vision and Pattern Recognition.

Yona, G. (2017, October 5). A Gentle Introduction to the Discussion on Algorithmic Fairness. Retrieved from https://towardsdatascience.com/a-gentle-introduction-to-the-discussion-onalgorithmic-fairness-740bbb469b6

Zweifler, J. (2019). Pop Health: From Tipping Health Care in the Right Direction. Retrieved from https://www.drjohnzweifler.com/tipping-health-care

## Appendix A: Recommended Reading

To further your understanding of the concepts discussed in the paper, the Data Science and Analytics Committee has complied reading material for each topic area of the paper.

I. Actuarial Standards of Practice

- ASOP No. 1, Introductory Actuarial Standard of Practice
- ASOP No. 2, Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts
- ASOP No. 7, Analysis of Life, Health, or Property/Casualty Insurer Cash Flows
- ASOP No. 12, Risk Classification (for All Practice Areas)
- ASOP No. 15, Dividends for Individual Participating Life Insurance, Annuities, and Disability

Insurance

- ASOP No. 23, Data Quality
- ASOP No. 41, Actuarial Communications
- ASOP No. 54, Pricing of Life Insurance and Annuity Products

II. Ethics and AI

- Char, D. S., Shah, N. H. \& Magnus, D. Implementing machine learning in health careaddressing ethical challenges. N. Engl. J. Med. 378, 981-983 (2018).
- Chiolero, A. Data are not enough-hurray for causality! Am. J. Public Health 108, 622 (2018).
- European Commission (EC). (2019). Ethical Guidelines for Ethical AI. Retrieved from https://ec.europa.eu/futurium/en/ai-alliance-consultation

$\cdot$ Cowgill, B., Dell'Acqua, F., Deng, S., Hsu, D., Verma, N., \& Chaintreau, A. (2020). Biased

Programmers? Or Biased Data? A Field Experiment in Operationalizing AI Ethics.

Proceedings of the 21st ACM Conference on Economics and Computation.

- Guszcza, J. (2018). Smarter Together: Why artificial intelligence needs human-centered design. Deloitte Insights, Retrieved from https://www2.deloitte.com/us/en/insights/ deloitte-review/issue-22/artificial-intelligence-human-centric-design.html
- Institute of Technological Ethics. (2020). Three kinds of bias in computer systems. Retrieved from https://www.technologicalethics.org/three-kinds-of-bias

$\cdot$ Frankish, K. \& Ramsey, W. (2014)). The Cambridge Handbook of Artificial Intelligence. Cambridge University Press.

- Hao, K. (2020, December 4). We read the paper that forced Timnit Gebru out of Google. Here's what it says.. MIT Technology Review. Retrieved from https://www. technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-outtimnit-gebru/

III. Veracity Modeling That Changes the Application Process

- Gianfrancesco, M. A., Tamang, S., Yazdany, J. \& Schmajuk, G. Potential biases in machine learning algorithms using electronic health record data. JAMA Intern. Med. 178, 15441547 (2018) https://mashupmd.com/potential-biases-in-machine-learning-algorithmsusing-electronic-health-record-data/

$\cdot$ Kuhlman, C., Jackson, L., \& Chunara, R. (2020). No Computation without Representation: Avoiding Data and Algorithm Biases through Diversity. Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining. - Larson, Anders. December 2016. "Creating a useful training data set for predictive modeling," SOA Predictive Analytics and Futurism Section Newsletter, Issue 14, pp. 32-34.

- Sanders, N. (2019). A Balanced Perspective on Prediction and Inference for Data Science in Industry. Harvard Data Science Review, 1(1). https://doi.org/10.1162/99608f92.644ef4a4 - Sgaier, S., Huang, V. \& Charles, G. (2020). The Case for Causal AI. Stanford Social Innovation Review. Retrieved from https://ssir.org/articles/entry/the case for causal ai - Rud, Olivia Parr 2001. Data Mining Cookbook: Modeling Data for Marketing, Risk, and Customer Relationship Management. New York: John Wiley \& Sons.

V. Assessing Sources of Nontraditional Data to Improve Consumer Experience

- Cai, L., Zhu, Y. (2015). The challenges of data quality and data quality assessment in the big data era. Data Sci. J. 14. https://datascience.codata.org/articles/10.5334/dsj-2015-002/ - Tyree, P. T., Lind, B. K., \& Lafferty, W. E. (2006). Challenges of using medical insurance claims data for utilization analysis. American journal of medical quality: the official journal of the American College of Medical Quality, 21(4), 269-275.

VI. Controlling for Systemic Influences and Socioeconomics

$\cdot$ Angwin, J., Larson, J., Mattu, S., \& Kirchner, L. (2016, May 23). Machine Bias. ProPublica. Retrieved from https://www.propublica.org/article/machine-bias-risk-assessments-incriminal-sentencing

$\cdot$ Buolamwini, J. (2018, February 9). Gender Shades. [YouTube Video]. Retrieved from https://www.youtube.com/watch?v=TWWsW1w-BVo\&ab channel=MITMediaLab $\cdot$ Eubanks, V. (2018) Automating Inequality. St. Martin's Press.

- Noble, S.U. (2018). Algorithms of Oppression - How Search Engines Reinforce Racism. NYU Press.

$\cdot$ West, S.M., Whittaker, M. \& Crawford, K. (2019). Discriminating Systems: Gender, Race and Power in AI. AI Now Institute. Retrieved from https://ainowinstitute.org/ discriminatingsystems.html

- Rogers, T. (Retrieved 2020, December 27). Type I and Type II Errors - Making Mistakes in the Justice System. Retrieved from http://intuitor.com/statistics/T1T2Errors.html
- Krishnamurthy, P. (2019, September 11). Understanding Data Bias. Retrieved from https:// towardsdatascience.com/survey-d4f168791e57

VII. Evaluating Nontraditional Data for Actuarial Use with Regulatory Collaboration - Kosten, S. (2020. June 15). What is Third-Party Risk Assessment and How Can You Do It? Towards Data Science. Retrieved from https://towardsdatascience.com/what-is-third-partyrisk-assessment-and-how-can-you-do-it-ef3c69a6e0ce

- Guiral, P. West, B. \& Padreres, A. (2019). Third-Party Data Providers: Transforming Client Experience and Data Quality. Accenture. Retrieved from https://www.accenture.com/ acnmedia/pdf-109/accenture-third-party-data-providers-transform-client-experiencedata-quality.pdf
- Deloitte. (2019, April 22). How Third-Party Information Can Enhance Data Analytics. Harvard Business Review. Retrieved from https://hbr.org/sponsored/2019/04/how-thirdparty-information-can-enhance-data-analytics
- Heale, B. (2014). Data Quality is the Biggest Challenge. Moody's Analytics. Retrieved from https://www.moodysanalytics.com/risk-perspectives-magazine/managing-insurance-risk/ insurance-regulatory-spotlight/data-quality-is-the-biggest-challenge European Commission (EC). (). Handbook on Data Quality Assessment Methods and Tools. Retrieved from https://unstats.un.org/unsd/dnss/docs-nqaf/EurostatHANDBOOK\ ON\ DATA\ QUALITY\ ASSESSMENT\ METHODS\  AND\%20TOOLS\%20\%20I.pdf

VIII. Regulatory Concerns Impacting the Work of the Actuary - American Academy of Actuaries. (In Press). Self-Regulation and the Actuarial Profession. Committee of Professional Responsibility. American Academy of Actuaries. Washington, D.C.

- American Academy of Actuaries. (2018). Big Data and The Role of The Actuary. Retrieved from https://www.actuary.org/sites/default/files/files/publications/ BigDataAndTheRoleOfTheActuary.pdf

IX. Transformational Impacts of Big Data and AI on the Future of Insurance and Society - Beam, A. L. \& Kohane, I. S. Big data and machine learning in health care. JAMA 319, $1317-1318(2018)$

- Miller, D. D. \& Brown, E. W. Artificial intelligence in medical practice: the question to the answer?. Am. J. Med. 131, 129-133 (2018).
- Chen, R. \& Snyder, M. Promise of personalized omics to precision medicine. Wiley Inter. Rev. Syst. Biol. Med. 5, 73-82 (2013).
- Obermeyer, Z., \& Emanuel, E. J. (2016). Predicting the Future - Big Data, Machine Learning, and Clinical Medicine. The New England journal of medicine, 375(13), 12161219. https://doi.org/10.1056/NEJMp1606181


## A

AMERICAN ACADEMy of ACTUARIES

Objective. Independent. Effective. ${ }^{\text {rn }}$

AMERICAN ACADEMY OF ACTUARIES

1850 M STREET NW, SUITE 300, WASHINGTON, D.C. 20036 202-223-8196 | ACTUARY.ORG


[^0]:    6 "Adverse selection"; Farlex Financial Dictionary; 2012.

    7 "What is artificial intelligence?"; Computer World; April 10, 2015.

    8 "Smarter together: Why artificial intelligence needs human-centered design"; Deloitte Review; Jan. 22, 2018.

    9 "Algorithms, A.I. and Insurance: Promise and Peril"; Insurance Information Institute; Dec. 12, 2019.

    10 Access to health care in America; National Academy Press; 1993.

    11 "Algorithmic Decision Making and the Cost of Fairness," Proceedings of the 23 rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining; 2017.

[^1]:    32 Big Data and the Role of the Actuary; American Academy of Actuaries; June 2018.

    33 Natural language processing (NLP) refers to the branch of computer science-and more specifically, the branch of artificial intelligence or AI-concerned with giving computers the ability to understand text and spoken words in much the same way human beings can. https:// www.ibm.com/cloud/learn/natural-language-processing

    34 The analysis of the polarity of text, which can be positive, negative, or neutral. "A Deep Learning Semantic Approach to Emotion Recognition Using the IBM Watson Bluemix Alchemy Language"; ICCSA; 2017.

[^2]:    39 Chu, R., Duling, D., Thompson, W. (2007). Best Practices for Managing Predictive Models in a Production Environment. SAS Institute "Inc. Retrieved from Best Practices for Managing Predictive Models in a Production Environment. 40 “Predictive Model Building 101”; SOA Predictive Analytics and Futurism Newsletter; 2017.

[^3]:    45 "What Do Your Consumer Habits Say About Your Health? Using Third-Party Data to Predict Individual Health Risk and Costs"; SAS Institute; 2013 46 Ibid.

[^4]:    47 "The Role of Wearables in Private Medical Insurance"; Milliman; 2020

    48 "Health Insurers Are Vacuuming Up Details About You—And It Could Raise Your Rates"; ProPublica; July 17, 2018. 49 Ibid.

[^5]:    78 “Usage-Based Insurance: Savings vs. Privacy"; Value Penguin; Aug. 23, 2021.

    80 Examples of such can be found in "Technological Innovation and Discrimination in Household Finance," U.S. Federal Reserve; Finance and Economics Discussion Series; 2020.

[^6]:    82 "Technological Innovation and Discrimination in Household Finance"; op. cit.

    83 "A computer program used for bail and sentencing decisions was labeled biased against blacks. It's actually not that clear";

    The Washington Post; October 17, 2016.

    84 "Type I and Type II Errors-Making Mistakes in the Justice System"; The Info Underground; Aug. 7, 2008.

    85 Ibid.

[^7]:    96 "How Predictive Modeling Has Revolutionized Insurance"; Insurance Journal; June 18, 2012. 97 "What is precision medicine?"; Medline Plus; Sept. 22, 2020.

    98 "Putting the data before the algorithm in big data addressing personalized healthcare". NPJ Digital Medicine; 2019.

    99 "Machine Learning for Clinical Decision-Making: Challenges and Opportunities"; Europe PMC; 2019.

    100 "Dealing with Noise in EEG Recording and Data Analysis"; Informatica Medica Slovenica; 2010

    101 "Machine Learning for Clinical Decision-Making: Challenges and Opportunities"; op. cit.

