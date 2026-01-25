# Advanced Analytics in Insurance: Utilizing Building Footprints Derived from Machine Learning and High-Resolution Imagery

APRIL | 2025
Greg Dietzen, FCAS, MAAA Consulting Actuary Milliman, Inc.

Garrett Bradford, GISP
Principal and GIS Consultant Milliman, Inc.

Kailey Adams
GIS Analyst
Milliman, Inc.

Claire Palmer, GISP
GIS Programmer
Milliman, Inc.

SPONSOR
- General Insurance Research Committee
- Casualty Actuarial Society

## CONTENTS

    Executive Summary ..... 4
    Section 1 Background ..... 6
    1.1 Geocoding ..... 6
    1.2 Building Footprint Delineation Process ..... 7
    1.3 Building Footprints and Flood ..... 8
    1.4 Building Footprints and Wildfire ..... 9
    Section 2 Flood Case Study ..... 11
    2.1 Data ..... 11
    2.2 Methodology ..... 11
    2.3 Results ..... 13
    2.3.1 Elevation ..... 15
    2.3.2 Relative Elevation ..... 16
    2.3.3 Distance to Coast ..... 18
    2.3.4 Distance to River ..... 19
    2.4 Conclusions ..... 21
    Section 3 Wildfire Case Study ..... 22
    3.1 Data ..... 23
    3.2 Methodology ..... 23
    3.2.1 Vegetation Cover. ..... 23
    3.2.2 Structure Separation ..... 25
    3.2.3 Distance to Wildland Vegetation ..... 26
    3.3 Results ..... 26
    3.3.1 Vegetation Cover. ..... 26
    3.3.2 Structure Separation ..... 31
    3.3.3 Distance to Wildland Vegetation ..... 33
    3.4 Conclusions ..... 37
    Section 4 Additional Applications and Future Research ..... 38
    4.1 Building Footprint ..... 38
    4.2 Ground Feature Identification ..... 38
    4.2.1 Roof Characteristics ..... 38
    4.2.2 Tree Overhang ..... 39
    4.2.3 Unique Property or Liability Exposures ..... 39
    4.3 Future flood and wildfire Research ..... 39
    Section 5 Conclusions ..... 41
    Section 6 Limitations ..... 42
    6.1 Data Reliance ..... 42
    6.2 Variability of Results ..... 42
    6.3 Geospatial Uncertainty ..... 42
    6.4 Model Reliances ..... 42
    Section 7 Acknowledgments ..... 43
    References ..... 44
    About The Society of Actuaries Research Institute ..... 47
    About The Casualty Actuarial Society ..... 48

## Executive Summary

Geospatial imagery and high-resolution image technology have spurred advances across many industries, including agriculture (Jain et al., 2017), transportation (Lee, Oh, \& Ryu, 2003), disaster response (NOAA, 2022), and construction (Ma, Wang, Cheng, Li, \& Tong, 2013). There are a wide variety of applications for the property and casualty (P\&C) insurance industry as well, including underwriting, rating, and claims settlement.

One narrow but critical slice of geospatial data relevant to the P\&C insurance industry is building location, typically inferred using address-based geocoding. Geocoding workflows typically result in a single point location that may or may not accurately represent the building(s) to be insured. New methods for determining building location, such as the use of structure footprints, may offer significant improvements in risk determination in certain cases.

The paper begins with an introduction to the use of remotely sensed imagery and artificial intelligence to delineate detailed building footprints across wide geographic scales. The addition of remotely sensed high-resolution elevation information (e.g., Light Detection and Ranging or LiDAR) to define key structural characteristics relevant to risk assessment will also be covered.

The paper then presents two cases studies to illustrate the utility of building footprint data.

### Cast Study 1: Flood

This study assessed the vulnerability to flooding of a portfolio of single-family homes in Hillsborough County, Florida. This is a coastal area where storm surge and inland flood hazards are high. In such areas, more precise information on structure location and elevation can have a large impact on measured flood risk.

The case study examined the expected flood losses and National Flood Insurance Program's (NFIP) estimated premiums for each home using two locations for each risk. The first location was based on the centroid of the property's parcel data. The second location was based on building footprint data. These different estimates of building location could be distant enough from each other to materially impact flood risk. The two approaches produced locations estimates more than ten meters apart for a majority (68\%) of homes.

Greater differences in location estimates produced greater differences in estimated flood losses and premiums. The study explored how certain geographic information systems' (GIS) data can explain these results. Elevation metrics were particularly relevant. The parcel- and footprint-derived locations for each home often were at different elevations, which can significantly drive flood risk. For homes where the footprint-derived location was more than three feet lower than the parcel-derived location, the average storm surge expected loss was over three times higher at the footprint-derived location. A similar result held for cases where the elevation difference was reversed.

The differences in flood risk illustrate the importance of location accuracy in flood insurance rating. Inaccurate locations can lead to unfair insurance premiums, either hurting policyholders or exposing insurers to unexpected risk.

### Case Study 2: Wildfire

The second case study examined the impact of building footprint and vegetation cover in calculating underwriting wildfire risk metrics for three communities in California: Scripps Ranch (San Diego County), Grizzly Flats (El Dorado County), and Fountaingrove (Sonoma County). These communities were chosen for their wildfire history and proximity to wildland areas. Three analyses were performed to assess the communities in their wildfire risk: vegetation cover, structure separation, and distance to wildland vegetation.

The surrounding vegetation cover (as a percentage of total area) was gathered for each single-family home in the communities. This was quantified in three areas around each home relevant to wildfire preparedness: immediate zone ( $0-5 \mathrm{ft}$ ), intermediate zone ( $5-30 \mathrm{ft}$ ), and extended zone ( $30-100 \mathrm{ft}$ ). The vegetation cover data was then aggregated by community to compare wildfire risk at that level. Based on vegetation cover, Grizzly Flats appeared to have a higher risk than the other communities.

Structure separation is the distance from the perimeter of a building to the perimeter of the nearest structure. This was calculated using building footprint data for each home in each community. Larger structure separation helps to prevent wildfire spread from building to building. Relatively small structure separation was identified as an important driver of fire growth in recent wildfires. Based on structure separation, Scripps Ranch appeared to have a higher risk than the other communities.

Wildland vegetation geographic data was developed to assess the risk each community faced due to wildfires originating or progressing through the Wildland Urban Interface (WUI), the area human structures are adjacent to, or interspersed with, wildland vegetation. Distance to wildland vegetation was calculated using the building footprint for each home. The study noted the importance of definitional thresholds in the identification of wildland vegetation. Under the assumptions of the study, based on the distance to wildland, Grizzly Flats appeared to have a higher risk than the other communities.

This case study is largely illustrative of how data derived from high-resolution imagery (e.g., building footprint, vegetation cover) can be used to evaluate wildfire risk at a community level. Although the metrics in the study are derived at the structure level, they are aggregated to gain insights into the different communities in whole.

The paper concludes with a discussion of other potential applications of building footprint or other highresolution imagery data for other property perils.

Click Here

## Section 1 Background

It is important for insurers to have accurate location data attached to property information so that location-based risk can be easily examined. Geographic information can take several forms. For example, structures can be represented by point locations or building footprint polygons. Point locations are coordinate pairs (i.e., latitude and longitude) that typically represent the centroid of a building. Building footprints are two-dimensional polygons that show the size, shape, and location of the building as viewed from directly above (Li et al., 2024). Point locations can also represent the delivery point (e.g., mailbox, street address) or the centroid of the parcel that the building resides on. Figure 1 shows examples of each of these representations and how they may differ for two residential buildings. While each of these geographic representations provide location information for the same structure, their differences can impact results from catastrophic risk assessments.

Figure 1
EXAMPLES OF BUILDING LOCATION REPRESENTATIONS
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-06.jpg?height=1011&width=1513&top_left_y=876&top_left_x=249" alt="image" style="width:100%;height:auto;">

### 1.1 GEOCODING

Geocoding is the process of linking a specific location to address information. A geocoder will pass an address through a locator to match the entered address with addresses and geospatial information stored in the locator database. Typical geocoders will return a precise location, expressed as latitude/longitude coordinates, in addition to a matched address and additional information about the quality of the match. There are numerous commercially available geocoding services used in property insurance, and within the United States, the Census Bureau maintains a publicly available geocoding service as well.

Regardless of the source, geocoded results should always be reviewed to ensure that the most accurate match is achieved. Depending on the quality of the input address information, geocoder, and locator database, geocoded point locations could represent points that are less accurate than the desired results. For example, if the input street name was entered incorrectly, the returned geocoded point may represent the ZIP Code centroid because it was
unable to match the input street name with an existing street name (Bradford, Barth, \& Wafer, 2023). If the geocoder and locator database is not up to date, and the input address contains a street number that does not exist in the database, the returned results may represent a point that is interpolated between two known addresses or a street corner. Geocoding is one of the best tools to estimate the location of insured properties and is able to produce reliable results when appropriate quality assurance steps are taken.

### 1.2 BUILDING FOOTPRINT DELINEATION PROCESS

In contrast to traditional geocoding, which results in a single point to represent a structure, building footprints are polygonal features that provide the size, shape, and location of structures. Building footprint data can be generated through field surveying and mapping, manual digitization from aerial photography, remote sensing, or a combination of these methods. Field surveying and manual digitization are the most accurate measures of building footprints, but these methods are time and labor intensive and are impractical for identifying buildings over a large geographic area. Remote sensing data can be used to efficiently delineate buildings over large areas with comparable accuracy. Remote sensing methods typically rely on high-resolution imagery (aerial or satellite) and/or LiDAR (Light Detection and Ranging) data.

High-resolution imagery refers to imagery obtained from airborne crafts or satellites with a high spatial resolution (typically $<4 \mathrm{~m}$ ) (Li et al., 2024). Satellite imagery can be generalized by spatial resolution, ranging from low ( $>30 \mathrm{~m})^{1}$ to very high-resolution $(<1 \mathrm{~m})^{2}$. Aerial imagery collected from manned aircrafts typically offers imagery with a fine spatial resolution $(<1 \mathrm{~m})^{3}$, while Unmanned Aerial Vehicles (UAVs) can be fitted with sensors to collect very highresolution imagery over small areas.

