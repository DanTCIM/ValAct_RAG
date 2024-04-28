# Model Governance
Some Considerations for Practicing Life Actuaries

A PUBLIC POLICY PRACTICE NOTE 

April 2017

Developed by the Model Governance Practice Note Work Group of the American Academy of Actuaries

## Model Governance

Some Considerations for Practicing Life Actuaries

Developed by the Model Governance Practice Note Work Group of the American Academy of Actuaries

The American Academy of Actuaries is a 19,000-member professional association whose mission is to serve the public and the U.S. actuarial profession. For more than 50 years, the Academy has assisted public policymakers on all levels by providing leadership, objective expertise, and actuarial advice on risk and financial security issues. The Academy also sets qualification, practice, and professionalism standards for actuaries in the United States.

## Model Governance Practice Note

This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement as to what constitutes generally accepted practice in the area under discussion. Events occurring subsequent to this publication of the practice note may make the practices described in this practice note irrelevant or obsolete.

We welcome comments and questions. Please send comments to lifeanalyst@actuary.org.

Principle-Based Reserve Model Governance Practice Note Work Group

Nadeem Chowdhury, MAAA, FSA, Chairperson

Michael Boerner, MAAA, ASA

Brandon J. Dwyer, MAAA, FSA

Jason E. Kehrberg, MAAA, FSA

Chanho Lee, MAAA, FSA
Arthur V. Panighetti, MAAA, FSA

Richard L. Sutton, MAAA, FSA

Christopher A. Wheeler, MAAA, FSA

Amanda E. Young, MAAA, FSA, CPA

TABLE OF CONTENTS

0. INTRODUCTION ..... 4
1. Model ..... 4
2. Model Development ..... 5
3. Model Governance Policy and Standards ..... 7
4. Model Risk ..... 7
5. Model Governance ..... 8
6. Model Processes and Controls ..... 10
7. Model Validation ..... 11
8. Model Documentation ..... 14
9. Principle-Based Reserve Model Governance
10. Considerations ..... 15
11. DEFINITIONS ..... 16

## INTRODUCTION

The purpose of this practice note is to provide a source of information to practicing life actuaries seeking to better understand models, model risks, model governance, and related issues as these actuaries implement and oversee principle-based reserving (PBR). Because PBR for life insurance is new and model governance is an emerging area, this practice note was not developed from a survey of current actuarial practices. The practices described in this document represent the approaches of a range of actuaries in industry, the regulatory community, and supporting organizations who are knowledgeable about models, model governance, and PBR. This practice note covers only certain approaches within the known or anticipated range of practices. There are, or may be, other methods that are being used, or that will emerge, in practice. It also should be noted that this practice note refers to the Valuation Manual adopted on November 22, 2015; the third exposure draft of an actuarial standard of practice (ASOP), Modeling (exposure draft dated June 2016); and the second exposure draft of the pending ASOP, Principle-Based Reserves for Life Products (exposure draft dated June 2014). ${ }^{1}$ To the extent that the final versions of the ASOPs differ from these drafts, this practice note will be subject to updating to address life products.

An additional resource for practicing life actuaries involved in actuarial model governance is the Academy's Model Governance Checklist. This checklist represents model governance practices that many life actuaries and their companies would aspire to, but may or may not be applicable to all situations, as model governance is a complex and evolving process specific to a company's modeling environment.

## 1. Model

Q1.1: What is a model?

A: The third exposure draft (dated June 2016) of the ASOP Modeling defines a model to be "[a] simplified representation of relationships among real world variables, entities, or events using statistical, financial, economic, mathematical, or scientific concepts and equations. Models are used to help explain a system, to study the effects of different parts of a system, and to derive estimates and guide decisions.” The exposure draft observes that a model evolves through a life cycle as follows: (1) a specification phase, (2) an implementation phase, and (3) a production phase that consists of one or more model runs. ${ }^{2}$

Q1.2: What are some of the purposes models can serve?

A: Actuaries create and use models for a variety of purposes. Common examples of processes in which models are used include:
- Product pricing and risk segmentation;
- Business planning;
- Assumption development;[^0]- Cash flow testing analysis;
- Financial reporting;
- Appraisals of insurance businesses;
- Asset adequacy analysis;
- Life insurance illustrations;
- Risk evaluations; and
- Reserve calculations.

Q1.3: What are some of the decisions that can be influenced through the use of models?

