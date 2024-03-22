-- Create a temporary table to compute the lifespan of bands
CREATE TEMPORARY TABLE tmp_band_lifespan AS
SELECT 
    band_name,
    IF(splitted[2] IS NOT NULL, (FORMED - SPLITTED[2]), 2022 - FORMED) AS lifespan
FROM (
    SELECT 
        band_name, 
        FORMED, 
        SPLITTED, 
        IF(FORMED != 0, 2022 - FORMED, 0) AS lifespan
    FROM metal_bands,
        SPLIT(formed, '-') AS SPLITTED
    WHERE style LIKE '%Glam rock%'
) AS t;

-- Rank the bands by their longevity
SELECT band_name, lifespan
FROM tmp_band_lifespan
ORDER BY lifespan DESC;