LiDAR is a remote sensing method in which light pulses from a laser are used to measure distances to the surface of the earth. The LiDAR system provides a 3D point cloud that represents the observed surface. The resolution (spacing between points) of 3D point clouds can range from under a millimeter (typical of ground based or Terrestrial Laser Scanning [TLS]) to a meter and upwards (in the case of Airborne Laser Scanning [ALS]). Each data point provides 3D positional and backscatter information (e.g., signal intensity). Location and intensity information can be used to assign data points into distinct classes, such as vegetation, roads, water, buildings, etc. (Tomljenovic, Hofle, Tiede, \& Blaschke, 2015). LiDAR data are used to generate gridded, raster ${ }^{4}$ data products such as Digital Elevation and Digital Surface Models (DEM/DSM). DEMs are bare-earth representations of the earth's surface. Built (buildings, powerlines, bridges, etc.) and natural (trees and other vegetation) surface elements are filtered out to produce a smoothed elevation dataset. In contrast, DSMs include both built and natural features.

The creation of building footprints from high-resolution imagery is commonly achieved through a variety of automation methods. These methods can range from relatively simple rule-based methods to sophisticated deep machine learning approaches. Rule-based methods rely on predefined rules or thresholds that are guided by the user, whereas deep learning techniques are designed to learn from data through complex training and pattern recognition. Furthermore, data fusion techniques combine data from different sources, such as LiDAR, to improve building footprint generation (Dabove, Daud, \& Olivotto, 2024). Regardless of what approach is used, building detection from aerial imagery relies on information from input imagery that can distinguish buildings from other surfaces. Geometric (size and shape), spectral (reflected energy), textural (visual patterns; individual buildings or

[^0]building clusters), and contextual (e.g., presence of shadows) characteristics of buildings are some of the most commonly used indicators of building presence in imagery (Tomljenovic, Hofle, Tiede, \& Blaschke, 2015). The goal of any technique employed is to use these characteristics to segment an image into categories corresponding to different parts of a landscape. For example, buildings often have well-defined lines and edges that form a rectangle or series of connected rectangles (e.g., an L-shaped building); pixels in an image that follow the recognized patterns of building shapes and sizes will be classified as a building.

### 1.3 BUILDING FOOTPRINTS AND FLOOD

Flood risk is determined in part by property-specific factors such as first floor height, construction, number of stories, proximity to flood sources, and flood zone designation. As such, building footprints are an essential component of detailed flood risk assessment by providing information about the location, size, and layout of structures at risk relative to flooding sources.

A number of studies have utilized building footprints to assess aggregate flood risk at local (community, city, and county) and national scales. In southeast France, building footprints and aerial imagery were used to assess the impact of urbanization from 1990-2020 on flood risk for two cities. By comparing building footprints from 2020 to aerial imagery from 2014, 1999, and 1990, the authors found that the flood risk was greatly increased due to the addition of more buildings in flood prone areas (Fox, Banitalebi, \& Rainaud, 2024).

Building footprints were used to estimate the number of buildings that moved into or out of the Special Flood Hazard Area (SFHA) for 255 counties across the U.S. where Flood Insurance Rate Maps (FIRMs) were updated between 2013 and 2017. Approximately 20,000 buildings were removed from SFHAs on FIRMs between preliminary and updated FIRMs, suggesting that SFHAs on FIRMs likely underpredict flood hazard in many regions across the U.S. (Lea \& Pralle, 2021). In a similar study, building footprints coupled with census-block group level population data were used to compare exposed populations in the United States within 100-year floodplain boundaries from the Federal Emergency Management Agency (FEMA) and three open access floodplain products. Results showed that the U.S. population within the 100 -year FEMA floodplain is lower compared to other floodplain datasets examined, suggesting that FEMA potentially underestimates flood exposure across the country (Huang \& Wang, 2020).

In addition to generalizing flood risk across communities or larger geographies, building footprints have been used to estimate building-scale flood loss. Footprints of buildings impacted by a 2014 flood in Milan, Italy, were used in combination with flood extent and depth maps, land use, and elevation data to analyze structural vulnerability patterns (Taramelli et al., 2022).

The importance of how a property or building location is defined when assessing flood exposure was highlighted in a 2017 study aimed at understanding the influence of different methods and parameters of flood exposure analysis in Switzerland. Building footprints were classified as 'exposed' if they were wholly contained within or partially intersected flood maps. One interesting result from this research was that the average building footprint area was greater for exposed buildings compared to unexposed buildings. As one explanation for this finding, the authors proposed that larger buildings, which require more flat terrain, are preferably built on floodplains (Rothlisberger, Zischg, \& Keiler, 2017). This concept was applied in a study examining the use of flood insurance claims to validate 2D flood inundation models (Zischg, Mosimann, Bernet, \& Rothlisberger, 2018). The authors acknowledged that spatial representation impacts flood risk determination: a building that is represented as a point (e.g., building centroid) is less likely to be classified as exposed to flooding than the same building if it is represented as a polygon (e.g., building footprint).

The impact of how a building is represented spatially was further underscored in a study estimating the effect of floodplain location on home sale prices in Portland, Oregon (Netusil, Moeltner, \& Jarrad, 2019). Reported results
showed that sale prices for properties were $21.5 \%$ less when the building footprint intersected the 100 -year floodplain than when it did not. There was only an $8.6 \%$ reduction in property sales when any part of the property ("tax lot") intersected the floodplain. Furthermore, in an analysis of residential properties at risk to flooding in Utah, the use of parcel boundaries to estimate property exposure in the 100-year floodplain resulted in a two-fold overestimation of flood risk compared to using building footprints (Clark, Collins, Grineski, Brewer, \& Flores, 2025).

### 1.4 BUILDING FOOTPRINTS AND WILDFIRE

The Wildland Urban Interface (WUI) is an area where houses are located in or in close proximity to wildland vegetation. A widely adopted formal definition specifies two types of WUI: interface (built areas that abut wildland vegetation) and intermix (areas built within wildland vegetation). Specifically, interface areas are those with $<50 \%$ vegetation within 1.5 miles of dense ( $\geq 75 \%$ ) wildland vegetation and have $\geq 1$ Housing Unit per 40 acres. Intermix areas are those with $>50 \%$ vegetation cover and $\geq 1$ Housing Unit per 40 acres (NIST, 2023).

There are three primary pathways through which fire spreads into and within WUI communities: radiant exposure that occurs when fire is close to structures, direct flame contact, and firebrand transport from the main fire front or nearby burning vegetation or structures (Caton, Hakes, Gorham, Zhou, \& Gollner, 2017). There are many factors that contribute to the risk of a home burning, some of which can be controlled directly by the homeowner and others that are pre-existing or community driven. Building features such as vents, roof materials, and eaves, as well as vegetation in close proximity, can be altered by the homeowner to decrease the risk from wildfire. However, factors such as the location and spatial arrangement of homes within a community and the distance between homes and wildland vegetation are pre-existing and are significant pathways through which fire can move through a WUI community. When structure separation distance, the distance between adjacent buildings, is low, the probability of home-to-home fire spread increases. Additionally, the proximity of wildland vegetation can significantly alter the chances of a home burning, where buildings on the perimeter of communities adjacent to vegetation have a higher susceptibility to burning (Hakes, Caton, Gorham, \& Gollner, 2017).

The impact of variables driving wildfire risk will vary greatly among different ecoregions (Alexandre et al., 2016). A study examining the impact of housing arrangement and vegetation factors associated with building loss in the 2018 Camp Fire that destroyed more than 18,000 structures in Paradise, California, found that both surrounding vegetation and distance to neighboring structures strongly influenced the probability of building survival (Knapp, Valachovic, Quarles, \& Johnson, 2021).

The presence of nearby buildings (within 30 m ) greatly increased the probability of a building burning in the 2019 McKinley Fire in Alaska (Schmidt, Berman, \& Waigl, 2024). Home assessment surveys following the 2012 Waldo Canyon Fire in Colorado concluded that the majority of home loss was likely attributable to home-to-home fire spread facilitated by low ( $3-6 \mathrm{~m}$ ) structure separation distance (Quarles, Leschak, Worley, Brown, \& Iskowitz, 2013). Seemingly conversely, a 2012 study examined the role of housing arrangement and location on the probability of housing loss due to wildfire across southern California. Results showed that structure loss was most likely to occur in areas where housing density was low, when homes were surrounded by wildland vegetation, and areas historically impacted by frequent fire (Syphard, Keeley, Bar Massada, Brennan, \& Radeloff, 2012). Though these conclusions may seem incongruous with other research, it may be that in the areas that Syphard et al. (2012) examined, the highest densities of housing (shown to have lower risk) may have had less surrounding vegetation, while lower densities of housing (shown to have higher risk) may have been interspersed in wildland vegetation (Caton, Hakes, Gorham, Zhou, \& Gollner, 2017). In addition, as previously noted, the risk posed by different factors can vary significantly by ecoregion, so counterintuitive examples like this should not be unexpected.

The degree to which building proximity or distance to wildland vegetation impacts building loss in a community is highly dependent on a number of factors. Importantly, wildfire spreads if there is available fuel, whether from vegetation or neighboring homes. The location of those homes relative to a given pathway through which fire may
travel is essential to understanding risk within WUI communities. Building footprint data that accurately represents the location of elements at risk is, therefore, a foundational necessity when assessing the risk due to wildfire.

## Section 2 Flood Case Study

Flood rating requires exact latitude and longitude, rather than a larger geographic designation such as county, ZIP Code, or census block. Flood risk can vary significantly over short horizontal distances, primarily due to associated changes in elevation. In traditional geocoding, the output latitude and longitude could represent a variety of different locations unrelated to the position of the insured structure, such as parcel centroid or mailbox location.

There are many location-specific attributes that can drive a property's flood risk, unrelated to its actual construction, including:

- Elevation (above sea level);
- Relative elevation ${ }^{5}$;
- Distance to coast; and
- Distance to river.

The first case study illustrates the importance of accurate identification of structure location in flood rating by quantifying potential differences in measured risk between parcel- and footprint-based data.

Note on units: Throughout this flood case study, vertical distances (e.g., elevation) are measured in feet, and horizontal distances (e.g., distance to coast) are measured in meters. This is done intentionally to align with methodologies used by the NFIP.

### 2.1 DATA