A: Models constitute a significant component of many processes. Models may have an impact on decisions that a company makes. Examples of such decisions include:

- Setting the appropriate level of reserves a company should hold to fulfill its obligations, particularly with respect to those calculated under PBR;
- Setting the rates to charge for new business;
- Targeting specific products to sell;
- Exiting the market for certain products;
- Management of the in-force business, including the current premiums, cost of insurance (COIs), credited rates, dividend scales, and replacement programs;
- Incorporating risk mitigation such as reinsurance agreements; and
- Management of capital resources.

Q1.4: What can happen if a model produces materially incorrect output or is interpreted incorrectly?

A: Because models may influence decisions that a company makes, the model outputs may have a substantial and lasting impact on business financial results and even the viability of corporations. For example, a model that produces materially incorrect output or that is interpreted incorrectly could affect the profitability of the company, impact the ability to pay benefits promised to consumers, or even threaten the solvency of the company. Additionally, there is potential for damage to the company's reputation, which could affect the manner in which the company conducts its business.

## 2. Model Development

Q2.1: What are some of the high-level steps that might be taken in the model development process?

A: The following are some high-level steps that some actuaries may consider as part of model development:

- Define and develop specifications for the model;
- Develop or modify code/program the model;
- Test/validate the model;
- Approve the model for implementation; and
- Validate that controls are in place and documentation is complete.

Q2.2: What typically is the actuary's role in the model development and use process?

A: Some actuaries may be more involved with models than other actuaries. In some cases, the actuary is the model developer who is responsible for designing, constructing, and maintaining the model. In other cases, the actuary is the model steward, primarily responsible for managing the development and governance of the model. Some actuaries may be primarily model users, a role that requires adequate knowledge of the underlying business and of the model being used to analyze that business. Some actuaries may be model
reviewers, a role that is distinct from that of the person who developed the model; a model reviewer would usually possess adequate knowledge and expertise regarding the model and its uses. An actuary may have multiple roles for a single model; for example, being both model developer and model user. See the definitions section for a further discussion of the various model roles.

Q2.3: What does the recent Modeling ASOP exposure say about the model development process?

A: Following is a list of key items described in the Modeling ASOP exposure draft and ASOP No. 41, Actuarial Communications, for both internally and externally developed models.

- Conceptual Framework-Section 3.6 of the Modeling ASOP exposure draft states (in part): "When the actuary presents the results of the model, the actuary should explain methodology, key assumptions and parameters..." Also, Section 3.8 of the exposure states (in part): "For model results used in actuarial communications, the actuary should document the nature of the data used, and material assumptions and parameters used in the model..." Some actuaries would include the design, theory, and logic underlying the model in such a presentation and related documentation.
- Intended Purpose-Section 3.6.2 of the Modeling ASOP exposure draft states: "In actuarial reports that include information derived from models, the actuary should consider including explanations of ... the intended purpose of the models and how the user's needs are addressed by those models..." Some actuaries would include a clear statement of purpose to ensure that the model development is aligned with its intended purpose. Some actuaries would also include a statement about any purposes for which the model is not appropriate.
- Potential Limitations of the Model-Section 3.6.1(a) and (b) of the Modeling ASOP exposure draft states: "In actuarial reports that include information derived from models, the actuary should include explanations ... if applicable[,] ... [of] the extent to which a model fails to fulfill its intended purpose, due to limited information, time constraints, or other practical consideration; and ... any other known material limitations of the models that have been used and the implications of those limitations."
- Calculations and Programming Code-Section 3.2 of ASOP No. 41 states: "In the actuarial report, the actuary should state the actuarial findings, and identify the methods, procedures, assumptions, and data used by the actuary with sufficient clarity that another actuary qualified in the same practice area could make an objective appraisal of the reasonableness of the actuary's work as presented in the actuarial report." In light of Section 3.2, some actuaries consider documenting the calculations and programming code over which they have control or responsibility. The extent of documentation would differ depending on whether they are using purchased software or a homegrown system. In the case of purchased software (externally developed), some actuaries consider requesting documentation of the calculations or code to support reliance on the purchased software. When documentation is limited due to proprietary reasons, some actuaries incorporate additional internal documentation for model governance purposes.
- Appropriate Governance and Controls-Section 3.5.2 of the Modeling ASOP exposure draft states: "The actuary should use or, if appropriate, rely on others to use appropriate governance and controls to minimize model risk, to maintain the integrity of the model, and to avoid the introduction or use of unintentional or untested changes." Some actuaries would establish, or rely on others to establish, and then document items such as the following:
o Roles \& Responsibilities-Define and document responsibilities for various roles in the governance of the model;

