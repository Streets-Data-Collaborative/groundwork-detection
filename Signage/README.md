# Week 1
* Karan is working on optimizing subcategories of signage (to be revamped)
* Duke is working to create ETL that can reliably generate data to either local or google drive path
    * inline documentation TBD
### Output
* Output Images: [Path](https://drive.google.com/open?id=1Sog0WTiPbTqZGdw25prTe2EDtQwfMsCG) to Google drive Image Storage
* Code: See [Here](https://github.com/Streets-Data-Collaborative/groundwork-detection/blob/ca46f5d7589762a750296e8367a1277ed0aabeeb/Signage/test/test_googleStreetViewEtl.py#L21) for the main method that ran the first iteration of ETL that generated above images
     
# Week2
* Duke worked in revamping ETL
    1. Shapefile Creation
        * The current ETL uses [shapefile](https://drive.google.com/drive/folders/1k5B8UGjrmHz8dUszCEgmp2fCK4QA5qvI?usp=sharing) that creates
            * LION lion and Node Data
            * LION NYC Street Centerline Shapefile
            * NYC PUMA Boundaries
        * Methodology
            1. LION Node Data Joined with NYC Street Centerline for Street Width, with lion to determine if the point is in fact on the street, and PUMA Shapefile for neighborhood label
                1. 20 <= [NYC Street Centerline].[st_width] <= 30
                2. Nodes joined to the closest lion street, and we filter join result where [Join Output].[Distance] == 0 
    2. ETL takes kwargs. Below are supported arguments. All iterables will be made into a single cartesian product, and will each be formatted to call StreetView Static API 
        * puma - if given, a sub directory will be made after puma string. Give number ID (e.g. 3701)
        * fov - iterable.
        * pitch - iterable.
        * heading - iterable.
    3. Image ETL: Photos are downloaded under [img](https://drive.google.com/open?id=1Sog0WTiPbTqZGdw25prTe2EDtQwfMsCG)/{PUMA_ID}
            