Parcel data from Hillsborough County, Florida, was taken from the Florida Department of Revenue, as of 2021. This data was filtered to include only single-family residential-zoned parcels. Footprint data for these parcels was taken from the Overture Maps Foundation, as of October 23, 2024. Due to differences in these data vintages, there is expected to be some differences in the datasets due to new construction. We do expect this effect to be material for the purposes of this study. Both datasets contain polygons representing the ground coverage of each parcel or building. The parcel and footprint data were combined to create a dataset representing 337,460 single-family homes. Elevation data was taken from USGS Elevation tiles, downloaded in 2022. Coastline data was taken from the USGS National Hydrography Dataset's (NHD) coastal and near-coastal features, downloaded in 2022. River data was taken from NHD river lines and polygons, downloaded in 2022. NFIP flood zone data was taken from the National Flood Hazard Layer (NFHL) from FEMA, downloaded in 2022.

### 2.2 METHODOLOGY

For each home, two latitude-longitude pairs were generated, one to represent the parcel ("parcel location") and one to represent the footprint ("footprint location"). The parcel locations were set to be the parcel centroids. The footprint locations were chosen from among the vertices of each footprint. For each home, ground elevations of each footprint vertex were generated, and the vertex with the lowest elevation was chosen as the footprint location. This process was done to estimate the most flood-vulnerable point for the house.

[^1]Figure 2
EXAMPLE OF BUILDING FOOTPRINT LOCATION BASED ON LOWEST ELEVATION POINT
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-12.jpg?height=996&width=1636&top_left_y=356&top_left_x=249" alt="image" style="width:100%;height:auto;">

Geographic data was joined to each parcel and footprint location. This data included distance to coast, distance to river, elevation, relative elevation, and flood zone. Please note that references to "elevation" and "relative elevation" throughout this report only consider terrain and do not consider any additional height of a structure's first floor. While first floor height is important in flood risk consideration and is also utilized in the case study, this is a distinct concept from elevation.

To generate expected flood loss costs, each parcel and footprint location was rated with Milliman Bungalow ${ }^{\text {™6 }}$, a residential flood rating plan developed by Milliman. Each location was rated with uniform property and policy characteristics to isolate the effects of geography in the results. Table 1 lists the characteristics used in loss cost determination. This produced expected loss costs for both inland flood and storm surge ${ }^{7}$ sub-perils.

[^2]Table 1
UNIFORM CHARACTERISTICS USED FOR MILLIMAN BUNGALOW™ LOSS COSTS
| Characteristic | Value | Characteristic | Value |
| :--- | :--- | :--- | :--- |
| Building limit | \$250,000 | First floor height ${ }^{8}$ | 1 foot |
| Building replacement cost | \$500,000 | Basement | No |
| Contents limit | \$100,000 | Construction | Frame |
| Contents replacement cost | \$100,000 | Number of Stories | 1 |
| Deductible | \$2,500 |  |  |


Additionally, NFIP premiums were estimated for these locations using publicly available documentation (FEMA, 2021) and data provided by KatRisk. Table 2 lists the characteristics used in NFIP premium estimation. These were generally similar to those used in the loss cost determination.

Table 2
UNIFORM CHARACTERISTICS USED FOR NATIONAL FLOOD INSURANCE PROGRAM PREMIUM ESTIMATES
| Characteristic | Value | Characteristic | Value |
| :--- | :--- | :--- | :--- |
| Building limit | \$250,000 | First floor height | 1 foot |
| Building replacement cost | \$500,000 | Foundation type | Slab |
| Building deductible | \$1,250 | Construction | Frame |
| Contents limit | \$100,000 | Number of Stories | 1 |
| Contents replacement cost | \$100,000 | Flood vents | No |
| Contents deductible | \$1,000 | Prior claims | 0 |


### 2.3 RESULTS

For each home, the horizontal distance between the parcel and footprint locations ("parcel-footprint distances") was measured. The parcel-footprint distances ranged from less than one meter ( m ) to 438 meters, with an average of 14 meters. Table 3 below contains the distribution of parcel-footprint distances.

Table 3
PARCEL-FOOTPRINT DISTANCE DISTRIBUTION
| Parcel-Footprint Distance (m) | Distribution of Homes |
| :--- | :---: |
| Less than 5 | $4 \%$ |
| 5 to 10 | $28 \%$ |
| 10 to 25 | $63 \%$ |
| 25 to 50 | $4 \%$ |
| Over 50 | $1 \%$ |


Please note that there is no special significance related to the endpoints of these distance groupings (e.g., $5 \mathrm{~m}, 10$ m , etc.). These were chosen simply for ease of understanding.

[^3]Figure 3 illustrates two examples of relatively large parcel-footprint distances. The yellow lines represent the border of each parcel, with the blue dots as their centroids (parcel locations). The pink polygons represent the homes' building footprints, with the red dots as the lowest-elevated vertex (footprint locations). The second example shows several adjacent parcels with their parcel and footprint locations marked as well.

Figure 3
LARGE PARCEL EXAMPLES
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-14.jpg?height=731&width=978&top_left_y=571&top_left_x=249" alt="image" style="width:100%;height:auto;">

Due to horizontal differences between the footprint and parcel locations, there were corresponding differences in the associated geographic data. Table 4 shows the average and maximum elevation and relative elevation differences between the parcel and footprint locations as the distances between them increase.

Table 4
ELEVATION GIS DATA SUMMARY
| Parcel-Footprint Distance (m) | Elevation Difference (ft) |  | Relative Elevation Difference (ft) |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Average | Max | Average | Max |
| Less than 5 | 0 | 10 | 0 | 10 |
| 5 to 10 | 1 | 18 | 1 | 18 |
| 10 to 25 | 1 | 23 | 1 | 23 |
| 25 to 50 | 2 | 21 | 2 | 20 |
| Over 50 | 4 | 30 | 3 | 27 |
| Total | 1 | 30 | 1 | 27 |


Both elevation and relative elevation show greater average and maximum differences between parcel and footprint location as the parcel-footprint distance increases. However, even when the parcel-footprint distance is relatively small, there are cases with significant elevation differences. The size of these elevation differences is notable in

Florida, considered the flattest state by some measures ${ }^{9}$. Significantly larger elevation differences could be expected in hillier terrain.

In Table 4, elevation difference is defined as the absolute value of the difference between the parcel location elevation and the footprint location elevation. Similarly, in Table 4, relative elevation difference is defined as the absolute value of the difference between the parcel location relative elevation and the footprint location relative elevation. Absolute values are used here to illustrate the extent of the differences. In the following section, elevation and relative differences are defined using the footprint value minus the parcel value, which can result in positive and negative differences. This allows for analysis of expected loss differences between the footprint and parcel locations, given positive or negative values for elevation difference and relative elevation difference.

#### 2.3.1 ELEVATION

Elevation is a predictor of storm surge risk. Properties at higher elevation are less vulnerable to coastal water being driven onto land. To illustrate the difference in storm surge risk by elevation, homes were bucketed by elevation difference. The average storm surge loss costs, as calculated with Milliman Bungalow ${ }^{\text {™ }}$, are shown for each bucket in Figure 4.

Figure 4
AVERAGE STORM SURGE EXPECTED LOSS BY ELEVATION DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-15.jpg?height=680&width=1587&top_left_y=1138&top_left_x=244" alt="image" style="width:100%;height:auto;">

Elevation difference was calculated as: footprint location elevation - parcel location elevation. Negative values represent homes with a lower footprint location, and positive values represent homes with a lower parcel location. Homes have significantly higher expected loss costs at the footprint locations when footprint locations are below parcel locations. Conversely, homes have significantly higher expected loss costs at the parcel locations when footprint locations are above parcel locations.

[^4]Figure 5 shows average estimated NFIP premium by the same elevation difference buckets.

Figure 5
AVERAGE ESTIMATED NFIP PREMIUM BY ELEVATION DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-16.jpg?height=704&width=1643&top_left_y=476&top_left_x=244" alt="image" style="width:100%;height:auto;">

Differences are directionally similar to Figure 4, but they are not as large. This is mainly because NFIP premium accounts for sub-perils, including inland flood, which may not be correlated with elevation.

#### 2.3.2 RELATIVE ELEVATION

Relative elevation is a predictor of inland flood risk. Properties generally higher than the surrounding area are less vulnerable to floodwater accumulation. To illustrate the difference in inland flood risk by elevation, homes were bucketed by relative elevation difference. The average inland flood loss costs, as calculated with Milliman Bungalow ${ }^{\text {™ }}$, are shown for each bucket in Figure 6.

Figure 6
AVERAGE INLAND FLOOD EXPECTED LOSS BY RELATIVE ELEVATION DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-16.jpg?height=699&width=1584&top_left_y=1781&top_left_x=247" alt="image" style="width:100%;height:auto;">

Relative elevation difference was calculated as: footprint location relative elevation - parcel location relative elevation. Negative values represent homes with a lower footprint location, and positive values represent homes with a lower parcel location. Expected loss costs are significantly higher for footprint locations when they are below parcel locations, and the opposite cases are true as well.

Figure 7 shows average estimated NFIP premium by the same relative elevation difference buckets.

Figure 7
AVERAGE ESTIMATED NFIP PREMIUM BY RELATIVE ELEVATION DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-17.jpg?height=703&width=1640&top_left_y=696&top_left_x=247" alt="image" style="width:100%;height:auto;">

Differences are directionally similar to Figure 6, but they are not as large. This is mainly because NFIP premium accounts for sub-perils, including storm surge, that may not be correlated with relative elevation.

Table 5 shows the average distance to coast and average distance to river differences between the parcel and footprint locations as the distances between them increase. It also shows the percentage of homes with a different special flood hazard area (SFHA) assignment based on parcel and footprint location.

Table 5
HORIZONTAL GIS DATA SUMMARY
| Parcel-Footprint Distance (m) | Distance to Coast Difference (m) | Distance to River Difference (m) | SFHA Assignment Difference |
| :--- | :--- | :--- | :--- |
|  | Average | Average |  |
| Less than 5 | 2 | 3 | 0.6\% |
| 5 to 10 | 5 | 7 | 0.8\% |
| 10 to 25 | 9 | 12 | 1.4\% |
| 25 to 50 | 21 | 25 | 14.9\% |
| Over 50 | 50 | 61 | 35.0\% |
| Total |  |  | 2.2\% |