o Document Access Controls-Processes for limiting access through access authorization and periodic access review;

o State Change Control Procedures-Processes for authorizing changes to the model, reviewing and testing those changes, and where appropriate implementing system controls to segregate the testing and production environments;

o Document Model Review Process-Process for reviewing and documenting various validation activities; and

o Model Review Sign-off-Maintain sign-off documentation for model review.

## 3. Model Governance Policy and Standards

Q3.1: What model governance policies and standards apply to actuaries?

A: Policy and standards are set by both enterprises and professional bodies. A company could adopt and require adherence to policy and standards as part of its model governance framework.

Enterprise standards can address process, ownership, controls, and documentation requirements. These could include model risk classification processes and model validation requirements, model change management testing requirements, and model coding standards. Enterprise standards may be adopted by a body with oversight responsibilities, such as a model governance steering committee.

Professional standards include actuarial standards of practice promulgated by the Actuarial Standards Board.

Actuaries typically are expected to follow enterprise policies and standards, and are required to follow professional standards, in performing their work. In addition, Annotation 3.2 of the Code of Professional Conduct states: "Where a question arises with regard to the applicability of a standard of practice, or where no applicable standard exists, an Actuary shall utilize professional judgment, taking into account generally accepted actuarial principles and practices."

## 4. Model Risk

## Q4.1: What is model risk?

A: Section 2.9 of the Modeling ASOP exposure draft defines model risk as " $[t]$ he risk of adverse consequences resulting from reliance on a model that does not adequately represent that which is being modeled or that is misused or misinterpreted." Some of the adverse consequences of model risk include restatements of published financial statements, poor experience relative to pricing expectations, and faulty strategic decisions from planning models. A comprehensive list of model risk and its potential adverse consequences is beyond the scope of this practice note.

Q4.2: Why is model risk measured? How is a model risk ranking typically used?

A: The impact of model risk may be estimated and measured (scored) to provide the actuary with information to make better decisions as to items such as:

- The appropriateness of model use- "fit for purpose";
- The frequency and depth of model reviews;
- The level of approval for new model development or when an old model is (substantially) revised; and
- The composition of a model review team.

For each model in the scope of the organization's model governance policy, some actuaries choose to develop a profile that evaluates and measures each of the significant model risks (such as financial statement errors, reputational risks, pricing errors, etc.). Some actuaries also choose to determine a summary aggregation of the model risks for each model. In deriving their summary aggregations, some actuaries apply risk severity judgment (relative ranking of the risk factors) to get a model risk score for the model.

Some actuaries use model risk ranking to drive decision and review priorities. Model risk ranking is a practice that may be defined in the company's model governance policy as an overall component of managing the enterprise model risk.

Q4.3: What are some key risk components that actuaries might consider in estimating model's risk?

A: Among the risk characteristics of model design that are typically considered are:

- Financial impact;
- Regulatory, reputational, and operational impacts;
- Complexity of data and assumptions utilized;
- Complexity of the calculation engine;
- Complexity of the overall process, intuitiveness/transparency; and
- Level of expertise/experience of the model developer and user.

Q4.4: How is model risk defined and profiled?

A: Actuaries typically use their professional judgment when establishing and maintaining a model's risk profile, and typically find that the level of judgment may increase with the level of model complexity. Actuaries' exercise of professional judgment is often informed by consideration of whether reliance on others, peer reviews, and reasonableness testing are appropriate.

Q4.5: What factors determine when to update the individual model's risk profile and overall model risk ranking?

A: A properly developed model governance policy (see next section) may address the frequency of updates to individual model risk profiles and the overall model risk ranking. The policy will likely update the model's risk profile more often for those models with the highest risk ranking scores. Significant changes to a model may also result in a review and possible update to the ranking. The company's plan for model reviews is also likely to be based on the overall risk ranking update. It is possible that regulatory requirements, such as those recently adopted in the NAIC's Valuation Manual, may mandate the timing of model risk profile and direct more frequent overall risk ranking updates than the company's model governance policy would call for.

