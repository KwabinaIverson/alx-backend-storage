-- Imports and  ranks country origins of bands, ordered by the number of (non-unique) fans
-- Temporary table to store the aggregated fan counts per country
CREATE TEMPORARY TABLE tmp_band_fans AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the countries by the number of non-unique fans
SELECT origin, nb_fans
FROM tmp_band_fans
ORDER BY nb_fans DESC;