Parcel-footprint distance, distance to coast, and distance to river each measure horizontal distance. Therefore, the differences in distance to coast and distance to river are correlated with and limited by the parcel-footprint distance.

#### 2.3.3 DISTANCE TO COAST

Distance to coast is a predictor of storm surge risk. Properties further inland (larger distance to coast) are less vulnerable to coastal water being driven onto land. To illustrate the difference in storm surge risk by distance to coast, homes were bucketed by distance to coast difference. The average storm surge loss costs, as calculated with Milliman Bungalow ${ }^{\text {™ }}$, are shown for each bucket in Figure 8.

Figure 8
AVERAGE STORM SURGE EXPECTED LOSS BY DISTANCE TO COAST DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-18.jpg?height=693&width=1582&top_left_y=627&top_left_x=247" alt="image" style="width:100%;height:auto;">

Distance to coast difference was calculated as: footprint location distance to coast - parcel location distance to coast. Negative values represent homes with a footprint location closer to the coast, and positive values represent homes with a parcel location closer to the coast. Expected loss costs are higher for footprint locations that are closer to the coast than parcel locations.

The opposite is true for cases where the parcel is significantly closer to the coast (over 25 m ), but not for cases where it is 0 to 25 meters closer. This "reversal" of expectations is due to random chance in the data. On average, homes in the " 0 to 10 m " and " 10 to 25 m " buckets have a parcel location elevated higher than the associated footprint location. As seen in subsection 2.3.1, elevation has a very strong connection with storm surge expected loss. In this case, the effect of elevation outweighs the effect of distance to coast.

Figure 9 shows average estimated NFIP premium by the same distance to coast difference buckets.

Figure 9
AVERAGE ESTIMATED NFIP PREMIUM BY DISTANCE TO COAST DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-19.jpg?height=718&width=1647&top_left_y=474&top_left_x=243" alt="image" style="width:100%;height:auto;">

Estimated NFIP premiums are relatively similar across all distance to coast difference buckets. Although some reversals appear, the amounts are not significantly different. From this we can conclude that, on average, at the scale of a parcel, differences in distance to coast are not significant drivers of NFIP premium. Distance to coast differences on larger scales (e.g., several neighboring parcels) are expected to more significantly impact NFIP premium.

#### 2.3.4 DISTANCE TO RIVER

Distance to river is a predictor of inland flood risk. Properties further from rivers and creeks (larger distance to river) are less vulnerable to riverine flooding. To illustrate the difference in inland flood risk by distance to river, homes were bucketed by distance to river difference. The average inland flood loss costs, as calculated with Milliman Bungalow ${ }^{™}$, are shown for each bucket in Figure 10.

Figure 10
AVERAGE INLAND FLOOD EXPECTED LOSS BY DISTANCE TO RIVER DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-20.jpg?height=675&width=1582&top_left_y=352&top_left_x=247" alt="image" style="width:100%;height:auto;">

Distance to river difference was calculated as: footprint location distance to river - parcel location distance to river. Negative values represent homes with a footprint location closer to a river, and positive values represent homes with a parcel location closer to a river. Expected loss costs are higher for parcel locations that are significantly (over $25 \mathrm{~m})$ closer to a river than footprint locations. Unexpectedly, the opposite is not true. Expected loss costs are lower for footprint locations that are significantly (more than 25 m ) closer to a river than parcel locations. Expected loss costs are relatively similar for differences in distance to river between - 25 and 25 meters.

The reversal seen in the far left of Figure 10 is due to random chance in the data. Homes in the "Less than -25 m " bucket have a positive average relative elevation difference. On average, the footprint location is higher than the parcel location. As seen in a previous section, relative elevation has a very strong connection with inland flood expected loss. In this case, the effect of relative elevation outweighs the effect of distance to river.

Figure 11 shows average estimated NFIP premium by the same distance to river difference buckets.

Figure 11
AVERAGE ESTIMATED NFIP PREMIUM BY DISTANCE TO RIVER DIFFERENCE (FOOTPRINT - PARCEL)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-21.jpg?height=701&width=1640&top_left_y=399&top_left_x=247" alt="image" style="width:100%;height:auto;">

Estimated NFIP premiums are relatively similar across all distance to river difference buckets. Although some reversals appear, the amounts are not significantly different. From this we can conclude that, on average, at the scale of a parcel, differences in distance to river are not significant drivers of NFIP premium. Distance to river differences on larger scales (e.g., several neighboring parcels) are expected to more significantly impact NFIP premium.

### 2.4 CONCLUSIONS

A precise knowledge of structure location is essential for accurate flood risk determination. Using parcel dataderived location may not be sufficient in certain cases as this can lead to measurement of risk at locations relatively distant from the actual structures.

Along with differences in horizontal location, using parcel data often results in locations with differences in elevation, distance to flooding source, and flood zone. Even across distances as short as five meters and differences in elevation up to ten feet were observed in the case study. Differences in elevation up to 30 feet were observed for cases where parcel-derived location was significantly further from the structure.

Most importantly, using incorrect location in flood rating can result in significant differences in expected flood loss and premium. Differences in elevation for storm surge and differences in relative elevation for inland flood were most clearly correlated with larger differences in expected flood losses. Differences in distance to flooding source (river and coast) were less clearly correlated but also appear to be important.

As discussed in the background section, there are many studies that highlight the importance of building footprints in flood risk determination but, in practice, traditional geocoding methods are still used by many in the insurance industry today. These results clearly indicate a role for the use of building footprints in flood pricing and underwriting, especially in areas of higher flood risk. As widespread use of remotely sensed imagery and machine learning make building footprints commercially available, private insurers and others in the flood risk management industry should adapt their existing practices to incorporate this type of data.

## Section 3 Wildfire Case Study

Wildfire risk to property, including the effects of individual- and community-level mitigation strategies, is a complex and evolving field of study. As with flood, there are many location-specific attributes that can influence a property's wildfire risk, including:

- Topography, including terrain slope and aspect;
- Local vegetation (fuel);
- Construction, including building codes, materials, and community mitigation; and
- Climate (wind, temperature, humidity, precipitation patterns).

Recent fire history and recent weather history can also determine wildfire risk by their influence on potential vegetative fuels. Unlike some other factors, these can vary significantly over time.

In addition to individual risk factors, community risk factors also appear to be significant for wildfire risk. The Insurance Institute for Business and Home Safety (IBHS) performed an analysis of the 2023 Lahaina Conflagration, a deadly Hawaii wildfire. They determined structure density to be a main factor contributing to the fire's fast growth due to "rapid building-to-building spread through flame contact and radiative heat." For communities surrounded by grassland, they recommended, "maintaining-or even increasing-the structure separation distance for buildings within the community" (IBHS, 2024). In early analysis of the 2025 Los Angeles County fires, IBHS again noted structure separation's role in the fires' development:

- As the Eaton Fire spread, "tighter structure spacing with more connective fuels transitioned the fire into a conflagration" (IBHS, 2025).
- For the Palisades Fire, "discrete ignitions occurred in areas with $30-70$ feet structure separation. When fire reached the densely constructed areas in Pacific Palisades with 8-14 feet structure separation, conflagration took hold" (IBHS, 2025).

Accurate building footprint data, available with aerial imagery and computer vision models, allows for assessment of structure separation at a community level.

The wildland urban interface (WUI) is the area where human structures are adjacent to, or interspersed with, wildland vegetation. Wildfires in the WUI are a significant threat due to the presence of both human development and wildland fuels. In a 2017 study, authors found that, from 2000 to 2013 in the contiguous United States, 59\% of the homes threatened and $69 \%$ of the homes destroyed by wildfire were in the WUI (Kramer, Mockrin, Alexandre, Stewart, \& Radeloff, 2018). Both the WUI area and the number of homes within the WUI has grown in recent years. Between 1990 and 2020, there was a 47\% increase in the number of homes in the WUI in the United States (USDA, 2024). Because of the lag in underlying data collection (e.g., census data is collected every ten years), the current update frequency of WUI maps is far behind the actual WUI growth rate (Li, Dao, Kumar, \& Banerjee, 2022). Aerial imagery and computer vision models offer a potential way to more frequently monitor WUI communities and the presence of nearby wildland vegetation.

This case study illustrates three techniques for using aerial imagery of homes to assess wildfire risk.
Note on units: Throughout this wildfire case study distances are generally measured in meters. One exception is for the vegetation cover portion of the case study, where feet are used, to be consistent with definitions used by the National Fire Preparedness Association and the California Department of Forestry and Fire Protection.

### 3.1 DATA

Three California communities were chosen for study.

1) Scripps Ranch is a community of San Diego, CA. It was affected by the 2003 Cedar Fire, which destroyed over 2,800 buildings throughout San Diego County (NBC 7 San Diego, 2023).
2) Grizzly Flats is a census-designated place in El Dorado County. Two-thirds of the community was destroyed by the 2021 Caldor Fire (Wulff, 2024).
3) Fountaingrove is a neighborhood of Santa Rosa, CA, in Sonoma County. Over 1,000 homes were burned by the 2017 Tubbs Fire (Pineda, 2022).

For each community, single family home footprint data was taken from the Overture Maps Foundation buildings dataset as of October 23, 2024. For each home, CAPE Analytics provided vegetation coverage data in zones surrounding the building footprint and was derived from aerial imagery. ${ }^{10}$ This data represented the percentage of area covered by large trees and large bushes. Fuel vegetation cover of the terrain within and surrounding the three communities was taken from 2022 LANDFIRE data.

### 3.2 METHODOLOGY

Three different analyses were conducted on the communities to illustrate potential use cases of aerial imagery and footprint data on wildfire risk determination, focusing on vegetation cover, structure separation, and distance to wildland vegetation. Unlike in the flood case study, there was no available data to estimate a wildfire's expected losses. Wildfire catastrophe models are capable of such estimates, but their use in this study was out of scope. Therefore, the analysis of each community's wildfire risk characteristics does not include a corresponding impact on insurance losses or premiums.

#### 3.2.1 VEGETATION COVER