## 5. Model Governance

Q5.1: What approaches typically are used to align resources with roles and associated responsibilities to address the needs of model governance?

A: Robust model governance may involve a number of activities. Some companies consider that a clear definition of roles and responsibilities may provide assurance that governance needs will be addressed. These roles and responsibilities often include:
o The initial development and validation of new models;

o Documentation of models and processes;

o Risk assessment of models for classification for determining frequency and level of periodic model validation;

o Model change management with robust validation and promotion of changes;

o Updates to production models, and the updating and running of production models to generate results; and

o Peer review of models, adoption of a model governance policy and standards, and oversight and monitoring compliance with standards.

Some companies designate their model developers as owners of their respective models with responsibility for initial development, risk assessments, model validation, change management, and generating model results.

To address the need for segregation of duties for some of these activities to separate the performance of activities from the approval of results, some companies recognize, and assign to an individual, the role of model steward (see Q5.2).

To provide oversight, some companies establish a steering committee to set policy and monitor compliance with model governance policy. Some companies confer on an internal auditor a key role in monitoring and reporting on compliance.

Q5.2: What is a model steward? What are the potential responsibilities of a model steward?

A: A model steward could help to ensure modeling best practices related to documentation, validation, and governance. The role of model steward can provide a segregation of duties between the activities connected with the initial model and the subsequent activities associated with model and system updates, change control management testing, and validation of these models.

The responsibilities of a model steward could include approval of new models and model changes for promotion to the production environment. Maintenance of testing, quality assurance, and production environments are also potential responsibilities of a model steward.

Q5.3: What are the pros and cons of a centralized versus a decentralized structure to meet the needs of a robust model governance framework?

A: Establishing a model governance framework can involve a significant commitment of resources and associated costs. Companies commonly consider the balance between the need for controls with competing priorities and the ability to allocate resources to meet changing priorities. A key decision in setting this framework may be whether the need for governance activities can best be met by a centralized modeling unit or whether these activities can be addressed by resources existing within individual actuarial functional areas. Actuaries are in a position to assist management in deciding the approach best suited for their companies. The decision may be particularly important for small companies challenged by limited resources.

Some actuaries believe a centralized modeling unit has the advantage that resources committed to model governance activities are less likely to be pulled away for competing priorities. These actuaries believe a centralized unit can be staffed with individuals possessing unique skills best suited for model governance roles and responsibilities. Other actuaries believe expertise with the existing models could reside with individuals within the functional areas, in consideration of the fact that knowledge transfer to a centralized
unit involves a time and resource commitment. Actuaries commonly believe that both approaches could be successful and that the decision on how best to address model governance needs will depend on the company's own situation.

Q5.4: What are the approaches companies might consider to align responsibilities to promote a successful model governance framework and defend themselves against the risk of ineffective implementation of controls?

A: One approach is the "three lines of defense model," which has evolved as an approach designed to enhance communications and provide added controls by clarifying roles and responsibilities.

Under one example of this approach, the first line of defense could reside within operating or business units, with responsibility being put on line management for the effective management of model risk through the design and maintenance of controls.

The second line of defense under this example could consist of individuals or areas responsible for providing assurances of the effectiveness of controls through monitoring the design and performance of those controls.

The third line of defense under this example could involve individuals or areas responsible for independent assurance and could include internal audit, external auditors, regulators, and possibly other internal resources that are independent of the models, but that provide peer review and possibly monitoring of compliance with enterprise policies and standards and professional standards.

## 6. Model Processes and Controls

Q6.1: What processes and controls might actuaries consider employing to ensure that model inputs are complete, accurate, and consistent?

A: Some actuaries believe the validation of model results for updates to inputs can provide assurance that inputs are accurate. Updates of inputs can include updates to policy inforce and investment data, economic parameters, as well as methods and assumptions. Some actuaries choose to establish expectations prior to an update by estimating impacts to model results because they believe doing so can assist in evaluating the reasonableness of results. Some actuaries choose to compare results to expectations and reconciliation to results generated from other models because they consider that these exercises can provide added assurance that updates to the model inputs are accurate. Among the additional testing procedures that some actuaries employ are inventory control checks, back-testing, visual inspection, attribution, and waterfall analysis.

Some actuaries choose to employ automated processes for inputting data to models, which provide automated verification with established controls, because they believe that these tools may provide further assurance of completeness and accuracy. Finally, some actuaries look to peer review as potentially adding yet another layer of control.