The National Fire Preparedness Association refers to three areas around the home as the immediate zone (within 5 ft ), intermediate zone ( $5-30 \mathrm{ft}$ ), and extended zone ( $30-100 \mathrm{ft}$ ) (Fitzgerald-McGowan, 2025). These zones can have alternative names; the California Department of Foresty and Fire Protection (CAL FIRE) refers to them as Zone 0, Zone 1, and Zone 2 (CAL FIRE, 2025). These areas of defensible space can act as a buffer between a structure and the surrounding area during a wildfire. Among other recommendations, CAL FIRE recommends removing dead and dying plants in the immediate zone, trimming trees regularly in the intermediate zone, and creating space between shrubs and trees in the extended zone (CAL FIRE, 2025). Figure 12 illustrates the concept of these zones using the CAL FIRE terminology (Ready for Wildfire - Defensible Space, 2025).

[^5]Figure 12
IMMEDIATE (0), INTERMEDIATE (1), AND EXTENDED (2) ZONES
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-24.jpg?height=959&width=1262&top_left_y=356&top_left_x=249" alt="image" style="width:100%;height:auto;">

Source: (Ready for Wildfire - Defensible Space, 2025)
Communities were assessed by the amount of vegetation surrounding their homes. This was performed using the CAPE Analytics data on vegetation cover. This data was provided as three percentages for each home, representing the percentage of vegetation coverage within the immediate, intermediate, and extended zones. Figure 13 shows an example home, and Table 6 shows the coverage percentages.

Figure 13
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-24.jpg?height=564&width=561&top_left_y=1692&top_left_x=249" alt="image" style="width:100%;height:auto;">

Table 6
VEGETATION COVER EXAMPLE
| Zone | Vegetation Cover |
| :--- | :---: |
| Immediate $(0-5 \mathrm{ft})$ | $9 \%$ |
| Intermediate $(5-30 \mathrm{ft})$ | $30 \%$ |
| Extended $(30-100 \mathrm{ft})$ | $55 \%$ |


#### 3.2.2 STRUCTURE SEPARATION

As previously discussed, building-to-building spread is a potential wildfire pathway, and structure density is an important factor in this possibility for a community. Structure separation was calculated for each home in each community using the Overture building footprint data. Structure separation was defined as the distance from the perimeter of a building's footprint to the perimeter of the nearest building, either within the community or within one kilometer of the community boundary. Figure 14 illustrates an example of how structure separation is measured for each home based on footprint data.

Figure 14
STRUCTURE SEPARATION METHODOLOGY
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-25.jpg?height=1183&width=916&top_left_y=1078&top_left_x=249" alt="image" style="width:100%;height:auto;">

#### 3.2.3 DISTANCE TO WILDLAND VEGETATION

In order to assess each home and each community's vulnerability to wildfires originating or progressing through the WUI, distance to wildland vegetation was calculated. Spatial data representing wildland vegetation first needed to be defined and created.

A wildland vegetation spatial data layer was created using the LANDFIRE fuel vegetation cover data. Wildland vegetation was defined as any tree/shrub/herbaceous vegetation with $40 \%$ or greater coverage. This was further restricted to continuous areas of greater than five square kilometers, to exclude parks, recreational green spaces, and urban green belts. These thresholds were in line with academic methods (Li, Dao, Kumar, \& Banerjee, 2022). As described in a later discussion, the resulting analysis is quite sensitive to the selection of these thresholds. With the wildland vegetation layer defined, distances to wildland vegetation were calculated for each home in the communities.

### 3.3 RESULTS

The following are results for three analyses: vegetation cover, structure separation, and distance to wildland vegetation. As a reminder, these do not include corresponding estimates of the impact on insurance losses or premiums. Rather, they serve to illustrate potential methodologies for wildfire risk evaluation.

#### 3.3.1 VEGETATION COVER

Figures 15, 16, and 17 below show the three communities by the vegetation cover in the extended zone for each home. The extended zone was chosen for these figures because it generally exhibits more vegetation coverage variation within each community than the immediate or intermediate zones. Each dot represents a home, with the color representing the percent of vegetation cover per the scale. Some parcels, particularly for Grizzly Flats in Figure 16, do not have a dot, implying there was no structure on that parcel at the time the data was collected.

Figure 15
SCRIPPS RANCH VEGETATION COVER, EXTENDED ZONE (30 - 100 FT)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-27.jpg?height=998&width=1388&top_left_y=354&top_left_x=247" alt="image" style="width:100%;height:auto;">

Figure 16
GRIZZLY FLATS VEGETATION COVER, EXTENDED ZONE ( 30 - 100 FT)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-27.jpg?height=716&width=1376&top_left_y=1491&top_left_x=247" alt="image" style="width:100%;height:auto;">

Figure 17
FOUNTAINGROVE VEGETATION COVER, EXTENDED ZONE ( 30 - 100 FT)
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-28.jpg?height=1127&width=1294&top_left_y=354&top_left_x=249" alt="image" style="width:100%;height:auto;">

For the extended zone, Scripps Ranch appears generally more homogenous in vegetation cover than the other two communities. Both Grizzly Flats and Fountaingrove contain distinct areas of high coverage and areas of low coverage.

Table 7 below shows summarized statistics for each community. The highest value for each statistic is bolded.

Table 7
VEGETATION COVERAGE COMMUNITY STATISTICS
| Community | Immediate Zone $(0-5 \mathrm{ft})$ |  |  |
| :--- | :---: | :---: | :---: |
|  | Average | Median | Max |
| Scripps Ranch | $9 \%$ | $7 \%$ | $59 \%$ |
| Grizzly Flats | $11 \%$ | $0 \%$ | $100 \%$ |
| Fountaingrove | $7 \%$ | $2 \%$ | $70 \%$ |


| Community | Intermediate Zone ( $\mathbf{5 - 3 0 ~ f t}$ ) |  |  |
| :--- | :---: | :---: | :---: |
|  | Average | Median | Max |
| Scripps Ranch | $20 \%$ | $19 \%$ | $78 \%$ |
| Grizzly Flats | $23 \%$ | $23 \%$ | $78 \%$ |
| Fountaingrove | $17 \%$ | $10 \%$ | $91 \%$ |


| Community | Extended Zone $(\mathbf{3 0}-\mathbf{1 0 0} \mathbf{f t})$ |  |  |
| :--- | :---: | :---: | :---: |
|  | Average | Median | Max |
| Scripps Ranch | $20 \%$ | $19 \%$ | $73 \%$ |
| Grizzly Flats | $32 \%$ | $36 \%$ | $86 \%$ |
| Fountaingrove | $17 \%$ | $12 \%$ | $93 \%$ |

At least half of the homes in Grizzly Flats have no vegetation cover in the immediate zone (median $=0 \%$ ), but this community has the highest average coverage in this zone $(11 \%)$. This is driven by homes with significant cover (max $=100 \%$ ). Grizzly Flats also has the highest average coverage in the intermediate and extended zones, although there are individual homes in Fountaingrove with higher coverages than any Grizzly Flats home in these zones. For each of the communities, the average vegetation coverage increases from immediate to intermediate to extended zone. Higher values in the extended zone may be driven by increased vegetation in areas near property boundaries (e.g., curb appeal, privacy).

To see a more complete picture of the distributions for each community, the cumulative distributions of vegetation cover are shown in Figure 18. Please note that the x-axis in each graph extends from 0\% to 30\% only, focusing on a particular part of the distribution.

Figure 18
VEGETATION COVER CUMULATIVE DISTRIBUTIONS
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-30.jpg?height=560&width=950&top_left_y=358&top_left_x=249" alt="image" style="width:100%;height:auto;">

<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-30.jpg?height=572&width=962&top_left_y=945&top_left_x=248" alt="image" style="width:100%;height:auto;">
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-30.jpg?height=575&width=965&top_left_y=1542&top_left_x=249" alt="image" style="width:100%;height:auto;">

To understand the cumulative distributions in Figure 18, one can read each point on each curve as the percentage of homes with a given vegetation coverage or less. For example, in the immediate zone, $40 \%$ of homes have a vegetation cover of $5 \%$ or less for Scripps Ranch. This is circled in red. In the same zone, $80 \%$ of homes have a vegetation cover of 15\% or less for Scripps Ranch. This is circled in blue.

A higher line implies less vegetation cover for the community: a higher percentage of homes have a given vegetation cover amount or less. In each case, Grizzly Flats has the highest percentage of "bare" zone ( $0 \%$ vegetation cover)
homes and the highest percentage of densely covered zones, defined here as above $30 \%$ coverage. Fountaingrove has less vegetation cover than Scripps Ranch in most cases.

Fountaingrove has the lowest average and median levels of vegetation cover. In a vacuum, this suggests lower risk for this community. Grizzly Flats has the highest average vegetation cover, but it also has the largest proportion of homes with no vegetation cover in the immediate zone. All else equal, this suggests a higher risk for the community, but that there are lower risk properties which can be identified.

Community underwriting is a possible use case of these cumulative distributions. For example, if $30 \%$ or less vegetation cover in the extended zone is an underwriting criterion, one can quickly see that over $80 \%$ of homes in Scripps Ranch and Fountaingrove are eligible, but only 44\% of homes in Grizzly Ranch are. (See green circles in Figure 18).

#### 3.3.2 STRUCTURE SEPARATION

Figures 19, 20, and 21 show maps of each community, color coded by structure separation. Because the values for structure separation differed so significantly for each community, the scale for each community is different.

Figure 19
STRUCTURE SEPARATION - SCRIPPS RANCH
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-31.jpg?height=845&width=1262&top_left_y=1130&top_left_x=249" alt="image" style="width:100%;height:auto;">

Figure 20
STRUCTURE SEPARATION - GRIZZLY FLATS
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-32.jpg?height=972&width=1255&top_left_y=354&top_left_x=249" alt="image" style="width:100%;height:auto;">

Figure 21
STRUCTURE SEPARATION - FOUNTAINGROVE
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-32.jpg?height=978&width=1262&top_left_y=1465&top_left_x=249" alt="image" style="width:100%;height:auto;">

Table 8 and Figure 22 display the distribution of structure separation for each community.

Table 8
STRUCTURE SEPARATION
| Community | Average | Distribution of Homes |  |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Distance $(\mathrm{m})$ | $0-5 \mathrm{~m}$ | $5-10 \mathrm{~m}$ | $10-20 \mathrm{~m}$ | $20-50 \mathrm{~m}$ | $50-100 \mathrm{~m}$ | $100+\mathrm{m}$ |  |
| Scripps Ranch | 4 | $75 \%$ | $20 \%$ | $4 \%$ | $1 \%$ | $0 \%$ | $0 \%$ |
| Grizzly Flats | 47 | $8 \%$ | $9 \%$ | $14 \%$ | $39 \%$ | $20 \%$ | $9 \%$ |
| Fountaingrove | 12 | $37 \%$ | $29 \%$ | $17 \%$ | $14 \%$ | $2 \%$ | $1 \%$ |


Figure 22
STRUCTURE SEPARATION
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-33.jpg?height=702&width=1580&top_left_y=809&top_left_x=247" alt="image" style="width:100%;height:auto;">

Scripps Ranch has the shortest average structure separation, giving this community the highest structure density. Fountaingrove homes are further spaced, and Grizzly Flats homes are the furthest spaced by a significant margin. In a vacuum, this suggests a higher risk for Scripps Ranch and a lower risk for Grizzly Flats. Indeed, it is an important consideration for community risk, as referenced in the IBHS report on Lahaina. However, while building-to-building spread is an important pathway for wildfire to spread, it is not the sole method. Surrounding vegetation, as described in a prior section, along with fencing, vehicles, and combustible items (e.g., outdoor furniture and planters) also provide pathways for flame spread and should be considered.

#### 3.3.3 DISTANCE TO WILDLAND VEGETATION

Figures 23,24 , and 25 show maps of each community, color coded by distance to wildland vegetation. The vegetation itself is represented as a green transparent layer. Because the values for distance to wildland vegetation differed so significantly for each community, the scale values and units for each community are different. Note that wildland vegetation does not appear in the main Scripps Ranch map because it is so distant, as seen in the map inset.

Figure 23
DISTANCE TO WILDLAND VEGETATION - SCRIPPS RANCH
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-34.jpg?height=876&width=1369&top_left_y=356&top_left_x=249" alt="image" style="width:100%;height:auto;">

Figure 24
DISTANCE TO WILDLAND VEGETATION - GRIZZLY FLATS
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-34.jpg?height=1065&width=1378&top_left_y=1370&top_left_x=249" alt="image" style="width:100%;height:auto;">

Figure 25
DISTANCE TO WILDLAND VEGETATION - FOUNTAINGROVE
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-35.jpg?height=1067&width=1380&top_left_y=356&top_left_x=251" alt="image" style="width:100%;height:auto;">

While wildland vegetation appears to be quite distant from Scripps Ranch above, this is due to the thresholds used to define wildland vegetation, as described in the methodology section. To help illustrate, Figure 26 shows all tree/shrub/herbaceous vegetation with at least $40 \%$ cover in the area surrounding Scripps Ranch. These areas are shown as dark blue patches. However, because none of these patches meet the second criterion-a continuous area of at least five square kilometers-they are excluded from the distance calculations. For example, the patch highlighted in bright blue represents an area of 0.12 square kilometers.

Figure 26
NEARBY TREE/SHRUB/HERBACEOUS VEGETATION - SCRIPPS RANCH
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-36.jpg?height=646&width=785&top_left_y=356&top_left_x=249" alt="image" style="width:100%;height:auto;">

Table 9 and Figure 27 display the distribution of distance to wildland vegetation for each community.

Table 9
DISTANCE TO WILDLAND VEGETATION
| Community | Average | Distribution of Homes |  |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Distance $(\mathrm{m})$ | $0-100 \mathrm{~m}$ | $100-500 \mathrm{~m}$ | $500-1000 \mathrm{~m}$ | $1000-2500 \mathrm{~m}$ | $2500-5000 \mathrm{~m}$ | $5000+\mathrm{m}$ |  |
| Scripps Ranch | 6,431 | $0 \%$ | $0 \%$ | $0 \%$ | $0 \%$ | $1 \%$ | $99 \%$ |
| Grizzly Flats | 126 | $54 \%$ | $45 \%$ | $2 \%$ | $0 \%$ | $0 \%$ | $0 \%$ |
| Fountaingrove | 1,890 | $0 \%$ | $0 \%$ | $9 \%$ | $80 \%$ | $11 \%$ | $0 \%$ |


Figure 27
DISTANCE TO WILDLAND VEGETATION
<img src="https://cdn.mathpix.com/cropped/15862d42-4bfb-45ca-b447-cea1840c7609-36.jpg?height=576&width=1642&top_left_y=1597&top_left_x=246" alt="image" style="width:100%;height:auto;">

The three communities differ more in this comparison than they did for vegetation coverage or structure separation. Homes in Grizzly Flats are significantly closer to wildland vegetation, on average. Scripps Ranch homes are quite removed from wildland vegetation, while Fountaingrove homes are at an intermediate distance. In a vacuum, this suggests higher risk for Grizzly Flats, intermediate risk for Fountaingrove, and lower risk for Scripps Ranch. It is important, however, to recall the prior discussion of wildland vegetation thresholds. It is quite possible for conclusions to change if different thresholds were selected.

### 3.4 CONCLUSIONS

A structure's relationship to its surrounding environment is a key driver of its wildfire risk in several ways. The concentration of nearby structures (structure density) has been identified as a driver of fire's ability to spread rapidly, as other structures can become fuel during a conflagration event. Surrounding vegetation can also offer fuel to grow or spread a fire. This includes landscaping in a home's immediate proximity, which can either act as a defensible buffer or provide connective fuels, as well as wildland vegetation for WUI communities.

Aerial imagery and computer vision models can help provide actionable data regarding these concepts. Identifying building footprint is key to distance calculations for both structure density and wildland vegetation. Correctly classifying and quantifying the amount of nearby vegetation can further contribute to a home safety inspection. It can also provide community-wide information that may lead to identification of larger scale vulnerabilities.

## Section 4 Additional Applications and Future Research

The power of using building footprints and other data derived from high-resolution imagery in understanding flood and wildfire risk was explored in the two case studies. For flood, the value was building footprint and corresponding accurate structure location, due to the extremely localized nature of flood risk. For wildfire, value came from both building footprint (for determining distance metrics) and identification of ground features (for quantifying nearby vegetation). ${ }^{11}$

### 4.1 BUILDING FOOTPRINT

For many insured perils, knowing exact structure location is not significantly important, and traditional geocoding provides sufficiently accurate location. For example, hurricane wind risk is not expected to vary over a distance of several dozen meters. In contrast, flood and wildfire represent more localized perils in that the risk may change either over short distances or, in the case of wildfire, based on the relative distances of structures to each other.

While the studies focused on single-family homes, building footprints may be as important or more so for commercial risks since a commercial property policy may cover several buildings represented by a single address. Furthermore, these buildings can have extremely large footprints relative to single-family homes. Flood risk may vary significantly across not only different structures on the same policy, but also across different portions of each individual structure. Accurate footprint data can aid in properly assessing this risk.

Building footprint provides not only location, but shape and size of a structure. Square footage is used in many property insurance products, typically as an aid to determine replacement cost. In some cases, explicit rating factors are wholly or partially based on square footage. Building footprints may aid in validating or updating data collected from prefill or other data sources.

### 4.2 GROUND FEATURE IDENTIFICATION

The following are several examples of property characteristics that can be discerned with high-resolution imagery. This data can aid several insurance operations. For example, there may be less need for in-person home inspections (and corresponding fees, generally passed along to policyholders) if similarly accurate data can be derived from remotely sensed imagery and machine learning methods. At the same time, rating data can become more accurate, resulting in fairer ratings for all policyholders and risk mitigation can be performed through the identification of specific vulnerabilities.

#### 4.2.1 ROOF CHARACTERISTICS

A home's roof can be classified in many ways, several of which are discernable from high-resolution imagery, including:

- Shape: hip, gable, etc.
- Material: shingle, tile, etc.
- Condition: staining, patching, etc.

[^6]- Presence of repairs, including temporary (e.g., tarps)

These features can be important drivers of a home's risk to a variety of perils, including wind, hail, leaks, and fire. For example, a study commissioned by the Florida Office of Insurance Regulation evaluated roof performance during the 2004 and 2005 hurricane seasons and found that gable roofs had higher losses than hip roofs, and tile roofs had higher losses than shingle roofs (Applied Research Associates, 2008). ${ }^{12}$ For another example, CAL FIRE identifies the roof as the most vulnerable part of a home, and recommends composite, metal, clay, or tile roofs to resist fires (Ready for Wildfire - Hardening Your Home, 2025).

Roof age has long been a common rating variable for many homeowners insurance companies to capture the effects of deteriorating quality and roof condition over time. A shortcoming of this approach is that homeownersupplied roof age has been shown to be extremely unreliable (Emison \& Tachovsky, 2013). Additionally, differences in local weather history, maintenance, and other factors may lead to differences in material conditions for similarly aged roofs.

#### 4.2.2 TREE OVERHANG

Trees overhanging structures present several risks. Fallen trees or branches can damage the building. Leaves and other debris can clog gutter and drainage systems, leading to roof pooling and leakage. Animals may access the roof via overhanging branches, leading to damaged roof material, roof-mounted equipment, or contents within the building.

#### 4.2.3 UNIQUE PROPERTY OR LIABILITY EXPOSURES

Swimming pools present property and liability exposure to insurers. Swimming pools were identified as an example of a "special hazard," along with trampolines and vicious dogs by the Louisiana Department of Insurance (Louisiana Department of Insurance, 2014).

Roof-mounted solar panels may be covered automatically by an insurance policy. In other cases, additional coverage or an endorsement is needed. Regardless, solar panels are another unique property exposure to insurers.

### 4.3 FUTURE FLOOD AND WILDFIRE RESEARCH

There are several potential areas of future research related to the flood and wildfire case studies in this report.

- Levees, man-made flood protection barriers, are extremely important to consider when determining flood risk. For example, FEMA incorporated levee information into NFIP rates in Risk Rating 2.0 (FEMA, 2022). Consideration of levees could be added to a flood case study to answer questions such as:
- How does accurate building footprint location affect estimated flood losses in areas protected by levees compared with other areas?
- Does distance to levee act similarly to other GIS variables examined in this report (e.g., distance to coast, distance to river)?