Q6.2: What practices might be employed in the development and governance of model assumptions?

A: Some companies believe that controls around the development, approval, and input of assumptions into models can reduce model risk. Companies may use a schedule or calendar of reviews of assumptions based on updated experience studies to help to assure that assumptions are based on current relevant data. For these companies, a defined approval process can involve all participants in the modeling process with a vested interest to see that they have a voice in setting assumptions. Some companies find that establishing a centralized location (an assumptions repository) for storage of assumptions can aid in creating consistency of assumptions across models, where consistency is appropriate, and can establish a source for approved
assumptions for model stewards and others involved in the process and as a source for automated processes to access and load assumptions to models. To assure that assumptions are accurately loaded to models, inspection, reasonableness checks, and peer review are often employed as validation procedures.

Q6.3: What processes and controls might actuaries consider employing to ensure that model outputs are complete, accurate, and consistent from output generation through to accounting entry, reporting, and analysis?

A: In some companies' experience, processes to report and analyze model results once these results are generated for purposes of financial reporting, as well for as other purposes, can potentially compromise the accuracy of those results without adequate controls. Often, these processes involve spreadsheets that do not employ the same level of rigorous controls as do the models themselves. Some companies have found benefit in automated processes for data warehousing model output in a structured format that facilitates analysis with drill-down capabilities, finding that such processes can enhance reporting and analytical capabilities. Spreadsheet controls to track spreadsheet data and formula changes together with version control can provide an added level of assurance. Spreadsheets can be viewed as an integral part of the reporting process and could be subject to the same level of rigorous change control as the models themselves.

## 7. Model Validation

## Q7.1: What is model validation?

A: Model validation is part of model risk management and quality control and is the practice of performing an independent challenge and thorough assessment of the reasonableness and adequacy of a model based on peer review and testing across multiple dimensions including design, data, assumptions, results, and governance. The assessment provides internal and external users of model results with a level of assurance that the model is fit for purpose and is performing as expected across a range of scenarios with limitations properly documented, is consistent with other internal and external models, and is in line with design objectives, regulations, enterprise standards, ASOPs, and industry practice.

Some of the testing procedures used by model validation teams to independently assess models may also be used elsewhere in the company to check and gain comfort with models; e.g., model development teams may use the procedures as they build out models, and model production teams may use the same procedures as they put models to use.

Q7.2: What is the scope and frequency of model validation?

A: The scope of model validation refers to the depth and breadth of reviews and testing performed on various areas of the model as part of the validation exercise. It often varies with the riskiness of the model (see Q4.2). Riskier models would generally have a larger scope for validation, more robust in number and severity of validation tests across all areas of the model. Examples of riskier models may include highimpact models relied upon for strategic planning or financial statements, complex in-house models with many lines of code, and/or new models. Model validation scope can also vary with other model characteristics besides risk rating, such as model type. Specialized economic scenario generators may have their own unique tests and reviews as part of their validation. Regression-based predictive models may require a different set of tests and reviews than non-regression-based cash flow models.

The frequency of model validation also often varies with the riskiness of the model, with riskier models subject to more frequent validation tests. Companies and their actuaries typically consider the frequency of external audits and regulatory reviews when determining the frequency of model validation. Some
companies may embed elements of validation in the modeling process itself, with updated validation reports produced on an ongoing basis. Other companies may conduct a big review every year or two, with selected less intensive validation checks and controls performed on certain areas of the model as part of every model run. Additional validation tests commonly are triggered upon failure of one or more model controls, or by a material change to the model or its assumptions. Some actuaries believe that validation is valuable even in the absence of changes to the model to confirm identical model results. Regardless of model validation frequency, it is widely acknowledged that scheduling model validations well in advance, due to the extra work required, is important.

Because the scope and frequency of model validation are often based on risk rating, model type, and other model classifications, some actuaries find that it is beneficial to have a thorough model classification scheme to methodically identify models according to their characteristics. For example, models can be classified according to risk rating (high, medium, low), model type (cash flow, regression), model purpose (valuation, pricing, RBC), accounting method (GAAP, stat, tax, IFRS), product type (life, annuity, health), etc. Some companies may have model validation team members involved with periodically reviewing the company's model classification schemes to ensure they support model validation work.

## Q7.3: What types of reviews and testing procedures are available for use in model validation?

A: Numerous types of reviews and testing procedures are available to independently challenge and assess the model. The validation scope documentation will often list review and testing procedures used for each dimension of the model. Results of validation reviews and tests typically would be documented. Some model validation teams will also make note of areas where the model could be improved.

Examples of reviews and testing procedures:

- Design Use/Fit - What is the model used for and is it fit for purpose? Reviews may include going over the business requirements for the model and having discussions with the model design team.
- Design Methods/Processing — Are the model's methods and processing appropriate, compliant, and best or accepted practice? Reviews often include evaluating model design documentation and model code and having discussions with the model implementation and change teams. Results of unit and regression testing of the model are often reviewed. The model validation team can also make comparisons of the model's methods and processing against regulatory requirements in the Valuation Manual, enterprise standards, industry practice, and technical literature.
- Data-Is the data accurate, timely, reliable, consistent, and complete, with outliers identified? Reviews often start with the model's data dictionary and other model data documentation. The validation team can also look at the treatment and storage of data over time and across models. Extracts and pre-modeling logic can be evaluated, such as ETL (extract-transform-load) processes, plan code mapping, compression, and the use of prior-date business data. It can also be useful to review data control totals and other data controls tying inputs to outputs.
- Assumptions-Have the assumptions been correctly loaded and are they accurate, consistent, and in line with enterprise standards, ASOPs, and industry practice? Do PBR assumptions meet the regulatory requirements outlined in the Valuation Manual? Reviews often start by with the model's assumption documentation. Assumption loading processes and controls can also be checked.

Validation teams can also do calibration tests and compare assumptions over time, across models, against industry practice, and to observable reference points. Some validation teams may have discussions with subject matter experts when assumptions incorporate expert judgment due to lack of credible data.

- Actual Results-How do actual model results compare to similar models, and can the model effectively make predictions? Benchmarking and replication are used by some actuaries, including static validation, parallel testing against other models, and spreadsheet replicas. Another common tool is outcome analysis, including dynamic validation, back-testing, and out-of-sample testing.
- Sound/Stable Results-Are model results sound and stable across a range of use and scenarios? Results of any scenario, stress, sensitivity, or extreme value testing can be reviewed, and additional tests may be performed. In some cases, validation teams may look into certain dependencies and correlations. Results across different levels of input granularity are sometimes looked at. In addition, aggregation benefits across different levels of results aggregation may be studied. Aggregation methods may be reviewed for appropriateness and to gauge the sensitivity of results to the method and level of aggregation.
- Results Communication-Are model results useful and understood by those using them? Some model validation teams may have discussions with internal users of model results to determine whether results are timely and relevant to their needs, and whether there is enough training and documentation for them to understand the results. PBR reports going to regulators need to meet VM31's PBR Actuarial Report requirements and document adherence to VM-G's guidance for corporate governance.
- Governance-Is the model and its use and development appropriately documented and governed? Model documentation should be complete, in compliance with regulatory requirements and ASOPs, in line with enterprise standards, and consistent with other models. Controls and signoffs can be reviewed to ensure model change procedures were followed and model production processes were properly executed. Roles and responsibilities related to the model can be reviewed to ensure there is sufficient security and separation of duties.


## Q7.4: What are the key parts of a typical model validation plan?

A: The model validation plan typically lists the model to validate, the person (or functional title of) who will conduct the validation, when the validation is to occur, and the scope of the validation. Validation plans may vary with the model classification. When developing a model validation plan, some actuaries find it helpful to refer to a plan from a prior validation or from a model with a similar model classification. Model governance policies and enterprise standards can also inform the development of a model validation plan.

Some companies may have a centralized model validation team responsible for validating all the company's models. Other companies may assign the validation to staff as available. In either case those performing model validation would usually be independent from those developing and using the model. The level of detail in the plan's scope can vary. Some plans may describe the general depth and breadth of reviews and testing to be performed. Other plans may list out individual reviews and tests along with how to perform them, while allowing for some flexibility to adapt as necessary over the course of the validation.

Some model validation plans may also include guidance on what should be included in the validation report and how it should be disseminated. The validation report will generally state the validation team's overall assessment of the model, identifying the model's intended use and whether or not it is fit for that purpose. Documentation for the assessment provided in the report can include a copy of the model validation plan, results of reviews and tests performed, and demonstration that the validation was independent and thorough. Some validation reports will also highlight key assumptions, limitations, and improvement opportunities for the model.