[^7]- Without estimated wildfire loss data available, the expected loss and premium differences between different homes or between different communities could not be fully quantified. Incorporating estimated loss data could shed further light on the importance of vegetation cover, structure separation, and distance to wildland metrics.
- The detection of ground features beyond building footprint and vegetation cover can be incorporated into a future wildfire case study. Roof type and the presence of an attached fence are two examples of property characteristics that could be considered.
- This study relied on publicly available building footprints and did not compare the impact of different highresolution data sources or machine learning methods on resulting building footprint accuracy. Future case studies should evaluate the relative accuracy and benefit of various data sources and method on modeled insurance losses.


## Section 5 Conclusions

Geospatial imagery and high-resolution image technology are changing what is possible in many industries, including property insurance. One important insurance application is building footprint data, which is precise information regarding a structure's size, shape, and location. Other applications are structure characteristics (e.g., roof condition) and other property features (e.g., presence of a swimming pool, vegetation cover).

Determination of building location can depend significantly on the data source used. In the flood case study, the distances between parcel-based and footprint-based locations were often significant and, in some cases, over 300 meters. Along with these horizontal distances, meaningful differences in elevation and distance to flood source (coast, river) were also observed.

Flood risk can vary greatly across relatively short horizontal distances, often in conjunction with elevation changes. There were many examples of Florida homes with significant differences in estimated flood loss and flood premium depending on the use of parcel- or footprint-based location. Given the footprint data's better accuracy at representing a structure's actual location, we can conclude that this data is extremely important for flood rating. The use of parcel data or other techniques may result in significant under or overcharging of fair premium.

The wildfire case study also illustrated the utility of footprint data. It allows for precise calculation of structure separation, expected to be a key driver in wildfire conflagration. Footprint data also allows for the quantification of wildland vegetation proximity. Another variable derived from high-resolution imagery, vegetation coverage, can also be quantified. These three variables and similar attributes can assist property insurers in their evaluation of both property and community wildfire risk.

Because flood and wildfire risk can vary over a shorter horizontal distance than many other property insurance perils, building footprint's utility is clear for these two perils. However, there are also other uses for high-resolution imagery in property insurance, including roof characteristics, tree overhang, and identification of unique exposures. These techniques have the potential to not only reduce costs (e.g., eliminating property inspections), but also to produce fairer premiums by increasing the accuracy of exposure data for insurers.

## Section 6 Limitations

### 6.1 DATA RELIANCE

In performing this analysis, we relied on data and other information obtained from FEMA, KatRisk, Florida Department of Revenue, USGS, Overture, CAPE Analytics, LANDFIRE, and other sources. We performed a limited review of the data to be used directly in our analysis for reasonableness and consistency. If there were material defects in the data, it is possible that they would be uncovered by a detailed, systematic review and comparison of the data to search for data values that are questionable or for relationships that are materially inconsistent. Such a review was beyond the scope of our assignment. If the underlying data or information is inaccurate or incomplete, the results of our analysis may likewise be inaccurate or incomplete. In that event, the results of our analysis may not be suitable for the intended purpose.

### 6.2 VARIABILITY OF RESULTS

Any projection of future loss ratios or loss relativities involves estimates of future contingencies. While our analysis is based on sound actuarial principles, it is important to note that variation from the projected result is not only possible, but, in fact, probable. While the degree of such variation cannot be quantified, it could be in either direction from the projections. Such uncertainty is inherent in any set of actuarial projections.

### 6.3 GEOSPATIAL UNCERTAINTY

All geospatial datasets are simplified representations of reality and contain varying levels of abstraction and uncertainty. It is certain that actual real-world values will not conform exactly to estimates provided by these services. The degree of uncertainty will depend heavily on the quality of the input property location, as well as the original data used to develop the underlying geospatial products.

### 6.4 MODEL RELIANCES

Our analysis is based in part on the KatRisk SpatialKat Flood and Storm Surge Models. To the extent that the selected models are biased, the resulting rates will be biased. An analysis based on different catastrophe models would likely produce a different result.

## Section 7 Acknowledgments

The researchers' deepest gratitude goes to those without whose efforts this project could not have come to fruition: the Project Oversight Group for their diligent work overseeing, reviewing and editing this report for accuracy and relevance.

Project Oversight Group members:

Yuzhou Chen, PhD<br>Christopher Clickner, ACAS, MAAA<br>Marco De Virgilis, FCAS<br>Xinyi Hu<br>Min Ji, FSA, FIA, MAAA<br>Nicholas LaHaye, PhD<br>Hugo Lee, PhD<br>Cheok Yeow Leow, FSA<br>Daniel Lupton, FCAS, MAAA, CSPA<br>Daniel Pribe, FSA, MAAA<br>Priya Rohatgi, ASA

At the Society of Actuaries Research Institute:

Rob Montgomery ASA, MAAA, FLMI, Consultant - Research Project Manager

The Society of Actuaries Research Institute would like to acknowledge the generous contribution of the Casualty Actuarial Society to the funding of this research.

## References

Alexandre, P., Stewart, S., Keuler, N., Clayton, M., Mockrin, M., Bar-Massada, A., . . . Radeloff, V. (2016). Factors related to building loss due to wildfires in the conterminous United States. Ecological Applications, 2323-2338. doi:10.1002/eap. 1376

Applied Research Associates. (2008). 2008 Florida Residential Wind Loss Mitigation Study. Florida Office of Insurance Regulation. Retrieved January 30, 2025, from https://floir.com/docs-sf/default-source/property-andcasualty/aralossmitigationstudy.pdf?sfvrsn=f77031e0_2

Bradford, G., Barth, M., \& Wafer, M. (2023, July 18). Geocoding for insurance: An overview. Retrieved February 7, 2025, from Milliman: https://www.milliman.com/en/insight/geocoding-for-insurance-overview

CAL FIRE. (2025). Defensible Space. Retrieved January 30, 2025, from https://www.fire.ca.gov/dspace
Caton, S., Hakes, R., Gorham, D., Zhou, A., \& Gollner, M. (2017). Review of Pathways for Building Fire Spread in the Wildland Urban Interface Part I: Exposure Conditions. Fire Technol, 429-473. doi:10.1007/s10694-016-0589-z

Clark, A., Collins, T., Grineski, S., Brewer, S., \& Flores, A. (2025). Comparative assessment of residential property values at risk to flooding: The case of Utah, USA. International Journal of Disaster Risk Reduction, 105247. doi:10.1016/j.ijdrr.2025.105247

Dabove, P., Daud, M., \& Olivotto, L. (2024). Revolutionizing urban mapping: deep learning and data fusion strategies for accurate building footprint segmentation. Scientific Reports. doi:10.1038/s41598-024-64231-0

Emison, J., \& Tachovsky, H. (2013, August 22). Part One: Homeowner-Supplied Roof Age is Disastrously Wrong. Retrieved January 30, 2025, from Claims Journal: https://www.claimsjournal.com/news/national/2013/08/22/235434.htm

ESA. (n.d.). GeoEye-1202. Retrieved February 7, 2025, from European Space Agency: https://earth.esa.int/eogateway/missions/geoeye-1

FEMA. (2021, March 25). National Flood Insurance Program; Risk Rating 2.0 Methodology and Data Sources. Retrieved February 10, 2025, from FEMA: https://www.fema.gov/sites/default/files/documents/fema_risk-rating-2.0-methodology-data-sources_3-2021.pdf

FEMA. (2022, February). Levees in Risk Rating 2.0. Retrieved March 4, 2025, from FEMA: https://www.fema.gov/sites/default/files/documents/FEMA_Levees-in-Risk-Rating-2.0_2_22.pdf

Fitzgerald-McGowan, M. (2025, January 6). What Is the Home Ignition Zone? Retrieved January 30, 2025, from NFPA: https://www.nfpa.org/news-blogs-and-articles/blogs/2025/01/06/what-is-the-wildfire-home-ignition-zone

FLOIR. (2024). Premium Discounts for Hurricane Loss Mitigation. Retrieved January 30, 2025, from FLOIR: https://floir.com/property-casualty/premium-discounts-for-hurricane-loss-mitigation

Fox, D., Banitalebi, M., \& Rainaud, A. (2024). Building footprint layers show that flooding risk increased more due to greater building exposure than to greater peak discharge with urbanisation in SE France. Journal of Hydrology: Regional Studies. doi:10.1016/j.ejrh.2024.101882

Hakes, R., Caton, S., Gorham, D., \& Gollner, M. (2017). A Review of Pathways for Building Fire Spread in the Wildland Urban Interface Part II: Response of Components and Systems and Mitigation Strategies in the United States. Fire Technol, 475-515. doi:10.1007/s10694-016-0601-7

Huang, X., \& Wang, C. (2020). Estimates of exposure to the 100-year floods in the conterminous United States using national building footprints. International Journal of Disaster Risk Reduction. doi:10.1016/j.ijdrr.2020.101731

IBHS. (2024). The 2023 Lahaina Conflagration. Retrieved January 30, 2025, from https://ibhs1.wpenginepowered.com/wp-content/uploads/FINAL-Lahaina-Standalone-Exec-Summary-.pdf

IBHS. (2025). 2025 LA County Wildfires; Early Insights. Retrieved February 3, 2025, from https://ibhs.org/wp-content/uploads/2025-LAFires-Earlylnsights-FINAL.pdf

Jain, M., Singh, B., Srivastava, A., Malik, R., McDonald, A., \& Lobell, D. (2017). Using satellite data to identify the causes of and potential solutions for yield gaps in India's Wheat Belt. Environmental Research Letters. doi:10.1088/1748-9326/aa8228

Knapp, E., Valachovic, Y., Quarles, S., \& Johnson, N. (2021). Housing arrangement and vegetation factors associated with singlefamily home survival in the 2018 Camp Fire, California. Fire Ecology. doi:10.1186/s42408-021-00117-0

Kramer, H., Mockrin, M., Alexandre, P., Stewart, S., \& Radeloff, V. (2018). Where wildfires destroy buildings in the US relative to the wildland-urban interface and national fire outreach programs. International Journal of Wildland Fire, 329-341. doi:10.1071/WF17135

Lea, D., \& Pralle, S. (2021). To appeal and amend: Changes to recently updated Flood Insurance Rate Maps. Risk, Hazards, \& Crisis in Public Policy. doi:10.1002/rhc3.12222