Q7.5: How do actuaries typically view the relationship between model validation and model governance?

A: A documented model governance framework will often formally establish enterprise standards for the process, ownership, controls, and documentation requirements necessary to ensure consistent model execution. Some actuaries consider it desirable to have this framework in place prior to performing a model validation, believing that the structure and oversight may not only ease model validation work, but may also increase the likelihood the model is judged fit for purpose and given a positive assessment by the validation team. The scope of model validation is often based on model classification schemes formalized in model governance frameworks. Some model governance frameworks will speak directly to model validation, establishing guiding principles for all validations performed on the company's models. Model governance frameworks, in the views of many actuaries, may also help establish the independence, incentives, influence, and authority the model validation team will need to effectively challenge the company's models, effecting change if necessary.

## 8. Model Documentation

Q8.1: What is usually documented as part of effective model risk management?

A: The documentation could include:

- A description of the model and its intended purpose, including modeling platform, inputs, and outputs;
- Process maps identifying key controls and data handoff points;
- Process(es) used to update model data;
- Assumptions and methodologies;
- Limitations and risks not modeled;
- Approximations and shortcuts;
- Applicable vendor or third-party documentation and rationale for the selection of options where options exist; and
- Data output and reports.

Q8.2: What are the reasons actuaries typically offer for documenting the intended purpose of a model?

A: Knowing the intended purpose of a model may be helpful in developing the choice of reasonable assumptions and in determination of appropriate margins to be used within the model. The intended purpose may also assist in developing the controls and governance for the model. Although it is not binding on actuaries, Section 3.4.2 of the Modeling ASOP exposure draft states, "In actuarial reports that include information derived from models, the actuary should consider including explanations of ... the intended purpose of the models and how the intended user's needs are addressed by those models..."

## Q8.3: What level of detail is typically provided in documentation?

A: The level of risk being modeled is typically a key factor in the level of detail chosen for the documentation. The level of detail may also be affected by the intended audience. Technical documentation used to run the model by another actuary will likely be more detailed than a summary for senior management. Similarly, detail for internal or external auditors may be more granular than that required by regulators.

Q8.4: Do actuaries typically repeat/prepare certain documentation for different audiences (e.g., model reviewer, senior management, etc.)?

A: Some actuaries find that certain documentation is appropriate for multiple audiences, while other documentation is audience-specific. When issuing actuarial communications, actuaries are guided by Section 3.1.1 of ASOP No. 41, which states, "The actuary should take appropriate steps to ensure that the form and content of each actuarial communication are appropriate to the particular circumstances, taking into account the intended users."

## 9. Principle-Based Reserve Model Governance Considerations

## Q9.1: What are some examples of a model in a PBR environment?

A: The stochastic reserve methodology and deterministic reserve methodology for life insurance reserves are examples of models in a PBR environment. The Stochastic Reserve Exclusion Test (SET) and margin determination could use models in the PBR process.

Q9.2: What legal documents, guidance, and reference materials might actuaries look to for building and maintaining a model in compliance with PBR requirements?

A: Following are some of the sources of information and reference materials that actuaries typically consult when building a model (please note that the VM-xx below refers to sections of the Valuation Manual):

- Section VM-20 of the Valuation Manual describes the requirements for stochastic and deterministic models for life insurance products;
- Section VM-G of the Valuation Manual provides guidance for governance and controls for PBR models;
- Section VM-21 of the Valuation Manual describes the requirements for variable annuity products;
- ASOP exposure draft, Principle-Based Reserves for Life Products (exposure draft dated June 2015);
- ASOP exposure draft, Modeling (exposure draft dated June 2016);
- Draft VM-20 practice note (expected release in 2017);
- The Federal Reserve System’s Model Risk Management Documents; and
- Actuarial Modeling Controls, a research report sponsored by the Society of Actuaries (published December 2012).

Q9.3: What ASOPs appear to apply to model development for PBR purposes?

A: According to VM-20, Section 7.A.1, "The company shall design and use a cash flow model that, among other requirements, complies with applicable Actuarial Standards of Practice in developing cash flow models and projecting cash flows." While each actuary is ultimately responsible for determining which ASOPs are applicable to a specific task, and the Academy's Council on Professionalism also publishes Applicability Guidelines that may be useful in determining those ASOPs that may be applicable to particular tasks. The following ASOPs, as of the date of this practice note, are among those the actuary may wish to consider as potentially applicable to model development:

- ASOP No. 1: Introductory Actuarial Standard of Practice
- ASOP No. 2: Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts
- ASOP No. 7: Analysis of Life, Health, or Property/Casualty Insurer Cash Flows
- ASOP No. 11: Financial Statement Treatment of Reinsurance Transactions Involving Life or Health Insurance
- ASOP No. 12: Risk Classification (for All Practice Areas)
- ASOP No. 21: Responding to or Assisting Auditors or Examiners in Connection with Financial Audits, Financia; Reviews, and Financial Examinations
- ASOP No. 22: Statements of Opinion Based on Asset Adequacy Analysis by Actuaries for Life or Health Insurers
- ASOP No. 23: Data Quality
- ASOP No. 25: Credibility Procedures
- ASOP No. 41: Actuarial Communications
- $\quad$ ASOP exposure draft, Principle-Based Reserves for Life Products (exposure draft dated March 2017)
- $\quad$ ASOP exposure draft, Modeling (exposure draft dated June 2016)

Q9.4: What is unique to a PBR model, in contrast to actuarial models generally?

A: While some actuarial models may not be created to be automated and governed for valuation purposes, the PBR model(s) may need to be a part of the regular valuation process, which generally requires some form of controls and automation.

Q9.5: What is required to be documented in the PBR Actuarial Report?

A: VM-31 of the Valuation Manual specifies the contents of the PBR Actuarial Report. Examples of required documentation related to models include details regarding asset model(s), cash flow model(s), and nonguaranteed elements.

## DEFINITIONS

The definitions below are for terms used in this practice note. Many of these definitions are further expanded upon in the practice note, giving greater context to the meaning of the particular term.

- Benchmarking: A model validation procedure comparing model results to the results of similar models, or to other external criteria.
- Model: A representation of relationships among variables, entities, or events using statistical, financial, economic, mathematical, or scientific concepts and equations.
- Model Classification Scheme: Methodical identification of models according to model characteristics. For example, models may be classified according to risk rating (high, medium, low), model type (cash flow, regression), model purpose (valuation, pricing, RBC), accounting method (GAAP, stat, tax, IFRS), product type (life, annuity, health), etc.
- Model Developer: A person who is responsible for designing, constructing, and maintaining the model.
- Model Steward: A person who oversees the model's development and use. A model steward is responsible for assuring that the model developers, model users, and model reviewers are carrying out the responsibilities outlined in the model governance policy.
- Model Reviewer: A person who provides an independent review of the reasonableness of various aspects of the modeling process. A reviewer will be someone distinct from the person who performed the work being reviewed, and will possess adequate knowledge and expertise regarding the model and its uses.
- Model Risk: The risk of adverse consequences from decisions made as a result of a model that does not adequately represent that which is being modeled.
- Model Risk Ranking: A process that may be used to consolidate the individual model risk scores and sort all models or a subset of the models to determine a relevant risk ranking for each model in the enterprise. An overall score relative to the severity of the model's risk could be determined for each model relative to the other enterprise models.
- $\quad$ Model User: The person who is responsible for running the model and using it to calculate results. This is a role that requires adequate knowledge of both the underlying business and of the model being used to analyze that business.
- Model Validation: The practice of performing an independent challenge and thorough assessment of the suitability and adequacy of the model based on tests carried out across multiple dimensions including design, data, assumptions, results, and governance.
- Model Validation Scope: The depth and breadth of reviews and testing performed on various areas of the model as part of the validation exercise.
- Valuation Manual: The manual detailing statutory reserve requirements, including PBR, adopted by the NAIC or as amended thereafter.


[^0]:    ${ }^{1}$ A third exposure draft of the pending ASOP on Principle-Based Reserves for Life Products was released in April 2017.

    ${ }^{2}$ For all references in this practice note to ASOP exposure drafts, please note that under ASOP No. 1 Section 3.1.7, "An ASOP is not binding until the effective date of the ASOP." Under Section 3.1.7, further, "[e]xposure drafts of an ASOP, and the ASOP itself from the date of its publication to its effective date, form part of the literature of the actuarial profession; actuaries may look to them at their discretion for advisory guidance, but they are not binding on actuaries."