Lee, K., Oh, S.-K., \& Ryu, H.-Y. (2003). Application of high-resolution satellite imagery to transportation: accessibility index extraction approach. 2003 IEEE International Geoscience and Remote Sensing Symposium Proceedings, 2942-2944. doi:10.1109/IGARSS.2003.1294639

Li, Q., Mou, L., Sun, Y., Hua, Y., Shi, Y., \& Zhu, X. (2024). A Review of Building Extraction From Remote Sensing Imagery: Geometrical Structures and Semantic Attributes. IEEE Transactions on Geoscience and Remote Sensing, 1-15. doi:10.1109/TGRS.2024.3369723

Li, S., Dao, V., Kumar, M., \& Banerjee, T. (2022). Mapping the wildland-urban interface in California using remote sensing data. Scientific Reports, 5789. doi:10.1038/s41598-022-09707-7

Louisiana Department of Insurance. (2014). A General Description of Homeowners Ratemaking Methodology. Baton Rouge, LA: Louisiana Department of Insurance. Retrieved January 30, 2025, from https://www.ldi.la.gov/docs/default-source/documents/propertycasualty/Forms/act-427---ratemaking-methodology.pdf?sfvrsn=9da07152_6

Ma, L., Wang, Y., Cheng, L., Li, M., \& Tong, L. (2013). Using High-Resolution Imagery Acquired with an Autonomous Unmanned Aerial Vehicle for Urban Construction and Planning. International Conference on Remote Sensing, Environment and Transportation Engineering, 200-203. doi:10.2991/rsete.2013.49

NASA. (2025, February 7). MODIS Data. Retrieved February 7, 2025, from NASA: https://terra.nasa.gov/data/modis-data

NBC 7 San Diego. (2023, October 23). Scripps Ranch to reflect on 2003 Cedar Fire that tore through community. Retrieved January 30, 2025, from NBC San Diego: https://www.nbcsandiego.com/news/local/scripps-ranch-to-reflect-on-2003-cedar-fire-that-tore-through-community/3338448/

Netusil, N., Moeltner, K., \& Jarrad, M. (2019). Floodplain designation and property sale prices in an urban watershed. Land Use Policy, 104112. doi:10.1016/j.landusepol.2019.104112

NIST. (2023, August 25). WUI Definitions. Retrieved February 7, 2025, from National Institute of Standards and Technology: https://www.nist.gov/el/fire-research-division-73300/wildland-urban-interface-fire-73305/hazard-mitigation-methodology-9

NOAA. (2022, July 26). Emergency Response Imagery. Retrieved January 31, 2025, from NOAA: https://storms.ngs.noaa.gov/
Pineda, P. (2022, October 29). Fountaingrove resurgence continues five years after Tubbs Fire. Retrieved January 30, 2025, from Santa Rosa Press Democrat: https://www.pressdemocrat.com/article/news/fountaingrove-resurgence-continues-five-years-after-firestorm/

Quarles, S., Leschak, P., Worley, K., Brown, R., \& Iskowitz, C. (2013). Lessons Learned from Waldo Canyon: FAC mitigation assessment team report. Northwest Fire Science Consortium. Retrieved February 7, 2025, from https://www.nwfirescience.org/biblio/lessons-learned-waldo-canyon-fac-mitigation-assessment-team-report

Ready for Wildfire - Defensible Space. (2025). Defensible Space. Retrieved February 3, 2025, from Ready for Wildfire: https://readyforwildfire.org/prepare-for-wildfire/defensible-space/

Ready for Wildfire - Hardening Your Home. (2025). Harden your home to reduce wildfire threats. Retrieved January 30, 2025, from Ready for Wildfire: https://readyforwildfire.org/prepare-for-wildfire/hardening-your-home/

Rothlisberger, V., Zischg, A., \& Keiler, M. (2017). Identifying spatial clusters of flood exposure to support decision making in risk management. Science of The Total Environment. doi:10.1016/j.scitotenv.2017.03.216

Schmidt, J., Berman, M., \& Waigl, C. (2024). Avoid getting burned: lessons from the McKinley wildfire in rural Alaska, USA. International Journal of Wildland Fire. doi:10.1071/WF24014

Syphard, A., Keeley, J., Bar Massada, A., Brennan, T., \& Radeloff, V. (2012). Housing Arrangement and Location Determine the Likelihood of Housing Loss Due to Wildfire. PLOS One. doi:10.1371/journal.pone. 0033954

Taramelli, A., Righini, M., Valentini, E., Alfieri, L., Gatti, I., \& Gabellani, S. (2022). Building-scale flood loss estimation through vulnerability pattern characterization: application to an urban flood in Milan, Italy. Natural Hazards and Earth System Sciences, 3543-3569. doi:10.5194/nhess-22-3543-2022

Tomljenovic, I., Hofle, B., Tiede, D., \& Blaschke, T. (2015). Building Extraction from Airborne Laser Scanning Data: An Analysis of the State of the Art. Remote Sensing, 3826-3862. doi:10.3390/rs70403826

USDA. (2024, May 7). Wildland-Urban Interface Growth in the U.S. Retrieved January 30, 2025, from USDA Forest Service: https://research.fs.usda.gov/nrs/projects/wuigrowth\#research

USGS. (2018, July 6). USGS EROS Archive - Aerial Photography - High Resolution Orthoimagery (HRO). Retrieved February 7, 2025, from USGS: https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-high-resolution-orthoimagery-hro?qt-science_center_objects=0\#qt-science_center_objects

USGS. (2018, July 6). USGS EROS Archive - Aerial Photography - National Agriculture Imagery Program (NAIP). Retrieved February 7, 2025, from USGS: https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-national-agriculture-imagery-program-naip

Wulff, R. (2024, August 14). Caldor Fire rebuild continues, three years after it tore through El Dorado County. Retrieved January 30, 2025, from CBS News: https://www.cbsnews.com/sacramento/news/caldor-fire-grizzly-flats-rebuild-3-years-later/

Zischg, A., Mosimann, M., Bernet, D., \& Rothlisberger, V. (2018). Validation of 2D flood models with insurance claims. Journal of Hydrology, 250-361. doi:10.1016/j.jhydrol.2017.12.042

## About The Society of Actuaries Research Institute

Serving as the research arm of the Society of Actuaries (SOA), the SOA Research Institute provides objective, datadriven research bringing together tried and true practices and future-focused approaches to address societal challenges and your business needs. The Institute provides trusted knowledge, extensive experience and new technologies to help effectively identify, predict and manage risks.

Representing the thousands of actuaries who help conduct critical research, the SOA Research Institute provides clarity and solutions on risks and societal challenges. The Institute connects actuaries, academics, employers, the insurance industry, regulators, research partners, foundations and research institutions, sponsors and nongovernmental organizations, building an effective network which provides support, knowledge and expertise regarding the management of risk to benefit the industry and the public.

Managed by experienced actuaries and research experts from a broad range of industries, the SOA Research Institute creates, funds, develops and distributes research to elevate actuaries as leaders in measuring and managing risk. These efforts include studies, essay collections, webcasts, research papers, survey reports, and original research on topics impacting society.

Harnessing its peer-reviewed research, leading-edge technologies, new data tools and innovative practices, the Institute seeks to understand the underlying causes of risk and the possible outcomes. The Institute develops objective research spanning a variety of topics with its strategic research programs: aging and retirement; actuarial innovation and technology; mortality and longevity; diversity, equity and inclusion; health care cost trends; and catastrophe and climate risk. The Institute has a large volume of topical research available, including an expanding collection of international and market-specific research, experience studies, models and timely research.

## About The Casualty Actuarial Society

The Casualty Actuarial Society (CAS) is a leading international organization for credentialing, professional education and research. Founded in 1914, the CAS is the world's only actuarial organization focused exclusively on propertycasualty risks and serves over 10,000 members worldwide. CAS members are sought after globally for their insights and ability to apply analytics to solve insurance and risk management problems.

As the world's premiere P\&C actuarial research organization, the CAS reaches practicing actuaries across the globe with thought-leading concepts and solutions. The CAS has been conducting research since its inception. Today, the CAS provides thousands of open-source research papers, including its prestigious publication, Variance - all of which advance actuarial science and enhance the P\&C insurance industry. Learn more at casact.org.

The Casualty Actuarial Society
4350 N. Fairfax Drive, Suite 250
Arlington, VA 22203
www.casact.org


[^0]:    ${ }^{1}$ For example, NASA Terra \& Aqua MODIS (NASA, 2025).
    ${ }^{2}$ For example, GeoEye-1 (ESA, n.d.).
    ${ }^{3}$ For example, National Agriculture Imagery Program (NAIP) imagery (USGS, 2018) and USGS EROS High Resolution Orthoimagery (USGS, 2018).
    ${ }^{4}$ Raster data is a geographic data structure that stores information in an equally space d grid of cells, or pixels. Raster data products are preprocessed and packaged datasets, often derived from satellite imagery or other sensor data, designed to simplify the display and use of imagery in GIS software.

[^1]:    ${ }^{5}$ In this report, relative elevation is defined as a location's elevation minus the average elevation within a circle of radius 500 m . It can be envisioned as a location's elevation relative to the surrounding neighborhood. The crest of a hill would likely have a positive relative elevation, while the bottom of a valley would likely have a negative relative elevation (regardless of its absolute elevation above sea level).

[^2]:    ${ }^{6}$ Milliman Bungalow ${ }^{\text {TM }}$ is based on the KatRisk SpatialKat flood catastrophe model and NFIP OpenFEMA data.
    ${ }^{7}$ Inland flood represents fluvial (riverine) and pluvial (flash) flood sources of flooding. Storm surge represents coastal, wind-driven flooding, typically associated with tropical cyclones.

[^3]:    ${ }^{8}$ First floor height represents the height of the first floor above ground level.

[^4]:    ${ }^{9}$ https://www.theatlantic.com/technology/archive/2014/03/science-several-us-states-led-by-florida-are-flatter-than-a-pancake/284348/

[^5]:    ${ }^{10}$ Aerial imagery data was provided to CAPE Analytics by Eagleview, Vexcel, and Maxar.

[^6]:    ${ }^{11}$ Building footprint is a special case of ground feature identification. However, due to its importance for certain perils, it is useful to consider it independently.

[^7]:    ${ }^{12}$ Florida property insurers are required to provide policy discounts for certain windstorm mitigation features, including certain roof characteristics (FLOIR, 2024).

